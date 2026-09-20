#!/usr/bin/env python3
r"""bench/run100.py - run the hundred on this machine, keep every result, commit to GitHub after each 25.

    python bench/run100.py --selftest      the runner proves it can catch a failure, a hang and a bad commit guard. Run first.
    python bench/run100.py                 run whatever has not yet run; safe to stop and start again at any time
    python bench/run100.py --workers 8     how many tests at once (default 8; this machine has 24 cores and about 9 GB free)
    python bench/run100.py --no-push       commit locally, do not push (for a dry night)

WATERTIGHT, MEANING:
  - one test = one process of its own with a time limit; a hang is killed and recorded as TIMEOUT; a crash is recorded as ERROR;
    neither stops the run.
  - the ledger on the E: drive is append only, one line a result, written and flushed the moment a result exists. Start the script
    again and it reads the ledger and runs only what is missing. Power cut, closed window, reboot: nothing is lost, nothing reruns.
  - results are copied into the repository and committed after every 25th result, then fetch, rebase, push, three tries. A push that
    fails loses nothing: the commit stands and the next batch pushes both.
  - before any commit a guard reads what is about to be committed and refuses paths of this machine, e-mail addresses and the names
    of private repositories. A refused commit is logged, not forced.
NOT BLOCKED, MEANING (the security program stopped Python on 19 September for a listening proxy and bursts of thirty processes):
  - no server, no socket, no proxy, no browser. Plain Python and git only.
  - a fixed small pool; starts are spaced a fifth of a second apart; never more than --workers processes alive.
  - it runs from a committed folder and rewrites no scripts.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
LEDGER_DIR = os.environ.get('BENCH_DIR', r'E:\faraday-bench')
LEDGER = os.path.join(LEDGER_DIR, 'ledger.jsonl')
RESULTS = os.path.join(HERE, 'results')
TOTAL = 100
BATCH = 25
TIMEOUT = 300
GUARD = [(re.compile(r'[A-Za-z]:\\Users\\|/c/Users/|AppData', re.I), 'a path of this machine'),
         (re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}'), 'an e-mail address'),
         (re.compile(r'\b(gis-sld-sandbox|pipelinenews-gridatlas-20260906|cable_selection)\b'), 'the name of a private repository')]
_lock = threading.Lock()
_start_gate = threading.Lock()


def log(msg):
    line = time.strftime('%Y-%m-%d %H:%M:%S ') + msg
    print(line, flush=True)
    with _lock, io.open(os.path.join(LEDGER_DIR, 'run.log'), 'a', encoding='utf-8') as f:
        f.write(line + '\n')


def write_status(done, note=''):
    """STATUS.md beside the ledger: thirty lines a supervisor can read in one glance instead of the whole ledger."""
    rows = [done[k] for k in sorted(done)]
    tally = {}
    for r in rows:
        tally[r['result']] = tally.get(r['result'], 0) + 1
    odd = [r for r in rows if r['result'] not in ('CONFIRMED',)][-12:]
    lines = ['# STATUS  ' + time.strftime('%Y-%m-%d %H:%M:%S'), '', '%d of %d run. %s' % (len(rows), TOTAL, ', '.join('%s %d' % kv for kv in sorted(tally.items()))), note, '',
             'Not confirmed (latest twelve):'] + ['- %s %s %s: %s' % (r['n'], r.get('family', ''), r['result'], str(r.get('observed', ''))[:140]) for r in odd]
    tmp = os.path.join(LEDGER_DIR, 'STATUS.md.tmp')
    with io.open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')
    os.replace(tmp, os.path.join(LEDGER_DIR, 'STATUS.md'))


def read_ledger(path=None):
    done = {}
    path = path or LEDGER
    if os.path.exists(path):
        with io.open(path, encoding='utf-8') as f:
            for ln in f:
                ln = ln.strip()
                if not ln:
                    continue
                try:
                    r = json.loads(ln)
                    done[int(r['n'])] = r
                except Exception:
                    pass                                   # a torn last line after a power cut: that test simply runs again
    return done


def append_ledger(rec, path=None):
    with _lock, io.open(path or LEDGER, 'a', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(rec, sort_keys=True) + '\n'); f.flush(); os.fsync(f.fileno())


def run_one(n, script=None, timeout=TIMEOUT):
    with _start_gate:                                      # starts are spaced: never a burst of processes
        time.sleep(0.2)
    t0 = time.time()
    try:
        p = subprocess.run([sys.executable, script or os.path.join(HERE, 'one.py'), str(n)], capture_output=True, text=True,
                           timeout=timeout, cwd=REPO, env={**os.environ, 'PYTHONIOENCODING': 'utf-8'})
        line = (p.stdout or '').strip().splitlines()[-1] if (p.stdout or '').strip() else ''
        rec = json.loads(line) if line else dict(n=n, result='ERROR', observed='no output; exit %s; %s' % (p.returncode, (p.stderr or '')[-300:]))
    except subprocess.TimeoutExpired:
        rec = dict(n=n, result='TIMEOUT', observed='killed after %d s' % timeout)
    except Exception as e:
        rec = dict(n=n, result='ERROR', observed='%s: %s' % (type(e).__name__, e))
    rec.setdefault('n', n); rec['wall_seconds'] = round(time.time() - t0, 2); rec['ran_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    return rec


def git(*a, check=True):
    r = subprocess.run(['git', '-C', REPO] + list(a), capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError('git %s: %s' % (' '.join(a), (r.stderr or r.stdout).strip()[-400:]))
    return r


def guard(texts):
    """Refuse to commit anything private. texts: {name: content}. Returns a list of findings."""
    found = []
    for name, text in texts.items():
        for rx, what in GUARD:
            m = rx.search(text)
            if m:
                found.append('%s holds %s (%s)' % (name, what, m.group(0)[:40]))
    return found


def write_results(done):
    """The repository's copy: the ledger in order, and a summary a person can read."""
    os.makedirs(RESULTS, exist_ok=True)
    rows = [done[k] for k in sorted(done)]
    led = ''.join(json.dumps(r, sort_keys=True) + '\n' for r in rows)
    tally = {}
    for r in rows:
        tally.setdefault(r.get('family', '?'), {}).setdefault(r['result'], 0)
        tally[r.get('family', '?')][r['result']] += 1
    md = ['# The hundred: results so far', '', '%d of %d run. Every line below is one test; rerun any of them with `python bench/one.py N`.' % (len(rows), TOTAL), '',
          '| family | ' + ' | '.join(sorted({r['result'] for r in rows})) + ' |', '|---|' + '---|' * len({r['result'] for r in rows})]
    for fam, t in tally.items():
        md.append('| %s | ' % fam + ' | '.join(str(t.get(k, 0)) for k in sorted({r['result'] for r in rows})) + ' |')
    md += ['', '| n | family | test | result | what was seen |', '|---|---|---|---|---|']
    for r in rows:
        md.append('| %s | %s | %s | %s | %s |' % (r['n'], r.get('family', ''), r.get('name', ''), r['result'], str(r.get('observed', '')).replace('|', '/')[:160]))
    import page                                              # the hundred as cells: one static page made from the same rows
    texts = {'bench/results/ledger.jsonl': led, 'bench/results/RESULTS.md': '\n'.join(md) + '\n', 'bench/results/index.html': page.build(rows)}
    bad = guard(texts)
    if bad:
        return bad
    for rel, text in texts.items():
        tmp = os.path.join(REPO, rel + '.tmp')
        with io.open(tmp, 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
        os.replace(tmp, os.path.join(REPO, rel))            # whole file or nothing
    return []


def commit_and_push(done, push=True):
    bad = write_results(done)
    if bad:
        log('COMMIT REFUSED by the guard: ' + '; '.join(bad)); return False
    git('add', 'bench/results')
    if git('diff', '--cached', '--quiet', check=False).returncode == 0:
        return True
    rows = [done[k] for k in sorted(done)]
    c = sum(r['result'] == 'CONFIRMED' for r in rows); f = sum(r['result'] == 'REFUTED' for r in rows); o = len(rows) - c - f
    msg = 'the hundred: %d of %d run on this machine: %d confirmed, %d refuted, %d other' % (len(rows), TOTAL, c, f, o)
    git('commit', '-q', '-m', msg, '-m', 'Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01FgogTWXuEXXcTgLTfWeaKB')
    log('COMMITTED: ' + msg)
    if not push:
        return True
    for attempt in (1, 2, 3):
        try:
            git('fetch', '-q', 'origin'); git('rebase', '-q', 'origin/main'); git('push', '-q', 'origin', 'HEAD:main')
            log('PUSHED to GitHub (try %d)' % attempt); return True
        except Exception as e:
            git('rebase', '--abort', check=False); log('push try %d failed: %s' % (attempt, str(e)[:200])); time.sleep(5 * attempt)
    log('NOT PUSHED: the commit stands locally and goes out with the next batch'); return False


def main(argv):
    os.makedirs(LEDGER_DIR, exist_ok=True)
    if '--selftest' in argv:
        return selftest()
    workers = int(argv[argv.index('--workers') + 1]) if '--workers' in argv else 8
    push = '--no-push' not in argv
    done = read_ledger(); todo = [n for n in range(1, TOTAL + 1) if n not in done]
    log('START: %d already in the ledger, %d to run, %d at once, ledger %s' % (len(done), len(todo), workers, LEDGER))
    since = len(done) % BATCH
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(run_one, n): n for n in todo}
        for fut in as_completed(futs):
            rec = fut.result(); append_ledger(rec); done[int(rec['n'])] = rec; since += 1
            log('%3d %-13s %-9s %s' % (rec['n'], rec.get('family', ''), rec['result'], str(rec.get('observed', ''))[:110]))
            if since >= BATCH:
                since = 0; pushed = commit_and_push(dict(done), push); write_status(dict(done), 'RUNNING. last batch %s.' % ('pushed' if pushed else 'NOT pushed'))
    pushed = commit_and_push(dict(done), push); write_status(dict(done), 'FINISHED. last batch %s.' % ('pushed' if pushed else 'NOT pushed'))
    rows = list(done.values())
    log('END: %d run: %s' % (len(rows), {k: sum(r['result'] == k for r in rows) for k in sorted({r['result'] for r in rows})}))
    return 0 if len(done) == TOTAL else 1


