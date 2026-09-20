#!/usr/bin/env python3
"""bench/national_cases.py - NATIONAL DAY: one spring day of a whole country's electricity, and how much storage it would take.

GENERIC round figures from a published article citing the system operator's public half hourly demand forecast: demand between 18 and
30.5 GW, 604 GWh in the day; a winter peak of about 44.4 GW. The day's shape is a stated smooth curve (CANDIDATE), scaled to the total.
Question: with G gigawatts of steady generation running all day (nuclear, wind, gas, or none), how much must storage deliver?
"""
import json
import math

def day():
    raw = [24.25 + 6.25 * math.sin(math.pi * (h / 2.0 - 7) / 12) for h in range(48)]          # half hours; low at night, high by day
    k = 604.0 / (sum(raw) / 2.0); return [x * k for x in raw]

def t_storage(firm_gw, eff):
    d = day(); short = sum(max(0.0, x - firm_gw) for x in d) / 2.0; spare = sum(max(0.0, firm_gw - x) for x in d) / 2.0
    need = short / eff
    return dict(question='With %g GW of steady generation all day, how much must storage deliver on a 604 GWh spring day, and how much must go in?' % firm_gw,
                sentence='National day: %g GW steady generation' % firm_gw, command='fire national-day ' + json.dumps(dict(firm_gw=firm_gw, round_trip=eff), sort_keys=True),
                did='48 half hours: demand above the steady generation comes from storage; what goes in is that divided by the round trip efficiency',
                numbers=dict(storage_delivers_gwh=round(short, 1), must_be_put_in_gwh=round(need, 1), spare_generation_that_day_gwh=round(spare, 1), day_low_gw=round(min(d), 1), day_high_gw=round(max(d), 1)),
                observed='storage delivers %.0f GWh and needs %.0f GWh put in; the steady generation has %.0f GWh to spare that day: %s' % (short, need, spare, 'enough to refill it' if spare >= need else 'NOT enough to refill it'),
                assumed='a smooth stated day shape scaled to 604 GWh; round trip efficiency as given', result='CONFIRMED' if abs(sum(d) / 2.0 - 604.0) < 1e-9 else 'REFUTED')

def t_known():
    avg = 604.0 / 24; need = 604.0 / 0.9
    ok = 18 <= avg <= 30.5 and abs(need - 670) < 2
    return dict(question='Do the published sums hold: 604 GWh in a day with demand between 18 and 30.5 GW, and about 670 GWh of storage to cover it all?', sentence='National day: the known answers',
                command='fire national-day-known {}', did='divided', numbers=dict(average_gw=round(avg, 1), storage_input_gwh_at_90_pct_round_trip=round(need)),
                observed='the day averages %.1f GW, inside 18 to 30.5; 604 / 0.90 = %.0f GWh: the published 670 holds at a 90%% round trip' % (avg, need), assumed='none', result='CONFIRMED' if ok else 'REFUTED')

def registry():
    R = [('NATIONAL DAY', 'the known answers', (t_known, ()))]
    for g in (0, 5, 10, 15, 18, 20, 22, 25, 28, 30.5):
        for eff in (0.85, 0.90): R.append(('NATIONAL DAY', '%g GW steady, %g round trip' % (g, eff), (t_storage, (g, eff))))
    return R
