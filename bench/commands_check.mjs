// bench/commands_check.mjs - THE SECOND OPINION ON THE LIST ITSELF. Reads the pointer the way a browser will, re-hashes the
// file it names, and then FIRES EVERY COMMAND in the list through FIRE - the same code a visitor's browser runs. A sentence
// that describes a number nobody can reproduce is a sentence that should not be published, so every network command's answer
// is compared with the row it was written from: power to 0.1 kW, volts to 1e-4 per unit, transformer loading to 0.1 per cent.
// The last line printed is one JSON object; exit 1 if anything at all is wrong.
//
//   node bench/commands_check.mjs            check bench/results/commands/
//   node bench/commands_check.mjs <dir>      check another folder of the same shape
import { createRequire } from 'node:module';
import { readFileSync, existsSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const HERE = dirname(fileURLToPath(import.meta.url));
const DIR = resolve(process.argv[2] || join(HERE, 'results', 'commands'));
const LIST_SCHEMA = 'faraday.commands.v2', POINTER_SCHEMA = 'faraday.commands.current.v1';

const FIRE = require('./fire.js');
require('./fire_site.js');
require('./fire_topo.js');

const faults = [];
const stop = (why) => { console.log(JSON.stringify({ ok: false, reason: why })); process.exit(1); };

const pointerPath = join(DIR, 'current.json');
if (!existsSync(pointerPath)) stop('there is no current.json in ' + DIR);
const pointer = JSON.parse(readFileSync(pointerPath, 'utf8'));
if (pointer.schema !== POINTER_SCHEMA) stop('the pointer says schema ' + JSON.stringify(pointer.schema) + ', not ' + POINTER_SCHEMA);
if (typeof pointer.file !== 'string' || !pointer.file) stop('the pointer names no file');
const listPath = join(DIR, pointer.file);
if (!existsSync(listPath)) stop('the pointer names ' + pointer.file + ' and there is no such file beside it');

const bytes = readFileSync(listPath);
const sha = createHash('sha256').update(bytes).digest('hex');
if (sha !== pointer.sha256) stop('the file hashes to ' + sha + ' and the pointer says ' + pointer.sha256);
if (bytes.length !== pointer.bytes) stop('the file is ' + bytes.length + ' bytes and the pointer says ' + pointer.bytes);

const list = JSON.parse(bytes.toString('utf8'));
if (list.schema !== LIST_SCHEMA) stop('the list says schema ' + JSON.stringify(list.schema) + ', not ' + LIST_SCHEMA);
if (list.generation !== pointer.generation) stop('the list is generation ' + list.generation + ' and the pointer says ' + pointer.generation);
if (!Array.isArray(list.commands)) stop('the list carries no commands array');
if (list.commands.length !== pointer.count || list.count !== pointer.count) stop('the pointer counts ' + pointer.count + ' and the list holds ' + list.commands.length);

// power to 0.1 kW, volts to 1e-4 per unit, transformer loading to 0.1 per cent: the row was rounded to exactly these places
const near = (got, want, tol) => Math.abs(got - want) <= tol + 1e-12;
let fired = 0, compared = 0;
const byFamily = {};
for (const c of list.commands) {
  for (const k of ['family', 'kind', 'sentence', 'command']) if (typeof c[k] !== 'string' || !c[k]) faults.push({ command: c.command, why: k + ' is missing or not text' });
  if (/\b(optimal|optimum|safe|safest|best|ideal|recommended|guaranteed)\b/i.test(c.sentence)) faults.push({ command: c.command, why: 'the sentence makes a claim: ' + c.sentence });
  let r;
  try { r = FIRE.fire(c.command); } catch (e) { faults.push({ command: c.command, why: 'threw: ' + e.message }); continue; }
  if (!r || !r.ran) { faults.push({ command: c.command, why: 'did not run: no such command' }); continue; }
  fired++;
  byFamily[c.family] = (byFamily[c.family] || 0) + 1;
  if (!c.row) continue;                                   // a site pulse sentence has no solved row to be checked against
  const n = r.numbers, row = c.row;
  const checks = [['connection point kW', n.connection_point_kw, row.p_kw, 0.1],
                  ['highest volts', n.highest_volts_pu, row.vmax_pu, 1e-4],
                  ['lowest volts', n.lowest_volts_pu, row.vmin_pu, 1e-4],
                  ['busiest transformer per cent', n.worst_transformer_pct, row.worst_tx_pct, 0.1]];
  for (const [what, got, want, tol] of checks) {
    if (typeof got !== 'number' || !near(got, want, tol)) faults.push({ command: c.command, why: what + ': fired ' + got + ', the row says ' + want });
  }
  compared++;
}

const out = { ok: faults.length === 0, generation: list.generation, file: pointer.file, sha256: sha.slice(0, 12), bytes: bytes.length,
              commands: list.commands.length, fired, compared_against_a_solved_row: compared, by_family: byFamily,
              faults: faults.length, first_faults: faults.slice(0, 5) };
console.log(JSON.stringify(out, null, 1));
process.exit(faults.length ? 1 : 0);
