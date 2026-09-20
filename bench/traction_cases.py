#!/usr/bin/env python3
"""bench/traction_cases.py - DC TRACTION: solar fed straight into a metro's direct current traction system, as sums that can fail.

GENERIC: the round figures of a published article on a large metro system, which cites a public freedom of information response:
about 1,216 GWh a year, 80 to 85 per cent of it traction, about 300 traction substations turning 11 to 22 kV alternating current into a
nominal 630 V direct current rail; a plan for 64 MW of solar giving about 80 GWh a year. Converter efficiencies are CANDIDATES.
The point: solar makes direct current and the trains use direct current; going through alternating current on the way loses energy twice.
"""
import json

def t_chain(inverter, transformer, rectifier, dcdc):
    ac = inverter * transformer * rectifier; saving = dcdc - ac
    inputs = dict(inverter=inverter, transformer=transformer, rectifier=rectifier, dc_converter=dcdc)
    return dict(question='Of each unit of solar, how much reaches the rail by the usual route (inverter, transformer, rectifier) and how much by one direct current converter?',
                sentence='DC traction: the two routes compared', command='fire dc-traction-chain ' + json.dumps(inputs, sort_keys=True), did='multiplied the efficiencies along each route',
                numbers=dict(reaches_rail_by_ac_route_pct=round(ac * 100, 2), reaches_rail_by_dc_route_pct=round(dcdc * 100, 2), saved_pct_of_the_solar=round(saving * 100, 2)),
                observed='%.1f%% arrives by the usual route, %.1f%% by the direct route: %.1f%% of the SOLAR is saved' % (ac * 100, dcdc * 100, saving * 100),
                assumed='converter efficiencies are CANDIDATE round figures', result='CONFIRMED' if 0 < saving < 0.2 else 'REFUTED')

def t_scale(solar_gwh, saving_share):
    total, traction_share, subs = 1216.0, 0.825, 300
    traction = total * traction_share; saved = solar_gwh * saving_share
    return dict(question='With %g GWh a year of solar fed on the direct current side and %g%% of it saved, how much energy is that, and against what?' % (solar_gwh, saving_share * 100),
                sentence='DC traction: %g GWh of solar, %g%% saved' % (solar_gwh, saving_share * 100), command='fire dc-traction-scale ' + json.dumps(dict(solar_gwh=solar_gwh, saving_share=saving_share), sort_keys=True),
                did='traction energy = total x share; saving = solar x share saved; average load per substation = traction / substations / hours',
                numbers=dict(traction_gwh=round(traction, 1), saved_gwh=round(saved, 2), solar_share_of_traction_pct=round(solar_gwh / traction * 100, 1), average_kw_per_substation=round(traction * 1e6 / subs / 8760)),
                observed='saves %.1f GWh a year; the solar is %.1f%% of traction energy; an average traction substation carries about %.0f kW' % (saved, solar_gwh / traction * 100, traction * 1e6 / subs / 8760),
                assumed='traction share 82.5%, the middle of the published 80 to 85%', result='CONFIRMED')

def t_known():
    cf = 80.0 / (64 * 8.76); full = 1216 * 0.825
    return dict(question='Do the published sums hold, and what do they apply to?', sentence='DC traction: the known answers', command='fire dc-traction-known {}', did='divided and multiplied',
                numbers=dict(capacity_factor_pct_implied_by_64_mw_and_80_gwh=round(cf * 100, 1), saving_gwh_if_all_traction_were_dc_fed_low=round(full * 0.05), saving_gwh_if_all_traction_were_dc_fed_high=round(full * 0.10),
                             saving_gwh_on_80_gwh_of_solar_low=round(80 * 0.05, 1), saving_gwh_on_80_gwh_of_solar_high=round(80 * 0.10, 1)),
                observed='50 to 100 GWh a year is 5 to 10%% of ALL traction energy (%.0f GWh): it is the prize if every unit came in on the direct current side. On 80 GWh of solar the same 5 to 10%% is 4 to 8 GWh. And 80 GWh from 64 MW implies a capacity factor of %.1f%%, above the 10 to 11%% usual for the city: check the yield.' % (full, cf * 100),
                assumed='none', result='CONFIRMED')

def registry():
    R = [('DC TRACTION', 'the known answers', (t_known, ()))]
    for inv in (0.97, 0.98):
        for rec in (0.95, 0.97):
            for dc in (0.97, 0.985): R.append(('DC TRACTION', 'routes inv %g rect %g dc %g' % (inv, rec, dc), (t_chain, (inv, 0.99, rec, dc))))
    for g in (80.0, 160.0, 400.0):
        for s in (0.05, 0.075, 0.10): R.append(('DC TRACTION', '%g GWh at %g%%' % (g, s * 100), (t_scale, (g, s))))
    return R
