#!/usr/bin/env python3
"""tools/build.py - render index.html from experiments.json, and refuse if a log entry is not whole.

Faraday numbered every paragraph of Experimental Researches in Electricity continuously, 1 to
3430, across thirty years, so that any later paragraph could cite any earlier one by its number
alone. This keeps that discipline mechanically: an experiment missing its question, its apparatus,
its observation or its result is refused, numbers must be unique and consecutive from 1, and
nothing is renumbered.

    python tools/build.py
"""
import io
import json
import sys

REQUIRED = ['n', 'date', 'title', 'question', 'apparatus', 'did', 'observed', 'shows',
            'law', 'result', 'keys']

CSS = """
  :root { color-scheme: dark; }
  html { background:#000; }
  body { background:#000; color:#fff; font-family:Courier,monospace; padding:40px; max-width:980px; margin:0 auto; font-size:20px; line-height:1.6; }
  h1 { margin:0 0 6px; }
  a { color:#66ccff; text-decoration:none; } a:hover { text-decoration:underline; }
  header p { color:#aaa; font-size:16px; margin:0 0 10px; }
  .rule { color:#aaa; font-size:15px; border-top:1px solid #333; border-bottom:1px solid #333; padding:14px 0; margin:22px 0 10px; }
  .rule b { color:#00ffff; } .rule ol { margin:8px 0 0; padding-left:26px; } .rule li { margin:3px 0; }
  .audit { color:#7a7a7a; font-size:14px; margin:0 0 26px; }
  details.x { border-bottom:1px solid #222; }
  details.x > summary { list-style:none; cursor:pointer; padding:13px 0; font-size:19px; font-weight:bold; }
  details.x > summary::-webkit-details-marker { display:none; }
  details.x > summary::before { content:"[+] "; color:#00ffff; }
  details.x[open] > summary::before { content:"[-] "; color:#00ffff; }
  .num { color:#00ffff; } .ttl { color:#66ccff; } details.x > summary:hover .ttl { color:#9fdcff; }
  .body { margin:0 0 22px 10px; border-left:1px solid #1c1c1c; padding-left:18px; }
  .lab { display:block; color:#00ffff; font-size:12px; letter-spacing:.09em; text-transform:uppercase; margin:15px 0 5px; }
  p.t { color:#cfcfcf; font-size:15px; margin:4px 0; }
  p.q { color:#fff; font-size:17px; margin:6px 0; }
  .obs { background:#0b0b0b; border-left:2px solid #00ffff; padding:11px 13px; margin:6px 0; color:#e8e6e1; font-size:15px; overflow-x:auto; }
  .meta { color:#7a7a7a; font-size:13px; margin:6px 0 0; }
  table.keys { width:100%; border-collapse:collapse; font-size:13px; margin:6px 0 0; }
  table.keys td { padding:5px 8px 5px 0; border-bottom:1px solid #161616; vertical-align:top; color:#9aa3af; }
  table.keys td.k { color:#e8e6e1; width:34%; }
  .res { font-weight:bold; font-size:11px; letter-spacing:.07em; padding:2px 6px; border:1px solid; white-space:nowrap; }
  .res-CONFIRMED { color:#53ff4c; border-color:#2a5f27; }
  .res-REFUTED { color:#ffbe45; border-color:#6b5220; }
  .res-NOEFFECT { color:#8b919c; border-color:#33383f; }
  .res-INCONCLUSIVE { color:#8b919c; border-color:#33383f; }
  .footer { margin-top:50px; font-size:14px; color:#aaa; line-height:1.5; border-top:1px solid #333; padding-top:18px; }
  .footer a { color:#5a5a5a; }
  @media(max-width:600px){ body{padding:22px;font-size:18px} details.x>summary{font-size:17px} }
"""


