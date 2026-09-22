"""Behavioral fixtures, actual source parity and independent reverse-distance audit."""
from collections import deque, defaultdict
import hashlib
import json
import math
from pathlib import Path
import subprocess
import time
import unittest
from grid_finder import GridFinder, distance_km, DATA_PATH, EARTH_RADIUS_KM, compare_published_path_ratings

HERE = Path(__file__).resolve().parent
FINDER = GridFinder()
AUDIT = {}


class GridFinderTests(unittest.TestCase):
    def test_source_counts_and_hashes(self):
        self.assertEqual(FINDER.data['counts']['sites'], 886)
        self.assertEqual(FINDER.data['counts']['located_sites'], 489)
        self.assertEqual(FINDER.data['counts']['unknown_voltage_nodes'], 726)
        self.assertEqual(hashlib.sha256(DATA_PATH.read_bytes()).hexdigest(), 'cf977c3cff6f6929e3b5edb530be5012b966311bdc449c79318019bf52fa9592')

    def test_actual_js_distance_source_parity(self):
        fixture = json.loads((HERE/'grid-finder-fixtures.json').read_text())
        errors = [abs(distance_km(*p)-v) for p,v in zip(fixture['pairs'], fixture['distance_km'])]
        self.assertLess(max(errors), 1e-9)
        AUDIT['js_source_parity'] = {'samples': len(errors), 'max_error_km': max(errors),
            'source': fixture['source'], 'sha256': fixture['source_sha256']}

    def test_distance_degenerate_and_antipodal(self):
        self.assertEqual(distance_km(0, 0, 0, 0), 0)
        self.assertAlmostEqual(distance_km(0, 0, 180, 0), math.pi*EARTH_RADIUS_KM, places=9)
        self.assertAlmostEqual(distance_km(179.9, 20, -179.9, 20), distance_km(-179.9, 20, 179.9, 20), places=9)

    def test_all_site_paths_against_reverse_multi_target_distances(self):
        # Independently build legal adjacency from packaged rows, then search FROM ALL 400kV nodes.
        nodes = {n['id']: n for n in FINDER.data['nodes']}
        graph = defaultdict(set)
        for e in FINDER.data['edges']:
            a, b = nodes.get(e['from']), nodes.get(e['to'])
            if not a or not b or a['voltage_kv'] is None or b['voltage_kv'] is None:
                continue
            if e['kind'] != 'transformer' and a['voltage_kv'] != b['voltage_kv']:
                continue
            graph[a['id']].add(b['id']); graph[b['id']].add(a['id'])
        dist = {n['id']: 0 for n in nodes.values() if n['voltage_kv'] is not None and n['voltage_kv'] >= 400}
        queue = deque(dist)
        while queue:
            n = queue.popleft()
            for neighbor in graph[n]:
                if neighbor not in dist:
                    dist[neighbor] = dist[n]+1
                    queue.append(neighbor)
        checked = found = 0
        for site in FINDER.sites.values():
            for kv in site['voltages_kv']:
                starts = [n['id'] for n in nodes.values() if n['site_code'] == site['code'] and n['voltage_kv'] == kv]
                expected = min([dist[n] for n in starts if n in dist], default=None)
                if expected is not None and expected > 12:
                    expected = None
                result = FINDER.path_to_voltage(site['code'], kv, 400, 12)
                self.assertEqual(result['hops'], expected, (site['code'], kv))
                checked += 1; found += expected is not None
        AUDIT['reverse_graph_audit'] = {'site_voltage_queries': checked, 'paths_within_12_edges': found}

    def test_unknown_capacity_and_user_entered_scenario(self):
        normal = FINDER.query(53.3, -.8, 100, 132, limit=3)
        first = normal['candidates'][0]
        self.assertEqual(first['site_code'], 'WBUR')
        self.assertEqual(first['capacity']['status'], 'UNKNOWN')
        self.assertEqual(first['topology']['hops'], 1)
        entered = FINDER.query(53.3, -.8, 100, 132, headroom_mw_by_site={'WBUR': 80}, limit=3)
        self.assertEqual(entered['candidates'][0]['capacity']['margin_mw'], -20)
        self.assertFalse(entered['candidates'][0]['capacity']['within_entered_headroom'])
        self.assertEqual([c['site_code'] for c in normal['candidates']], [c['site_code'] for c in entered['candidates']])
        (HERE/'grid-finder-example-result.json').write_text(json.dumps(normal, indent=2), encoding='utf-8')

    def test_published_nameplate_is_not_spare_capacity(self):
        path = FINDER.path_to_voltage('WBUR', 132)['path']
        self.assertEqual(path[0]['source_row'], 'transformers[1262]')
        self.assertEqual(path[0]['published_ratings_mva']['rating_mva'], 274)
        below = compare_published_path_ratings(path, 100, .95)
        above = compare_published_path_ratings(path, 300, .95)
        self.assertFalse(below['edges'][0]['exceeds_nameplate'])
        self.assertTrue(above['edges'][0]['exceeds_nameplate'])
        self.assertIsNone(below['available_headroom_mw'])
        self.assertIsNone(above['available_headroom_mw'])
        self.assertAlmostEqual(below['edges'][0]['entered_apparent_mva'], 100/.95)
        self.assertAlmostEqual(above['edges'][0]['entered_apparent_mva'], 300/.95)
        AUDIT['published_rating_experiment'] = {'site_code':'WBUR', 'below': below, 'above': above}

    def test_no_assumed_voltage(self):
        result = FINDER.query(53.3, -.8, 100, limit=4)
        self.assertTrue(all(c['topology']['status'] == 'CONNECTION_VOLTAGE_NOT_ENTERED' and c['pareto_tier'] is None for c in result['candidates']))

    def test_input_refusals(self):
        for change in [{'latitude': 91}, {'longitude': float('nan')}, {'mw': -1},
                       {'headroom_mw_by_site': []}, {'headroom_mw_by_site': {'MISSING': 10}}, {'max_hops': 1.5}]:
            args = dict(latitude=53.3, longitude=-.8, mw=100, voltage_kv=132)
            args.update(change)
            with self.assertRaises(ValueError): FINDER.query(**args)

    def test_unknown_voltage_and_no_invented_same_site_ties(self):
        data = {'schema': 'globalgrid.grid-finder-data.v1', 'sites': [{'code': 'A'}, {'code': 'B'}],
            'nodes': [{'id': 'a1', 'site_code': 'A', 'voltage_kv': 132}, {'id': 'a2', 'site_code': 'A', 'voltage_kv': 400},
                      {'id': 'b', 'site_code': 'B', 'voltage_kv': 400}, {'id': 'u', 'site_code': 'B', 'voltage_kv': None}],
            'edges': [{'id': 'bad', 'from': 'a1', 'to': 'b', 'kind': 'circuit', 'source_row': 'synthetic'},
                      {'id': 'unknown', 'from': 'a1', 'to': 'u', 'kind': 'transformer', 'source_row': 'synthetic'}]}
        f = GridFinder(data=data)
        result = f.path_to_voltage('A', 132)
        self.assertIsNone(result['hops'])
        self.assertEqual(result['refused_edge_count'], 2)
        data['edges'].append({'id': 'valid', 'from': 'a1', 'to': 'b', 'kind': 'transformer', 'source_row': 'synthetic'})
        self.assertEqual(GridFinder(data=data).path_to_voltage('A', 132)['hops'], 1)


if __name__ == '__main__':
    began = time.perf_counter()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(GridFinderTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    AUDIT.update(status='passed' if result.wasSuccessful() else 'failed', tests=result.testsRun,
                 failures=len(result.failures), errors=len(result.errors), elapsed_seconds=time.perf_counter()-began,
                 data_sha256=hashlib.sha256(DATA_PATH.read_bytes()).hexdigest(), counts=FINDER.data['counts'],
                 implementation_sha256=hashlib.sha256((HERE/'grid_finder.py').read_bytes()).hexdigest())
    (HERE/'grid-finder-test-results.json').write_text(json.dumps(AUDIT, indent=2), encoding='utf-8')
    raise SystemExit(0 if result.wasSuccessful() else 1)
