#!/usr/bin/env python3
"""bench/site_cases.py - SITE PULSE: a generic industrial site behind its meter, as cells and two pulses.

A factory with its own 11 kV intake, a few site substations (each a transformer with a lumped load on its low voltage side), solar
on the low voltage side of ONE of them, an on site generator, and an export limit agreed with the network operator. The questions a
site owner pays an engineer to answer: what flows at the connection point, what voltage each bus sees, how loaded each transformer is,
whether the export limit binds, and how much the fault level at a low voltage board rises. Here they are ESTIMATES from stated,
generic figures, so that the right study can be commissioned; every figure is an input the owner can overwrite with their own.

NOTHING HERE IS ANY REAL SITE. Sizes are round numbers chosen to be typical. Every electrical figure is a CANDIDATE quoted from memory.
Method: the same forward-backward sweep as the feeder pulse (tests.py), per phase, in volts and amps at 11 kV, transformers as series
impedances referred to 11 kV, constant power loads and sources (a source is a negative load).
"""
import json
import math
import random

CANDIDATE = dict(kv=11.0, grid_fault_mva=150.0, grid_x_over_r=10.0, hv_cable_r=0.20, hv_cable_x=0.09, tx_z_pct=5.5, tx_x_over_r=5.0,
                 load_pf=0.90, gen_pf=0.95, pv_pf=1.0, volts_high_pu=1.06, volts_low_pu=0.94, inverter_fault_x_rated=1.1, generator_subtransient_pu=0.15)

def standard_site():
    """Five site substations off one intake. Solar on number 4. A generator on the intake board. Round, generic figures."""
    return dict(intake_cable_km=0.6, export_limit_kw=500.0, generator_kw=500.0, pv_kw=1000.0, pv_on=4,
                subs=[dict(n=1, kva=1600, load_kw=900, km=0.15), dict(n=2, kva=1000, load_kw=550, km=0.25), dict(n=3, kva=1000, load_kw=500, km=0.35),
                      dict(n=4, kva=1000, load_kw=350, km=0.45), dict(n=5, kva=800, load_kw=300, km=0.30, tenant=True)])

SCENARIOS = {1: ('no solar, no generator', 0.0, False, ()), 2: ('no solar, generator running', 0.0, True, ()),
             3: ('solar at full output, no generator', 1.0, False, ()), 4: ('solar at full output, generator running', 1.0, True, ()),
             5: ('solar at half output, no generator', 0.5, False, ()), 6: ('solar at half output, generator running', 0.5, True, ()),
             7: ('solar at full output, the tenant substation disconnected', 1.0, False, ('tenant',)),
             8: ('solar at full output, the tenant substation and the load beside the solar both disconnected', 1.0, False, ('tenant', 'pvload'))}

