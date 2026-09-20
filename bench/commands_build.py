#!/usr/bin/env python3
"""bench/commands_build.py - THE COMMAND LIST, BUILT LIKE A GRIDATLAS RELEASE.

The page's "choose an example sentence" list is not written into the page: the page fetches it. This builds that list from
the networks the bench has already solved, and publishes it the way the Atlas publishes a composition:

  a POINTER   bench/results/commands/current.json   - which generation is live, which file it is, its sha256 and its length
  a FILE      bench/results/commands/commands-<generation>.json  - the list itself, named after its generation, never edited

so a reader can fetch the pointer with no cache, fetch the file it names, re-hash the bytes it received and refuse anything
that does not match. The previous generation is kept in the pointer, so a roll back is one line.

WHAT IS IN THE LIST. bench/results/topo/top.json holds the most telling cases found so far, by kind, merged across every
shard of the billion-case run. The best 200 of each of the five kinds make up to 1,000 commands. Nothing is padded: a kind
with fewer cases contributes fewer. Nothing is run here - every number in a sentence is read from the row that was solved
twice (once in Python, once in JavaScript) and the sentence only describes it. No claim words: a sentence says what was
computed, never that it is good, safe or best. bench/commands_check.mjs then fires every command and checks the numbers.

  python bench/commands_build.py            build a new generation
  python bench/commands_build.py --check    re-read the pointer, re-hash the file it names, and fail on any mismatch
"""
import hashlib, io, json, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import topo

TOP = os.path.join(HERE, 'results', 'topo', 'top.json')
OLD_LIST = os.path.join(HERE, 'results', 'commands.json')
OUT = os.path.join(HERE, 'results', 'commands')
PER_KIND = 200
LIST_SCHEMA = 'faraday.commands.v2'
POINTER_SCHEMA = 'faraday.commands.current.v1'

SOLAR = {0.0: 'no solar', 0.5: 'half solar', 1.0: 'full solar'}
LOAD = {1.0: 'full load', 0.6: 'load at 60 per cent', 0.3: 'load at 30 per cent'}
# the four shapes as a reader would say them: "a sub-boards of 8 substations" is not English
SHAPE = {'star': 'A star', 'chain': 'A chain', 'tree': 'A tree', 'sub-boards': 'A sub-board network'}


def when(case):
    """The operating case in words, in the order topo.CASES holds it."""
    ps, g, ls = topo.CASES[case]
    return '%s, generator %s, %s' % (SOLAR[ps], 'running' if g else 'off', LOAD[ls])


def kw(x):
    return '%d kW' % round(x)


def sentence(kind, net, case, p_kw, vmax, vmin, tx):
    """A description of one solved case, from the row and the network. Nothing here is computed again."""
    head = '%s of %d substations: ' % (SHAPE.get(net['shape'], 'A ' + net['shape']), len(net['subs']))
    tail = ', at ' + when(case)
    if kind == 'export on the line':
        export = max(0.0, -p_kw)
        limit = net['export_limit_kw']
        gap = export - limit
        if gap > 0:
            body = 'export %s, %s over its %s limit' % (kw(export), kw(gap), kw(limit))
        elif round(-gap) == 0:
            body = 'export %s, on its %s limit' % (kw(export), kw(limit))
        else:
            body = 'export %s, within %s of its %s limit' % (kw(export), kw(-gap), kw(limit))
    elif kind == 'volts high on the line':
        body = 'highest voltage %.4f against the %s line' % (vmax, topo.C['volts_high_pu'])
    elif kind == 'volts low on the line':
        body = 'lowest voltage %.4f against the %s line' % (vmin, topo.C['volts_low_pu'])
    elif kind == 'transformer on the line':
        body = 'busiest transformer at %.1f per cent of its rating' % tx
    elif kind == 'most solar inside every limit':
        ps, _g, ls = topo.CASES[case]
        pv = sum(s['pv_kw'] for s in net['subs']) * ps
        load = sum(s['load_kw'] for s in net['subs']) * ls
        body = '%s of solar against %s of load, every figure inside its limit' % (kw(pv), kw(load))
    else:
        body = 'connection point %s, volts %.4f to %.4f, busiest transformer %.1f per cent' % (kw(p_kw), vmin, vmax, tx)
    return head + body + tail


def command(seed, case):
    ps, g, ls = topo.CASES[case]
    return 'fire network {"seed":%d,"solar":%s,"generator":%d,"load":%s}' % (seed, repr(ps), g, repr(ls))


