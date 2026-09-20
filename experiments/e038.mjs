// 38: a four bit comparator. Is "A greater than B" right for all 256 pairs?
import { builder, compile, read, settles } from './lib.mjs';

export default async function () {
  const b = builder(38000);
  const a = [], bb = [];
  for (let i = 0; i < 4; i++) a.push(b.input('a' + i));
  for (let i = 0; i < 4; i++) bb.push(b.input('b' + i));
  const zero = b.input('zero');
  // from the lowest bit up: greater = (a and not b) or (same and greater so far)
  let g = zero;
  for (let i = 0; i < 4; i++) {
    const gt = b.and(a[i], b.not(bb[i])), same = b.not(b.xor(a[i], bb[i]));
    g = b.or(gt, b.and(same, g));
  }
  const rules = compile(b.program);
  let right = 0, worst = 0; const wrong = [];
  for (let x = 0; x < 16; x++) for (let y = 0; y < 16; y++) {
    const sch = { zero: 0 };
    for (let i = 0; i < 4; i++) { sch['a' + i] = (x >> i) & 1; sch['b' + i] = (y >> i) & 1; }
    const at = settles(rules, sch, [g]); worst = Math.max(worst, at);
    const got = read(rules, sch, [g], at + 8)[0];
    if (at >= 0 && got === (x > y ? 1 : 0)) right++; else if (wrong.length < 5) wrong.push(x + '>' + y + ' gave ' + got);
  }
  return {
    did: 'Built the comparator from gate cells only. Set every pair of numbers from 0 to 15, waited for the output cell to settle, read it.',
    observed: `${right} of 256 pairs right; ${b.program.length} cells; slowest settles at tick ${worst}` + (wrong.length ? '; wrong: ' + wrong.join(', ') : ''),
    shows: right === 256 ? 'The dots can decide which of two numbers is larger.' : 'The comparator as built is wrong.',
    result: right === 256 ? 'CONFIRMED' : 'REFUTED'
  };
}
