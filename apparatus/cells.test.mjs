// cells.test.mjs - run with:  node apparatus/cells.test.mjs
// Every check READS THE CELLS (their lit or dark state at a tick). None of them looks at how the program is wired.
// The results are written to apparatus/cells.result.json so an experiment entry can quote them exactly.
import { compile, read, settles, state, place, halfAdder, adder4, latch } from './cells.mjs';
import { writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const out = { ran: new Date().toISOString(), checks: [] };
let failed = 0;
function check(name, pass, detail) {
  out.checks.push({ name, pass: !!pass, detail });
  if (!pass) failed++;
  console.log((pass ? 'PASS  ' : 'FAIL  ') + name + (detail ? '   ' + detail : ''));
}

// ---- 16. the half adder, from one kind of gate ----
{
  const h = halfAdder(), rules = compile(h.program);
  const gates = h.program.filter(r => r.gate).length;
  const rows = [];
  let ok = true, okNoCache = true, worst = 0;
  for (const a of [0, 1]) for (const b of [0, 1]) {
    const sched = { a, b };
    const t = settles(rules, sched, [h.sum, h.carry]);
    worst = Math.max(worst, t);
    const [s, c] = read(rules, sched, [h.sum, h.carry], t + 8);
    const [s2, c2] = read(rules, sched, [h.sum, h.carry], t + 8, false);      // no cache at all: pure recursion
    rows.push({ a, b, sum: s, carry: c, settled_at_tick: t });
    if (s !== (a ^ b) || c !== (a & b)) ok = false;
    if (s2 !== s || c2 !== c) okNoCache = false;
  }
  out.halfAdder = { cells: h.program.length, gate_cells: gates, rows, slowest_settle_tick: worst };
  check('16 half adder: all four rows of the truth table, read from the cells', ok, JSON.stringify(rows));
  check('16 the same answers with no cache (nothing kept between questions)', okNoCache);
  check('16 it is made of one kind of gate cell only', h.program.every(r => r.input !== undefined || r.gate.length === 2), gates + ' gate cells, 2 input cells');
}

// ---- 16b. a planted fault must be caught: the test is able to fail ----
{
  const h = halfAdder();
  const bad = h.program.map(r => r.key === h.carry ? { key: r.key, gate: [h.A, h.A] } : r);   // carry rewired to "not A"
  const rules = compile(bad);
  let ok = true;
  for (const a of [0, 1]) for (const b of [0, 1]) {
    const [s, c] = read(rules, { a, b }, [h.sum, h.carry], 40);
    if (s !== (a ^ b) || c !== (a & b)) ok = false;
  }
  check('16 planted fault (carry rewired) is CAUGHT by the same check', ok === false);
}

// ---- 17. the four bit adder: every one of the 256 sums ----
{
  const d = adder4(), rules = compile(d.program);
  let wrong = 0, worst = 0;
  const examples = [];
  for (let x = 0; x < 16; x++) for (let y = 0; y < 16; y++) {
    const sched = { zero: 0 };
    for (let i = 0; i < 4; i++) { sched['a' + i] = (x >> i) & 1; sched['b' + i] = (y >> i) & 1; }
    const keys = [...d.sum, d.carry];
    const t = settles(rules, sched, keys, 300, 8);
    worst = Math.max(worst, t);
    const bits = read(rules, sched, keys, t + 8);
    const got = bits.reduce((n, bit, i) => n + (bit << i), 0);
    if (got !== x + y) wrong++;
    if ((x === 7 && y === 9) || (x === 15 && y === 15) || (x === 6 && y === 3)) examples.push({ x, y, cells_say: got, settled_at_tick: t });
  }
  out.adder4 = { cells: d.program.length, gate_cells: d.program.filter(r => r.gate).length, sums_checked: 256, wrong, slowest_settle_tick: worst, examples };
  check('17 four bit adder: 256 of 256 sums right, read from the cells', wrong === 0, 'wrong=' + wrong + ', slowest settles at tick ' + worst);
}

// ---- 18. the pulse has a finite speed: an answer is never there before the change could have reached it ----
{
  const h = halfAdder(), rules = compile(h.program);
  // a and b both switch on at tick 10. carry is two gate cells away from the inputs.
  const sched = { a: [[10, 1e9]], b: [[10, 1e9]] };
  const trace = [];
  for (let t = 8; t <= 16; t++) trace.push({ t, carry: state(rules, sched, h.carry, t, new Map()) });
  const first = trace.find(r => r.carry === 1)?.t;
  out.pulse = { inputs_switch_at: 10, carry_first_lit_at: first, trace };
  check('18 carry lights exactly two ticks after the inputs, never sooner', first === 12, 'first lit at tick ' + first);
}

// ---- 19. memory: does a latch remember, with nothing stored per cell? ----
{
  const L = latch(), rules = compile(L.program);
  // A. start it properly: hold reset for ticks 0 to 5, then SET for ticks 10 to 13, then leave both inputs idle (on).
  const sched = { resetN: [[5, 40], [44, 1e9]], setN: [[0, 10], [13, 1e9]] };
  const q = t => state(rules, sched, L.Q, t, new Map());
  const afterReset = q(9), duringSet = q(13), longAfterSet = q(39), afterSecondReset = q(60);
  out.latch = { afterReset, duringSet, longAfterSet, afterSecondReset };
  check('19 after reset the latch is dark', afterReset === 0);
  check('19 it is lit by a three tick SET pulse', duringSet === 1);
  check('19 it is STILL lit 26 ticks after the pulse ended: it remembers', longAfterSet === 1);
  check('19 a later reset pulse (ticks 40 to 43) makes it dark again', afterSecondReset === 0);
  // B. what happens if it is never reset: both inputs idle from tick 0.
  const idle = { resetN: 1, setN: 1 };
  const flick = [];
  for (let t = 1; t <= 8; t++) flick.push(state(rules, idle, L.Q, t, new Map()));
  out.latch.never_reset = flick;
  const oscillates = flick.join('') === '10101010';
  check('19 OBSERVED: never reset, it flickers lit, dark, lit, dark for ever (recorded, not hidden)', oscillates, flick.join(''));
  // C. the cost of remembering without storing: the question at tick t works back through t ticks.
  let calls = 0;
  const count = (key, t) => { calls++; const r = rules.get(key); if (r.input !== undefined || t <= 0) return; count(r.gate[0], t - 1); count(r.gate[1], t - 1); };
  calls = 0; count(L.Q, 12); const c12 = calls; calls = 0; count(L.Q, 24); const c24 = calls;
  out.latch.cost = { questions_at_tick_12: c12, questions_at_tick_24: c24 };
  check('19 remembering costs TIME not storage: with no cache the work grows with the tick asked for', c24 > c12, c12 + ' then ' + c24 + ' questions');
}

// ---- place: a cell here is a dot there ----
{
  const [x, y] = place(1002);
  check('place is a pure function of the key, the Kuiper law', Math.abs(Math.hypot(x, y) - Math.sqrt(1002)) < 1e-9);
}

out.failed = failed;
const here = dirname(fileURLToPath(import.meta.url));
writeFileSync(join(here, 'cells.result.json'), JSON.stringify(out, null, 1));
console.log(failed === 0 ? '\nALL PASS' : '\n' + failed + ' FAILED');
process.exit(failed === 0 ? 0 : 1);
