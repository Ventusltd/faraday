#!/usr/bin/env python3
"""bench/million.py - SITE PULSE BY THE MILLION, EVERY TEST TESTED TWICE.

One seed = one generic site (no real one) x 8 scenarios x 3 load shares = 24 cases. Each case is solved here in Python
(site_cases.solve) and AGAIN in JavaScript (fire_site.js, the code the Kuiper runs in a visitor's browser) by million_check.mjs,
which rebuilds the same site from the same seed and must get the same numbers, or the shard is marked DIFFERS.

The site comes from a small stated generator (mulberry32, whole number arithmetic only) written identically in both languages,
because Python's random cannot be reproduced in JavaScript.

Plain Python and node: no server, no browser. Shards on E: (one file per 1,000 seeds, written whole then renamed, so a stop
at any moment loses at most the shards in flight and a restart skips what is finished). Git gets the summary, never the shards.

  python bench/million.py --seeds 420000 --workers 16        # about ten million cases
  python bench/million.py --selftest
"""
import argparse, json, math, os, subprocess, sys, time
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import site_cases as SC

OUT = os.environ.get('MILLION_OUT', r'E:\faraday-bench\million')
PER_SHARD = 1000
LOADS = (1.0, 0.6, 0.3)
KVA = (500, 800, 1000, 1600, 2000); LIMITS = (0, 50, 200, 500, 1000); GENS = (0, 250, 500, 1000)

def mulberry32(a):
    a &= 0xFFFFFFFF
    def nxt():
        nonlocal a
        a = (a + 0x6D2B79F5) & 0xFFFFFFFF
        t = a
        t = ((t ^ (t >> 15)) * (t | 1)) & 0xFFFFFFFF
        t ^= (t + (((t ^ (t >> 7)) * (t | 61)) & 0xFFFFFFFF)) & 0xFFFFFFFF
        return ((t ^ (t >> 14)) & 0xFFFFFFFF)
    return nxt

