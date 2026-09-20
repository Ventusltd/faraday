#!/usr/bin/env python3
"""bench/topo.py - NETWORKS BY THE BILLION: different TOPOLOGIES, not one site with different numbers.

One seed = one generic private network behind one connection point (no real one): a star, a chain, a tree or sub-boards, 2 to 12
substations, solar on some, a generator somewhere, an export limit. x 18 operating cases (solar 0, half, full; generator off, on;
load 100, 60, 30 per cent). Solved by the two pulse sweep over ANY radial tree. EVERY CASE IS SOLVED TWICE: here, and by
bench/fire_topo.js (the code the Kuiper runs: `fire network {"seed":N,...}`), rebuilt from the seed alone.

A billion rows are not kept. Each shard keeps its counts and its MOST TELLING cases; topo_top.py merges those into the top 1,000
that become commands with sentences. Shards of 2,000 seeds (36,000 cases); resumable; plain Python and node.

  python bench/topo.py --seeds 56000000 --workers 16        # about a billion cases
  python bench/topo.py --selftest
"""
import argparse, heapq, json, math, os, subprocess, sys, time
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get('TOPO_OUT', r'E:\faraday-bench\topo')
PER_SHARD = 2000
C = dict(kv=11.0, grid_x_over_r=10.0, hv_cable_r=0.20, hv_cable_x=0.09, tx_z_pct=5.5, tx_x_over_r=5.0, load_pf=0.90, gen_pf=0.95, volts_high_pu=1.06, volts_low_pu=0.94)
KVA = (500, 800, 1000, 1600, 2000); LIMITS = (0, 50, 200, 500, 1000); GENS = (0, 250, 500, 1000); FAULT = (100, 150, 250, 350, 500)
SHAPES = ('star', 'chain', 'tree', 'sub-boards')
CASES = [(ps, g, ls) for ps in (0.0, 0.5, 1.0) for g in (0, 1) for ls in (1.0, 0.6, 0.3)]

def mulberry32(a):
    a &= 0xFFFFFFFF
    def nxt():
        nonlocal a
        a = (a + 0x6D2B79F5) & 0xFFFFFFFF
        t = a
        t = ((t ^ (t >> 15)) * (t | 1)) & 0xFFFFFFFF
        t ^= (t + (((t ^ (t >> 7)) * (t | 61)) & 0xFFFFFFFF)) & 0xFFFFFFFF
        return (t ^ (t >> 14)) & 0xFFFFFFFF
    return nxt

VARIANT = int(os.environ.get('TOPO_VARIANT', '0'))
START = int(os.environ.get('TOPO_START_SHARD', '0'))

def network(seed, variant=None):
    if variant is None: variant = VARIANT
    """Whole numbers until the last division, in a fixed order of draws: fire_topo.js makes the identical network."""
    g = mulberry32(seed * 2654435761 + 777); pick = lambda n: g() % n
    shape = pick(4); n = 2 + pick(11); fault = FAULT[pick(5)]; intake = (10 + pick(191)) / 100; limit = LIMITS[pick(5)]
    subs = []
    for k in range(1, n + 1):
        kva = KVA[pick(5)]; load = kva * (25 + pick(56)) // 100; km = (5 + pick(76)) / 100
        if k == 1 or shape == 0: parent = 0
        elif shape == 1: parent = k - 1 if pick(10) < 8 else 0
        elif shape == 2: parent = pick(k)
        else: parent = 0 if k <= 3 else 1 + pick(3)
        pv = kva * (30 + pick(121)) // 100 if pick(10) < 3 else 0
        subs.append(dict(n=k, kva=kva, load_kw=load, km=km, parent=parent, pv_kw=pv))
    gen = GENS[pick(4)]; gen_at = pick(n + 1)
    # THE SAME NETWORKS, ASKED IN A DIFFERENT WAY. 1: half as much solar again on every roof that has any. 2: a connection of half
    # the fault level (a weak grid). 3: every cable three times as long (a spread out site). 4: every transformer one size down the list.
    if variant == 1:
        for s in subs: s['pv_kw'] = s['pv_kw'] * 3 // 2
    elif variant == 2: fault = fault // 2
    elif variant == 3:
        intake = intake * 3
        for s in subs: s['km'] = s['km'] * 3
    elif variant == 4:
        for s in subs: s['kva'] = KVA[max(0, KVA.index(s['kva']) - 1)]
    return dict(seed=seed, shape=SHAPES[shape], fault_mva=fault, intake_km=intake, export_limit_kw=limit, generator_kw=gen, generator_at=gen_at, subs=subs)

