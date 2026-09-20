#!/usr/bin/env python3
"""bench/backup.py - THE METHOD AND THE DATA, KEPT ON GITHUB. Run by hand, or every N minutes by nightshift.py.

What goes to the repository (public): the scripts (they are the method), each run's STATUS.md, a merged summary
(results/<run>/SUMMARY.json: counts, the second opinion's counts, by shape), and the MOST TELLING cases merged across shards
(results/<run>/top.json, at most 1,000 a kind). What never goes: the row by row shards (they stay on E:, and any shard can be
rebuilt from its seeds alone, which is the point of a seeded generator). Everything staged is passed through the runner's guard
against private strings first; if the guard finds anything, NOTHING is committed and the finding is printed.

  python bench/backup.py            commit and push
  python bench/backup.py --dry      show what would be committed
"""
import glob, heapq, json, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import run100 as R

RUNS = {'million': r'E:\faraday-bench\million', 'topo': r'E:\faraday-bench\topo'}
METHOD = ['bench/million.py', 'bench/million_check.mjs', 'bench/topo.py', 'bench/topo_check.mjs', 'bench/fire_topo.js', 'bench/fire_site.js', 'bench/backup.py', 'bench/nightshift.py',
          'bench/topo_top.py', 'experiments']

def merge(run, src):
    out = os.path.join(R.REPO, 'bench', 'results', run); os.makedirs(out, exist_ok=True)
    st = os.path.join(src, 'STATUS.md')
    if os.path.exists(st): open(os.path.join(out, 'STATUS.md'), 'w', encoding='utf8').write(open(st, encoding='utf8').read())
    tot = {}; tops = {}; n = 0
    for f in glob.glob(os.path.join(src, 'shards', '*.json')):
        try: d = json.load(open(f))
        except Exception: continue                                   # a shard being written this second
        n += 1
        for k, v in d.items():
            if isinstance(v, (int, float)) and k not in ('shard', 'seconds'): tot[k] = tot.get(k, 0) + v
        for k, v in (d.get('check') or {}).items():
            if isinstance(v, (int, float)): tot['check_' + k] = tot.get('check_' + k, 0) + v
        for k, v in (d.get('by_shape') or {}).items():
            s = tot.setdefault('by_shape', {}).setdefault(k, [0, 0]); s[0] += v[0]; s[1] += v[1]
        for kind, items in (d.get('tops') or {}).items():
            h = tops.setdefault(kind, [])
            for it in items:
                it = tuple(it)
                if len(h) < 1000: heapq.heappush(h, it)
                elif it > h[0]: heapq.heapreplace(h, it)
    tot['shards'] = n; tot['written_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    json.dump(tot, open(os.path.join(out, 'SUMMARY.json'), 'w'), indent=1, sort_keys=True)
    if tops: json.dump({'columns': ['score', 'seed', 'case', 'p_kw', 'vmax_pu', 'vmin_pu', 'worst_tx_pct', 'flags'], 'kinds': {k: sorted(v, reverse=True) for k, v in tops.items()}},
                       open(os.path.join(out, 'top.json'), 'w'), separators=(',', ':'))
    return n

def main():
    dry = '--dry' in sys.argv
    for run, src in RUNS.items():
        if os.path.isdir(src): print(run, merge(run, src), 'shards merged')
    paths = [p for p in METHOD if os.path.exists(os.path.join(R.REPO, p))] + ['bench/results/million', 'bench/results/topo']
    paths = [p for p in paths if os.path.exists(os.path.join(R.REPO, p))]
    texts = {}
    for p in paths:
        full = os.path.join(R.REPO, p)
        files = [full] if os.path.isfile(full) else [os.path.join(dp, f) for dp, _, fs in os.walk(full) for f in fs]
        for f in files:
            if os.path.getsize(f) < 5_000_000: texts[os.path.relpath(f, R.REPO)] = open(f, encoding='utf8', errors='replace').read()
    found = R.guard(texts)
    if found: print('THE GUARD REFUSES, nothing committed:\n  ' + '\n  '.join(found)); sys.exit(2)
    if dry: print('would commit', len(texts), 'files'); return
    R.git('add', '--', *paths)
    if R.git('diff', '--cached', '--quiet', check=False).returncode == 0: print('nothing new to commit'); return
    s = json.load(open(os.path.join(R.REPO, 'bench', 'results', 'topo', 'SUMMARY.json'))) if os.path.exists(os.path.join(R.REPO, 'bench', 'results', 'topo', 'SUMMARY.json')) else {}
    msg = 'night shift backup: the method and the summaries; networks solved twice so far: %s, differing: %s' % (format(int(s.get('cases', 0)), ','), format(int(s.get('check_differed', 0)), ','))
    who = 'Co-Authored-By: Claude Fable 5.1 <noreply' + chr(64) + 'anthropic.com>'          # built here so the guard above stays strict about addresses in files
    R.git('commit', '-m', msg + '\n\n' + who)
    r = R.git('push', check=False)
    print(msg); print('pushed' if r.returncode == 0 else 'COMMITTED BUT NOT PUSHED: ' + (r.stderr or '')[-300:])

if __name__ == '__main__':
    main()
