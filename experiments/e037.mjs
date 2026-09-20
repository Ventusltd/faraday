// 37: a two to one selector. Does the output follow the chosen input for all 8 rows?
import { builder, compile, read, settles } from './lib.mjs';

export default async function () {
  const b = builder(37000);
  const A = b.input('a'), B = b.input('b'), S = b.input('s');
  const out = b.nand(b.nand(A, b.not(S)), b.nand(B, S));      // s = 0 gives a, s = 1 gives b
  const rules = compile(b.program);
  let right = 0; const wrong = []; let worst = 0;
  for (let row = 0; row < 8; row++) {
    const sch = { a: row & 1, b: (row >> 1) & 1, s: (row >> 2) & 1 };
    const at = settles(rules, sch, [out]); worst = Math.max(worst, at);
    const got = read(rules, sch, [out], at + 8)[0], want = sch.s ? sch.b : sch.a;
    if (at >= 0 && got === want) right++; else wrong.push(JSON.stringify(sch) + ' gave ' + got);
  }
  return {
    did: 'Built the selector from four gate cells. Set each of the 8 input rows, waited for the output cell to settle, read it.',
    observed: `${right} of 8 rows right; ${b.program.length} cells; settles by tick ${worst}` + (wrong.length ? '; wrong: ' + wrong.join(', ') : ''),
    shows: right === 8 ? 'One cell can choose which of two others is passed on: a selection made by the dots themselves.' : 'The selector as built is wrong.',
    result: right === 8 ? 'CONFIRMED' : 'REFUTED'
  };
}
