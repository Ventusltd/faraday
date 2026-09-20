// bench/fire_check.mjs - the browser's commands against the saved records: same inputs, same numbers, or the port is wrong.
//   node bench/fire_check.mjs        exits 1 on any difference
import { readFileSync, existsSync } from 'node:fs';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
const here = dirname(fileURLToPath(import.meta.url)), require = createRequire(import.meta.url);
const FIRE = require(join(here, 'fire.js'));
if (existsSync(join(here, 'fire_site.js'))) { globalThis.FIRE = FIRE; require(join(here, 'fire_site.js')); }
const rows = readFileSync(join(here, 'results', 'ledger.jsonl'), 'utf8').split('\n').filter(Boolean).map(l => JSON.parse(l));
const same = (a, b) => (a === null || b === null || typeof a !== 'number' || typeof b !== 'number') ? JSON.stringify(a) === JSON.stringify(b) : Math.abs(a - b) <= 1e-6 * Math.max(1, Math.abs(a), Math.abs(b));
const tally = {}; let bad = 0;
for (const r of rows) {
  if (!r.command) continue;
  let c; try { c = FIRE.parse(r.command); } catch { continue; }
  if (!FIRE.names.includes(c.name)) continue;
  const o = FIRE.fire(r.command); tally[c.name] = tally[c.name] || { matched: 0, differed: 0 };
  const diffs = Object.keys(r.numbers).filter(k => k in o.numbers && !same(o.numbers[k], r.numbers[k]));
  const missing = Object.keys(r.numbers).filter(k => !(k in o.numbers) && !/error|rounds/.test(k));
  if (diffs.length || missing.length) { tally[c.name].differed++; if (bad++ < 5) console.log('DIFFERS record', r.n, c.name, diffs.map(k => k + ': js ' + o.numbers[k] + ' py ' + r.numbers[k]).join('; '), missing.length ? 'missing ' + missing.join(',') : ''); }
  else tally[c.name].matched++;
}
for (const [k, v] of Object.entries(tally)) console.log(k.padEnd(20), 'matched', v.matched, 'differed', v.differed);
console.log(bad ? 'FIRE CHECK FAIL' : 'FIRE CHECK PASS'); process.exit(bad ? 1 : 0);