def solve(site, pv_share, gen_on, off=(), load_share=1.0, c=CANDIDATE, tol=1e-9):
    vb = c['kv'] * 1000 / math.sqrt(3)
    zs_mag = (c['kv'] ** 2) / c['grid_fault_mva']; xr = c['grid_x_over_r']; rs = zs_mag / math.sqrt(1 + xr * xr)
    Z = {'poc': complex(rs, rs * xr), 'board': complex(c['hv_cable_r'], c['hv_cable_x']) * site['intake_cable_km']}
    parent = {'grid': None, 'poc': 'grid', 'board': 'poc'}; S = {}; kva = {}
    tanl = math.tan(math.acos(c['load_pf'])); tang = math.tan(math.acos(c['gen_pf']))
    if gen_on: S['board'] = -complex(site['generator_kw'], site['generator_kw'] * tang) * 1000 / 3
    for s in site['subs']:
        hv, lv = 'hv%d' % s['n'], 'lv%d' % s['n']; parent[hv] = 'board'; parent[lv] = hv
        Z[hv] = complex(c['hv_cable_r'], c['hv_cable_x']) * s['km']
        zt = c['tx_z_pct'] / 100 * (c['kv'] ** 2) / (s['kva'] / 1000); txr = c['tx_x_over_r']; rt = zt / math.sqrt(1 + txr * txr)
        Z[lv] = complex(rt, rt * txr); kva[lv] = s['kva']
        dead = ('tenant' in off and s.get('tenant'))
        if dead: parent.pop(hv); parent.pop(lv); Z.pop(hv); Z.pop(lv); kva.pop(lv); continue
        kw = 0.0 if ('pvload' in off and s['n'] == site['pv_on']) else s['load_kw'] * load_share
        p = complex(kw, kw * tanl)
        if s['n'] == site['pv_on']: p -= complex(site['pv_kw'] * pv_share, 0)
        S[lv] = p * 1000 / 3
    kids = {}
    for n, p in parent.items():
        if p is not None: kids.setdefault(p, []).append(n)
    order = ['grid']
    for n in order: order += kids.get(n, [])
    V = {n: complex(vb, 0) for n in order}; rounds = 0
    while True:
        rounds += 1
        J = {n: ((S[n] / V[n]).conjugate() if n in S else 0j) for n in order}
        for n in reversed(order):                                   # PULSE ONE: currents sum back toward the grid
            if parent[n] is not None: J[parent[n]] += J[n]
        nv = {'grid': complex(vb, 0)}
        for n in order[1:]: nv[n] = nv[parent[n]] - J[n] * Z[n]    # PULSE TWO: volts fall (or rise) out from the grid
        step = max(abs(nv[n] - V[n]) for n in order); V = nv
        if step < tol or rounds > 300: break
    s_poc = V['poc'] * J['poc'].conjugate() * 3                      # + import, - export, in volt amperes
    loss = sum(abs(J[n]) ** 2 * Z[n].real for n in order[1:]) * 3
    net = sum(S.values()).real * 3
    source = (V['grid'] * J['poc'].conjugate()).real * 3
    tx = {n: abs(V[n] * J[n].conjugate() * 3) / 1000 / kva[n] * 100 for n in kva}
    # fault level at the low voltage board beside the solar: grid through the impedances, plus the inverters, plus the generator
    lv = 'lv%d' % site['pv_on']; fault_ka = None
    if lv in Z:
        zpath = Z['poc'] + Z['board'] + Z['hv%d' % site['pv_on']] + Z[lv]
        i_grid = vb / abs(zpath)                                     # amps at 11 kV
        i_pv = c['inverter_fault_x_rated'] * site['pv_kw'] * pv_share * 1000 / (math.sqrt(3) * c['kv'] * 1000)
        i_gen = (site['generator_kw'] / c['gen_pf'] * 1000 / (math.sqrt(3) * c['kv'] * 1000) / c['generator_subtransient_pu']) if gen_on else 0.0
        fault_ka = dict(grid_only=round(i_grid * c['kv'] / 0.4 / 1000, 2), with_sources=round((i_grid + i_pv + i_gen) * c['kv'] / 0.4 / 1000, 2))
    return dict(V={n: abs(V[n]) / vb for n in order}, p_poc_kw=s_poc.real / 1000, q_poc_kvar=s_poc.imag / 1000, loss_kw=loss / 1000,
                tx_loading_pct=tx, rounds=rounds, balance=abs(source - net - loss) / max(abs(net), 1.0), fault_ka=fault_ka)

def record(site, scen, load_share, note=''):
    name, pv_share, gen_on, off = SCENARIOS[scen]; c = CANDIDATE
    r = solve(site, pv_share, gen_on, off, load_share)
    export = max(0.0, -r['p_poc_kw']); over = max(0.0, export - site['export_limit_kw'])
    vmax = max(r['V'].values()); vmin = min(r['V'].values()); worst_tx = max(r['tx_loading_pct'].values())
    ok = r['rounds'] <= 300 and r['balance'] < 1e-6
    flags = []
    if over > 0: flags.append('export %.0f kW is %.0f kW over the %.0f kW limit: the solar must be held back' % (export, over, site['export_limit_kw']))
    if vmax > c['volts_high_pu']: flags.append('highest voltage %.3f of nominal is over %.2f' % (vmax, c['volts_high_pu']))
    if vmin < c['volts_low_pu']: flags.append('lowest voltage %.3f of nominal is under %.2f' % (vmin, c['volts_low_pu']))
    if worst_tx > 100: flags.append('a transformer is at %.0f%% of its rating' % worst_tx)
    inputs = dict(scenario=scen, load_share=load_share, site=site)
    return dict(question='Site pulse, scenario %d (%s), site load at %d%%%s: what flows at the connection point, what does each bus see, how loaded is each transformer?' % (scen, name, round(load_share * 100), note),
                sentence='Site pulse: %s, load %d%%' % (name, round(load_share * 100)),
                command='fire site-pulse ' + json.dumps(inputs, separators=(',', ':'), sort_keys=True),
                did='two pulses per round until the volts stop moving: currents summed back to the grid, volts dropped or raised out from it; then power in = net load + losses',
                numbers=dict(connection_point_kw=round(r['p_poc_kw'], 1), connection_point_kvar=round(r['q_poc_kvar'], 1), export_kw=round(export, 1), over_limit_kw=round(over, 1),
                             losses_kw=round(r['loss_kw'], 2), highest_volts_pu=round(vmax, 4), lowest_volts_pu=round(vmin, 4), worst_transformer_pct=round(worst_tx, 1),
                             rounds=r['rounds'], power_balance_error=float('%.2e' % r['balance']), fault_level_beside_solar_ka=r['fault_ka']),
                observed=('connection point %+.0f kW (plus is import), %+.0f kvar; volts %.3f to %.3f; busiest transformer %.0f%%; ' % (r['p_poc_kw'], r['q_poc_kvar'], vmin, vmax, worst_tx)) + ('; '.join(flags) if flags else 'inside every limit'),
                assumed='a GENERIC site, no real one; every electrical figure a CANDIDATE: ' + json.dumps(c, sort_keys=True), result='CONFIRMED' if ok else 'REFUTED')

