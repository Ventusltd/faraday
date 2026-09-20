// 36: a ring of 3, 5, 7 NOT cells. Is the period 2 x cells ticks?
import { builder, compile, read } from './lib.mjs';

export default async function () {
  const lines = []; let allExpected = true;
  for (const n of [3, 5, 7]) {
    const b = builder(36000 + n * 100);
    const keys = Array.from({ length: n }, () => b.fresh());
    keys.forEach((k, i) => b.program.push({ key: k, gate: [keys[(i + n - 1) % n], keys[(i + n - 1) % n]] }));
    const rules = compile(b.program);
    const seq = [];
    for (let t = 0; t < 8 * n; t++) seq.push(read(rules, {}, keys, t).join(''));
    let period = -1;
    for (let p = 1; p <= 4 * n && period < 0; p++) {
      let ok = true;
      for (let t = 2 * n; t + p < seq.length; t++) if (seq[t] !== seq[t + p]) { ok = false; break; }
      if (ok) period = p;
    }
    if (period !== 2 * n) allExpected = false;
    lines.push(`${n} cells: period ${period} (expected ${2 * n}); first ticks ${seq.slice(0, 5).join(' ')}`);
  }
  return {
    did: 'Built rings of 3, 5 and 7 cells, each lit unless the one before it was lit a tick earlier. No inputs. Read every cell for 8 x cells ticks and found the shortest repeat.',
    observed: lines.join('; '),
    shows: allExpected ? 'The ring oscillates with period twice its length.'
      : 'It does not. Every cell starts HOME at tick 0, so they all see the same thing and all flip together: the ring beats as one, period 2, whatever its length. A travelling wave needs the symmetry broken by an input.',
    result: allExpected ? 'CONFIRMED' : 'REFUTED'
  };
}