def generic_site(seed):
    """Whole numbers only until the last division, so both languages hold exactly the same site."""
    g = mulberry32(seed * 2654435761 + 12345); pick = lambda n: g() % n
    n = 2 + pick(7); subs = []; total = 0
    for k in range(1, n + 1):
        kva = KVA[pick(5)]; load = kva * (25 + pick(56)) // 100; total += load
        subs.append(dict(n=k, kva=kva, load_kw=load, km=(5 + pick(76)) / 100, tenant=(k == n and pick(10) < 3)))
    pv = (total * (20 + pick(131)) // 1000) * 10
    return dict(intake_cable_km=(10 + pick(191)) / 100, export_limit_kw=float(LIMITS[pick(5)]), generator_kw=float(GENS[pick(4)]),
                pv_kw=float(pv), pv_on=1 + pick(n), subs=subs)

def one_case(site, scen, ls):
    _, pv_share, gen_on, off = SC.SCENARIOS[scen]
    r = SC.solve(site, pv_share, gen_on, off, ls)
    ok = r['rounds'] <= 300 and r['balance'] < 1e-6
    export = max(0.0, -r['p_poc_kw']); over = max(0.0, export - site['export_limit_kw'])
    vmax = max(r['V'].values()); vmin = min(r['V'].values()); tx = max(r['tx_loading_pct'].values()) if r['tx_loading_pct'] else 0.0
    flags = (1 if over > 0 else 0) | (2 if vmax > SC.CANDIDATE['volts_high_pu'] else 0) | (4 if vmin < SC.CANDIDATE['volts_low_pu'] else 0) | (8 if tx > 100 else 0)
    return r, ok, flags, vmax, vmin, tx

def shard(i):
    path = os.path.join(OUT, 'shards', 's%06d.csv' % i); done = path + '.json'
    if os.path.exists(done): return json.load(open(done))
    t0 = time.time(); rows = []; ok_n = 0; flag_n = [0, 0, 0, 0]
    for seed in range(i * PER_SHARD, (i + 1) * PER_SHARD):
        site = generic_site(seed)
        for scen in range(1, 9):
            for ls in LOADS:
                r, ok, flags, vmax, vmin, tx = one_case(site, scen, ls)
                ok_n += ok
                for b in range(4): flag_n[b] += (flags >> b) & 1
                rows.append('%d,%d,%g,%.12g,%.12g,%.12g,%.12g,%.12g,%.12g,%d,%.3g,%d,%d' % (seed, scen, ls, r['p_poc_kw'], r['q_poc_kvar'], r['loss_kw'], vmax, vmin, tx, r['rounds'], r['balance'], flags, 1 if ok else 0))
    tmp = path + '.tmp'
    with open(tmp, 'w', newline='\n') as f: f.write('seed,scenario,load_share,p_kw,q_kvar,loss_kw,vmax_pu,vmin_pu,worst_tx_pct,rounds,balance,flags,ok\n' + '\n'.join(rows) + '\n')
    os.replace(tmp, path)
    # THE SECOND OPINION: the same shard, rebuilt from the seeds and solved again by the code the browser runs
    try:
        c = subprocess.run(['node', os.path.join(HERE, 'million_check.mjs'), path], capture_output=True, text=True, timeout=600)
        check = json.loads(c.stdout.strip().splitlines()[-1]) if c.returncode in (0, 1) and c.stdout.strip() else dict(error=(c.stderr or 'no output')[:300])
    except Exception as e:
        check = dict(error=str(e)[:300])
    out = dict(shard=i, cases=len(rows), confirmed=ok_n, refuted=len(rows) - ok_n, export_over=flag_n[0], volts_high=flag_n[1], volts_low=flag_n[2], tx_over=flag_n[3],
               seconds=round(time.time() - t0, 2), check=check)
    with open(done + '.tmp', 'w') as f: json.dump(out, f)
    os.replace(done + '.tmp', done)
    return out

def status(done, total_shards, t0, note=''):
    cases = sum(d['cases'] for d in done); conf = sum(d['confirmed'] for d in done)
    matched = sum(d['check'].get('matched', 0) for d in done); differed = sum(d['check'].get('differed', 0) for d in done)
    rdiff = sum(d['check'].get('rounds_differ', 0) for d in done); errs = [d['shard'] for d in done if 'error' in d['check']]
    el = time.time() - t0; rate = cases / el if el > 0 else 0
    lines = ['# MILLION STATUS  ' + time.strftime('%Y-%m-%d %H:%M:%S'), '',
             '%d of %d shards; %s cases solved in Python; %s a second this run' % (len(done), total_shards, format(cases, ','), format(int(rate), ',')),
             'CONFIRMED %s, REFUTED %s (did not converge or power did not balance)' % (format(conf, ','), format(cases - conf, ',')),
             'SECOND OPINION (JavaScript, the code the Kuiper runs): matched %s, DIFFERED %s, rounds differ by count only %s, shards the check could not run %d' % (format(matched, ','), format(differed, ','), format(rdiff, ','), len(errs)),
             'What the sites showed: export over the limit %s; volts over 1.06 %s; volts under 0.94 %s; a transformer over its rating %s' % tuple(format(sum(d[k] for d in done), ',') for k in ('export_over', 'volts_high', 'volts_low', 'tx_over')),
             note]
    if differed or errs: lines.append('ACT: BLOCKED or DIFFERS. first shards: ' + ', '.join(str(d['shard']) for d in done if d['check'].get('differed') or 'error' in d['check'])[:200])
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, 'STATUS.md'), 'w') as f: f.write('\n'.join(lines) + '\n')
    return lines

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--seeds', type=int, default=42000); ap.add_argument('--workers', type=int, default=16); ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args()
    os.makedirs(os.path.join(OUT, 'shards'), exist_ok=True)
    if a.selftest:
        s1, s2 = generic_site(7), generic_site(7); assert s1 == s2 and generic_site(8) != s1
        r, ok, *_ = one_case(SC.standard_site(), 3, 0.3); assert ok and abs(r['p_poc_kw'] - (-209.1)) < 0.06, r['p_poc_kw']
        print('selftest ok; site 7:', json.dumps(s1)[:200]); return
    n = (a.seeds + PER_SHARD - 1) // PER_SHARD; t0 = time.time(); done = []
    with Pool(a.workers) as pool:
        for d in pool.imap_unordered(shard, range(n)):
            done.append(d)
            if len(done) % 5 == 0 or len(done) == n: status(done, n, t0, 'RUNNING' if len(done) < n else 'FINISHED')
    print('\n'.join(status(done, n, t0, 'FINISHED')))

if __name__ == '__main__':
    main()
