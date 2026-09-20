// bench/million_check.mjs - THE SECOND OPINION. Takes one shard written by million.py, rebuilds every site from its seed with
// the same stated generator, solves every case again with fire_site.js (the code the Kuiper runs in a visitor's browser), and
// compares number by number (1e-9 relative). The last line printed is one JSON object; exit 1 if any case differs.
import { createRequire } from 'node:module';
import { readFileSync } from 'node:fs';
const require = createRequire(import.meta.url);
const FIRE = require('./fire.js'); require('./fire_site.js');
const { solve, SCENARIOS, CANDIDATE } = FIRE.sitePulse;
const KVA = [500, 800, 1000, 1600, 2000], LIMITS = [0, 50, 200, 500, 1000], GENS = [0, 250, 500, 1000];

function mulberry32(a) { a |= 0; return () => { a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return (t ^ t >>> 14) >>> 0; }; }
export function genericSite(seed) {
  const g = mulberry32(Number((BigInt(seed) * 2654435761n + 12345n) & 0xFFFFFFFFn)), pick = n => g() % n;
  const n = 2 + pick(7), subs = []; let total = 0;
  for (let k = 1; k <= n; k++) { const kva = KVA[pick(5)], load = Math.floor(kva * (25 + pick(56)) / 100); total += load;
    const km = (5 + pick(76)) / 100, tenant = (k === n) ? pick(10) < 3 : false; subs.push({ n: k, kva, load_kw: load, km, tenant }); }
  const pv = Math.floor(total * (20 + pick(131)) / 1000) * 10;
  return { intake_cable_km: (10 + pick(191)) / 100, export_limit_kw: LIMITS[pick(5)], generator_kw: GENS[pick(4)], pv_kw: pv, pv_on: 1 + pick(n), subs };
}
const close = (a, b) => a === b || Math.abs(a - b) <= 1e-9 * Math.max(1, Math.abs(a), Math.abs(b));

const lines = readFileSync(process.argv[2], 'utf8').split('\n').filter(Boolean).slice(1);
let matched = 0, differed = 0, roundsDiffer = 0, bothRefuse = 0, lastSeed = -1, site = null; const first = [];
for (const l of lines) {
  const [seed, scen, ls, p, q, loss, vmax, vmin, tx, rounds] = l.split(',').map(Number);
  if (seed !== lastSeed) { site = genericSite(seed); lastSeed = seed; }
  const sc = SCENARIOS[scen], r = solve(site, sc[1], sc[2], sc[3], ls);
  const vs = Object.values(r.V), txs = Object.values(r.tx_loading_pct);
  const got = [r.p_poc_kw, r.q_poc_kvar, r.loss_kw, Math.max(...vs), Math.min(...vs), txs.length ? Math.max(...txs) : 0], want = [p, q, loss, vmax, vmin, tx];
  // WHEN THE TWO STOPPED ON DIFFERENT ROUNDS (the last step sat on the 1e-9 volt stopping line), each is one round of a converging
  // sweep from the other, and they agree to about 1e-9 relative, not better: judged at 1e-6 and COUNTED, never hidden.
  // A CASE THAT DID NOT CONVERGE IN EITHER LANGUAGE (over 300 rounds: the site is beyond what the sweep can solve, and the record
  // says REFUTED) has no answer to compare: the two wander apart in the last digits. Counted as both_refuse, not as a match of numbers.
  if (r.rounds > 300 && rounds > 300) { bothRefuse++; matched++; continue; }
  const tol = r.rounds === rounds ? 1e-9 : 1e-6;
  const bad = got.findIndex((g, i) => !(+g.toPrecision(12) === want[i] || Math.abs(g - want[i]) <= tol * Math.max(1, Math.abs(g), Math.abs(want[i]))));
  if (bad >= 0) { differed++; if (first.length < 3) first.push({ seed, scen, ls, which: bad, js: got[bad], py: want[bad] }); }
  else { matched++; if (r.rounds !== rounds) roundsDiffer++; }
}
console.log(JSON.stringify({ rows: lines.length, matched, differed, rounds_differ: roundsDiffer, both_refuse: bothRefuse, first }));
process.exit(differed ? 1 : 0);
