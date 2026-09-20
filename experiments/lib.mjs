// lib.mjs - circuit builders for the experiments, on the one rule of apparatus/cells.mjs and nothing else.
export { compile, state, read, settles, place, GOLDEN_ANGLE } from '../apparatus/cells.mjs';

export function builder(from = 20000) {
  let next = from;
  const p = [];
  const fresh = () => ++next;
  const input = name => { const k = fresh(); p.push({ key: k, input: name }); return k; };
  const nand = (a, b) => { const k = fresh(); p.push({ key: k, gate: [a, b] }); return k; };
  const not = a => nand(a, a);
  const and = (a, b) => not(nand(a, b));
  const or = (a, b) => nand(not(a), not(b));
  const xor = (a, b) => { const n = nand(a, b); return nand(nand(a, n), nand(b, n)); };
  return { program: p, fresh, input, nand, not, and, or, xor };
}

// A forward sweep: every cell's next state from the whole of the last tick. The other way to run the same rule.
export function sweep(program, schedule, ticks, inputOn) {
  const keys = program.map(r => r.key);
  let now = new Map(keys.map(k => [k, 0]));
  const frames = [];
  for (let t = 0; t <= ticks; t++) {
    const nxt = new Map();
    for (const r of program) {
      if (r.input !== undefined) nxt.set(r.key, inputOn(schedule, r.input, t));
      else nxt.set(r.key, t <= 0 ? 0 : ((now.get(r.gate[0]) && now.get(r.gate[1])) ? 0 : 1));
    }
    // inputs at tick t-1 must be what the gates saw: keep last tick's map for the next round
    frames.push(nxt);
    now = nxt;
  }
  return frames;
}

export function inputOn(schedule, name, t) {
  const s = schedule[name];
  if (s === 0 || s === 1) return s;
  if (!s) return 0;
  for (const [from, to] of s) if (t >= from && t < to) return 1;
  return 0;
}
