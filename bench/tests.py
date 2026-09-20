#!/usr/bin/env python3
"""bench/tests.py - the hundred. Each test is a pure function of its id: same id, same answer, on any machine.

Every test returns one record: the question, what was done, what was seen, the numbers, and a verdict that CAN be
REFUTED. Nothing here draws anything. These are the sums and the rules; the Kuiper and the wafer show them.

FAMILIES (real names, not numbers):
  ARRANGEMENTS  ten ways to place n cells; the black sky rule decides (a dot is never wider than a third of the gap)
  GATES         ten selections and compositions on a real population; lit + dark = the whole, exactly
  PULSES        ten pulse fronts over a real population; no cell switches before the front reaches it
  LOGIC         ten circuits made of one kind of gate cell (lit unless both its two cells were lit a tick earlier)
  FEEDER PULSE  sixty load flows by the forward-backward sweep on estimated feeders joining REAL substation points

WHAT IS REAL AND WHAT IS ASSUMED in FEEDER PULSE, said once and carried in every record:
  REAL      the places of 15,126 secondary substations in the UK Power Networks area (estate layer grid_11kv_ukpn)
  ASSUMED   which substation feeds which: a minimum spanning tree from a chosen root (the estate holds no 11 kV lines)
  CANDIDATE every electrical figure (cable ohms per km, homes per substation, kW per home, charger kW, diversity):
            typical values quoted from memory, NOT yet keyed to a source. A client overwrites them with their own.
"""
import cmath
import glob
import hashlib
import json
import math
import os
import random

GOLDEN = math.pi * (3 - math.sqrt(5))
# the estate layer sits in the data-gridatlas repository, cloned beside this one; UKPN_POINTS overrides where to look
DATA_GLOB = os.environ.get('UKPN_POINTS', os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                                       'data-gridatlas', '**', 'grid_11kv_ukpn.parquet'))


# ------------------------------------------------------------------ the population of real places
_points = None
def points():
    """(lon, lat) of every substation point, in the file's own order. Read once per process."""
    global _points
    if _points is None:
        import pyarrow.parquet as pq
        hits = glob.glob(DATA_GLOB, recursive=True)
        if not hits:
            raise FileNotFoundError('the estate layer grid_11kv_ukpn.parquet was not found')
        t = pq.read_table(hits[0], columns=['min_x', 'min_y']).to_pydict()
        _points = [(float(x), float(y)) for x, y in zip(t['min_x'], t['min_y'])]
    return _points

def km(a, b):
    """Distance in km between two (lon, lat), flat earth at this latitude: good to a part in a thousand over 30 km."""
    kx = 111.32 * math.cos(math.radians((a[1] + b[1]) / 2))
    return math.hypot((a[0] - b[0]) * kx, (a[1] - b[1]) * 110.57)


