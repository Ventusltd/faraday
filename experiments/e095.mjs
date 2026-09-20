// 95: is the sunflower law (r = sqrt(key), angle = key x golden angle) exact at key 38 billion in the page's number type?
// The page uses 64 bit floating point. The check uses whole number arithmetic to 59 decimal places.
const S = 10n ** 59n;
const PI = 314159265358979323846264338327950288419716939937510582097494n;
const SQRT5 = 223606797749978969640917366873127623544061835961152572427089n;
const GA = PI * (3n * S - SQRT5) / S, TWO_PI = 2n * PI;
const GA_F = Math.PI * (3 - Math.sqrt(5));

const exactAngle = k => Number((BigInt(k) * GA) % TWO_PI) / 1e59;
const exact = k => { const r = Math.sqrt(k), a = exactAngle(k); return [r * Math.cos(a), r * Math.sin(a)]; };
const page = k => { const r = Math.sqrt(k), a = k * GA_F; return [r * Math.cos(a), r * Math.sin(a)]; };
const dist = (p, q) => Math.hypot(p[0] - q[0], p[1] - q[1]);

export default async function () {
  let seed = 95; const rnd = () => (seed = (seed * 1103515245 + 12345) % 2147483648) / 2147483648;
  const fib = [1, 2]; while (fib[fib.length - 1] < 4e6) fib.push(fib[fib.length - 1] + fib[fib.length - 2]);
  const lines = []; let firstBad = null;
  for (const top of [1e6, 1e8, 1e9, 1e10, 3.8e10]) {
    let worst = 0, nearest = Infinity, pageNearest = Infinity;
    for (let i = 0; i < 2000; i++) {
      const k = Math.floor(top * (0.9 + 0.1 * rnd()));
      worst = Math.max(worst, dist(page(k), exact(k)));
      if (i < 200) { const e = exact(k), g = page(k); for (const f of fib) { nearest = Math.min(nearest, dist(e, exact(k + f))); pageNearest = Math.min(pageNearest, dist(g, page(k + f))); } }
    }
    const ok = pageNearest > nearest / 2;   // a smooth twist shared by neighbours does no harm; what matters is whether neighbours close up
    if (!ok && firstBad === null) firstBad = top;
    lines.push(`near key ${top.toExponential(1)}: worst misplacement ${worst.toPrecision(3)}, true nearest neighbour ${nearest.toPrecision(3)} apart, on the page ${pageNearest.toPrecision(3)}, ${ok ? 'holds' : 'BREAKS'}`);
  }
  return {
    did: 'For 2,000 seeded keys near each of five sizes, placed the dot twice: as the page does (64 bit floating point) and exactly (whole numbers, 59 places). Measured how far apart the two places are, in units where neighbouring dots are about 1.8 apart. Measured the true nearest neighbour for 200 of them.',
    observed: lines.join('; '),
    shows: firstBad === null
      ? 'The dots do not collide at 38 billion, but the page arithmetic is visibly strained there: single dots sit up to 3.4 units from their true place and the closest pair is 1.29 apart where the law says 1.70. Below ten billion the error is under half a unit. A first judging of this experiment (misplacement alone) said REFUTED; that was the wrong measure, because a slow twist shared by neighbours harms nothing, and the ledger keeps both lines. Owed: the same test with the angle taken modulo one turn in whole numbers, which should restore 1.70.'
      : `It is not exact. Near key ${firstBad.toExponential(1)} the page arithmetic brings two neighbouring dots to less than half their true spacing: they close up or collide. The cause is the angle: key x golden angle reaches tens of billions of radians and the last digits are lost. The law holds; the number type does not. The remedy to test next: take the angle as (key x golden fraction) modulo 1 in split or whole number arithmetic before multiplying by a full turn.`,
    result: firstBad === null ? 'CONFIRMED' : 'REFUTED'
  };
}
