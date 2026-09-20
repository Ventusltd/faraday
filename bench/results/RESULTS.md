# The hundred: results so far

100 of 100 run. Every line below is one test; rerun any of them with `python bench/one.py N`.

| family | CONFIRMED | REFUTED |
|---|---|---|
| ARRANGEMENTS | 3 | 7 |
| GATES | 10 | 0 |
| PULSES | 10 | 0 |
| LOGIC | 10 | 0 |
| FEEDER PULSE | 60 | 0 |

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
| 51 | FEEDER PULSE | feeder 4, 30% chargers | CONFIRMED | settled in 13 rounds; lowest voltage 0.902 of nominal; heaviest section 880 A; lowest voltage 0.902 of nominal is under the 0.94 band; heaviest section 880 A is |
| 52 | FEEDER PULSE | feeder 4, 60% chargers | CONFIRMED | settled in 15 rounds; lowest voltage 0.862 of nominal; heaviest section 1238 A; lowest voltage 0.862 of nominal is under the 0.94 band; heaviest section 1238 A  |
| 53 | FEEDER PULSE | feeder 5, 0% chargers | CONFIRMED | settled in 10 rounds; lowest voltage 0.949 of nominal; heaviest section 318 A; inside band and rating |
| 54 | FEEDER PULSE | feeder 5, 30% chargers | CONFIRMED | settled in 12 rounds; lowest voltage 0.918 of nominal; heaviest section 506 A; lowest voltage 0.918 of nominal is under the 0.94 band; heaviest section 506 A is |
| 55 | FEEDER PULSE | feeder 5, 60% chargers | CONFIRMED | settled in 14 rounds; lowest voltage 0.885 of nominal; heaviest section 703 A; lowest voltage 0.885 of nominal is under the 0.94 band; heaviest section 703 A is |
| 56 | FEEDER PULSE | feeder 6, 0% chargers | CONFIRMED | settled in 12 rounds; lowest voltage 0.923 of nominal; heaviest section 535 A; lowest voltage 0.923 of nominal is under the 0.94 band; heaviest section 535 A is |
| 57 | FEEDER PULSE | feeder 6, 30% chargers | CONFIRMED | settled in 14 rounds; lowest voltage 0.874 of nominal; heaviest section 865 A; lowest voltage 0.874 of nominal is under the 0.94 band; heaviest section 865 A is |
| 58 | FEEDER PULSE | feeder 6, 60% chargers | CONFIRMED | settled in 17 rounds; lowest voltage 0.820 of nominal; heaviest section 1227 A; lowest voltage 0.820 of nominal is under the 0.94 band; heaviest section 1227 A  |
| 59 | FEEDER PULSE | feeder 7, 0% chargers | CONFIRMED | settled in 6 rounds; lowest voltage 0.995 of nominal; heaviest section 270 A; inside band and rating |
| 60 | FEEDER PULSE | feeder 7, 30% chargers | CONFIRMED | settled in 6 rounds; lowest voltage 0.992 of nominal; heaviest section 422 A; heaviest section 422 A is over the 355 A cable rating |
| 61 | FEEDER PULSE | feeder 7, 60% chargers | CONFIRMED | settled in 7 rounds; lowest voltage 0.989 of nominal; heaviest section 575 A; heaviest section 575 A is over the 355 A cable rating |
| 62 | FEEDER PULSE | feeder 8, 0% chargers | CONFIRMED | settled in 11 rounds; lowest voltage 0.935 of nominal; heaviest section 470 A; lowest voltage 0.935 of nominal is under the 0.94 band; heaviest section 470 A is |
| 63 | FEEDER PULSE | feeder 8, 30% chargers | CONFIRMED | settled in 13 rounds; lowest voltage 0.895 of nominal; heaviest section 753 A; lowest voltage 0.895 of nominal is under the 0.94 band; heaviest section 753 A is |
| 64 | FEEDER PULSE | feeder 8, 60% chargers | CONFIRMED | settled in 16 rounds; lowest voltage 0.851 of nominal; heaviest section 1056 A; lowest voltage 0.851 of nominal is under the 0.94 band; heaviest section 1056 A  |
| 65 | FEEDER PULSE | feeder 9, 0% chargers | CONFIRMED | settled in 8 rounds; lowest voltage 0.977 of nominal; heaviest section 523 A; heaviest section 523 A is over the 355 A cable rating |
| 66 | FEEDER PULSE | feeder 9, 30% chargers | CONFIRMED | settled in 9 rounds; lowest voltage 0.964 of nominal; heaviest section 824 A; heaviest section 824 A is over the 355 A cable rating |
| 67 | FEEDER PULSE | feeder 9, 60% chargers | CONFIRMED | settled in 10 rounds; lowest voltage 0.951 of nominal; heaviest section 1130 A; heaviest section 1130 A is over the 355 A cable rating |
| 68 | FEEDER PULSE | feeder 10, 0% chargers | CONFIRMED | settled in 9 rounds; lowest voltage 0.966 of nominal; heaviest section 556 A; heaviest section 556 A is over the 355 A cable rating |
| 69 | FEEDER PULSE | feeder 10, 30% chargers | CONFIRMED | settled in 10 rounds; lowest voltage 0.946 of nominal; heaviest section 880 A; heaviest section 880 A is over the 355 A cable rating |
| 70 | FEEDER PULSE | feeder 10, 60% chargers | CONFIRMED | settled in 11 rounds; lowest voltage 0.925 of nominal; heaviest section 1215 A; lowest voltage 0.925 of nominal is under the 0.94 band; heaviest section 1215 A  |
| 71 | FEEDER PULSE | feeder 11, 0% chargers | CONFIRMED | settled in 9 rounds; lowest voltage 0.957 of nominal; heaviest section 638 A; heaviest section 638 A is over the 355 A cable rating |
| 72 | FEEDER PULSE | feeder 11, 30% chargers | CONFIRMED | settled in 11 rounds; lowest voltage 0.931 of nominal; heaviest section 1012 A; lowest voltage 0.931 of nominal is under the 0.94 band; heaviest section 1012 A  |
| 73 | FEEDER PULSE | feeder 11, 60% chargers | CONFIRMED | settled in 12 rounds; lowest voltage 0.904 of nominal; heaviest section 1401 A; lowest voltage 0.904 of nominal is under the 0.94 band; heaviest section 1401 A  |
| 74 | FEEDER PULSE | feeder 12, 0% chargers | CONFIRMED | settled in 9 rounds; lowest voltage 0.960 of nominal; heaviest section 360 A; heaviest section 360 A is over the 355 A cable rating |
| 75 | FEEDER PULSE | feeder 12, 30% chargers | CONFIRMED | settled in 11 rounds; lowest voltage 0.937 of nominal; heaviest section 571 A; lowest voltage 0.937 of nominal is under the 0.94 band; heaviest section 571 A is |
| 76 | FEEDER PULSE | feeder 12, 60% chargers | CONFIRMED | settled in 12 rounds; lowest voltage 0.913 of nominal; heaviest section 792 A; lowest voltage 0.913 of nominal is under the 0.94 band; heaviest section 792 A is |
| 77 | FEEDER PULSE | feeder 13, 0% chargers | CONFIRMED | settled in 8 rounds; lowest voltage 0.970 of nominal; heaviest section 615 A; heaviest section 615 A is over the 355 A cable rating |
| 78 | FEEDER PULSE | feeder 13, 30% chargers | CONFIRMED | settled in 10 rounds; lowest voltage 0.952 of nominal; heaviest section 971 A; heaviest section 971 A is over the 355 A cable rating |
| 79 | FEEDER PULSE | feeder 13, 60% chargers | CONFIRMED | settled in 11 rounds; lowest voltage 0.934 of nominal; heaviest section 1334 A; lowest voltage 0.934 of nominal is under the 0.94 band; heaviest section 1334 A  |
| 80 | FEEDER PULSE | feeder 14, 0% chargers | CONFIRMED | settled in 9 rounds; lowest voltage 0.965 of nominal; heaviest section 532 A; heaviest section 532 A is over the 355 A cable rating |
| 81 | FEEDER PULSE | feeder 14, 30% chargers | CONFIRMED | settled in 10 rounds; lowest voltage 0.945 of nominal; heaviest section 840 A; heaviest section 840 A is over the 355 A cable rating |
| 82 | FEEDER PULSE | feeder 14, 60% chargers | CONFIRMED | settled in 11 rounds; lowest voltage 0.924 of nominal; heaviest section 1157 A; lowest voltage 0.924 of nominal is under the 0.94 band; heaviest section 1157 A  |
| 83 | FEEDER PULSE | feeder 15, 0% chargers | CONFIRMED | settled in 7 rounds; lowest voltage 0.991 of nominal; heaviest section 280 A; inside band and rating |
| 84 | FEEDER PULSE | feeder 15, 30% chargers | CONFIRMED | settled in 7 rounds; lowest voltage 0.987 of nominal; heaviest section 439 A; heaviest section 439 A is over the 355 A cable rating |
| 85 | FEEDER PULSE | feeder 15, 60% chargers | CONFIRMED | settled in 8 rounds; lowest voltage 0.982 of nominal; heaviest section 599 A; heaviest section 599 A is over the 355 A cable rating |
| 86 | FEEDER PULSE | feeder 16, 0% chargers | CONFIRMED | settled in 14 rounds; lowest voltage 0.884 of nominal; heaviest section 554 A; lowest voltage 0.884 of nominal is under the 0.94 band; heaviest section 554 A is |
| 87 | FEEDER PULSE | feeder 16, 30% chargers | CONFIRMED | settled in 19 rounds; lowest voltage 0.802 of nominal; heaviest section 940 A; lowest voltage 0.802 of nominal is under the 0.94 band; heaviest section 940 A is |
| 88 | FEEDER PULSE | feeder 16, 60% chargers | CONFIRMED | settled in 30 rounds; lowest voltage 0.694 of nominal; heaviest section 1445 A; lowest voltage 0.694 of nominal is under the 0.94 band; heaviest section 1445 A  |
| 89 | FEEDER PULSE | feeder 17, 0% chargers | CONFIRMED | settled in 11 rounds; lowest voltage 0.926 of nominal; heaviest section 649 A; lowest voltage 0.926 of nominal is under the 0.94 band; heaviest section 649 A is |
| 90 | FEEDER PULSE | feeder 17, 30% chargers | CONFIRMED | settled in 14 rounds; lowest voltage 0.880 of nominal; heaviest section 1050 A; lowest voltage 0.880 of nominal is under the 0.94 band; heaviest section 1050 A  |
| 91 | FEEDER PULSE | feeder 17, 60% chargers | CONFIRMED | settled in 17 rounds; lowest voltage 0.828 of nominal; heaviest section 1490 A; lowest voltage 0.828 of nominal is under the 0.94 band; heaviest section 1490 A  |
| 92 | FEEDER PULSE | feeder 18, 0% chargers | CONFIRMED | settled in 9 rounds; lowest voltage 0.971 of nominal; heaviest section 588 A; heaviest section 588 A is over the 355 A cable rating |
| 93 | FEEDER PULSE | feeder 18, 30% chargers | CONFIRMED | settled in 10 rounds; lowest voltage 0.954 of nominal; heaviest section 930 A; heaviest section 930 A is over the 355 A cable rating |
| 94 | FEEDER PULSE | feeder 18, 60% chargers | CONFIRMED | settled in 11 rounds; lowest voltage 0.937 of nominal; heaviest section 1282 A; lowest voltage 0.937 of nominal is under the 0.94 band; heaviest section 1282 A  |
| 95 | FEEDER PULSE | feeder 19, 0% chargers | CONFIRMED | settled in 7 rounds; lowest voltage 0.984 of nominal; heaviest section 258 A; inside band and rating |
| 96 | FEEDER PULSE | feeder 19, 30% chargers | CONFIRMED | settled in 8 rounds; lowest voltage 0.974 of nominal; heaviest section 406 A; heaviest section 406 A is over the 355 A cable rating |
| 97 | FEEDER PULSE | feeder 19, 60% chargers | CONFIRMED | settled in 9 rounds; lowest voltage 0.965 of nominal; heaviest section 556 A; heaviest section 556 A is over the 355 A cable rating |
| 98 | FEEDER PULSE | feeder 20, 0% chargers | CONFIRMED | settled in 9 rounds; lowest voltage 0.958 of nominal; heaviest section 558 A; heaviest section 558 A is over the 355 A cable rating |
| 99 | FEEDER PULSE | feeder 20, 30% chargers | CONFIRMED | settled in 11 rounds; lowest voltage 0.933 of nominal; heaviest section 885 A; lowest voltage 0.933 of nominal is under the 0.94 band; heaviest section 885 A is |
| 100 | FEEDER PULSE | feeder 20, 60% chargers | CONFIRMED | settled in 12 rounds; lowest voltage 0.907 of nominal; heaviest section 1225 A; lowest voltage 0.907 of nominal is under the 0.94 band; heaviest section 1225 A  |