def build_network_commands():
    top = json.load(io.open(TOP, encoding='utf-8'))
    cols = top['columns']
    want = ['score', 'seed', 'case', 'p_kw', 'vmax_pu', 'vmin_pu', 'worst_tx_pct', 'flags']
    if cols != want:
        raise SystemExit('top.json does not have the columns this reads: %r' % (cols,))
    out = []
    for kind in sorted(top['kinds']):
        rows = top['kinds'][kind]
        rows = sorted(rows, reverse=True)[:PER_KIND]          # already sorted; sorted again so the choice never depends on that
        for _score, seed, case, p_kw, vmax, vmin, tx, flags in rows:
            net = topo.network(seed)
            out.append(dict(family='NETWORKS', kind=kind, sentence=sentence(kind, net, case, p_kw, vmax, vmin, tx),
                            command=command(seed, case), seed=seed, case=case,
                            row=dict(p_kw=p_kw, vmax_pu=vmax, vmin_pu=vmin, worst_tx_pct=tx, flags=flags)))
    return out


def site_pulse_commands():
    """The sentences that already draw a reader in, carried forward unchanged from the list the page fetches today."""
    if not os.path.exists(OLD_LIST):
        return []
    old = json.load(io.open(OLD_LIST, encoding='utf-8'))
    return [dict(family='SITE PULSE', kind='site pulse', sentence=e['sentence'], command=e['command'], seed=None, case=None)
            for e in old.get('commands', []) if e.get('family') == 'SITE PULSE']


def sha256_of(path):
    h = hashlib.sha256()
    with io.open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def check():
    """Read the pointer as a stranger would, re-hash the file it names, and say exactly what is wrong if anything is."""
    p = os.path.join(OUT, 'current.json')
    if not os.path.exists(p):
        raise SystemExit('CHECK FAILED: there is no pointer at ' + os.path.relpath(p, HERE))
    cur = json.load(io.open(p, encoding='utf-8'))
    bad = []
    if cur.get('schema') != POINTER_SCHEMA:
        bad.append('the pointer says schema %r, not %r' % (cur.get('schema'), POINTER_SCHEMA))
    f = os.path.join(OUT, cur.get('file', ''))
    if not cur.get('file') or not os.path.exists(f):
        bad.append('the pointer names %r and there is no such file beside it' % (cur.get('file'),))
    else:
        got = sha256_of(f)
        size = os.path.getsize(f)
        if got != cur.get('sha256'):
            bad.append('the file hashes to %s and the pointer says %s' % (got[:16], str(cur.get('sha256'))[:16]))
        if size != cur.get('bytes'):
            bad.append('the file is %d bytes and the pointer says %s' % (size, cur.get('bytes')))
        lst = json.load(io.open(f, encoding='utf-8'))
        if lst.get('schema') != LIST_SCHEMA:
            bad.append('the list says schema %r, not %r' % (lst.get('schema'), LIST_SCHEMA))
        if lst.get('generation') != cur.get('generation'):
            bad.append('the list is generation %r and the pointer says %r' % (lst.get('generation'), cur.get('generation')))
        if len(lst.get('commands', [])) != cur.get('count') or lst.get('count') != cur.get('count'):
            bad.append('the pointer counts %s and the list holds %d' % (cur.get('count'), len(lst.get('commands', []))))
    if bad:
        raise SystemExit('CHECK FAILED:\n  ' + '\n  '.join(bad))
    print('check ok: generation %s, %d commands, sha256 %s, %d bytes'
          % (cur['generation'], cur['count'], cur['sha256'][:12], cur['bytes']))


def main():
    if '--check' in sys.argv:
        return check()
    os.makedirs(OUT, exist_ok=True)
    cmds = build_network_commands() + site_pulse_commands()
    gen = time.strftime('%Y%m%d%H%M', time.gmtime())
    name = 'commands-%s.json' % gen
    doc = dict(schema=LIST_SCHEMA, generation=gen, generated_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
               count=len(cmds), commands=cmds)
    path = os.path.join(OUT, name)
    with io.open(path, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(doc, fh, separators=(',', ':'))
    prev = None
    p = os.path.join(OUT, 'current.json')
    if os.path.exists(p):
        try:
            prev = json.load(io.open(p, encoding='utf-8')).get('generation')
        except Exception:
            prev = None
    pointer = dict(schema=POINTER_SCHEMA, generation=gen, previous_generation=prev, file=name,
                   sha256=sha256_of(path), bytes=os.path.getsize(path), count=len(cmds))
    with io.open(p, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(pointer, fh, indent=1)
        fh.write('\n')
    by = {}
    for c in cmds:
        by[c['kind']] = by.get(c['kind'], 0) + 1
    print('generation %s: %d commands (%s)' % (gen, len(cmds), '; '.join('%s %d' % kv for kv in sorted(by.items()))))
    print('  ' + name + '  sha256 ' + pointer['sha256'][:12] + '  ' + format(pointer['bytes'], ',') + ' bytes')
    if prev:
        print('  previous generation ' + prev)
    check()


if __name__ == '__main__':
    main()
