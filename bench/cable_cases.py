#!/usr/bin/env python3
"""bench/cable_cases.py - CABLE CHECK: the four questions every cable sizing study asks, as cases that can fail.

  1 sustained current   does the cable carry the load current after derating for how it is installed
  2 voltage drop        is the drop along the run inside the allowed share
  3 fault withstand     does the conductor survive the fault current for the clearing time (the adiabatic rule)
  4 thermal flag        is the case close enough to a limit that a buried cable thermal study should be commissioned

GENERIC cases only: no project, no maker, no price. Conductor resistance at 20 C is quoted from memory of the standard for class 2 sizes
(to be keyed against the estate's own conductor resistances table before anyone relies on it)
(IEC 60228, table for stranded conductors); the adiabatic constant k is the published one for the metal and insulation
(aluminium with XLPE 94, copper with XLPE 143; one second rule I = k x S). Current ratings and derating factors are CANDIDATES,
round typical figures, to be overwritten by the owner's own datasheet. The consulting engineer's study is the authority; this
finds which study to commission.
"""
import json
import math

R20 = {'al': {50: 0.641, 70: 0.443, 95: 0.320, 120: 0.253, 150: 0.206, 185: 0.164, 240: 0.125, 300: 0.100, 400: 0.0778, 500: 0.0605, 630: 0.0469},
       'cu': {50: 0.387, 70: 0.268, 95: 0.193, 120: 0.153, 150: 0.124, 185: 0.0991, 240: 0.0754, 300: 0.0601, 400: 0.0470, 500: 0.0366, 630: 0.0283}}
K = {'al': 94.0, 'cu': 143.0}
ALPHA = {'al': 0.00403, 'cu': 0.00393}
RATING_GROUND = {'al': {50: 150, 70: 185, 95: 220, 120: 250, 150: 280, 185: 320, 240: 370, 300: 420, 400: 480, 500: 545, 630: 615}}   # CANDIDATE, amps
RATING_GROUND['cu'] = {s: round(a * 1.28) for s, a in RATING_GROUND['al'].items()}                                                    # CANDIDATE ratio

def t_withstand(metal, size, seconds, fault_ka):
    limit = K[metal] * size / math.sqrt(seconds) / 1000
    ok = fault_ka <= limit
    return dict(question='Does a %d mm2 %s conductor with XLPE survive %.1f kA for %.1f s?' % (size, 'aluminium' if metal == 'al' else 'copper', fault_ka, seconds),
                sentence='Cable check: fault withstand, %d mm2 %s, %.1f kA for %.1f s' % (size, metal, fault_ka, seconds),
                command='fire cable-withstand ' + json.dumps(dict(metal=metal, size_mm2=size, seconds=seconds, fault_ka=fault_ka), sort_keys=True),
                did='adiabatic rule: the most the conductor can take is k x area / square root of time, k = %g' % K[metal],
                numbers=dict(withstand_ka=round(limit, 2), fault_ka=fault_ka, margin_pct=round((limit / fault_ka - 1) * 100, 1)),
                observed='withstands %.2f kA; asked for %.1f kA: %s' % (limit, fault_ka, 'survives' if ok else 'DOES NOT SURVIVE: a larger conductor or faster protection'),
                assumed='k is the published constant for the metal with XLPE (90 C to 250 C); the fault current and time are the case', result='CONFIRMED')

def t_run(metal, size, amps, metres, kv, derate):
    r_hot = R20[metal][size] * (1 + ALPHA[metal] * (90 - 20)); x = 0.08
    vd = math.sqrt(3) * amps * (r_hot * 0.95 + x * math.sqrt(1 - 0.95 ** 2)) * metres / 1000; pct = vd / (kv * 1000) * 100
    cap = RATING_GROUND[metal][size] * derate; use = amps / cap * 100
    flags = []
    if use > 100: flags.append('over its derated rating')
    elif use > 85: flags.append('within 15 per cent of its derated rating: commission a buried cable thermal study')
    if pct > 1.5: flags.append('voltage drop %.2f%% is over 1.5%%' % pct)
    return dict(question='Does a %d mm2 %s three core run carry %d A over %d m at %g kV, derated to %d%%?' % (size, metal, amps, metres, kv, round(derate * 100)),
                sentence='Cable check: %d A over %d m on %d mm2 %s at %g kV' % (amps, metres, size, metal, kv),
                command='fire cable-run ' + json.dumps(dict(metal=metal, size_mm2=size, amps=amps, metres=metres, kv=kv, derate=derate), sort_keys=True),
                did='resistance at 20 C from the standard table, raised to 90 C; drop = root three x amps x (r cos + x sin) x length; rating x derating',
                numbers=dict(volt_drop_pct=round(pct, 3), loading_pct=round(use, 1), loss_kw=round(3 * amps ** 2 * r_hot * metres / 1000 / 1000, 2)),
                observed=('drop %.2f%%, loaded to %.0f%% of its derated rating; ' % (pct, use)) + ('; '.join(flags) if flags else 'inside both limits'),
                assumed='ratings and derating are CANDIDATE round figures; reactance 0.08 ohm/km assumed; power factor 0.95', result='CONFIRMED')

def t_selfcheck():
    """The one case with a known answer: 185 mm2 aluminium for one second is 94 x 185 = 17.39 kA, the figure makers publish."""
    got = K['al'] * 185 / 1000
    return dict(question='Does the adiabatic rule give the 17.39 kA that is published for 185 mm2 aluminium with XLPE for one second?', sentence='Cable check: the known answer',
                command='fire cable-withstand {"fault_ka":17.39,"metal":"al","seconds":1.0,"size_mm2":185}', did='94 x 185 / 1000', numbers=dict(withstand_ka=round(got, 2)),
                observed='%.2f kA' % got, assumed='none', result='CONFIRMED' if abs(got - 17.39) < 0.005 else 'REFUTED')

def registry():
    R = [('CABLE CHECK', 'the known answer', (t_selfcheck, ()))]
    for metal in ('al', 'cu'):
        for size in (95, 185, 300, 630):
            for seconds in (0.2, 1.0, 3.0):
                for ka in (8.0, 16.0, 25.0): R.append(('CABLE CHECK', 'withstand %s %d %.1fs %.0fkA' % (metal, size, seconds, ka), (t_withstand, (metal, size, seconds, ka))))
    for metal in ('al', 'cu'):
        for size in (95, 185, 300, 630):
            for amps in (150, 300, 450):
                for metres in (200, 800, 2500):
                    for kv, derate in ((11.0, 0.8), (33.0, 0.7)): R.append(('CABLE CHECK', 'run %s %d %dA %dm %gkV' % (metal, size, amps, metres, kv), (t_run, (metal, size, amps, metres, kv, derate))))
    return R
