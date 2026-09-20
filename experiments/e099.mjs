// 99: the same rule run two ways, backwards (ask one cell at one tick) and forwards (sweep every cell, tick by tick).
// Do they ever disagree, and which is faster? One core here; the 24 core run is owed.
import { compile, state, sweep, inputOn } from './lib.mjs';
import { adder4 } from '../apparatus/cells.mjs';

export default async function () {
  const { program } = adder4(), rules = compile(program), TICKS = 40;
  let differ = 0, states = 0, tBack = 0, tFwd = 0;
  for (let x = 0; x < 16; x++) for (let y = 0; y < 16; y++) {
    const sch = { zero: 0 };
    for (let i = 0; i < 4; i++) { sch['a' + i] = (x >> i) & 1; sch['b' + i] = (y >> i) & 1; }
    let t0 = performance.now();
    const frames = sweep(program, sch, TICKS, inputOn);
    tFwd += performance.now() - t0;
    t0 = performance.now();
    const cache = new Map(), back = [];
    for (let t = 0; t <= TICKS; t++) back.push(program.map(r => state(rules, sch, r.key, t, cache)));
    tBack += performance.now() - t0;
    for (let t = 0; t <= TICKS; t++) program.forEach((r, i) => { states++; if (frames[t].get(r.key) !== back[t][i]) differ++; });
  }
  const perSecFwd = Math.round(states / (tFwd / 1000)), perSecBack = Math.round(states / (tBack / 1000));
  return {
    did: `Ran the four bit adder (${program.length} cells) for all 256 input pairs and ${TICKS + 1} ticks, both ways, and compared every cell at every tick.`,
    observed: `${states.toLocaleString('en-GB')} states compared, ${differ} differ; forwards ${perSecFwd.toLocaleString('en-GB')} states a second, backwards with its cache ${perSecBack.toLocaleString('en-GB')} a second, one core`,
    shows: differ === 0 ? 'The two ways are the same machine. Forwards is the one a graphics card can do (every cell at once from the last frame); backwards is the one that needs nothing held. Either may be used and checked against the other.' : 'They disagree: one of them is wrong.',
    result: differ === 0 ? 'CONFIRMED' : 'REFUTED'
  };
}