def selftest():
    """The runner must catch a failing test, a hanging test and a private string, and must resume from a torn ledger."""
    import tempfile
    d = tempfile.mkdtemp(prefix='bench-selftest-'); ok = True
    def say(name, good):
        nonlocal ok
        ok = ok and good; print(('PASS  ' if good else 'FAIL  ') + name, flush=True)
    hang = os.path.join(d, 'hang.py'); io.open(hang, 'w').write('import time\ntime.sleep(60)\n')
    boom = os.path.join(d, 'boom.py'); io.open(boom, 'w').write('raise SystemExit(3)\n')
    good = os.path.join(d, 'good.py'); io.open(good, 'w').write('import json,sys\nprint(json.dumps({"n": int(sys.argv[1]), "result": "CONFIRMED"}))\n')
    say('a hanging test is killed and recorded as TIMEOUT', run_one(1, hang, timeout=3)['result'] == 'TIMEOUT')
    say('a crashing test is recorded as ERROR, the run goes on', run_one(2, boom)['result'] == 'ERROR')
    say('a good test is recorded as it reports', run_one(3, good)['result'] == 'CONFIRMED')
    led = os.path.join(d, 'ledger.jsonl')
    append_ledger({'n': 1, 'result': 'CONFIRMED'}, led); io.open(led, 'a').write('{"n": 2, "resu')       # a torn line, as after a power cut
    say('a torn ledger is read up to the tear; the torn test will run again', sorted(read_ledger(led)) == [1])
    say('the guard refuses a path of this machine', bool(guard({'x': 'see C:\\Users\\somebody\\file'})))
    say('the guard refuses an e-mail address', bool(guard({'x': 'write to someone@example.com'})))
    say('the guard passes clean text', not guard({'x': '41 places, lowest voltage 0.97 of nominal'}))
    import tests
    a, b = tests.run(31), tests.run(31)
    say('the same test gives the same fingerprint twice', a['fingerprint'] == b['fingerprint'])
    say('the planted fault in LOGIC is caught (test 40 is CONFIRMED only because the check saw the fault)', tests.run(40)['result'] == 'CONFIRMED' and tests.run(40)['numbers']['wrong'] > 0)
    print('SELFTEST ' + ('PASS' if ok else 'FAIL'), flush=True)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