def main():
    d = json.load(io.open('experiments.json', encoding='utf-8'))
    xs = d['experiments']

    problems, seen = [], set()
    for x in xs:
        for f in REQUIRED:
            if x.get(f) in (None, '', []):
                problems.append('experiment %s is missing %s' % (x.get('n', '?'), f))
        if x.get('result') not in d['results']:
            problems.append('experiment %s has unknown result %r' % (x.get('n'), x.get('result')))
        if x.get('n') in seen:
            problems.append('number %s used twice. Numbers are never reused.' % x.get('n'))
        seen.add(x.get('n'))
    expected = list(range(1, len(xs) + 1))
    if sorted(seen) != expected:
        problems.append('numbers must run consecutively from 1 with no gaps; got %s'
                        % sorted(seen))
    if problems:
        print('REFUSING TO BUILD. An experiment that is not whole does not get published.')
        for p in problems:
            print('  ' + p)
        return 1

    tally = {}
    for x in xs:
        tally[x['result']] = tally.get(x['result'], 0) + 1

    o = []
    w = o.append
    w('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">')
    w('<link rel="icon" href="data:,">\n<title>%s</title>' % d['title'])
    w('<meta name="viewport" content="width=device-width, initial-scale=1">')
    w('<style>%s</style>\n</head>\n<body>' % CSS)
    w('<header><h1>%s</h1><p>%s</p></header>' % (d['title'], d['lede']))

    w('<div class="rule"><b>The method.</b><ol>')
    for m in d['method']:
        w('  <li>%s</li>' % m)
    w('</ol></div>')

    w('<p class="audit">%d experiments &middot; %s. Numbers run continuously and are never '
      'reused. The build refuses an entry missing its question, apparatus, observation or '
      'result.</p>'
      % (len(xs), ', '.join('%d %s' % (v, k) for k, v in sorted(tally.items()))))

    w('<main>')
    for x in xs:
        cls = x['result'].replace(' ', '')
        w('<details class="x"><summary><span class="num">%d</span> &middot; '
          '<span class="ttl">%s</span></summary>' % (x['n'], x['title']))
        w('  <div class="body">')
        w('    <p class="meta">%s &middot; tests <b>%s</b> &middot; '
          '<span class="res res-%s">%s</span></p>' % (x['date'], x['law'], cls, x['result']))
        w('    <span class="lab">The question</span>')
        w('    <p class="q">%s</p>' % x['question'])
        w('    <span class="lab">Apparatus</span>')
        w('    <p class="t">%s</p>' % x['apparatus'])
        w('    <span class="lab">What was done</span>')
        w('    <p class="t">%s</p>' % x['did'])
        w('    <span class="lab">What was observed</span>')
        w('    <div class="obs">%s</div>' % x['observed'])
        w('    <span class="lab">What it shows</span>')
        w('    <p class="t">%s</p>' % x['shows'])
        w('    <span class="lab">Keys</span>')
        w('    <table class="keys">')
        for k in x['keys']:
            w('      <tr><td class="k">%s</td><td>%s</td></tr>' % (k[0], k[1]))
        w('    </table>')
        w('  </div>\n</details>')
    w('</main>')

    w('<div class="footer"><b>Disclaimer:</b> Content provided for general technical documentation '
      'and research purposes only. These are records of what was done and observed, not advice. '
      'An experiment recorded as REFUTED is a record of an error that was made here and then '
      'corrected, kept deliberately.<br><br>'
      'Built from <a href="experiments.json">experiments.json</a> by '
      '<a href="tools/build.py">tools/build.py</a>. The laws these test are at '
      '<a href="https://github.com/Ventusltd/law">Ventusltd/law</a>.<br>'
      'Code under Apache-2.0. Documentation under CC BY 4.0. No warranty is given.</div>')
    w('</body>\n</html>')

    io.open('index.html', 'w', encoding='utf-8', newline='\n').write('\n'.join(o) + '\n')
    print('built index.html: %d experiments' % len(xs))
    for k, v in sorted(tally.items()):
        print('  %-14s %d' % (k, v))
    return 0


if __name__ == '__main__':
    sys.exit(main())
