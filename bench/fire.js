// bench/fire.js - the pop commands that RUN IN THE VISITOR'S BROWSER. Plain JavaScript, no library, nothing leaves the device.
// Each function is a port of the Python in bench/*_cases.py and is checked against the saved records by bench/fire_check.mjs:
// same inputs, same numbers, or the port is wrong. A command is:  fire <name> {inputs as JSON}
(function (root) {
  const R20 = { al: { 50: 0.641, 70: 0.443, 95: 0.320, 120: 0.253, 150: 0.206, 185: 0.164, 240: 0.125, 300: 0.100, 400: 0.0778, 500: 0.0605, 630: 0.0469 },
                cu: { 50: 0.387, 70: 0.268, 95: 0.193, 120: 0.153, 150: 0.124, 185: 0.0991, 240: 0.0754, 300: 0.0601, 400: 0.0470, 500: 0.0366, 630: 0.0283 } };
  const K = { al: 94.0, cu: 143.0 }, ALPHA = { al: 0.00403, cu: 0.00393 };
  const RATE_AL = { 50: 150, 70: 185, 95: 220, 120: 250, 150: 280, 185: 320, 240: 370, 300: 420, 400: 480, 500: 545, 630: 615 };
  const rate = (m, s) => m === 'al' ? RATE_AL[s] : Math.round(RATE_AL[s] * 1.28);
  // as Python's round(): the number as it is actually held decides; only an EXACT half goes to the even side
  const r = (x, d) => { const up = Number(x.toFixed(d)), t = Math.abs(x).toFixed(d + 25), tail = t.slice(t.indexOf('.') + 1 + d);
    if (!/^50*$/.test(tail)) return up;
    const k = Math.pow(10, d), n = Math.round(Math.abs(up) * k); return n % 2 === 0 ? up : Number((up - Math.sign(x) / k).toFixed(d)); };
  const need = (o, keys) => { for (const k of keys) if (o[k] === undefined) throw new Error('this command needs "' + k + '"'); };

  const RUN = {
    'cable-withstand': { family: 'CABLE CHECK', run(i) { need(i, ['metal', 'size_mm2', 'seconds', 'fault_ka']);
      if (!K[i.metal]) throw new Error('metal is "al" or "cu"');
      const limit = K[i.metal] * i.size_mm2 / Math.sqrt(i.seconds) / 1000, ok = i.fault_ka <= limit;
      return { numbers: { withstand_ka: r(limit, 2), fault_ka: i.fault_ka, margin_pct: r((limit / i.fault_ka - 1) * 100, 1) },
               said: 'withstands ' + limit.toFixed(2) + ' kA; asked for ' + i.fault_ka + ' kA: ' + (ok ? 'survives' : 'DOES NOT SURVIVE: a larger conductor or faster protection'),
               how: 'adiabatic rule: k x area / square root of time, k = ' + K[i.metal] }; } },
    'cable-run': { family: 'CABLE CHECK', run(i) { need(i, ['metal', 'size_mm2', 'amps', 'metres', 'kv', 'derate']);
      if (!R20[i.metal] || !R20[i.metal][i.size_mm2]) throw new Error('sizes: ' + Object.keys(R20.al).join(', ') + ' mm2; metal "al" or "cu"');
      const rh = R20[i.metal][i.size_mm2] * (1 + ALPHA[i.metal] * 70), x = 0.08;
      const vd = Math.sqrt(3) * i.amps * (rh * 0.95 + x * Math.sqrt(1 - 0.95 * 0.95)) * i.metres / 1000, pct = vd / (i.kv * 1000) * 100;
      const use = i.amps / (rate(i.metal, i.size_mm2) * i.derate) * 100, flags = [];
      if (use > 100) flags.push('over its derated rating'); else if (use > 85) flags.push('within 15 per cent of its derated rating: commission a buried cable thermal study');
      if (pct > 1.5) flags.push('voltage drop ' + pct.toFixed(2) + '% is over 1.5%');
      return { numbers: { volt_drop_pct: r(pct, 3), loading_pct: r(use, 1), loss_kw: r(3 * i.amps * i.amps * rh * i.metres / 1000 / 1000, 2) },
               said: 'drop ' + pct.toFixed(2) + '%, loaded to ' + use.toFixed(0) + '% of its derated rating; ' + (flags.length ? flags.join('; ') : 'inside both limits'),
               how: 'resistance at 20 C raised to 90 C; drop = root three x amps x (r cos + x sin) x length; rating x derating (ratings are CANDIDATE round figures)' }; } },
    'national-day': { family: 'NATIONAL DAY', run(i) { need(i, ['firm_gw', 'round_trip']);
      const raw = []; for (let h = 0; h < 48; h++) raw.push(24.25 + 6.25 * Math.sin(Math.PI * (h / 2 - 7) / 12));
      const k = 604 / (raw.reduce((a, b) => a + b, 0) / 2), d = raw.map(v => v * k);
      const short = d.reduce((a, v) => a + Math.max(0, v - i.firm_gw), 0) / 2, spare = d.reduce((a, v) => a + Math.max(0, i.firm_gw - v), 0) / 2, inp = short / i.round_trip;
      return { numbers: { storage_delivers_gwh: r(short, 1), must_be_put_in_gwh: r(inp, 1), spare_generation_that_day_gwh: r(spare, 1), day_low_gw: r(Math.min(...d), 1), day_high_gw: r(Math.max(...d), 1) },
               said: 'storage delivers ' + short.toFixed(0) + ' GWh and needs ' + inp.toFixed(0) + ' GWh put in; the steady generation has ' + spare.toFixed(0) + ' GWh to spare that day: ' + (spare >= inp ? 'enough to refill it' : 'NOT enough to refill it'),
               how: '48 half hours of a 604 GWh spring day; demand above the steady generation comes from storage' }; } },
    'dc-traction-chain': { family: 'DC TRACTION', run(i) { need(i, ['inverter', 'transformer', 'rectifier', 'dc_converter']);
      const ac = i.inverter * i.transformer * i.rectifier, s = i.dc_converter - ac;
      return { numbers: { reaches_rail_by_ac_route_pct: r(ac * 100, 2), reaches_rail_by_dc_route_pct: r(i.dc_converter * 100, 2), saved_pct_of_the_solar: r(s * 100, 2) },
               said: (ac * 100).toFixed(1) + '% arrives by the usual route, ' + (i.dc_converter * 100).toFixed(1) + '% by the direct route: ' + (s * 100).toFixed(1) + '% of the SOLAR is saved',
               how: 'multiplied the efficiencies along each route' }; } },
    'dc-traction-scale': { family: 'DC TRACTION', run(i) { need(i, ['solar_gwh', 'saving_share']);
      const traction = 1216 * 0.825, saved = i.solar_gwh * i.saving_share;
      return { numbers: { traction_gwh: r(traction, 1), saved_gwh: r(saved, 2), solar_share_of_traction_pct: r(i.solar_gwh / traction * 100, 1), average_kw_per_substation: Math.round(traction * 1e6 / 300 / 8760) },
               said: 'saves ' + saved.toFixed(1) + ' GWh a year; the solar is ' + (i.solar_gwh / traction * 100).toFixed(1) + '% of traction energy',
               how: 'traction = total x 82.5%; saving = solar x share saved' }; } },
  };

  function parse(text) {
    const m = String(text).trim().match(/^fire\s+([a-z0-9-]+)\s*(\{[\s\S]*\})?\s*$/i);
    if (!m) throw new Error('a command looks like:  fire cable-withstand {"metal":"al","size_mm2":185,"seconds":1,"fault_ka":16}');
    let inputs = {}; if (m[2]) { try { inputs = JSON.parse(m[2]); } catch (e) { throw new Error('the part in { } is not valid: ' + e.message); } }
    return { name: m[1].toLowerCase(), inputs };
  }
  function fire(text) { const c = parse(text), f = RUN[c.name]; if (!f) return { name: c.name, inputs: c.inputs, ran: false }; const o = f.run(c.inputs); return Object.assign({ name: c.name, inputs: c.inputs, ran: true, family: f.family }, o); }
  // another file may add commands:  FIRE.register('site-pulse', 'SITE PULSE', inputs => ({ numbers, said, how }))
  function register(name, family, run) { RUN[name] = { family, run }; }
  root.FIRE = { fire, parse, register, get names() { return Object.keys(RUN); } };
  if (typeof module !== 'undefined') module.exports = root.FIRE;
})(typeof window !== 'undefined' ? window : globalThis);
