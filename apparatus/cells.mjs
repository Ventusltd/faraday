// cells.mjs - the apparatus for experiments 16 to 19: can the dots compute?
//
// A CELL is one dot. It has a permanent key and nothing else of its own. Its state is HOME (dark, 0) or AWAY (lit, 1).
// A PROGRAM is a list of rules. There are only two kinds of rule:
//
//   { key, input: 'a' }            an INPUT cell: lit when the visitor's schedule says input 'a' is on at that tick
//   { key, gate: [k1, k2] }        a GATE cell: lit UNLESS both cells k1 and k2 were lit one tick earlier
//
// The second rule is the whole machine. It is the NAND gate, the one gate from which every other can be made, and it
// is "select the cells that another rule lit, and answer to them": one cell's OUTPUT drives another cell's GATE.
// The one tick of delay is the pulse: a change travels from cell to cell at a finite speed and never faster.
//
// NOTHING IS STORED PER CELL. state() is a pure function of (key, program, schedule, tick). It works backwards from
// the tick asked for to tick 0, when every cell is HOME. Ask twice, on any machine, and the answer is the same.
// (A cache inside one call only saves time; experiment 16 runs with it off and with it on and compares.)
//
// Place is also a pure function of the key, by the law the Kuiper draws with: r = sqrt(key), angle = key x golden angle.
// It plays no part in the logic. It is here so that a cell in this file is the same thing as a dot on the screen.

export const GOLDEN_ANGLE = Math.PI * (3 - Math.sqrt(5));

export function place(key) {
  const r = Math.sqrt(key), a = key * GOLDEN_ANGLE;
  return [r * Math.cos(a), r * Math.sin(a)];
}

// schedule: { a: [[from, to], ...] }  input 'a' is on for ticks from <= t < to. A plain 0 or 1 means always.
function inputOn(schedule, name, t) {
  const s = schedule[name];
  if (s === 0 || s === 1) return s;
  if (!s) return 0;
  for (const [from, to] of s) if (t >= from && t < to) return 1;
  return 0;
}

export function compile(program) {
  const rules = new Map();
  for (const r of program) {
    if (rules.has(r.key)) throw new Error('two rules for key ' + r.key + ': a cell answers to one rule');
    rules.set(r.key, r);
  }
  for (const r of program) if (r.gate) for (const k of r.gate)
    if (!rules.has(k)) throw new Error('key ' + r.key + ' is gated by key ' + k + ', which has no rule');
  return rules;
}

// The state of one cell at one tick. 1 = AWAY (lit), 0 = HOME (dark).
export function state(rules, schedule, key, t, cache) {
  const r = rules.get(key);
  if (r.input !== undefined) return inputOn(schedule, r.input, t);
  if (t <= 0) return 0;                                   // at tick 0 every gate cell is HOME
  const id = cache ? key + ':' + t : null;
  if (cache && cache.has(id)) return cache.get(id);
  const a = state(rules, schedule, r.gate[0], t - 1, cache);
  const b = state(rules, schedule, r.gate[1], t - 1, cache);
  const out = (a && b) ? 0 : 1;                           // lit UNLESS both of its gate cells were lit
  if (cache) cache.set(id, out);
  return out;
}

// Read a set of cells at a tick, as the test does: it looks at the dots, not at the wiring.
export function read(rules, schedule, keys, t, useCache = true) {
  const cache = useCache ? new Map() : null;
  return keys.map(k => state(rules, schedule, k, t, cache));
}

// The first tick after which none of the named cells changes again for `hold` ticks, or -1 if they never settle.
export function settles(rules, schedule, keys, limit = 200, hold = 8) {
  const cache = new Map();
  let last = null, since = 0;
  for (let t = 0; t <= limit; t++) {
    const now = keys.map(k => state(rules, schedule, k, t, cache)).join('');
    if (now === last) { if (t - since >= hold) return since; } else { last = now; since = t; }
  }
  return -1;
}

// ---- the circuits, written as programs. Every key is a real integer; nothing about a key is special. ----

let next = 0;
const fresh = () => ++next;
export function resetKeys(from = 0) { next = from; }

const nand = (p, a, b) => { const k = fresh(); p.push({ key: k, gate: [a, b] }); return k; };
const not = (p, a) => nand(p, a, a);
const and = (p, a, b) => not(p, nand(p, a, b));
const or = (p, a, b) => nand(p, not(p, a), not(p, b));
function xor(p, a, b) { const n = nand(p, a, b); return nand(p, nand(p, a, n), nand(p, b, n)); }

// HALF ADDER: two inputs, two outputs. sum = one of them but not both; carry = both.
export function halfAdder() {
  resetKeys(1000);
  const p = [];
  const A = fresh(), B = fresh();
  p.push({ key: A, input: 'a' }, { key: B, input: 'b' });
  const sum = xor(p, A, B), carry = and(p, A, B);
  return { program: p, A, B, sum, carry };
}

// FOUR BIT ADDER: adds any two numbers from 0 to 15. Made of the same cells and nothing else.
export function adder4() {
  resetKeys(5000);
  const p = [], a = [], b = [], s = [];
  for (let i = 0; i < 4; i++) { a.push(fresh()); p.push({ key: a[i], input: 'a' + i }); }
  for (let i = 0; i < 4; i++) { b.push(fresh()); p.push({ key: b[i], input: 'b' + i }); }
  const zero = fresh(); p.push({ key: zero, input: 'zero' });
  let c = zero;
  for (let i = 0; i < 4; i++) {
    const x = xor(p, a[i], b[i]);
    s.push(xor(p, x, c));
    c = or(p, and(p, a[i], b[i]), and(p, x, c));
  }
  return { program: p, a, b, sum: s, carry: c };
}

// LATCH: two gate cells, each gated by the other. setN and resetN are "active low": OFF means "do it".
export function latch() {
  resetKeys(9000);
  const p = [];
  const S = fresh(), R = fresh();
  p.push({ key: S, input: 'setN' }, { key: R, input: 'resetN' });
  const Q = fresh(), Qn = fresh();
  p.push({ key: Q, gate: [S, Qn] }, { key: Qn, gate: [R, Q] });
  return { program: p, S, R, Q, Qn };
}
