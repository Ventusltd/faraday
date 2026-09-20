# The hundred: results so far

50 of 100 run. Every line below is one test; rerun any of them with `python bench/one.py N`.

| family | CONFIRMED | REFUTED |
|---|---|---|
| ARRANGEMENTS | 3 | 7 |
| GATES | 10 | 0 |
| PULSES | 10 | 0 |
| LOGIC | 10 | 0 |
| FEEDER PULSE | 10 | 0 |

| n | family | test | result | what was seen |
|---|---|---|---|---|
| 1 | ARRANGEMENTS | sunflower | CONFIRMED | largest honest dot 1.73 px |
| 2 | ARRANGEMENTS | ring | REFUTED | largest honest dot 0.16 px |
| 3 | ARRANGEMENTS | two rings | REFUTED | largest honest dot 0.19 px |
| 4 | ARRANGEMENTS | orbit | REFUTED | largest honest dot 0.08 px |
| 5 | ARRANGEMENTS | square lattice | CONFIRMED | largest honest dot 2.27 px |
| 6 | ARRANGEMENTS | hexagonal lattice | CONFIRMED | largest honest dot 2.22 px |
| 7 | ARRANGEMENTS | spiral arms | REFUTED | largest honest dot 0.10 px |
| 8 | ARRANGEMENTS | busbar and feeders | REFUTED | largest honest dot 0.25 px |
| 9 | ARRANGEMENTS | random scatter | REFUTED | largest honest dot 0.04 px |
| 10 | ARRANGEMENTS | clock | REFUTED | largest honest dot 0.00 px |
| 11 | GATES | north | CONFIRMED | 4806 lit + 10320 dark = 15126 |
| 12 | GATES | east | CONFIRMED | 4059 lit + 11067 dark = 15126 |
| 13 | GATES | within 25 km of Charing Cross | CONFIRMED | 4319 lit + 10807 dark = 15126 |
| 14 | GATES | north AND east | CONFIRMED | 1816 lit + 13310 dark = 15126 |
| 15 | GATES | north OR east | CONFIRMED | 7049 lit + 8077 dark = 15126 |
| 16 | GATES | NOT north | CONFIRMED | 10320 lit + 4806 dark = 15126 |
| 17 | GATES | De Morgan: NOT (north AND east) = NOT north OR NOT east | CONFIRMED | 13310 lit + 1816 dark = 15126 |
| 18 | GATES | De Morgan: NOT (north OR east) = NOT north AND NOT east | CONFIRMED | 8077 lit + 7049 dark = 15126 |
| 19 | GATES | north AND NOT north is empty | CONFIRMED | 0 lit + 15126 dark = 15126 |
| 20 | GATES | inner OR NOT inner is everything | CONFIRMED | 15126 lit + 0 dark = 15126 |
| 21 | PULSES | charing at 1 km a tick | CONFIRMED | 0 lit early; the last cell switches at tick 180 |
| 22 | PULSES | charing at 5 km a tick | CONFIRMED | 0 lit early; the last cell switches at tick 36 |
| 23 | PULSES | charing at 25 km a tick | CONFIRMED | 0 lit early; the last cell switches at tick 8 |
| 24 | PULSES | norwich at 1 km a tick | CONFIRMED | 0 lit early; the last cell switches at tick 289 |
| 25 | PULSES | norwich at 5 km a tick | CONFIRMED | 0 lit early; the last cell switches at tick 58 |
| 26 | PULSES | brighton at 5 km a tick | CONFIRMED | 0 lit early; the last cell switches at tick 49 |
| 27 | PULSES | charing at 5 km a tick meeting norwich | CONFIRMED | 0 lit early; the last cell switches at tick 36 |
| 28 | PULSES | charing at 5 km a tick meeting brighton | CONFIRMED | 0 lit early; the last cell switches at tick 36 |
| 29 | PULSES | norwich at 5 km a tick meeting brighton | CONFIRMED | 0 lit early; the last cell switches at tick 58 |
| 30 | PULSES | brighton at 1 km a tick meeting norwich | CONFIRMED | 0 lit early; the last cell switches at tick 244 |
| 31 | LOGIC | half adder | CONFIRMED | 0 of 4 rows wrong |
| 32 | LOGIC | adder 2 bit | CONFIRMED | 0 of 16 rows wrong |
| 33 | LOGIC | adder 4 bit | CONFIRMED | 0 of 256 rows wrong |
| 34 | LOGIC | adder 8 bit | CONFIRMED | 0 of 200 rows wrong |
| 35 | LOGIC | parity of 8 | CONFIRMED | 0 of 256 rows wrong |
| 36 | LOGIC | majority of 3 | CONFIRMED | 0 of 8 rows wrong |
| 37 | LOGIC | mux 2 to 1 | CONFIRMED | 0 of 8 rows wrong |
| 38 | LOGIC | decoder 2 to 4 | CONFIRMED | 0 of 4 rows wrong |
| 39 | LOGIC | comparator 2 bit equal | CONFIRMED | 0 of 16 rows wrong |
| 40 | LOGIC | planted fault must be caught | CONFIRMED | 3 of 4 rows wrong (a fault was planted: the check must see it) |
| 41 | FEEDER PULSE | feeder 1, 0% chargers | CONFIRMED | settled in 7 rounds; lowest voltage 0.988 of nominal; heaviest section 514 A; heaviest section 514 A is over the 355 A cable rating |
| 42 | FEEDER PULSE | feeder 1, 30% chargers | CONFIRMED | settled in 8 rounds; lowest voltage 0.981 of nominal; heaviest section 806 A; heaviest section 806 A is over the 355 A cable rating |
| 43 | FEEDER PULSE | feeder 1, 60% chargers | CONFIRMED | settled in 8 rounds; lowest voltage 0.974 of nominal; heaviest section 1101 A; heaviest section 1101 A is over the 355 A cable rating |
| 44 | FEEDER PULSE | feeder 2, 0% chargers | CONFIRMED | settled in 10 rounds; lowest voltage 0.955 of nominal; heaviest section 571 A; heaviest section 571 A is over the 355 A cable rating |
| 45 | FEEDER PULSE | feeder 2, 30% chargers | CONFIRMED | settled in 11 rounds; lowest voltage 0.928 of nominal; heaviest section 911 A; lowest voltage 0.928 of nominal is under the 0.94 band; heaviest section 911 A is |
| 46 | FEEDER PULSE | feeder 2, 60% chargers | CONFIRMED | settled in 13 rounds; lowest voltage 0.899 of nominal; heaviest section 1268 A; lowest voltage 0.899 of nominal is under the 0.94 band; heaviest section 1268 A  |
| 47 | FEEDER PULSE | feeder 3, 0% chargers | CONFIRMED | settled in 13 rounds; lowest voltage 0.892 of nominal; heaviest section 622 A; lowest voltage 0.892 of nominal is under the 0.94 band; heaviest section 622 A is |
| 48 | FEEDER PULSE | feeder 3, 30% chargers | CONFIRMED | settled in 17 rounds; lowest voltage 0.820 of nominal; heaviest section 1018 A; lowest voltage 0.820 of nominal is under the 0.94 band; heaviest section 1018 A  |
| 49 | FEEDER PULSE | feeder 3, 60% chargers | CONFIRMED | settled in 23 rounds; lowest voltage 0.733 of nominal; heaviest section 1471 A; lowest voltage 0.733 of nominal is under the 0.94 band; heaviest section 1471 A  |
| 50 | FEEDER PULSE | feeder 4, 0% chargers | CONFIRMED | settled in 11 rounds; lowest voltage 0.939 of nominal; heaviest section 547 A; lowest voltage 0.939 of nominal is under the 0.94 band; heaviest section 547 A is |