def solve(net, pv_share, gen_on, load_share, tol=1e-9):
    c = C; vb = c['kv'] * 1000 / math.sqrt(3)
    zs = (c['kv'] ** 2) / net['fault_mva']; xr = c['grid_x_over_r']; rs = zs / math.sqrt(1 + xr * xr)
    cable = complex(c['hv_cable_r'], c['hv_cable_x'])
    Z = {'poc': complex(rs, rs * xr), 'board': cable * net['intake_km']}; parent = {'grid': None, 'poc': 'grid', 'board': 'poc'}; S = {}; kva = {}
    tanl = math.tan(math.acos(c['load_pf'])); tang = math.tan(math.acos(c['gen_pf']))
    gen = complex(net['generator_kw'], net['generator_kw'] * tang) if gen_on else 0j
    if gen_on and net['generator_at'] == 0: S['board'] = -gen * 1000 / 3
    for s in net['subs']:
        hv, lv = 'hv%d' % s['n'], 'lv%d' % s['n']
        parent[hv] = 'board' if s['parent'] == 0 else 'hv%d' % s['parent']; parent[lv] = hv
        Z[hv] = cable * s['km']
        zt = c['tx_z_pct'] / 100 * (c['kv'] ** 2) / (s['kva'] / 1000); txr = c['tx_x_over_r']; rt = zt / math.sqrt(1 + txr * txr)
        Z[lv] = complex(rt, rt * txr); kva[lv] = s['kva']
        kw = s['load_kw'] * load_share; p = complex(kw, kw * tanl) - complex(s['pv_kw'] * pv_share, 0)
        if gen_on and net['generator_at'] == s['n']: p -= gen
        S[lv] = p * 1000 / 3
    kids = {}
    for n, p in parent.items():
        if p is not None: kids.setdefault(p, []).append(n)
    order = ['grid']
    for n in order: order += kids.get(n, [])
    V = {n: complex(vb, 0) for n in order}; rounds = 0
    while True:
        rounds += 1
        J = {n: ((S[n] / V[n]).conjugate() if n in S else 0j) for n in order}
        for n in reversed(order):
            if parent[n] is not None: J[parent[n]] += J[n]
        nv = {'grid': complex(vb, 0)}
        for n in order[1:]: nv[n] = nv[parent[n]] - J[n] * Z[n]
        step = max(abs(nv[n] - V[n]) for n in order); V = nv
        if step < tol or rounds > 300: break
    s_poc = V['poc'] * J['poc'].conjugate() * 3
    loss = sum(abs(J[n]) ** 2 * Z[n].real for n in order[1:]) * 3
    net_p = sum(S.values()).real * 3; source = (V['grid'] * J['poc'].conjugate()).real * 3
    tx = max(abs(V[n] * J[n].conjugate() * 3) / 1000 / kva[n] * 100 for n in kva)
    # the busiest cable section, in amps: what a chain or a tree adds that a star never shows
    amps = max(abs(J[n]) for n in order[1:] if n not in kva)
    vm = [abs(V[n]) / vb for n in order]
    return dict(p=s_poc.real / 1000, q=s_poc.imag / 1000, loss=loss / 1000, vmax=max(vm), vmin=min(vm), tx=tx, amps=amps, rounds=rounds,
                balance=abs(source - net_p - loss) / max(abs(net_p), 1.0))

