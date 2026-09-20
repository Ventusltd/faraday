// bench/fire_site.js - SITE PULSE in the visitor's browser: a port of solve() and record() in bench/site_cases.py.
// Plain JavaScript, no library. JavaScript has no complex numbers, so every volt, amp and ohm is a pair [re, im].
// Checked against every saved SITE PULSE and SITE SURVEY record by bench/fire_check.mjs. Load after fire.js.
(function (root) {
  const CANDIDATE = { kv: 11.0, grid_fault_mva: 150.0, grid_x_over_r: 10.0, hv_cable_r: 0.20, hv_cable_x: 0.09, tx_z_pct: 5.5, tx_x_over_r: 5.0,
                      load_pf: 0.90, gen_pf: 0.95, pv_pf: 1.0, volts_high_pu: 1.06, volts_low_pu: 0.94, inverter_fault_x_rated: 1.1, generator_subtransient_pu: 0.15 };
  const SCENARIOS = { 1: ['no solar, no generator', 0.0, false, []], 2: ['no solar, generator running', 0.0, true, []],
                      3: ['solar at full output, no generator', 1.0, false, []], 4: ['solar at full output, generator running', 1.0, true, []],
                      5: ['solar at half output, no generator', 0.5, false, []], 6: ['solar at half output, generator running', 0.5, true, []],
                      7: ['solar at full output, the tenant substation disconnected', 1.0, false, ['tenant']],
                      8: ['solar at full output, the tenant substation and the load beside the solar both disconnected', 1.0, false, ['tenant', 'pvload']] };
  const standardSite = () => ({ intake_cable_km: 0.6, export_limit_kw: 500.0, generator_kw: 500.0, pv_kw: 1000.0, pv_on: 4,
    subs: [{ n: 1, kva: 1600, load_kw: 900, km: 0.15 }, { n: 2, kva: 1000, load_kw: 550, km: 0.25 }, { n: 3, kva: 1000, load_kw: 500, km: 0.35 },
           { n: 4, kva: 1000, load_kw: 350, km: 0.45 }, { n: 5, kva: 800, load_kw: 300, km: 0.30, tenant: true }] });

  // pairs
  const add = (a, b) => [a[0] + b[0], a[1] + b[1]], sub = (a, b) => [a[0] - b[0], a[1] - b[1]];
  const mul = (a, b) => [a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]];
  const div = (a, b) => { const d = b[0] * b[0] + b[1] * b[1]; return [(a[0] * b[0] + a[1] * b[1]) / d, (a[1] * b[0] - a[0] * b[1]) / d]; };
  const conj = a => [a[0], -a[1]], scale = (a, k) => [a[0] * k, a[1] * k], mag = a => Math.hypot(a[0], a[1]);
  const rnd = (x, d) => Number(x.toFixed(d));                        // decimal rounding of the value held, as Python's round does

  function solve(site, pvShare, genOn, off, loadShare, c, tol) {
    c = c || CANDIDATE; tol = tol || 1e-9; off = off || []; if (loadShare === undefined) loadShare = 1.0;
    const vb = c.kv * 1000 / Math.sqrt(3);
    const zsMag = (c.kv ** 2) / c.grid_fault_mva, xr = c.grid_x_over_r, rs = zsMag / Math.sqrt(1 + xr * xr);
    const Z = { poc: [rs, rs * xr], board: scale([c.hv_cable_r, c.hv_cable_x], site.intake_cable_km) };
    const parent = { grid: null, poc: 'grid', board: 'poc' }, S = {}, kva = {};
    const tanl = Math.tan(Math.acos(c.load_pf)), tang = Math.tan(Math.acos(c.gen_pf));
    if (genOn) S.board = scale([site.generator_kw, site.generator_kw * tang], -1000 / 3);
    for (const s of site.subs) {
      if (off.includes('tenant') && s.tenant) continue;                // a disconnected substation is not in the network at all
      const hv = 'hv' + s.n, lv = 'lv' + s.n; parent[hv] = 'board'; parent[lv] = hv;
      Z[hv] = scale([c.hv_cable_r, c.hv_cable_x], s.km);
      const zt = c.tx_z_pct / 100 * (c.kv ** 2) / (s.kva / 1000), txr = c.tx_x_over_r, rt = zt / Math.sqrt(1 + txr * txr);
      Z[lv] = [rt, rt * txr]; kva[lv] = s.kva;
      const kw = (off.includes('pvload') && s.n === site.pv_on) ? 0.0 : s.load_kw * loadShare;
      let p = [kw, kw * tanl];
      if (s.n === site.pv_on) p = sub(p, [site.pv_kw * pvShare, 0]);
      S[lv] = scale(p, 1000 / 3);
    }
    const kids = {};
    for (const n of Object.keys(parent)) if (parent[n] !== null) (kids[parent[n]] = kids[parent[n]] || []).push(n);
    const order = ['grid'];
    for (let i = 0; i < order.length; i++) order.push(...(kids[order[i]] || []));
    let V = {}; for (const n of order) V[n] = [vb, 0];
    let rounds = 0, J;
    for (;;) {
      rounds++;
      J = {}; for (const n of order) J[n] = S[n] ? conj(div(S[n], V[n])) : [0, 0];
      for (let i = order.length - 1; i >= 0; i--) { const n = order[i]; if (parent[n] !== null) J[parent[n]] = add(J[parent[n]], J[n]); }   // PULSE ONE: currents sum back toward the grid
      const nv = { grid: [vb, 0] };
      for (const n of order.slice(1)) nv[n] = sub(nv[parent[n]], mul(J[n], Z[n]));                                                        // PULSE TWO: volts fall (or rise) out from the grid
      let step = 0; for (const n of order) step = Math.max(step, mag(sub(nv[n], V[n])));
      V = nv;
      if (step < tol || rounds > 300) break;
    }
    const sPoc = scale(mul(V.poc, conj(J.poc)), 3);                   // + import, - export, in volt amperes
    let loss = 0; for (const n of order.slice(1)) loss += mag(J[n]) ** 2 * Z[n][0]; loss *= 3;
    let net = 0; for (const n of Object.keys(S)) net += S[n][0]; net *= 3;
    const source = mul(V.grid, conj(J.poc))[0] * 3;
    const tx = {}; for (const n of Object.keys(kva)) tx[n] = mag(scale(mul(V[n], conj(J[n])), 3)) / 1000 / kva[n] * 100;
    const lv = 'lv' + site.pv_on; let faultKa = null;
    if (Z[lv]) {
      const zpath = add(add(Z.poc, Z.board), add(Z['hv' + site.pv_on], Z[lv]));
      const iGrid = vb / mag(zpath);
      const iPv = c.inverter_fault_x_rated * site.pv_kw * pvShare * 1000 / (Math.sqrt(3) * c.kv * 1000);
      const iGen = genOn ? (site.generator_kw / c.gen_pf * 1000 / (Math.sqrt(3) * c.kv * 1000) / c.generator_subtransient_pu) : 0.0;
      faultKa = { grid_only: rnd(iGrid * c.kv / 0.4 / 1000, 2), with_sources: rnd((iGrid + iPv + iGen) * c.kv / 0.4 / 1000, 2) };
    }
    const Vpu = {}; for (const n of order) Vpu[n] = mag(V[n]) / vb;
    return { V: Vpu, p_poc_kw: sPoc[0] / 1000, q_poc_kvar: sPoc[1] / 1000, loss_kw: loss / 1000, tx_loading_pct: tx, rounds,
             balance: Math.abs(source - net - loss) / Math.max(Math.abs(net), 1.0), fault_ka: faultKa };
  }

  function sitePulse(i) {
    if (i.scenario === undefined) throw new Error('this command needs "scenario" (1 to 8)');
    const sc = SCENARIOS[i.scenario]; if (!sc) throw new Error('scenario is a number from 1 to 8');
    const site = i.site || standardSite(), loadShare = i.load_share === undefined ? 1.0 : i.load_share, c = CANDIDATE;
    const r = solve(site, sc[1], sc[2], sc[3], loadShare);
    const exp = Math.max(0.0, -r.p_poc_kw), over = Math.max(0.0, exp - site.export_limit_kw);
    const vs = Object.values(r.V), vmax = Math.max(...vs), vmin = Math.min(...vs), worst = Math.max(...Object.values(r.tx_loading_pct));
    const flags = [];
    if (over > 0) flags.push('export ' + exp.toFixed(0) + ' kW is ' + over.toFixed(0) + ' kW over the ' + site.export_limit_kw.toFixed(0) + ' kW limit: the solar must be held back');
    if (vmax > c.volts_high_pu) flags.push('highest voltage ' + vmax.toFixed(3) + ' of nominal is over ' + c.volts_high_pu.toFixed(2));
    if (vmin < c.volts_low_pu) flags.push('lowest voltage ' + vmin.toFixed(3) + ' of nominal is under ' + c.volts_low_pu.toFixed(2));
    if (worst > 100) flags.push('a transformer is at ' + worst.toFixed(0) + '% of its rating');
    const signed = (x) => (x < 0 ? '-' : '+') + Math.abs(x).toFixed(0);
    return { numbers: { connection_point_kw: rnd(r.p_poc_kw, 1), connection_point_kvar: rnd(r.q_poc_kvar, 1), export_kw: rnd(exp, 1), over_limit_kw: rnd(over, 1),
                        losses_kw: rnd(r.loss_kw, 2), highest_volts_pu: rnd(vmax, 4), lowest_volts_pu: rnd(vmin, 4), worst_transformer_pct: rnd(worst, 1),
                        rounds: r.rounds, fault_level_beside_solar_ka: r.fault_ka },
             said: sc[0] + ', load ' + Math.round(loadShare * 100) + '%: connection point ' + signed(r.p_poc_kw) + ' kW (plus is import), ' + signed(r.q_poc_kvar) + ' kvar; volts ' + vmin.toFixed(3) + ' to ' + vmax.toFixed(3) +
                   '; busiest transformer ' + worst.toFixed(0) + '%; ' + (flags.length ? flags.join('; ') : 'inside every limit'),
             how: 'two pulses per round until the volts stop moving: currents summed back to the grid, volts dropped or raised out from it. A GENERIC site, no real one; every electrical figure is a CANDIDATE. An estimate, not a study.' };
  }

  const F = root.FIRE || (typeof require !== 'undefined' ? require('./fire.js') : null);
  if (!F) throw new Error('fire_site.js needs fire.js loaded first');
  F.register('site-pulse', 'SITE PULSE', sitePulse);
  F.sitePulse = { solve, standardSite, SCENARIOS, CANDIDATE };
})(typeof window !== 'undefined' ? window : globalThis);