def t_scenario(scen, load_share): return record(standard_site(), scen, load_share)

def t_threshold(kind):
    """Bisect to the number an owner wants: how much solar before a limit binds, at light load (the hard case)."""
    lo, hi = 0.0, 6000.0
    def bad(pv):
        s = standard_site(); s['pv_kw'] = pv; r = solve(s, 1.0, False, (), 0.3)
        if kind == 'export limit': return max(0.0, -r['p_poc_kw']) > s['export_limit_kw']
        if kind == 'voltage rise': return max(r['V'].values()) > CANDIDATE['volts_high_pu']
        if kind == 'transformer rating': return max(r['tx_loading_pct'].values()) > 100
    if not bad(hi): return dict(question='How much solar before the %s binds (load at 30%%)?' % kind, sentence='Site threshold: %s' % kind, command='fire site-threshold {"limit":"%s"}' % kind,
                                did='tried up to 6,000 kW', numbers=dict(threshold_kw=None), observed='never binds below 6,000 kW on this site', assumed='generic site; CANDIDATE figures', result='NO EFFECT')
    for _ in range(40):
        mid = (lo + hi) / 2
        if bad(mid): hi = mid
        else: lo = mid
    return dict(question='How much solar can this generic site carry at 30%% load before the %s binds?' % kind, sentence='Site threshold: %s' % kind,
                command='fire site-threshold {"limit":"%s","load_share":0.3}' % kind, did='halved the interval forty times between a solar size that is fine and one that is not',
                numbers=dict(threshold_kw=round(hi, 1)), observed='the %s first binds at about %.0f kW of solar' % (kind, hi), assumed='generic site; CANDIDATE figures: ' + json.dumps(CANDIDATE, sort_keys=True), result='CONFIRMED')

def random_site(seed):
    g = random.Random(seed); n = g.randint(2, 8); subs = []
    for k in range(1, n + 1):
        kva = g.choice([500, 800, 1000, 1600, 2000]); subs.append(dict(n=k, kva=kva, load_kw=round(kva * g.uniform(0.25, 0.8)), km=round(g.uniform(0.05, 0.8), 2), tenant=(k == n and g.random() < 0.3)))
    total = sum(s['load_kw'] for s in subs)
    return dict(intake_cable_km=round(g.uniform(0.1, 2.0), 2), export_limit_kw=float(g.choice([0, 50, 200, 500, 1000])), generator_kw=float(g.choice([0, 250, 500, 1000])),
                pv_kw=float(round(total * g.uniform(0.2, 1.5), -1)), pv_on=g.randint(1, n), subs=subs)

def t_survey(seed):
    """One of many generic sites: full solar at light load, generator off: the case that finds trouble."""
    return record(random_site(seed), 3, 0.3, note=', generic site number %d' % seed)

def registry():
    R = []
    for scen in range(1, 9):
        for ls in (1.0, 0.6, 0.3): R.append(('SITE PULSE', 'scenario %d at %d%% load' % (scen, round(ls * 100)), (t_scenario, (scen, ls))))
    for k in ('export limit', 'voltage rise', 'transformer rating'): R.append(('SITE THRESHOLDS', k, (t_threshold, (k,))))
    for seed in range(1, 2001): R.append(('SITE SURVEY', 'generic site %d' % seed, (t_survey, (seed,))))
    return R
