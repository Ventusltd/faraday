// bench/fire_topo.js - NETWORKS FROM A SEED, in the visitor's browser: the same generator and the same two pulse sweep as
// bench/topo.py, draw for draw and sum for sum. Checked against every Python case by bench/topo_check.mjs. Load after fire.js.
//   fire network {"seed":123456,"solar":1,"generator":1,"load":0.3}
(function (root) {
  const C = { kv: 11.0, grid_x_over_r: 10.0, hv_cable_r: 0.20, hv_cable_x: 0.09, tx_z_pct: 5.5, tx_x_over_r: 5.0, load_pf: 0.90, gen_pf: 0.95, volts_high_pu: 1.06, volts_low_pu: 0.94 };
  const KVA = [500, 800, 1000, 1600, 2000], LIMITS = [0, 50, 200, 500, 1000], GENS = [0, 250, 500, 1000], FAULT = [100, 150, 250, 350, 500];
  const SHAPES = ['star', 'chain', 'tree', 'sub-boards'];
  const CASES = []; for (const ps of [0.0, 0.5, 1.0]) for (const g of [0, 1]) for (const ls of [1.0, 0.6, 0.3]) CASES.push([ps, g, ls]);
  function mulberry32(a) { a |= 0; return () => { a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return (t ^ t >>> 14) >>> 0; }; }
  function network(seed) {
    const g = mulberry32(Number((BigInt(seed) * 2654435761n + 777n) & 0xFFFFFFFFn)), pick = n => g() % n;
    const shape = pick(4), n = 2 + pick(11), fault = FAULT[pick(5)], intake = (10 + pick(191)) / 100, limit = LIMITS[pick(5)], subs = [];
    for (let k = 1; k <= n; k++) {
      const kva = KVA[pick(5)], load = Math.floor(kva * (25 + pick(56)) / 100), km = (5 + pick(76)) / 100; let parent;
      if (k === 1 || shape === 0) parent = 0; else if (shape === 1) parent = pick(10) < 8 ? k - 1 : 0; else if (shape === 2) parent = pick(k); else parent = k <= 3 ? 0 : 1 + pick(3);
      const pv = pick(10) < 3 ? Math.floor(kva * (30 + pick(121)) / 100) : 0;
      subs.push({ n: k, kva, load_kw: load, km, parent, pv_kw: pv });
    }
    const gen = GENS[pick(4)], genAt = pick(n + 1);
    return { seed, shape: SHAPES[shape], fault_mva: fault, intake_km: intake, export_limit_kw: limit, generator_kw: gen, generator_at: genAt, subs };
  }
  const add = (a, b) => [a[0] + b[0], a[1] + b[1]], sub = (a, b) => [a[0] - b[0], a[1] - b[1]];
  const mul = (a, b) => [a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]];
  const div = (a, b) => { const d = b[0] * b[0] + b[1] * b[1]; return [(a[0] * b[0] + a[1] * b[1]) / d, (a[1] * b[0] - a[0] * b[1]) / d]; };
  const conj = a => [a[0], -a[1]], scale = (a, k) => [a[0] * k, a[1] * k], mag = a => Math.hypot(a[0], a[1]);
  function solve(net, pvShare, genOn, loadShare, tol) {
    tol = tol || 1e-9; const c = C, vb = c.kv * 1000 / Math.sqrt(3);
    const zs = (c.kv ** 2) / net.fault_mva, xr = c.grid_x_over_r, rs = zs / Math.sqrt(1 + xr * xr), cable = [c.hv_cable_r, c.hv_cable_x];
    const Z = { poc: [rs, rs * xr], board: scale(cable, net.intake_km) }, parent = { grid: null, poc: 'grid', board: 'poc' }, S = {}, kva = {};
    const tanl = Math.tan(Math.acos(c.load_pf)), tang = Math.tan(Math.acos(c.gen_pf));
    const gen = genOn ? [net.generator_kw, net.generator_kw * tang] : [0, 0];
    if (genOn && net.generator_at === 0) S.board = scale(gen, -1000 / 3);
    for (const s of net.subs) {
      const hv = 'hv' + s.n, lv = 'lv' + s.n; parent[hv] = s.parent === 0 ? 'board' : 'hv' + s.parent; parent[lv] = hv;
      Z[hv] = scale(cable, s.km);
      const zt = c.tx_z_pct / 100 * (c.kv ** 2) / (s.kva / 1000), txr = c.tx_x_over_r, rt = zt / Math.sqrt(1 + txr * txr);
      Z[lv] = [rt, rt * txr]; kva[lv] = s.kva;
      const kw = s.load_kw * loadShare; let p = sub([kw, kw * tanl], [s.pv_kw * pvShare, 0]);
      if (genOn && net.generator_at === s.n) p = sub(p, gen);
      S[lv] = scale(p, 1000 / 3);
    }
    const kids = {}; for (const n of Object.keys(parent)) if (parent[n] !== null) (kids[parent[n]] = kids[parent[n]] || []).push(n);
    const order = ['grid']; for (let i = 0; i < order.length; i++) order.push(...(kids[order[i]] || []));
    let V = {}; for (const n of order) V[n] = [vb, 0]; let rounds = 0, J;
    for (;;) {
      rounds++; J = {}; for (const n of order) J[n] = S[n] ? conj(div(S[n], V[n])) : [0, 0];
      for (let i = order.length - 1; i >= 0; i--) { const n = order[i]; if (parent[n] !== null) J[parent[n]] = add(J[parent[n]], J[n]); }
      const nv = { grid: [vb, 0] }; for (let i = 1; i < order.length; i++) { const n = order[i]; nv[n] = sub(nv[parent[n]], mul(J[n], Z[n])); }
      let step = 0; for (const n of order) step = Math.max(step, mag(sub(nv[n], V[n]))); V = nv;
      if (step < tol || rounds > 300) break;
    }
    const sPoc = scale(mul(V.poc, conj(J.poc)), 3);
    let loss = 0; for (let i = 1; i < order.length; i++) loss += mag(J[order[i]]) ** 2 * Z[order[i]][0]; loss *= 3;
    let netP = 0; for (const n of Object.keys(S)) netP += S[n][0]; netP *= 3;
    const source = mul(V.grid, conj(J.poc))[0] * 3;
    let tx = -Infinity, amps = -Infinity; const txEach = {}, ampsEach = {}, vEach = {};
    for (const n of Object.keys(kva)) { txEach[n] = mag(scale(mul(V[n], conj(J[n])), 3)) / 1000 / kva[n] * 100; tx = Math.max(tx, txEach[n]); }
    for (let i = 1; i < order.length; i++) { const n = order[i]; if (!(n in kva)) { ampsEach[n] = mag(J[n]); amps = Math.max(amps, ampsEach[n]); } }
    let vmax = -Infinity, vmin = Infinity; for (const n of order) { const v = mag(V[n]) / vb; vEach[n] = v; vmax = Math.max(vmax, v); vmin = Math.min(vmin, v); }
    return { p: sPoc[0] / 1000, q: sPoc[1] / 1000, loss: loss / 1000, vmax, vmin, tx, amps, rounds, balance: Math.abs(source - netP - loss) / Math.max(Math.abs(netP), 1.0),
             each: { volts: vEach, tx: txEach, amps: ampsEach }, parent };
  }
  const rnd = (x, d) => Number(x.toFixed(d));
  function run(i) {
    if (i.seed === undefined) throw new Error('this command needs "seed" (any whole number: each one is a different network)');
    const net = i.network || network(i.seed), ps = i.solar === undefined ? 1 : i.solar, g = i.generator === undefined ? 0 : i.generator, ls = i.load === undefined ? 1 : i.load;
    const r = solve(net, ps, !!g, ls), c = C, exp = Math.max(0, -r.p), over = Math.max(0, exp - net.export_limit_kw), flags = [];
    if (r.rounds > 300 || r.balance >= 1e-6) flags.push('THE SWEEP DID NOT CONVERGE: this network is beyond the method, and no number here should be used');
    if (over > 0) flags.push('export ' + exp.toFixed(0) + ' kW is ' + over.toFixed(0) + ' kW over the ' + net.export_limit_kw + ' kW limit');
    if (r.vmax > c.volts_high_pu) flags.push('highest voltage ' + r.vmax.toFixed(3) + ' is over ' + c.volts_high_pu);
    if (r.vmin < c.volts_low_pu) flags.push('lowest voltage ' + r.vmin.toFixed(3) + ' is under ' + c.volts_low_pu);
    if (r.tx > 100) flags.push('a transformer is at ' + r.tx.toFixed(0) + '% of its rating');
    const pv = net.subs.reduce((t, s) => t + s.pv_kw, 0), load = net.subs.reduce((t, s) => t + s.load_kw, 0);
    return { numbers: { substations: net.subs.length, load_kw: rnd(load * ls, 0), solar_kw: rnd(pv * ps, 0), generator_kw: g ? net.generator_kw : 0, export_limit_kw: net.export_limit_kw,
                        connection_point_kw: rnd(r.p, 1), connection_point_kvar: rnd(r.q, 1), losses_kw: rnd(r.loss, 2), highest_volts_pu: rnd(r.vmax, 4), lowest_volts_pu: rnd(r.vmin, 4),
                        worst_transformer_pct: rnd(r.tx, 1), busiest_cable_amps: rnd(r.amps, 1), rounds: r.rounds },
             said: 'A ' + net.shape + ' of ' + net.subs.length + ' substations behind a ' + net.fault_mva + ' MVA connection: ' + (r.p < 0 ? 'exports ' : 'imports ') + Math.abs(r.p).toFixed(0) + ' kW; volts ' + r.vmin.toFixed(3) + ' to ' + r.vmax.toFixed(3) +
                   '; busiest transformer ' + r.tx.toFixed(0) + '%; ' + (flags.length ? flags.join('; ') : 'inside every limit'),
             how: 'network number ' + net.seed + ' from a stated generator (no real site); two pulses per round until the volts stop moving; every figure a CANDIDATE. An estimate, not a study.', net, solved: r };
  }
  const F = root.FIRE || (typeof require !== 'undefined' ? require('./fire.js') : null);
  if (!F) throw new Error('fire_topo.js needs fire.js loaded first');
  F.register('network', 'NETWORKS', run);
  F.topo = { network, solve, CASES, C };
})(typeof window !== 'undefined' ? window : globalThis);