def telling(net, case, r):
    """How telling is this case, by kind. Bigger is more telling. Only converged cases."""
    ps, g, ls = case; out = []; lim = net['export_limit_kw']; export = max(0.0, -r['p'])
    if ps > 0 and lim > 0 and export > 0: out.append(('export on the line', -abs(export - lim) / lim))
    if r['vmax'] > 1.03: out.append(('volts high on the line', -abs(r['vmax'] - C['volts_high_pu'])))
    if r['vmin'] < 0.97: out.append(('volts low on the line', -abs(r['vmin'] - C['volts_low_pu'])))
    out.append(('transformer on the line', -abs(r['tx'] - 100.0) / 100))
    inside = export <= lim and r['vmax'] <= C['volts_high_pu'] and r['vmin'] >= C['volts_low_pu'] and r['tx'] <= 100
    if inside and ps == 1.0:
        pv = sum(s['pv_kw'] for s in net['subs']); load = sum(s['load_kw'] for s in net['subs']) * ls
        if pv > 0: out.append(('most solar inside every limit', pv / max(load, 1.0)))
    return out

def shard(i):
    base = os.path.join(OUT, 'shards', 't%07d' % i); done = base + '.json'
    if os.path.exists(done): return json.load(open(done))
    t0 = time.time(); rows = []; n_ok = 0; flags = [0, 0, 0, 0]; by_shape = {}; tops = {}
    for seed in range(i * PER_SHARD, (i + 1) * PER_SHARD):
        net = network(seed); lim = net['export_limit_kw']
        for ci, case in enumerate(CASES):
            r = solve(net, *case); ok = r['rounds'] <= 300 and r['balance'] < 1e-6; n_ok += ok
            f = (1 if max(0.0, -r['p']) > lim else 0) | (2 if r['vmax'] > C['volts_high_pu'] else 0) | (4 if r['vmin'] < C['volts_low_pu'] else 0) | (8 if r['tx'] > 100 else 0)
            for b in range(4): flags[b] += (f >> b) & 1
            sh = by_shape.setdefault(net['shape'], [0, 0]); sh[0] += 1; sh[1] += 1 if (ok and f == 0) else 0
            rows.append('%d,%d,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,%d' % (seed, ci, r['p'], r['q'], r['loss'], r['vmax'], r['vmin'], r['tx'], r['amps'], r['rounds']))
            if ok:
                for kind, score in telling(net, case, r):
                    h = tops.setdefault(kind, [])
                    item = (score, seed, ci, round(r['p'], 1), round(r['vmax'], 4), round(r['vmin'], 4), round(r['tx'], 1), f)
                    if len(h) < 40: heapq.heappush(h, item)
                    elif item > h[0]: heapq.heapreplace(h, item)
    csv = base + '.csv'
    with open(csv, 'w', newline='\n') as fh: fh.write('seed,case,p_kw,q_kvar,loss_kw,vmax_pu,vmin_pu,worst_tx_pct,busiest_amps,rounds\n' + '\n'.join(rows) + '\n')
    try:
        cp = subprocess.run(['node', os.path.join(HERE, 'topo_check.mjs'), csv, str(VARIANT)], capture_output=True, text=True, timeout=900)
        check = json.loads(cp.stdout.strip().splitlines()[-1]) if cp.stdout.strip() else dict(error=(cp.stderr or 'no output')[:300])
    except Exception as e:
        check = dict(error=str(e)[:300])
    if not check.get('differed') and 'error' not in check: os.remove(csv)       # a shard that was matched in full is not kept row by row; one that differs IS kept
    out = dict(shard=i, cases=len(rows), confirmed=n_ok, export_over=flags[0], volts_high=flags[1], volts_low=flags[2], tx_over=flags[3], by_shape=by_shape,
               tops={k: sorted(v, reverse=True) for k, v in tops.items()}, seconds=round(time.time() - t0, 2), check=check)
    with open(done + '.tmp', 'w') as fh: json.dump(out, fh)
    os.replace(done + '.tmp', done)
    return out

