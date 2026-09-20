#!/usr/bin/env python3
"""bench/one.py N - run test N in a process of its own and print its record as one line of JSON. Nothing else."""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    n = int(sys.argv[1]); t0 = time.time()
    try:
        import tests
        rec = tests.run(n)
    except Exception as e:                                  # a test that throws is a result, not a crash of the run
        rec = dict(n=n, result='ERROR', observed='%s: %s' % (type(e).__name__, e))
    rec['seconds'] = round(time.time() - t0, 2)
    sys.stdout.write(json.dumps(rec, sort_keys=True) + '\n')

if __name__ == '__main__':
    main()
