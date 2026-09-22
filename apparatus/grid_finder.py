"""Offline, evidence-bound candidate search. No headroom inferred from a map.

CLI: python grid_finder.py --lat 53.3 --lon -0.8 --mw 100 --voltage-kv 132
API: GridFinder().query(latitude=..., longitude=..., mw=..., voltage_kv=...)
"""
import argparse
from collections import defaultdict, deque
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA_PATH = HERE / 'grid-finder-data.json'
EARTH_RADIUS_KM = 6378.137
LIMITATION = ('Candidate screening over a dated published graph, not a connection offer, '
              'available capacity, power-flow result or engineering approval.')


def distance_km(lon1, lat1, lon2, lat2):
    """Atlas spherical radius; clamp protects antipodal rounding."""
    dlat, dlon = math.radians(lat2-lat1), math.radians(lon2-lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(dlon/2)**2
    a = min(1., max(0., a))
    return 2*EARTH_RADIUS_KM*math.atan2(math.sqrt(a), math.sqrt(1-a))


def _number(name, value, minimum=None, maximum=None):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(name+' must be a finite number')
    if minimum is not None and value < minimum or maximum is not None and value > maximum:
        raise ValueError(name+' outside supported range')
    return value


def compare_published_path_ratings(path, mw, power_factor, season='winter'):
    """Compare entered demand against each published nameplate, never spare capacity."""
    _number('mw', mw, 0)
    _number('power_factor', power_factor, .000001, 1)
    if season not in ('winter', 'spring', 'summer', 'autumn'):
        raise ValueError('season must be winter, spring, summer or autumn')
    apparent_mva = mw/power_factor
    rows = []
    for edge in path:
        field = 'rating_mva' if edge['kind'] == 'transformer' else season+'_mva'
        rating = edge.get('published_ratings_mva', {}).get(field)
        known = isinstance(rating, (int, float)) and math.isfinite(rating) and rating > 0
        rows.append({'edge_id': edge['edge_id'], 'source_row': edge['source_row'],
                     'rating_field': field, 'published_rating_mva': rating if known else None,
                     'entered_apparent_mva': apparent_mva,
                     'ratio_to_nameplate': apparent_mva/rating if known else None,
                     'exceeds_nameplate': apparent_mva > rating if known else None})
    return {'schema': 'globalgrid.published-rating-comparison.v1', 'mw': mw,
            'power_factor': power_factor, 'season': season, 'edges': rows,
            'available_headroom_mw': None,
            'basis': 'Entered apparent demand compared separately with published edge ratings. Existing flows, power sharing, contingencies and connection headroom are not solved.'}


class GridFinder:
    def __init__(self, data_path=DATA_PATH, data=None):
        self.data = data if data is not None else json.loads(Path(data_path).read_text(encoding='utf-8'))
        if self.data.get('schema') != 'globalgrid.grid-finder-data.v1':
            raise ValueError('Unsupported graph schema')
        self.sites = {s['code']: s for s in self.data['sites']}
        self.nodes = {n['id']: n for n in self.data['nodes']}
        self.site_nodes = defaultdict(list)
        for n in self.nodes.values():
            self.site_nodes[n['site_code']].append(n['id'])
        self.adj = defaultdict(list)
        self.refused_edges = defaultdict(list)
        for edge in self.data['edges']:
            a, b = self.nodes.get(edge['from']), self.nodes.get(edge['to'])
            reason = None
            if not a or not b:
                reason = 'MISSING_PUBLISHED_NODE'
            elif a.get('voltage_kv') is None or b.get('voltage_kv') is None:
                reason = 'UNDECLARED_NODE_VOLTAGE'
            elif a['voltage_kv'] != b['voltage_kv'] and edge['kind'] != 'transformer':
                reason = 'CIRCUIT_CHANGES_VOLTAGE'
            for near, far in [(edge['from'], edge['to']), (edge['to'], edge['from'])]:
                if reason:
                    self.refused_edges[near].append({'edge': edge['id'], 'reason': reason})
                else:
                    self.adj[near].append((far, edge))
        for edges in self.adj.values():
            edges.sort(key=lambda x: (x[0], x[1]['id']))

    def path_to_voltage(self, site_code, voltage_kv, target_kv=400, max_hops=12):
        starts = sorted(n for n in self.site_nodes[site_code]
                        if self.nodes[n].get('voltage_kv') == voltage_kv)
        if not starts:
            return {'status': 'NO_VALIDATED_NODE_AT_REQUESTED_VOLTAGE', 'hops': None, 'path': [],
                    'explored_nodes': 0, 'refused_edge_count': 0}
        queue = deque(starts)
        parent = {n: None for n in starts}
        depth = {n: 0 for n in starts}
        refused, cutoff = set(), False
        while queue:
            node = queue.popleft()
            if self.nodes[node]['voltage_kv'] >= target_kv:
                path = []
                at = node
                while parent[at] is not None:
                    near, edge = parent[at]
                    path.append({'from_node': near, 'to_node': at, 'edge_id': edge['id'],
                                 'kind': edge['kind'], 'from_kv': self.nodes[near]['voltage_kv'],
                                 'to_kv': self.nodes[at]['voltage_kv'],
                                 'published_ratings_mva': edge.get('ratings_mva', {}),
                                 'source_row': edge['source_row']})
                    at = near
                return {'status': 'PUBLISHED_PATH_FOUND', 'hops': len(path), 'path': path[::-1],
                        'target_node': node, 'target_site': self.nodes[node]['site_code'],
                        'target_voltage_kv': self.nodes[node]['voltage_kv'],
                        'explored_nodes': len(parent), 'refused_edge_count': len(refused)}
            refused.update(e['edge'] for e in self.refused_edges[node])
            if depth[node] >= max_hops:
                cutoff = cutoff or any(far not in parent for far, _ in self.adj[node])
                continue
            for far, edge in self.adj[node]:
                if far not in parent:
                    parent[far] = (node, edge)
                    depth[far] = depth[node]+1
                    queue.append(far)
        return {'status': 'HOP_LIMIT_REACHED' if cutoff else 'NO_PATH_IN_VALIDATED_PUBLISHED_GRAPH',
                'hops': None, 'path': [], 'explored_nodes': len(parent),
                'refused_edge_count': len(refused)}

    def query(self, latitude, longitude, mw, voltage_kv=None, target_kv=400,
              headroom_mw_by_site=None, limit=12, max_hops=12, radius_km=None):
        _number('latitude', latitude, -90, 90)
        _number('longitude', longitude, -180, 180)
        _number('mw', mw, 0)
        _number('target_kv', target_kv, .001)
        if voltage_kv is not None:
            _number('voltage_kv', voltage_kv, .001)
        if not isinstance(limit, int) or isinstance(limit, bool) or not 1 <= limit <= 886:
            raise ValueError('limit must be an integer in [1,886]')
        if not isinstance(max_hops, int) or isinstance(max_hops, bool) or not 0 <= max_hops <= 100:
            raise ValueError('max_hops must be an integer in [0,100]')
        if radius_km is not None:
            _number('radius_km', radius_km, 0)
        headroom = {} if headroom_mw_by_site is None else headroom_mw_by_site
        if not isinstance(headroom, dict):
            raise ValueError('headroom_mw_by_site must be a mapping of site code to entered MW')
        for code, value in headroom.items():
            if code not in self.sites:
                raise ValueError('Unknown headroom site code: '+str(code))
            _number('entered headroom '+code, value, 0)
        candidates = []
        for code, site in sorted(self.sites.items()):
            if voltage_kv is not None and voltage_kv not in site['voltages_kv']:
                continue
            point = site.get('location')
            if not point:
                continue
            km = distance_km(longitude, latitude, point['lon'], point['lat'])
            if radius_km is not None and km > radius_km:
                continue
            if voltage_kv is None:
                topology = {'status': 'CONNECTION_VOLTAGE_NOT_ENTERED', 'hops': None, 'path': []}
            else:
                topology = self.path_to_voltage(code, voltage_kv, target_kv, max_hops)
            capacity = {'status': 'UNKNOWN', 'entered_headroom_mw': None, 'margin_mw': None,
                        'within_entered_headroom': None}
            if code in headroom:
                capacity.update(status='USER_ENTERED_SCENARIO', entered_headroom_mw=headroom[code],
                                margin_mw=headroom[code]-mw, within_entered_headroom=mw <= headroom[code])
            candidates.append({'site_code': code, 'name': site['name'], 'location': point,
                               'transmission_owner': site.get('transmission_owner'),
                               'voltages_kv': site['voltages_kv'], 'distance_km': km,
                               'topology': topology, 'capacity': capacity, 'pareto_tier': None})
        # Incomparable unknown paths remain ungraded. Do not treat unknown as failure or infinity.
        remaining = [c for c in candidates if c['topology']['hops'] is not None]
        tier = 1
        while remaining:
            front = [a for a in remaining if not any(
                b['distance_km'] <= a['distance_km'] and b['topology']['hops'] <= a['topology']['hops']
                and (b['distance_km'] < a['distance_km'] or b['topology']['hops'] < a['topology']['hops'])
                for b in remaining)]
            for c in front:
                c['pareto_tier'] = tier
            remaining = [c for c in remaining if c['pareto_tier'] is None]
            tier += 1
        # Distance order keeps nearby unknown cases visible; Pareto is an explicit separate annotation.
        candidates.sort(key=lambda c: (c['distance_km'], c['site_code']))
        result = {'schema': 'globalgrid.grid-finder-result.v1', 'limitation': LIMITATION,
                  'query': {'latitude': latitude, 'longitude': longitude, 'mw': mw,
                            'voltage_kv': voltage_kv, 'target_kv': target_kv, 'max_hops': max_hops,
                            'radius_km': radius_km},
                  'counts': self.data.get('counts', {}), 'matching_located_sites': len(candidates),
                  'ordering': 'geographic_distance_then_site_code',
                  'pareto_basis': 'distance_km and validated published hop count; fewer of each; unknown paths ungraded; tiers computed across all matching located sites',
                  'distance_basis': 'Spherical separation on Atlas radius 6378.137 km, not cable route length',
                  'topology_basis': 'Existing published circuits and transformers only; no invented same-site bus ties; unknown voltage edges excluded; fewest edges, not impedance or available capacity',
                  'source_publication': self.data.get('source_publication'),
                  'geometry_attribution': self.data.get('geometry_attribution'),
                  'sources': self.data.get('sources', []), 'candidates': candidates[:limit]}
        return result


def build_data(source_root):
    """Compact public products; preserve precise provenance, not inferred connections."""
    root = Path(source_root)
    paths = [root/'connection-points.v3.json', root/'gb-transmission-network.v1.json']
    points, network = [json.loads(p.read_text(encoding='utf-8')) for p in paths]
    assert points['schema'] == 'data-grid-gb.connection-points.v3'
    assert network['schema'] == 'data-grid-gb.transmission-network.v1'
    sites = []
    for p in points['connection_points']:
        sites.append({'code': p['site_code'], 'name': p['name'], 'voltages_kv': p['voltages_kv'],
                      'transmission_owner': p.get('transmission_owner'), 'location': p.get('location')})
    nodes = [{'id': n['node'], 'site_code': n['site_code'],
              'voltage_kv': n.get('voltage_kv') if n.get('voltage_consistent_with_site') is True else None}
             for n in network['nodes']]
    edges = []
    for field, kind in [('circuits', 'circuit'), ('transformers', 'transformer')]:
        for i, row in enumerate(network[field]):
            ratings = {k: v for k, v in row.items() if k.endswith('_mva') and isinstance(v, (int, float))}
            edges.append({'id': kind+':'+str(i), 'from': row['node_1'], 'to': row['node_2'],
                          'kind': kind, 'ratings_mva': ratings, 'source_row': field+'['+str(i)+']'})
    data = {'schema': 'globalgrid.grid-finder-data.v1', 'source_publication': network['source'],
            'geometry_attribution': points['join']['geometry_source'],
            'voltage_basis': 'Only voltage_consistent_with_site=true retained; undocumented node digits never decoded',
            'sources': [{'repository': 'Ventusltd/data-grid-gb', 'path': 'derived/'+p.name,
                         'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'bytes': p.stat().st_size}
                        for p in paths],
            'counts': {'sites': len(sites), 'located_sites': sum(bool(s['location']) for s in sites),
                       'unlocated_sites': sum(not s['location'] for s in sites), 'nodes': len(nodes),
                       'circuits': len(network['circuits']), 'transformers': len(network['transformers']),
                       'unknown_voltage_nodes': sum(n['voltage_kv'] is None for n in nodes)},
            'sites': sites, 'nodes': nodes, 'edges': edges}
    DATA_PATH.write_text(json.dumps(data, separators=(',', ':')), encoding='utf-8')
    return data


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--build-data', metavar='DERIVED_DIRECTORY')
    p.add_argument('--lat', type=float)
    p.add_argument('--lon', type=float)
    p.add_argument('--mw', type=float, default=100)
    p.add_argument('--voltage-kv', type=float)
    p.add_argument('--target-kv', type=float, default=400)
    p.add_argument('--limit', type=int, default=12)
    p.add_argument('--headroom-json', default='{}')
    args = p.parse_args()
    if args.build_data:
        print(json.dumps(build_data(args.build_data)['counts'], indent=2))
    else:
        if args.lat is None or args.lon is None:
            p.error('--lat and --lon are required')
        print(json.dumps(GridFinder().query(args.lat, args.lon, args.mw, args.voltage_kv,
                         args.target_kv, json.loads(args.headroom_json), args.limit), indent=2, allow_nan=False))