def status(tot, n_done, n_all, t0, note):
    el = time.time() - t0
    lines = ['# TOPO STATUS  ' + time.strftime('%Y-%m-%d %H:%M:%S'), '',
             '%d of %d shards; %s cases solved in Python; %s a second this run' % (n_done, n_all, format(tot['cases'], ','), format(int(tot['run_cases'] / el) if el > 0 else 0, ',')),
             'CONFIRMED %s, REFUTED %s (the sweep did not converge or power did not balance)' % (format(tot['confirmed'], ','), format(tot['cases'] - tot['confirmed'], ',')),
             'SECOND OPINION (JavaScript, the code the Kuiper runs): matched %s, DIFFERED %s, stopped a round apart %s, neither converged %s, shards the check could not run %d' % (
                 format(tot['matched'], ','), format(tot['differed'], ','), format(tot['rounds_differ'], ','), format(tot['both_refuse'], ','), tot['errors']),
             'Over a limit: export %s; volts high %s; volts low %s; a transformer %s' % tuple(format(tot[k], ',') for k in ('export_over', 'volts_high', 'volts_low', 'tx_over')),
             'Inside every limit, by shape: ' + '; '.join('%s %s of %s' % (k, format(v[1], ','), format(v[0], ',')) for k, v in sorted(tot['by_shape'].items())), note]
    if tot['differed'] or tot['errors']: lines.append('ACT: DIFFERS or ERROR in shards ' + ', '.join(map(str, tot['bad'][:12])))
    with open(os.path.join(OUT, 'STATUS.md'), 'w') as fh: fh.write('\n'.join(lines) + '\n')
    return lines

def add(tot, d, this_run):
    tot['cases'] += d['cases']; tot['confirmed'] += d['confirmed']
    if this_run: tot['run_cases'] += d['cases']
    for k in ('export_over', 'volts_high', 'volts_low', 'tx_over'): tot[k] += d[k]
    ch = d['check']
    for k in ('matched', 'differed', 'rounds_differ', 'both_refuse'): tot[k] += ch.get(k, 0)
    if 'error' in ch: tot['errors'] += 1
    if 'error' in ch or ch.get('differed'): tot['bad'].append(d['shard'])
    for k, v in d['by_shape'].items():
        s = tot['by_shape'].setdefault(k, [0, 0]); s[0] += v[0]; s[1] += v[1]

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--seeds', type=int, default=200000); ap.add_argument('--workers', type=int, default=16); ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args(); os.makedirs(os.path.join(OUT, 'shards'), exist_ok=True)
    if a.selftest:
        n1 = network(11); assert n1 == network(11) and network(12) != n1
        r = solve(n1, 1.0, 1, 0.3); assert r['rounds'] <= 300 and r['balance'] < 1e-6, r
        print('selftest ok:', n1['shape'], len(n1['subs']), 'substations; p = %.3f kW' % r['p']); return
    n = (a.seeds + PER_SHARD - 1) // PER_SHARD; t0 = time.time()
    tot = dict(cases=0, run_cases=0, confirmed=0, export_over=0, volts_high=0, volts_low=0, tx_over=0, matched=0, differed=0, rounds_differ=0, both_refuse=0, errors=0, bad=[], by_shape={})
    todo = []
    for i in range(START, START + n):
        p = os.path.join(OUT, 'shards', 't%07d.json' % i)
        if os.path.exists(p): add(tot, json.load(open(p)), False)
        else: todo.append(i)
    k = n - len(todo); last = 0
    with Pool(a.workers) as pool:
        for d in pool.imap_unordered(shard, todo, chunksize=1):
            add(tot, d, True); k += 1
            if time.time() - last > 20: status(tot, k, n, t0, 'RUNNING'); last = time.time()
    print('\n'.join(status(tot, k, n, t0, 'FINISHED')))

if __name__ == '__main__':
    main()
