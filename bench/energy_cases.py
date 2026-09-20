#!/usr/bin/env python3
"""bench/energy_cases.py - SITE ENERGY: a very large private network (the scale of a major airport) hour by hour for a year.

The question an owner asks before any electrical study: if we put this much solar and this much battery behind our meter, how much of
our own electricity do we make, what is the most we still pull from the grid, and how much solar is thrown away?
GENERIC: the round figures of a published article on a major airport, which cites the operator's public sustainability report:
about 271 GWh a year, peak about 100 MW; an option of 150 MWp of solar (about 135 GWh a year) and 600 MWh of battery.
Every hour: solar first, then the battery, then the grid. Load and solar shapes are simple stated curves (CANDIDATE), seeded, not data.
THE CHECK THAT CAN FAIL: energy in = energy out, to a part in a billion, every case.
"""
import json
import math
import random

def year(annual_gwh=271.0, peak_mw=100.0, pv_mwp=150.0, pv_gwh_per_150=135.0, batt_mwh=600.0, batt_mw=100.0, eff=0.90, seed=1):
    g = random.Random(seed); load = []; sun = []
    for h in range(8760):
        d, hr = divmod(h, 24)
        shape = 0.55 + 0.45 * max(0.0, math.sin(math.pi * (hr - 4) / 18)) if 4 <= hr <= 22 else 0.55      # busy by day, never off
        load.append(shape * (1 + 0.08 * math.cos(2 * math.pi * (d - 15) / 365)))                          # a little more in winter
        elev = max(0.0, math.sin(math.pi * (hr - 6) / 12)) if 6 <= hr <= 18 else 0.0
        season = 0.55 + 0.45 * math.cos(2 * math.pi * (d - 172) / 365)                                   # long days in June
        sun.append(elev * season * g.uniform(0.25, 1.0))                                                # cloud, seeded
    k = annual_gwh * 1000 / sum(load); load = [min(x * k, peak_mw) for x in load]
    k = annual_gwh * 1000 / sum(load); load = [x * k for x in load]
    ks = (pv_gwh_per_150 * 1000 * pv_mwp / 150.0) / max(sum(sun), 1e-9); sun = [x * ks for x in sun]
    soc = 0.0; imp = 0.0; spill = 0.0; charged = 0.0; discharged = 0.0; peak_import = 0.0; own = 0.0; rt = math.sqrt(eff)
    for L, S in zip(load, sun):
        direct = min(L, S); own += direct; need = L - direct; spare = S - direct
        c = min(spare, batt_mw, (batt_mwh - soc) / rt); soc += c * rt; charged += c; spill += spare - c
        dch = min(need, batt_mw, soc * rt); soc -= dch / rt; discharged += dch; own += dch
        g_in = need - dch; imp += g_in; peak_import = max(peak_import, g_in)
    total_load = sum(load); total_sun = sum(sun)
    # energy in = energy out: solar + grid = load + thrown away + (what went into the battery - what came out: its losses and what is left in it)
    balance = abs(total_sun + imp - total_load - spill - (charged - discharged)) / total_load
    return dict(load_gwh=total_load / 1000, solar_gwh=total_sun / 1000, import_gwh=imp / 1000, spilled_gwh=spill / 1000, own_share=own / total_load,
                peak_import_mw=peak_import, battery_full_cycles=discharged / batt_mwh if batt_mwh else 0.0, average_mw=total_load / 8760, balance=balance, soc_end=soc)

def t_energy(pv_mwp, batt_mwh):
    r = year(pv_mwp=pv_mwp, batt_mwh=batt_mwh, batt_mw=max(1.0, batt_mwh / 6.0) if batt_mwh else 0.0)
    inputs = dict(annual_gwh=271, peak_mw=100, pv_mwp=pv_mwp, battery_mwh=batt_mwh)
    return dict(question='A site using 271 GWh a year, peak 100 MW, with %g MWp of solar and %g MWh of battery: how much of its own electricity does it make?' % (pv_mwp, batt_mwh),
                sentence='Site energy: %g MWp solar, %g MWh battery' % (pv_mwp, batt_mwh), command='fire site-energy ' + json.dumps(inputs, sort_keys=True),
                did='8,760 hours: solar first, then the battery, then the grid; then energy in against energy out',
                numbers=dict(own_share_pct=round(r['own_share'] * 100, 1), solar_gwh=round(r['solar_gwh'], 1), grid_import_gwh=round(r['import_gwh'], 1), solar_thrown_away_gwh=round(r['spilled_gwh'], 1),
                             peak_grid_import_mw=round(r['peak_import_mw'], 1), battery_full_cycles_a_year=round(r['battery_full_cycles']), energy_balance_error=float('%.1e' % r['balance'])),
                observed='makes %.0f%% of its own electricity; still pulls up to %.0f MW from the grid; throws away %.1f GWh of solar' % (r['own_share'] * 100, r['peak_import_mw'], r['spilled_gwh']),
                assumed='load and solar shapes are simple stated curves with seeded cloud, not measured data; round trip efficiency 90%; battery power = a sixth of its energy',
                result='CONFIRMED' if r['balance'] < 1e-9 else 'REFUTED')

def t_known():
    """Two sums from the published article, checked: 600 MWh lasts 9.7 hours at 62 MW and 6 hours at 100 MW; and what 62 MW means."""
    a, b = 600 / 62, 600 / 100; avg_all_hours = 271000 / 8760; avg_12h_day = 271000 / (365 * 12)
    ok = abs(a - 9.7) < 0.05 and abs(b - 6.0) < 1e-9 and abs(avg_12h_day - 61.9) < 0.1
    return dict(question='Do the published sums hold: 600 MWh = 9.7 hours at 62 MW and 6 hours at 100 MW; and is 62 MW the average demand?', sentence='Site energy: the known answers',
                command='fire site-energy-known {}', did='divided', numbers=dict(hours_at_62_mw=round(a, 2), hours_at_100_mw=round(b, 2), average_over_all_hours_mw=round(avg_all_hours, 1), average_over_a_12_hour_day_mw=round(avg_12h_day, 1)),
                observed='both durations hold. 62 MW is the average if the 271 GWh falls in a 12 hour day; spread over all 8,760 hours the average is %.1f MW. A model must say which it uses.' % avg_all_hours,
                assumed='none', result='CONFIRMED' if ok else 'REFUTED')

def registry():
    R = [('SITE ENERGY', 'the known answers', (t_known, ()))]
    for pv in (0, 50, 100, 150, 200, 300):
        for batt in (0, 150, 300, 600, 1200): R.append(('SITE ENERGY', '%g MWp, %g MWh' % (pv, batt), (t_energy, (pv, batt))))
    return R