# ------------------------------------------------------------------ ARRANGEMENTS
def shape(name, n):
    P = []
    if name == 'sunflower':
        P = [(math.sqrt((j + .5) / n) * math.cos(j * GOLDEN), math.sqrt((j + .5) / n) * math.sin(j * GOLDEN)) for j in range(n)]
    elif name == 'ring':
        P = [(math.cos(2 * math.pi * j / n), math.sin(2 * math.pi * j / n)) for j in range(n)]
    elif name == 'two rings':
        h = n // 2
        P = [(math.cos(2 * math.pi * j / h), math.sin(2 * math.pi * j / h)) for j in range(h)] + \
            [(.6 * math.cos(2 * math.pi * j / (n - h)), .6 * math.sin(2 * math.pi * j / (n - h))) for j in range(n - h)]
    elif name == 'orbit':
        e = 0.3
        for j in range(n):
            a = 2 * math.pi * j / n; r = (1 - e * e) / (1 + e * math.cos(a)) / (1 + e)
            P.append((r * math.cos(a), r * math.sin(a)))
    elif name == 'square lattice':
        s = math.ceil(math.sqrt(n)); P = [(-1 + 2 * (j % s) / (s - 1), -1 + 2 * (j // s) / (s - 1)) for j in range(n)]
    elif name == 'hexagonal lattice':
        s = math.ceil(math.sqrt(n))
        P = [(-1 + 2 * ((j % s) + .5 * ((j // s) % 2)) / s, -1 + 2 * (j // s) * math.sqrt(3) / 2 / s) for j in range(n)]
    elif name == 'spiral arms':
        for j in range(n):
            arm = j % 4; t = (j // 4 + 1) / (n / 4); a = arm * math.pi / 2 + 3 * t
            P.append((t * math.cos(a), t * math.sin(a)))
    elif name == 'busbar and feeders':
        bus = n // 5; P = [(-1 + 2 * j / (bus - 1), .8) for j in range(bus)]
        rest = n - bus; f = 8
        for j in range(rest):
            P.append((-1 + 2 * (j % f + .5) / f, .7 - 1.6 * (j // f) / max(1, (rest // f))))
    elif name == 'random scatter':
        rng = random.Random(7); P = [(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in range(n)]
    elif name == 'clock':
        ticks = 12; per = n // 15
        for k in range(ticks):
            a = 2 * math.pi * k / ticks
            P += [((.85 + .15 * i / per) * math.sin(a), (.85 + .15 * i / per) * math.cos(a)) for i in range(per)]
        for length, a in ((.5, 1.0), (.75, 3.4), (.8, 5.2)):
            m = (n - len(P)) // 3 if length < .8 else n - len(P)
            P += [(length * i / m * math.sin(a), length * i / m * math.cos(a)) for i in range(m)]
    return P[:n]

def nearest_gap(P):
    """Smallest distance between any two points, by a grid of buckets."""
    n = len(P); cell = 2.2 / math.sqrt(n); B = {}
    for i, (x, y) in enumerate(P):
        B.setdefault((int(x / cell), int(y / cell)), []).append(i)
    best = 9.0
    for (cx, cy), ids in B.items():
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for j in B.get((cx + dx, cy + dy), ()):
                    for i in ids:
                        if i < j:
                            d = math.hypot(P[i][0] - P[j][0], P[i][1] - P[j][1])
                            if d < best: best = d
    return best

def t_arrangement(name, n=2000, body_px=150):
    P = shape(name, n); gap = nearest_gap(P)
    dot_px = gap / 3 * body_px                       # the black sky rule: radius at most a third of the gap
    ok = len(P) == n and dot_px >= 0.5               # a dot under half a pixel cannot be seen: the shape fails at this n
    return dict(question='Can %d cells be placed as "%s" in a body %d px in radius and still obey the black sky rule with a dot that can be seen?' % (n, name, body_px),
                did='placed the cells; found the smallest gap between any two; took a third of it as the largest honest dot',
                numbers=dict(cells=len(P), smallest_gap=round(gap, 6), largest_honest_dot_px=round(dot_px, 3)),
                observed='largest honest dot %.2f px' % dot_px, result='CONFIRMED' if ok else 'REFUTED')


# ------------------------------------------------------------------ GATES
def t_gate(kind):
    P = points(); N = len(P)
    north = {i for i, p in enumerate(P) if p[1] > 51.6}; east = {i for i, p in enumerate(P) if p[0] > 0.2}
    inner = {i for i, p in enumerate(P) if km(p, (-0.1276, 51.5072)) < 25}
    U = set(range(N)); comp = lambda s: U - s
    cases = {
        'north': (north, None), 'east': (east, None), 'within 25 km of Charing Cross': (inner, None),
        'north AND east': (north & east, None), 'north OR east': (north | east, None), 'NOT north': (comp(north), None),
        'De Morgan: NOT (north AND east) = NOT north OR NOT east': (comp(north & east), comp(north) | comp(east)),
        'De Morgan: NOT (north OR east) = NOT north AND NOT east': (comp(north | east), comp(north) & comp(east)),
        'north AND NOT north is empty': (north & comp(north), set()),
        'inner OR NOT inner is everything': (inner | comp(inner), U),
    }
    lit, same_as = cases[kind]; dark = U - lit
    ok = len(lit) + len(dark) == N and (same_as is None or lit == same_as)
    return dict(question='Gate "%s" on %d real substation places: do lit and dark make the whole, and does the identity hold?' % (kind, N),
                did='selected by the rule; counted lit, dark and whole; compared the two sides where the gate is an identity',
                numbers=dict(lit=len(lit), dark=len(dark), whole=N), observed='%d lit + %d dark = %d' % (len(lit), len(dark), len(lit) + len(dark)),
                result='CONFIRMED' if ok else 'REFUTED')


# ------------------------------------------------------------------ PULSES
def t_pulse(origin_name, speed_km_per_tick, second=None):
    P = points(); O = dict(charing=(-0.1276, 51.5072), norwich=(1.2974, 52.6309), brighton=(-0.1372, 50.8225))
    o = O[origin_name]; early = 0; last = 0; met = None
    for p in P[::3]:                                   # every third place: 5,042 cells, the same every run
        d = km(p, o); t_arrive = math.ceil(d / speed_km_per_tick)
        if t_arrive * speed_km_per_tick < d - 1e-9: early += 1     # lit before the front could have reached it
        last = max(last, t_arrive)
        if second:
            d2 = km(p, O[second]); t2 = math.ceil(d2 / speed_km_per_tick)
            if t_arrive == t2 and (met is None or t2 < met): met = t2
    ok = early == 0 and (second is None or met is not None)
    return dict(question='A front leaves %s at %g km a tick%s: is any cell lit before the front could reach it?' % (origin_name, speed_km_per_tick, (' and another leaves ' + second) if second else ''),
                did='gave every cell the first tick at which the front has covered its distance; counted cells lit early',
                numbers=dict(cells=len(P[::3]), lit_early=early, last_cell_tick=last, fronts_first_meet_tick=met),
                observed='%d lit early; the last cell switches at tick %d' % (early, last), result='CONFIRMED' if ok else 'REFUTED')


# ------------------------------------------------------------------ LOGIC (one kind of gate cell)
class Cells:
    def __init__(self): self.rules = {}; self.k = 0
    def inp(self, name): self.k += 1; self.rules[self.k] = ('in', name); return self.k
    def nand(self, a, b): self.k += 1; self.rules[self.k] = ('g', a, b); return self.k
    def NOT(self, a): return self.nand(a, a)
    def AND(self, a, b): return self.NOT(self.nand(a, b))
    def OR(self, a, b): return self.nand(self.NOT(a), self.NOT(b))
    def XOR(self, a, b): n = self.nand(a, b); return self.nand(self.nand(a, n), self.nand(b, n))
    def run(self, inputs, outs, ticks=400):
        """State of every cell tick by tick from all dark; stops when nothing has changed for 8 ticks."""
        s = {k: (inputs[r[1]] if r[0] == 'in' else 0) for k, r in self.rules.items()}; quiet = 0
        for t in range(1, ticks):
            n = {k: (inputs[r[1]] if r[0] == 'in' else (0 if (s[r[1]] and s[r[2]]) else 1)) for k, r in self.rules.items()}
            quiet = quiet + 1 if n == s else 0; s = n
            if quiet >= 8: return [s[o] for o in outs], t - 8
        return None, -1

def adder(bits):
    c = Cells(); a = [c.inp('a%d' % i) for i in range(bits)]; b = [c.inp('b%d' % i) for i in range(bits)]; z = c.inp('z')
    carry = z; out = []
    for i in range(bits):
        x = c.XOR(a[i], b[i]); out.append(c.XOR(x, carry)); carry = c.OR(c.AND(a[i], b[i]), c.AND(x, carry))
    return c, out + [carry]

def t_logic(kind):
    wrong = 0; cases = 0; slow = 0; cells = 0
    if kind.startswith('adder'):
        bits = int(kind.split()[1]); c, outs = adder(bits); cells = len(c.rules)
        rng = random.Random(bits); pairs = [(x, y) for x in range(2 ** bits) for y in range(2 ** bits)] if bits <= 4 else [(rng.randrange(2 ** bits), rng.randrange(2 ** bits)) for _ in range(200)]
        for x, y in pairs:
            i = {'z': 0}; i.update({'a%d' % k: (x >> k) & 1 for k in range(bits)}); i.update({'b%d' % k: (y >> k) & 1 for k in range(bits)})
            o, t = c.run(i, outs); cases += 1; slow = max(slow, t)
            if o is None or sum(v << k for k, v in enumerate(o)) != x + y: wrong += 1
    else:
        c = Cells(); n = dict(parity=8, majority=3, mux=3, decoder=2, comparator=4, planted=2, half=2)[kind.split()[0]]
        ins = [c.inp('i%d' % k) for k in range(n)]
        if kind == 'half adder': outs = [c.XOR(ins[0], ins[1]), c.AND(ins[0], ins[1])]; want = lambda v: [v[0] ^ v[1], v[0] & v[1]]
        elif kind == 'parity of 8':
            p = ins[0]
            for k in ins[1:]: p = c.XOR(p, k)
            outs = [p]; want = lambda v: [sum(v) % 2]
        elif kind == 'majority of 3': outs = [c.OR(c.OR(c.AND(ins[0], ins[1]), c.AND(ins[1], ins[2])), c.AND(ins[0], ins[2]))]; want = lambda v: [1 if sum(v) >= 2 else 0]
        elif kind == 'mux 2 to 1': outs = [c.OR(c.AND(ins[0], c.NOT(ins[2])), c.AND(ins[1], ins[2]))]; want = lambda v: [v[1] if v[2] else v[0]]
        elif kind == 'decoder 2 to 4':
            n0, n1 = c.NOT(ins[0]), c.NOT(ins[1]); outs = [c.AND(n0, n1), c.AND(ins[0], n1), c.AND(n0, ins[1]), c.AND(ins[0], ins[1])]
            want = lambda v: [1 if k == v[0] + 2 * v[1] else 0 for k in range(4)]
        elif kind == 'comparator 2 bit equal': outs = [c.AND(c.NOT(c.XOR(ins[0], ins[2])), c.NOT(c.XOR(ins[1], ins[3])))]; want = lambda v: [1 if (v[0], v[1]) == (v[2], v[3]) else 0]
        elif kind == 'planted fault must be caught': outs = [c.XOR(ins[0], ins[1]), c.NOT(ins[0])]; want = lambda v: [v[0] ^ v[1], v[0] & v[1]]
        cells = len(c.rules)
        for m in range(2 ** n):
            v = [(m >> k) & 1 for k in range(n)]; o, t = c.run({'i%d' % k: v[k] for k in range(n)}, outs); cases += 1; slow = max(slow, t)
            if o != want(v): wrong += 1
    planted = kind.startswith('planted'); ok = (wrong > 0) if planted else (wrong == 0)
    return dict(question='Do cells run by one rule (lit unless both the cells it answers to were lit a tick earlier) make a correct "%s"?' % kind,
                did='built it from that one gate cell; set every input row (or 200 seeded rows); waited for the outputs to settle; read the output cells',
                numbers=dict(cells=cells, rows=cases, wrong=wrong, slowest_settle_tick=slow),
                observed=('%d of %d rows wrong' % (wrong, cases)) + (' (a fault was planted: the check must see it)' if planted else ''),
                result='CONFIRMED' if ok else 'REFUTED')


# ------------------------------------------------------------------ FEEDER PULSE
CANDIDATE = dict(r_ohm_per_km=0.164, x_ohm_per_km=0.080, kv=11.0, kw_per_home_after_diversity=1.5, power_factor=0.95,
                 charger_kw=7.0, charger_diversity=0.4, volts_band_low_pu=0.94, cable_rating_a=355)

def feeder(seed, size=40):
    """A root chosen by seed among the real places, its nearest `size` neighbours, joined by a minimum spanning tree."""
    P = points(); rng = random.Random(seed); root = rng.randrange(len(P))
    near = sorted(range(len(P)), key=lambda i: km(P[i], P[root]))[:size + 1]
    intree = {near[0]}; parent = {near[0]: None}; length = {}
    while len(intree) < len(near):
        best = None
        for i in near:
            if i in intree: continue
            for j in intree:
                d = km(P[i], P[j])
                if best is None or d < best[0]: best = (d, i, j)
        d, i, j = best; intree.add(i); parent[i] = j; length[i] = max(d, 0.05)      # never shorter than 50 m of cable
    homes = {i: rng.randint(50, 300) for i in near if parent[i] is not None}
    return near[0], parent, length, homes

def sweep(root, parent, length, homes, ev_share, c=CANDIDATE, tol=1e-9):
    """Forward-backward sweep, per phase, constant power loads. Returns volts (pu), section amps, losses, rounds."""
    vbase = c['kv'] * 1000 / math.sqrt(3); z = complex(c['r_ohm_per_km'], c['x_ohm_per_km'])
    kids = {}
    for i, p in parent.items():
        if p is not None: kids.setdefault(p, []).append(i)
    order = [root]
    for n in order: order += kids.get(n, [])
    tanphi = math.tan(math.acos(c['power_factor']))
    S = {}
    for i, h in homes.items():
        kw = h * c['kw_per_home_after_diversity'] + h * ev_share * c['charger_kw'] * c['charger_diversity']
        S[i] = complex(kw, kw * tanphi) * 1000 / 3            # volt amperes per phase
    V = {n: complex(vbase, 0) for n in order}; rounds = 0
    while True:
        rounds += 1
        I = {n: (S[n] / V[n]).conjugate() if n in S else 0j for n in order}          # what each place draws
        J = dict(I)
        for n in reversed(order):                                                   # PULSE ONE: currents sum back toward the root
            if parent[n] is not None: J[parent[n]] += J[n]
        newV = {root: complex(vbase, 0)}
        for n in order[1:]:                                                         # PULSE TWO: volts fall out from the root
            newV[n] = newV[parent[n]] - J[n] * z * length[n]
        step = max(abs(newV[n] - V[n]) for n in order); V = newV
        if step < tol or rounds > 200: break
    loss = sum(abs(J[n]) ** 2 * z.real * length[n] for n in order[1:]) * 3
    load = sum(S.values()).real * 3
    source = (V[root] * J[root].conjugate()).real * 3
    return V, J, loss, load, source, rounds, vbase

def t_feeder(seed, ev_share):
    root, parent, length, homes = feeder(seed)
    V, J, loss, load, source, rounds, vbase = sweep(root, parent, length, homes, ev_share)
    c = CANDIDATE
    vmin = min(abs(v) for v in V.values()) / vbase; imax = max(abs(J[n]) for n in parent if parent[n] is not None)
    # THE CHECKS THAT CAN FAIL: (1) it converged; (2) what leaves the source = what the homes take + what the cable burns;
    # (3) at every place, current in = current drawn + currents out (redone from the final volts, not reused)
    balance = abs(source - load - loss) / max(load, 1)
    worst_kcl = 0.0
    kids = {}
    for i, p in parent.items():
        if p is not None: kids.setdefault(p, []).append(i)
    z = complex(c['r_ohm_per_km'], c['x_ohm_per_km'])
    for n, p in parent.items():
        if p is None: continue
        flow_in = (V[p] - V[n]) / (z * length[n])
        worst_kcl = max(worst_kcl, abs(flow_in - J[n]) / max(abs(J[n]), 1e-9))
    ok = rounds <= 200 and balance < 1e-6 and worst_kcl < 1e-6
    trouble = []
    if vmin < c['volts_band_low_pu']: trouble.append('lowest voltage %.3f of nominal is under the %.2f band' % (vmin, c['volts_band_low_pu']))
    if imax > c['cable_rating_a']: trouble.append('heaviest section %.0f A is over the %d A cable rating' % (imax, c['cable_rating_a']))
    return dict(question='Feeder pulse, estimated feeder number %d (41 real substation places, tree assumed), %d%% of homes with a charger: does the sweep settle, and do the books balance?' % (seed, round(ev_share * 100)),
                did='two pulses per round: currents summed back to the root, volts dropped out from the root; then power in = load + loss, and current in = current out at every place, checked from the final volts',
                numbers=dict(places=len(parent), homes=sum(homes.values()), cable_km=round(sum(length.values()), 2), rounds=rounds,
                             load_kw=round(load / 1000, 1), loss_kw=round(loss / 1000, 2), lowest_volts_pu=round(vmin, 4), heaviest_section_a=round(imax, 1),
                             power_balance_error=float('%.2e' % balance), worst_current_law_error=float('%.2e' % worst_kcl)),
                observed=('settled in %d rounds; lowest voltage %.3f of nominal; heaviest section %.0f A; ' % (rounds, vmin, imax)) + ('; '.join(trouble) if trouble else 'inside band and rating'),
                assumed='tree, homes per substation, and every electrical figure are CANDIDATE estimates: ' + json.dumps(c, sort_keys=True),
                result='CONFIRMED' if ok else 'REFUTED')


# ------------------------------------------------------------------ the hundred, in order
def registry():
    R = []
    for s in ['sunflower', 'ring', 'two rings', 'orbit', 'square lattice', 'hexagonal lattice', 'spiral arms', 'busbar and feeders', 'random scatter', 'clock']:
        R.append(('ARRANGEMENTS', s, (t_arrangement, (s,))))
    for g in ['north', 'east', 'within 25 km of Charing Cross', 'north AND east', 'north OR east', 'NOT north',
              'De Morgan: NOT (north AND east) = NOT north OR NOT east', 'De Morgan: NOT (north OR east) = NOT north AND NOT east',
              'north AND NOT north is empty', 'inner OR NOT inner is everything']:
        R.append(('GATES', g, (t_gate, (g,))))
    for o, v, s2 in [('charing', 1, None), ('charing', 5, None), ('charing', 25, None), ('norwich', 1, None), ('norwich', 5, None), ('brighton', 5, None),
                     ('charing', 5, 'norwich'), ('charing', 5, 'brighton'), ('norwich', 5, 'brighton'), ('brighton', 1, 'norwich')]:
        R.append(('PULSES', '%s at %g km a tick%s' % (o, v, ' meeting ' + s2 if s2 else ''), (t_pulse, (o, v, s2))))
    for l in ['half adder', 'adder 2 bit', 'adder 4 bit', 'adder 8 bit', 'parity of 8', 'majority of 3', 'mux 2 to 1', 'decoder 2 to 4', 'comparator 2 bit equal', 'planted fault must be caught']:
        R.append(('LOGIC', l, (t_logic, (l,))))
    for seed in range(1, 21):
        for ev in (0.0, 0.3, 0.6):
            R.append(('FEEDER PULSE', 'feeder %d, %d%% chargers' % (seed, round(ev * 100)), (t_feeder, (seed, ev))))
    assert len(R) == 100, len(R)
    return R

def run(n):
    family, name, (fn, args) = registry()[n - 1]
    rec = fn(*args); rec.update(n=n, family=family, name=name)
    rec['fingerprint'] = hashlib.sha256(json.dumps({k: rec[k] for k in ('n', 'family', 'name', 'numbers', 'result')}, sort_keys=True).encode()).hexdigest()
    return rec
