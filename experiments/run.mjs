// run.mjs - run experiments by number: node experiments/run.mjs 36 37 38
// Each experiment is experiments/eNNN.mjs, default export async () => ({ did, observed, shows, result })
// result is CONFIRMED, REFUTED or NO EFFECT. The question, apparatus and what would refute it come from INDEX.tsv.
// Writes experiments/results/eNNN.json and appends one line to experiments/LEDGER.tsv. A crash is recorded, not hidden.
import { readFileSync, writeFileSync, appendFileSync, mkdirSync, existsSync } from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { dirname, join } from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));
const rows = readFileSync(join(here, 'INDEX.tsv'), 'utf8').trim().split('\n').slice(1).map(l => {
  const [n, family, question, apparatus, refuted_if] = l.split('\t');
  return { n: +n, family, question, apparatus, refuted_if };
});
mkdirSync(join(here, 'results'), { recursive: true });
const ledger = join(here, 'LEDGER.tsv');
if (!existsSync(ledger)) writeFileSync(ledger, 'when\tn\tfamily\tresult\tseconds\tobserved\n');

let bad = 0;
for (const arg of process.argv.slice(2)) {
  const n = +arg, row = rows.find(r => r.n === n);
  const id = 'e' + String(n).padStart(3, '0');
  if (!row) { console.error('no experiment ' + arg + ' in INDEX.tsv'); bad++; continue; }
  const t0 = performance.now();
  let out;
  try {
    const mod = await import(pathToFileURL(join(here, id + '.mjs')).href);
    out = await mod.default();
    if (!['CONFIRMED', 'REFUTED', 'NO EFFECT'].includes(out.result)) throw new Error('result must be CONFIRMED, REFUTED or NO EFFECT');
  } catch (e) {
    out = { did: 'the run stopped', observed: String(e && e.stack || e).slice(0, 600), shows: 'nothing: the apparatus failed', result: 'NO EFFECT', crashed: true };
    bad++;
  }
  const seconds = +((performance.now() - t0) / 1000).toFixed(2);
  const when = new Date().toISOString();
  writeFileSync(join(here, 'results', id + '.json'), JSON.stringify({ ...row, when, seconds, ...out }, null, 1));
  appendFileSync(ledger, [when, n, row.family, out.result + (out.crashed ? ' (crashed)' : ''), seconds, String(out.observed).replace(/\s+/g, ' ').slice(0, 300)].join('\t') + '\n');
  console.log(id, out.result, seconds + 's', '|', String(out.observed).replace(/\s+/g, ' ').slice(0, 200));
}
process.exit(bad ? 1 : 0);
