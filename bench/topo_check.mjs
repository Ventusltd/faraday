// bench/topo_check.mjs - THE SECOND OPINION for bench/topo.py. One shard in; every network rebuilt from its seed by fire_topo.js
// (the code the Kuiper runs), every case solved again, every number compared. Same rounds: 1e-9 relative. A round apart: 1e-6,
// counted. Neither converged: counted as both_refuse, no numbers compared. Last line printed is one JSON object.
import { createRequire } from 'node:module';
import { readFileSync } from 'node:fs';
const require = createRequire(import.meta.url);
const FIRE = require('./fire.js'); require('./fire_topo.js');
const { network, solve, CASES } = FIRE.topo;
const lines = readFileSync(process.argv[2], 'utf8').split('\n').filter(Boolean).slice(1);
let matched = 0, differed = 0, roundsDiffer = 0, bothRefuse = 0, last = -1, net = null; const first = [];
for (const l of lines) {
  const [seed, ci, p, q, loss, vmax, vmin, tx, amps, rounds] = l.split(',').map(Number);
  if (seed !== last) { net = network(seed, +(process.argv[3] || 0)); last = seed; }
  const c = CASES[ci], r = solve(net, c[0], !!c[1], c[2]);
  if (r.rounds > 300 && rounds > 300) { bothRefuse++; matched++; continue; }
  const tol = r.rounds === rounds ? 1e-9 : 1e-6, got = [r.p, r.q, r.loss, r.vmax, r.vmin, r.tx, r.amps], want = [p, q, loss, vmax, vmin, tx, amps];
  const bad = got.findIndex((g, i) => !(+g.toPrecision(12) === want[i] || Math.abs(g - want[i]) <= tol * Math.max(1, Math.abs(g), Math.abs(want[i]))));
  if (bad >= 0) { differed++; if (first.length < 3) first.push({ seed, case: ci, which: bad, js: got[bad], py: want[bad], js_rounds: r.rounds, py_rounds: rounds }); }
  else { matched++; if (r.rounds !== rounds) roundsDiffer++; }
}
console.log(JSON.stringify({ rows: lines.length, matched, differed, rounds_differ: roundsDiffer, both_refuse: bothRefuse, first }));
process.exit(differed ? 1 : 0);
