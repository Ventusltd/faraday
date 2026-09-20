# The hundred: results so far

2393 of 2393 run. Every line below is one test; rerun any of them with `python bench/one.py N`.

| family | CONFIRMED | NO EFFECT | REFUTED |
|---|---|---|---|
| ARRANGEMENTS | 3 | 0 | 7 |
| GATES | 10 | 0 | 0 |
| PULSES | 10 | 0 | 0 |
| LOGIC | 10 | 0 | 0 |
| FEEDER PULSE | 60 | 0 | 0 |
| SITE PULSE | 24 | 0 | 0 |
| SITE THRESHOLDS | 2 | 1 | 0 |
| SITE SURVEY | 1971 | 0 | 29 |
| CABLE CHECK | 217 | 0 | 0 |
| SITE ENERGY | 31 | 0 | 0 |
| DC TRACTION | 18 | 0 | 0 |

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
| 101 | SITE PULSE | scenario 1 at 100% load | CONFIRMED | connection point +2628 kW (plus is import), +1356 kvar; volts 0.964 to 1.000; busiest transformer 62%; inside every limit |
| 102 | SITE PULSE | scenario 1 at 60% load | CONFIRMED | connection point +1570 kW (plus is import), +789 kvar; volts 0.979 to 1.000; busiest transformer 37%; inside every limit |
| 103 | SITE PULSE | scenario 1 at 30% load | CONFIRMED | connection point +782 kW (plus is import), +386 kvar; volts 0.990 to 1.000; busiest transformer 19%; inside every limit |
| 104 | SITE PULSE | scenario 2 at 100% load | CONFIRMED | connection point +2125 kW (plus is import), +1190 kvar; volts 0.966 to 1.000; busiest transformer 62%; inside every limit |
| 105 | SITE PULSE | scenario 2 at 60% load | CONFIRMED | connection point +1068 kW (plus is import), +624 kvar; volts 0.981 to 1.000; busiest transformer 37%; inside every limit |
| 106 | SITE PULSE | scenario 2 at 30% load | CONFIRMED | connection point +282 kW (plus is import), +221 kvar; volts 0.992 to 1.000; busiest transformer 19%; inside every limit |
| 107 | SITE PULSE | scenario 3 at 100% load | CONFIRMED | connection point +1627 kW (plus is import), +1370 kvar; volts 0.965 to 1.000; busiest transformer 67%; inside every limit |
| 108 | SITE PULSE | scenario 3 at 60% load | CONFIRMED | connection point +574 kW (plus is import), +820 kvar; volts 0.980 to 1.000; busiest transformer 80%; inside every limit |
| 109 | SITE PULSE | scenario 3 at 30% load | CONFIRMED | connection point -209 kW (plus is import), +428 kvar; volts 0.991 to 1.004; busiest transformer 90%; inside every limit |
| 110 | SITE PULSE | scenario 4 at 100% load | CONFIRMED | connection point +1125 kW (plus is import), +1205 kvar; volts 0.967 to 1.000; busiest transformer 67%; inside every limit |
| 111 | SITE PULSE | scenario 4 at 60% load | CONFIRMED | connection point +74 kW (plus is import), +655 kvar; volts 0.982 to 1.000; busiest transformer 80%; inside every limit |
| 112 | SITE PULSE | scenario 4 at 30% load | CONFIRMED | connection point -709 kW (plus is import), +264 kvar; volts 0.993 to 1.006; busiest transformer 90%; export 709 kW is 209 kW over the 500 kW limit: the solar mu |
| 113 | SITE PULSE | scenario 5 at 100% load | CONFIRMED | connection point +2124 kW (plus is import), +1349 kvar; volts 0.964 to 1.000; busiest transformer 62%; inside every limit |
| 114 | SITE PULSE | scenario 5 at 60% load | CONFIRMED | connection point +1069 kW (plus is import), +791 kvar; volts 0.980 to 1.000; busiest transformer 37%; inside every limit |
| 115 | SITE PULSE | scenario 5 at 30% load | CONFIRMED | connection point +284 kW (plus is import), +394 kvar; volts 0.990 to 1.000; busiest transformer 40%; inside every limit |
| 116 | SITE PULSE | scenario 6 at 100% load | CONFIRMED | connection point +1622 kW (plus is import), +1183 kvar; volts 0.967 to 1.000; busiest transformer 62%; inside every limit |
| 117 | SITE PULSE | scenario 6 at 60% load | CONFIRMED | connection point +568 kW (plus is import), +626 kvar; volts 0.982 to 1.000; busiest transformer 37%; inside every limit |
| 118 | SITE PULSE | scenario 6 at 30% load | CONFIRMED | connection point -217 kW (plus is import), +229 kvar; volts 0.992 to 1.000; busiest transformer 40%; inside every limit |
| 119 | SITE PULSE | scenario 7 at 100% load | CONFIRMED | connection point +1324 kW (plus is import), +1216 kvar; volts 0.967 to 1.000; busiest transformer 67%; inside every limit |
| 120 | SITE PULSE | scenario 7 at 60% load | CONFIRMED | connection point +394 kW (plus is import), +730 kvar; volts 0.981 to 1.000; busiest transformer 80%; inside every limit |
| 121 | SITE PULSE | scenario 7 at 30% load | CONFIRMED | connection point -299 kW (plus is import), +384 kvar; volts 0.991 to 1.004; busiest transformer 90%; inside every limit |
| 122 | SITE PULSE | scenario 8 at 100% load | CONFIRMED | connection point +979 kW (plus is import), +1075 kvar; volts 0.969 to 1.001; busiest transformer 100%; inside every limit |
| 123 | SITE PULSE | scenario 8 at 60% load | CONFIRMED | connection point +187 kW (plus is import), +647 kvar; volts 0.982 to 1.005; busiest transformer 100%; a transformer is at 100% of its rating |
| 124 | SITE PULSE | scenario 8 at 30% load | CONFIRMED | connection point -402 kW (plus is import), +343 kvar; volts 0.992 to 1.008; busiest transformer 100%; a transformer is at 100% of its rating |
| 125 | SITE THRESHOLDS | export limit | CONFIRMED | the export limit first binds at about 1298 kW of solar |
| 126 | SITE THRESHOLDS | voltage rise | NO EFFECT | never binds below 6,000 kW on this site |
| 127 | SITE THRESHOLDS | transformer rating | CONFIRMED | the transformer rating first binds at about 1104 kW of solar |
| 128 | SITE SURVEY | generic site 1 | CONFIRMED | connection point -1839 kW (plus is import), +540 kvar; volts 0.991 to 1.005; busiest transformer 113%; export 1839 kW is 1339 kW over the 500 kW limit: the sola |
| 129 | SITE SURVEY | generic site 2 | CONFIRMED | connection point -2558 kW (plus is import), +3245 kvar; volts 0.932 to 1.000; busiest transformer 897%; export 2558 kW is 1558 kW over the 1000 kW limit: the so |
| 130 | SITE SURVEY | generic site 3 | CONFIRMED | connection point -1083 kW (plus is import), +454 kvar; volts 0.992 to 1.002; busiest transformer 78%; export 1083 kW is 583 kW over the 500 kW limit: the solar  |
| 131 | SITE SURVEY | generic site 4 | CONFIRMED | connection point -518 kW (plus is import), +367 kvar; volts 0.989 to 1.006; busiest transformer 106%; a transformer is at 106% of its rating |
| 132 | SITE SURVEY | generic site 5 | CONFIRMED | connection point -2602 kW (plus is import), +1114 kvar; volts 0.993 to 1.018; busiest transformer 350%; export 2602 kW is 2102 kW over the 500 kW limit: the sol |
| 133 | SITE SURVEY | generic site 6 | CONFIRMED | connection point -5370 kW (plus is import), +2774 kvar; volts 0.982 to 1.009; busiest transformer 461%; export 5370 kW is 5370 kW over the 0 kW limit: the solar |
| 134 | SITE SURVEY | generic site 7 | CONFIRMED | connection point -1501 kW (plus is import), +614 kvar; volts 0.996 to 1.015; busiest transformer 264%; export 1501 kW is 1501 kW over the 0 kW limit: the solar  |
| 135 | SITE SURVEY | generic site 8 | CONFIRMED | connection point -1652 kW (plus is import), +763 kvar; volts 0.989 to 1.015; busiest transformer 443%; export 1652 kW is 1152 kW over the 500 kW limit: the sola |
| 136 | SITE SURVEY | generic site 9 | CONFIRMED | connection point -133 kW (plus is import), +592 kvar; volts 0.988 to 1.003; busiest transformer 131%; export 133 kW is 83 kW over the 50 kW limit: the solar mus |
| 137 | SITE SURVEY | generic site 10 | CONFIRMED | connection point -2447 kW (plus is import), +1350 kvar; volts 0.987 to 1.011; busiest transformer 444%; export 2447 kW is 2397 kW over the 50 kW limit: the sola |
| 138 | SITE SURVEY | generic site 11 | CONFIRMED | connection point -4681 kW (plus is import), +3027 kvar; volts 0.981 to 1.000; busiest transformer 651%; export 4681 kW is 3681 kW over the 1000 kW limit: the so |
| 139 | SITE SURVEY | generic site 12 | CONFIRMED | connection point +15 kW (plus is import), +465 kvar; volts 0.989 to 1.000; busiest transformer 45%; inside every limit |
| 140 | SITE SURVEY | generic site 13 | CONFIRMED | connection point -2114 kW (plus is import), +736 kvar; volts 0.992 to 1.016; busiest transformer 329%; export 2114 kW is 1114 kW over the 1000 kW limit: the sol |
| 141 | SITE SURVEY | generic site 14 | CONFIRMED | connection point -1211 kW (plus is import), +414 kvar; volts 0.993 to 1.014; busiest transformer 204%; export 1211 kW is 1011 kW over the 200 kW limit: the sola |
| 142 | SITE SURVEY | generic site 15 | CONFIRMED | connection point -427 kW (plus is import), +188 kvar; volts 0.991 to 1.006; busiest transformer 86%; export 427 kW is 227 kW over the 200 kW limit: the solar mu |
| 143 | SITE SURVEY | generic site 16 | CONFIRMED | connection point -1802 kW (plus is import), +596 kvar; volts 0.995 to 1.016; busiest transformer 237%; export 1802 kW is 1602 kW over the 200 kW limit: the sola |
| 144 | SITE SURVEY | generic site 17 | CONFIRMED | connection point -311 kW (plus is import), +725 kvar; volts 0.987 to 1.007; busiest transformer 147%; a transformer is at 147% of its rating |
| 145 | SITE SURVEY | generic site 18 | CONFIRMED | connection point -742 kW (plus is import), +322 kvar; volts 0.990 to 1.011; busiest transformer 216%; export 742 kW is 742 kW over the 0 kW limit: the solar mus |
| 146 | SITE SURVEY | generic site 19 | CONFIRMED | connection point -1399 kW (plus is import), +1198 kvar; volts 0.987 to 1.008; busiest transformer 502%; export 1399 kW is 1399 kW over the 0 kW limit: the solar |
| 147 | SITE SURVEY | generic site 20 | CONFIRMED | connection point -1892 kW (plus is import), +1001 kvar; volts 0.989 to 1.016; busiest transformer 357%; export 1892 kW is 1892 kW over the 0 kW limit: the solar |
| 148 | SITE SURVEY | generic site 21 | CONFIRMED | connection point -1212 kW (plus is import), +604 kvar; volts 0.989 to 1.004; busiest transformer 118%; export 1212 kW is 1212 kW over the 0 kW limit: the solar  |
| 149 | SITE SURVEY | generic site 22 | CONFIRMED | connection point -1523 kW (plus is import), +375 kvar; volts 0.992 to 1.008; busiest transformer 178%; export 1523 kW is 523 kW over the 1000 kW limit: the sola |
| 150 | SITE SURVEY | generic site 23 | REFUTED | connection point +17597 kW (plus is import), +29023 kvar; volts 0.519 to 4.713; busiest transformer 44835%; highest voltage 4.713 of nominal is over 1.06; lowes |
| 151 | SITE SURVEY | generic site 24 | CONFIRMED | connection point -3837 kW (plus is import), +2850 kvar; volts 0.983 to 1.000; busiest transformer 701%; export 3837 kW is 3837 kW over the 0 kW limit: the solar |
| 152 | SITE SURVEY | generic site 25 | CONFIRMED | connection point -884 kW (plus is import), +343 kvar; volts 0.994 to 1.011; busiest transformer 158%; export 884 kW is 834 kW over the 50 kW limit: the solar mu |
| 153 | SITE SURVEY | generic site 26 | CONFIRMED | connection point -1239 kW (plus is import), +1146 kvar; volts 0.985 to 1.009; busiest transformer 476%; export 1239 kW is 739 kW over the 500 kW limit: the sola |
| 154 | SITE SURVEY | generic site 27 | CONFIRMED | connection point -1321 kW (plus is import), +1191 kvar; volts 0.987 to 1.007; busiest transformer 181%; export 1321 kW is 1321 kW over the 0 kW limit: the solar |
| 155 | SITE SURVEY | generic site 28 | CONFIRMED | connection point -682 kW (plus is import), +142 kvar; volts 0.996 to 1.005; busiest transformer 96%; export 682 kW is 182 kW over the 500 kW limit: the solar mu |
| 156 | SITE SURVEY | generic site 29 | CONFIRMED | connection point -2691 kW (plus is import), +760 kvar; volts 0.996 to 1.017; busiest transformer 169%; export 2691 kW is 2641 kW over the 50 kW limit: the solar |
| 157 | SITE SURVEY | generic site 30 | CONFIRMED | connection point +279 kW (plus is import), +625 kvar; volts 0.986 to 1.004; busiest transformer 105%; a transformer is at 105% of its rating |
| 158 | SITE SURVEY | generic site 31 | CONFIRMED | connection point -498 kW (plus is import), +107 kvar; volts 0.997 to 1.002; busiest transformer 35%; export 498 kW is 448 kW over the 50 kW limit: the solar mus |
| 159 | SITE SURVEY | generic site 32 | CONFIRMED | connection point -263 kW (plus is import), +111 kvar; volts 0.994 to 1.002; busiest transformer 49%; export 263 kW is 263 kW over the 0 kW limit: the solar must |
| 160 | SITE SURVEY | generic site 33 | CONFIRMED | connection point -4823 kW (plus is import), +1806 kvar; volts 0.983 to 1.007; busiest transformer 309%; export 4823 kW is 3823 kW over the 1000 kW limit: the so |
| 161 | SITE SURVEY | generic site 34 | CONFIRMED | connection point -1914 kW (plus is import), +1061 kvar; volts 0.988 to 1.006; busiest transformer 524%; export 1914 kW is 914 kW over the 1000 kW limit: the sol |
| 162 | SITE SURVEY | generic site 35 | CONFIRMED | connection point -2946 kW (plus is import), +1546 kvar; volts 0.986 to 1.012; busiest transformer 419%; export 2946 kW is 2946 kW over the 0 kW limit: the solar |
| 163 | SITE SURVEY | generic site 36 | CONFIRMED | connection point -741 kW (plus is import), +367 kvar; volts 0.990 to 1.003; busiest transformer 74%; export 741 kW is 241 kW over the 500 kW limit: the solar mu |
| 164 | SITE SURVEY | generic site 37 | CONFIRMED | connection point -3448 kW (plus is import), +1490 kvar; volts 0.987 to 1.011; busiest transformer 297%; export 3448 kW is 2948 kW over the 500 kW limit: the sol |
| 165 | SITE SURVEY | generic site 38 | CONFIRMED | connection point -361 kW (plus is import), +696 kvar; volts 0.988 to 1.001; busiest transformer 89%; export 361 kW is 161 kW over the 200 kW limit: the solar mu |
| 166 | SITE SURVEY | generic site 39 | CONFIRMED | connection point +189 kW (plus is import), +314 kvar; volts 0.990 to 1.000; busiest transformer 21%; inside every limit |
| 167 | SITE SURVEY | generic site 40 | CONFIRMED | connection point -3111 kW (plus is import), +1885 kvar; volts 0.987 to 1.009; busiest transformer 557%; export 3111 kW is 3111 kW over the 0 kW limit: the solar |
| 168 | SITE SURVEY | generic site 41 | CONFIRMED | connection point -1937 kW (plus is import), +1337 kvar; volts 0.989 to 1.004; busiest transformer 583%; export 1937 kW is 1887 kW over the 50 kW limit: the sola |
| 169 | SITE SURVEY | generic site 42 | CONFIRMED | connection point -326 kW (plus is import), +559 kvar; volts 0.991 to 1.002; busiest transformer 114%; export 326 kW is 126 kW over the 200 kW limit: the solar m |
| 170 | SITE SURVEY | generic site 43 | CONFIRMED | connection point -764 kW (plus is import), +232 kvar; volts 0.993 to 1.004; busiest transformer 61%; inside every limit |
| 171 | SITE SURVEY | generic site 44 | CONFIRMED | connection point +27 kW (plus is import), +469 kvar; volts 0.988 to 1.003; busiest transformer 97%; inside every limit |
| 172 | SITE SURVEY | generic site 45 | CONFIRMED | connection point -348 kW (plus is import), +327 kvar; volts 0.992 to 1.000; busiest transformer 75%; export 348 kW is 148 kW over the 200 kW limit: the solar mu |
| 173 | SITE SURVEY | generic site 46 | CONFIRMED | connection point -826 kW (plus is import), +168 kvar; volts 0.995 to 1.006; busiest transformer 61%; export 826 kW is 826 kW over the 0 kW limit: the solar must |
| 174 | SITE SURVEY | generic site 47 | CONFIRMED | connection point -1677 kW (plus is import), +343 kvar; volts 0.994 to 1.011; busiest transformer 101%; export 1677 kW is 677 kW over the 1000 kW limit: the sola |
| 175 | SITE SURVEY | generic site 48 | CONFIRMED | connection point +100 kW (plus is import), +530 kvar; volts 0.988 to 1.000; busiest transformer 32%; inside every limit |
| 176 | SITE SURVEY | generic site 49 | CONFIRMED | connection point -1284 kW (plus is import), +371 kvar; volts 0.995 to 1.011; busiest transformer 164%; export 1284 kW is 1234 kW over the 50 kW limit: the solar |
| 177 | SITE SURVEY | generic site 50 | CONFIRMED | connection point -2154 kW (plus is import), +978 kvar; volts 0.991 to 1.019; busiest transformer 310%; export 2154 kW is 1954 kW over the 200 kW limit: the sola |
| 178 | SITE SURVEY | generic site 51 | CONFIRMED | connection point -993 kW (plus is import), +556 kvar; volts 0.992 to 1.009; busiest transformer 204%; export 993 kW is 793 kW over the 200 kW limit: the solar m |
| 179 | SITE SURVEY | generic site 52 | CONFIRMED | connection point -428 kW (plus is import), +360 kvar; volts 0.989 to 1.004; busiest transformer 93%; inside every limit |
| 180 | SITE SURVEY | generic site 53 | CONFIRMED | connection point -1520 kW (plus is import), +754 kvar; volts 0.988 to 1.010; busiest transformer 282%; export 1520 kW is 1320 kW over the 200 kW limit: the sola |
| 181 | SITE SURVEY | generic site 54 | CONFIRMED | connection point -1560 kW (plus is import), +550 kvar; volts 0.992 to 1.005; busiest transformer 104%; export 1560 kW is 1510 kW over the 50 kW limit: the solar |
| 182 | SITE SURVEY | generic site 55 | CONFIRMED | connection point -239 kW (plus is import), +99 kvar; volts 0.996 to 1.001; busiest transformer 65%; inside every limit |
| 183 | SITE SURVEY | generic site 56 | CONFIRMED | connection point -579 kW (plus is import), +892 kvar; volts 0.987 to 1.008; busiest transformer 233%; export 579 kW is 529 kW over the 50 kW limit: the solar mu |
| 184 | SITE SURVEY | generic site 57 | CONFIRMED | connection point -1427 kW (plus is import), +368 kvar; volts 0.995 to 1.010; busiest transformer 172%; export 1427 kW is 927 kW over the 500 kW limit: the solar |
| 185 | SITE SURVEY | generic site 58 | CONFIRMED | connection point +76 kW (plus is import), +503 kvar; volts 0.987 to 1.005; busiest transformer 151%; a transformer is at 151% of its rating |
| 186 | SITE SURVEY | generic site 59 | CONFIRMED | connection point -744 kW (plus is import), +218 kvar; volts 0.991 to 1.010; busiest transformer 186%; a transformer is at 186% of its rating |
| 187 | SITE SURVEY | generic site 60 | CONFIRMED | connection point -140 kW (plus is import), +302 kvar; volts 0.990 to 1.000; busiest transformer 32%; inside every limit |
| 188 | SITE SURVEY | generic site 61 | CONFIRMED | connection point -1122 kW (plus is import), +546 kvar; volts 0.992 to 1.012; busiest transformer 180%; export 1122 kW is 922 kW over the 200 kW limit: the solar |
| 189 | SITE SURVEY | generic site 62 | CONFIRMED | connection point -820 kW (plus is import), +485 kvar; volts 0.990 to 1.004; busiest transformer 139%; export 820 kW is 770 kW over the 50 kW limit: the solar mu |
| 190 | SITE SURVEY | generic site 63 | CONFIRMED | connection point -1789 kW (plus is import), +602 kvar; volts 0.990 to 1.010; busiest transformer 153%; export 1789 kW is 1739 kW over the 50 kW limit: the solar |
| 191 | SITE SURVEY | generic site 64 | CONFIRMED | connection point -62 kW (plus is import), +285 kvar; volts 0.991 to 1.003; busiest transformer 100%; export 62 kW is 62 kW over the 0 kW limit: the solar must b |
| 192 | SITE SURVEY | generic site 65 | CONFIRMED | connection point -2239 kW (plus is import), +841 kvar; volts 0.990 to 1.016; busiest transformer 298%; export 2239 kW is 2189 kW over the 50 kW limit: the solar |
| 193 | SITE SURVEY | generic site 66 | CONFIRMED | connection point -578 kW (plus is import), +202 kvar; volts 0.994 to 1.003; busiest transformer 79%; export 578 kW is 78 kW over the 500 kW limit: the solar mus |
| 194 | SITE SURVEY | generic site 67 | CONFIRMED | connection point -732 kW (plus is import), +167 kvar; volts 0.992 to 1.003; busiest transformer 53%; export 732 kW is 682 kW over the 50 kW limit: the solar mus |
| 195 | SITE SURVEY | generic site 68 | CONFIRMED | connection point -2256 kW (plus is import), +1253 kvar; volts 0.985 to 1.012; busiest transformer 348%; export 2256 kW is 2206 kW over the 50 kW limit: the sola |
| 196 | SITE SURVEY | generic site 69 | CONFIRMED | connection point -176 kW (plus is import), +913 kvar; volts 0.984 to 1.000; busiest transformer 81%; inside every limit |
| 197 | SITE SURVEY | generic site 70 | CONFIRMED | connection point -285 kW (plus is import), +228 kvar; volts 0.990 to 1.000; busiest transformer 54%; inside every limit |
| 198 | SITE SURVEY | generic site 71 | CONFIRMED | connection point -932 kW (plus is import), +585 kvar; volts 0.991 to 1.010; busiest transformer 204%; export 932 kW is 432 kW over the 500 kW limit: the solar m |
| 199 | SITE SURVEY | generic site 72 | CONFIRMED | connection point -495 kW (plus is import), +388 kvar; volts 0.992 to 1.000; busiest transformer 44%; export 495 kW is 445 kW over the 50 kW limit: the solar mus |
| 200 | SITE SURVEY | generic site 73 | CONFIRMED | connection point -990 kW (plus is import), +546 kvar; volts 0.992 to 1.016; busiest transformer 316%; a transformer is at 316% of its rating |
| 201 | SITE SURVEY | generic site 74 | CONFIRMED | connection point -3873 kW (plus is import), +2779 kvar; volts 0.980 to 1.000; busiest transformer 692%; export 3873 kW is 2873 kW over the 1000 kW limit: the so |
| 202 | SITE SURVEY | generic site 75 | CONFIRMED | connection point -985 kW (plus is import), +705 kvar; volts 0.989 to 1.003; busiest transformer 97%; inside every limit |
| 203 | SITE SURVEY | generic site 76 | CONFIRMED | connection point +233 kW (plus is import), +380 kvar; volts 0.988 to 1.000; busiest transformer 26%; inside every limit |
| 204 | SITE SURVEY | generic site 77 | CONFIRMED | connection point -2718 kW (plus is import), +3852 kvar; volts 0.903 to 1.000; busiest transformer 966%; export 2718 kW is 2668 kW over the 50 kW limit: the sola |
| 205 | SITE SURVEY | generic site 78 | CONFIRMED | connection point -2871 kW (plus is import), +1125 kvar; volts 0.987 to 1.014; busiest transformer 208%; export 2871 kW is 2671 kW over the 200 kW limit: the sol |
| 206 | SITE SURVEY | generic site 79 | CONFIRMED | connection point -603 kW (plus is import), +319 kvar; volts 0.992 to 1.011; busiest transformer 199%; export 603 kW is 403 kW over the 200 kW limit: the solar m |
| 207 | SITE SURVEY | generic site 80 | CONFIRMED | connection point -265 kW (plus is import), +490 kvar; volts 0.988 to 1.000; busiest transformer 62%; inside every limit |
| 208 | SITE SURVEY | generic site 81 | CONFIRMED | connection point -565 kW (plus is import), +689 kvar; volts 0.988 to 1.000; busiest transformer 94%; export 565 kW is 515 kW over the 50 kW limit: the solar mus |
| 209 | SITE SURVEY | generic site 82 | CONFIRMED | connection point -1445 kW (plus is import), +458 kvar; volts 0.993 to 1.006; busiest transformer 113%; export 1445 kW is 1395 kW over the 50 kW limit: the solar |
| 210 | SITE SURVEY | generic site 83 | CONFIRMED | connection point -3126 kW (plus is import), +951 kvar; volts 0.995 to 1.021; busiest transformer 249%; export 3126 kW is 3076 kW over the 50 kW limit: the solar |
| 211 | SITE SURVEY | generic site 84 | CONFIRMED | connection point +315 kW (plus is import), +582 kvar; volts 0.986 to 1.003; busiest transformer 138%; a transformer is at 138% of its rating |
| 212 | SITE SURVEY | generic site 85 | CONFIRMED | connection point -1542 kW (plus is import), +427 kvar; volts 0.995 to 1.006; busiest transformer 92%; export 1542 kW is 1492 kW over the 50 kW limit: the solar  |
| 213 | SITE SURVEY | generic site 86 | CONFIRMED | connection point -1650 kW (plus is import), +1115 kvar; volts 0.989 to 1.016; busiest transformer 355%; export 1650 kW is 1150 kW over the 500 kW limit: the sol |
| 214 | SITE SURVEY | generic site 87 | CONFIRMED | connection point -804 kW (plus is import), +415 kvar; volts 0.992 to 1.008; busiest transformer 160%; export 804 kW is 804 kW over the 0 kW limit: the solar mus |
| 215 | SITE SURVEY | generic site 88 | CONFIRMED | connection point +54 kW (plus is import), +379 kvar; volts 0.990 to 1.004; busiest transformer 114%; a transformer is at 114% of its rating |
| 216 | SITE SURVEY | generic site 89 | CONFIRMED | connection point -1 kW (plus is import), +295 kvar; volts 0.989 to 1.000; busiest transformer 24%; inside every limit |
| 217 | SITE SURVEY | generic site 90 | CONFIRMED | connection point -1027 kW (plus is import), +510 kvar; volts 0.992 to 1.015; busiest transformer 307%; export 1027 kW is 827 kW over the 200 kW limit: the solar |
| 218 | SITE SURVEY | generic site 91 | CONFIRMED | connection point -227 kW (plus is import), +170 kvar; volts 0.995 to 1.001; busiest transformer 55%; inside every limit |
| 219 | SITE SURVEY | generic site 92 | CONFIRMED | connection point -1750 kW (plus is import), +538 kvar; volts 0.995 to 1.011; busiest transformer 117%; export 1750 kW is 750 kW over the 1000 kW limit: the sola |
| 220 | SITE SURVEY | generic site 93 | CONFIRMED | connection point +94 kW (plus is import), +793 kvar; volts 0.985 to 1.000; busiest transformer 79%; inside every limit |
| 221 | SITE SURVEY | generic site 94 | CONFIRMED | connection point -267 kW (plus is import), +649 kvar; volts 0.987 to 1.000; busiest transformer 79%; export 267 kW is 217 kW over the 50 kW limit: the solar mus |
| 222 | SITE SURVEY | generic site 95 | CONFIRMED | connection point -3245 kW (plus is import), +1549 kvar; volts 0.989 to 1.019; busiest transformer 304%; export 3245 kW is 2245 kW over the 1000 kW limit: the so |
| 223 | SITE SURVEY | generic site 96 | CONFIRMED | connection point -2212 kW (plus is import), +574 kvar; volts 0.991 to 1.010; busiest transformer 166%; export 2212 kW is 2162 kW over the 50 kW limit: the solar |
| 224 | SITE SURVEY | generic site 97 | CONFIRMED | connection point -1129 kW (plus is import), +481 kvar; volts 0.990 to 1.014; busiest transformer 311%; export 1129 kW is 629 kW over the 500 kW limit: the solar |
| 225 | SITE SURVEY | generic site 98 | CONFIRMED | connection point -2342 kW (plus is import), +665 kvar; volts 0.993 to 1.015; busiest transformer 153%; export 2342 kW is 2342 kW over the 0 kW limit: the solar  |
| 226 | SITE SURVEY | generic site 99 | CONFIRMED | connection point -282 kW (plus is import), +554 kvar; volts 0.988 to 1.007; busiest transformer 145%; a transformer is at 145% of its rating |
| 227 | SITE SURVEY | generic site 100 | CONFIRMED | connection point -419 kW (plus is import), +336 kvar; volts 0.991 to 1.000; busiest transformer 52%; export 419 kW is 369 kW over the 50 kW limit: the solar mus |
| 228 | SITE SURVEY | generic site 101 | CONFIRMED | connection point -1392 kW (plus is import), +834 kvar; volts 0.991 to 1.012; busiest transformer 285%; export 1392 kW is 1342 kW over the 50 kW limit: the solar |
| 229 | SITE SURVEY | generic site 102 | CONFIRMED | connection point -2080 kW (plus is import), +562 kvar; volts 0.995 to 1.011; busiest transformer 134%; export 2080 kW is 1080 kW over the 1000 kW limit: the sol |
| 230 | SITE SURVEY | generic site 103 | CONFIRMED | connection point -612 kW (plus is import), +832 kvar; volts 0.986 to 1.015; busiest transformer 340%; a transformer is at 340% of its rating |
| 231 | SITE SURVEY | generic site 104 | CONFIRMED | connection point -36 kW (plus is import), +117 kvar; volts 0.992 to 1.000; busiest transformer 22%; export 36 kW is 36 kW over the 0 kW limit: the solar must be |
| 232 | SITE SURVEY | generic site 105 | CONFIRMED | connection point -2261 kW (plus is import), +833 kvar; volts 0.994 to 1.014; busiest transformer 197%; export 2261 kW is 2211 kW over the 50 kW limit: the solar |
| 233 | SITE SURVEY | generic site 106 | CONFIRMED | connection point -1407 kW (plus is import), +636 kvar; volts 0.991 to 1.011; busiest transformer 142%; export 1407 kW is 1357 kW over the 50 kW limit: the solar |
| 234 | SITE SURVEY | generic site 107 | CONFIRMED | connection point -2290 kW (plus is import), +547 kvar; volts 0.994 to 1.011; busiest transformer 136%; export 2290 kW is 2290 kW over the 0 kW limit: the solar  |
| 235 | SITE SURVEY | generic site 108 | CONFIRMED | connection point -1292 kW (plus is import), +304 kvar; volts 0.991 to 1.011; busiest transformer 154%; export 1292 kW is 1242 kW over the 50 kW limit: the solar |
| 236 | SITE SURVEY | generic site 109 | CONFIRMED | connection point +28 kW (plus is import), +245 kvar; volts 0.992 to 1.003; busiest transformer 77%; inside every limit |
| 237 | SITE SURVEY | generic site 110 | CONFIRMED | connection point -683 kW (plus is import), +431 kvar; volts 0.991 to 1.001; busiest transformer 61%; inside every limit |
| 238 | SITE SURVEY | generic site 111 | CONFIRMED | connection point -1352 kW (plus is import), +1006 kvar; volts 0.987 to 1.009; busiest transformer 172%; export 1352 kW is 352 kW over the 1000 kW limit: the sol |
| 239 | SITE SURVEY | generic site 112 | CONFIRMED | connection point -2698 kW (plus is import), +1116 kvar; volts 0.992 to 1.012; busiest transformer 190%; export 2698 kW is 2648 kW over the 50 kW limit: the sola |
| 240 | SITE SURVEY | generic site 113 | CONFIRMED | connection point -735 kW (plus is import), +141 kvar; volts 0.997 to 1.006; busiest transformer 103%; export 735 kW is 535 kW over the 200 kW limit: the solar m |
| 241 | SITE SURVEY | generic site 114 | CONFIRMED | connection point -2129 kW (plus is import), +607 kvar; volts 0.988 to 1.010; busiest transformer 140%; export 2129 kW is 1929 kW over the 200 kW limit: the sola |
| 242 | SITE SURVEY | generic site 115 | CONFIRMED | connection point -1949 kW (plus is import), +688 kvar; volts 0.989 to 1.012; busiest transformer 253%; export 1949 kW is 1899 kW over the 50 kW limit: the solar |
| 243 | SITE SURVEY | generic site 116 | CONFIRMED | connection point -4618 kW (plus is import), +2190 kvar; volts 0.985 to 1.009; busiest transformer 328%; export 4618 kW is 4618 kW over the 0 kW limit: the solar |
| 244 | SITE SURVEY | generic site 117 | CONFIRMED | connection point -1010 kW (plus is import), +518 kvar; volts 0.990 to 1.013; busiest transformer 206%; export 1010 kW is 960 kW over the 50 kW limit: the solar  |
| 245 | SITE SURVEY | generic site 118 | CONFIRMED | connection point -2866 kW (plus is import), +1202 kvar; volts 0.988 to 1.015; busiest transformer 212%; export 2866 kW is 2866 kW over the 0 kW limit: the solar |
| 246 | SITE SURVEY | generic site 119 | CONFIRMED | connection point -2994 kW (plus is import), +1554 kvar; volts 0.988 to 1.012; busiest transformer 504%; export 2994 kW is 2494 kW over the 500 kW limit: the sol |
| 247 | SITE SURVEY | generic site 120 | CONFIRMED | connection point -1711 kW (plus is import), +752 kvar; volts 0.988 to 1.005; busiest transformer 128%; export 1711 kW is 711 kW over the 1000 kW limit: the sola |
| 248 | SITE SURVEY | generic site 121 | CONFIRMED | connection point -711 kW (plus is import), +186 kvar; volts 0.993 to 1.006; busiest transformer 108%; export 711 kW is 211 kW over the 500 kW limit: the solar m |
| 249 | SITE SURVEY | generic site 122 | CONFIRMED | connection point -2433 kW (plus is import), +1414 kvar; volts 0.983 to 1.008; busiest transformer 450%; export 2433 kW is 2433 kW over the 0 kW limit: the solar |
| 250 | SITE SURVEY | generic site 123 | CONFIRMED | connection point -73 kW (plus is import), +99 kvar; volts 0.996 to 1.000; busiest transformer 34%; inside every limit |
| 251 | SITE SURVEY | generic site 124 | CONFIRMED | connection point -47 kW (plus is import), +271 kvar; volts 0.990 to 1.004; busiest transformer 97%; inside every limit |
| 252 | SITE SURVEY | generic site 125 | CONFIRMED | connection point -1923 kW (plus is import), +556 kvar; volts 0.993 to 1.008; busiest transformer 120%; export 1923 kW is 1423 kW over the 500 kW limit: the sola |
| 253 | SITE SURVEY | generic site 126 | CONFIRMED | connection point -2511 kW (plus is import), +1973 kvar; volts 0.983 to 1.000; busiest transformer 735%; export 2511 kW is 1511 kW over the 1000 kW limit: the so |
| 254 | SITE SURVEY | generic site 127 | CONFIRMED | connection point -1374 kW (plus is import), +525 kvar; volts 0.992 to 1.018; busiest transformer 358%; export 1374 kW is 1174 kW over the 200 kW limit: the sola |
| 255 | SITE SURVEY | generic site 128 | CONFIRMED | connection point -4911 kW (plus is import), +7390 kvar; volts 0.817 to 1.000; busiest transformer 1000%; export 4911 kW is 4711 kW over the 200 kW limit: the so |
| 256 | SITE SURVEY | generic site 129 | CONFIRMED | connection point -4633 kW (plus is import), +3785 kvar; volts 0.952 to 1.000; busiest transformer 809%; export 4633 kW is 4433 kW over the 200 kW limit: the sol |
| 257 | SITE SURVEY | generic site 130 | CONFIRMED | connection point -2485 kW (plus is import), +1181 kvar; volts 0.991 to 1.016; busiest transformer 352%; export 2485 kW is 2435 kW over the 50 kW limit: the sola |
| 258 | SITE SURVEY | generic site 131 | CONFIRMED | connection point -1252 kW (plus is import), +365 kvar; volts 0.993 to 1.014; busiest transformer 165%; export 1252 kW is 752 kW over the 500 kW limit: the solar |
| 259 | SITE SURVEY | generic site 132 | CONFIRMED | connection point -1184 kW (plus is import), +523 kvar; volts 0.995 to 1.003; busiest transformer 83%; export 1184 kW is 684 kW over the 500 kW limit: the solar  |
| 260 | SITE SURVEY | generic site 133 | CONFIRMED | connection point -1004 kW (plus is import), +578 kvar; volts 0.988 to 1.004; busiest transformer 109%; export 1004 kW is 1004 kW over the 0 kW limit: the solar  |
| 261 | SITE SURVEY | generic site 134 | CONFIRMED | connection point -1924 kW (plus is import), +1018 kvar; volts 0.989 to 1.014; busiest transformer 525%; export 1924 kW is 1724 kW over the 200 kW limit: the sol |
| 262 | SITE SURVEY | generic site 135 | CONFIRMED | connection point -3168 kW (plus is import), +1233 kvar; volts 0.994 to 1.021; busiest transformer 272%; export 3168 kW is 2968 kW over the 200 kW limit: the sol |
| 263 | SITE SURVEY | generic site 136 | CONFIRMED | connection point -3629 kW (plus is import), +1470 kvar; volts 0.992 to 1.018; busiest transformer 308%; export 3629 kW is 3429 kW over the 200 kW limit: the sol |
| 264 | SITE SURVEY | generic site 137 | CONFIRMED | connection point -778 kW (plus is import), +172 kvar; volts 0.996 to 1.008; busiest transformer 113%; export 778 kW is 578 kW over the 200 kW limit: the solar m |
| 265 | SITE SURVEY | generic site 138 | CONFIRMED | connection point -1167 kW (plus is import), +374 kvar; volts 0.995 to 1.012; busiest transformer 190%; export 1167 kW is 1117 kW over the 50 kW limit: the solar |
| 266 | SITE SURVEY | generic site 139 | CONFIRMED | connection point -1137 kW (plus is import), +310 kvar; volts 0.994 to 1.005; busiest transformer 68%; export 1137 kW is 937 kW over the 200 kW limit: the solar  |
| 267 | SITE SURVEY | generic site 140 | CONFIRMED | connection point -2848 kW (plus is import), +2937 kvar; volts 0.940 to 1.000; busiest transformer 879%; export 2848 kW is 2798 kW over the 50 kW limit: the sola |
| 268 | SITE SURVEY | generic site 141 | CONFIRMED | connection point -1921 kW (plus is import), +1082 kvar; volts 0.988 to 1.012; busiest transformer 307%; export 1921 kW is 921 kW over the 1000 kW limit: the sol |
| 269 | SITE SURVEY | generic site 142 | CONFIRMED | connection point -201 kW (plus is import), +448 kvar; volts 0.989 to 1.000; busiest transformer 56%; export 201 kW is 201 kW over the 0 kW limit: the solar must |
| 270 | SITE SURVEY | generic site 143 | CONFIRMED | connection point -1248 kW (plus is import), +214 kvar; volts 0.994 to 1.006; busiest transformer 70%; export 1248 kW is 1048 kW over the 200 kW limit: the solar |
| 271 | SITE SURVEY | generic site 144 | CONFIRMED | connection point -913 kW (plus is import), +614 kvar; volts 0.989 to 1.015; busiest transformer 319%; export 913 kW is 713 kW over the 200 kW limit: the solar m |
| 272 | SITE SURVEY | generic site 145 | CONFIRMED | connection point +250 kW (plus is import), +852 kvar; volts 0.983 to 1.000; busiest transformer 144%; a transformer is at 144% of its rating |
| 273 | SITE SURVEY | generic site 146 | CONFIRMED | connection point -89 kW (plus is import), +137 kvar; volts 0.992 to 1.003; busiest transformer 60%; inside every limit |
| 274 | SITE SURVEY | generic site 147 | CONFIRMED | connection point -2161 kW (plus is import), +1240 kvar; volts 0.988 to 1.015; busiest transformer 342%; export 2161 kW is 1661 kW over the 500 kW limit: the sol |
| 275 | SITE SURVEY | generic site 148 | CONFIRMED | connection point -781 kW (plus is import), +900 kvar; volts 0.988 to 1.010; busiest transformer 368%; export 781 kW is 581 kW over the 200 kW limit: the solar m |
| 276 | SITE SURVEY | generic site 149 | CONFIRMED | connection point -42 kW (plus is import), +48 kvar; volts 0.997 to 1.000; busiest transformer 17%; inside every limit |
| 277 | SITE SURVEY | generic site 150 | CONFIRMED | connection point -4219 kW (plus is import), +2011 kvar; volts 0.982 to 1.008; busiest transformer 371%; export 4219 kW is 4169 kW over the 50 kW limit: the sola |
| 278 | SITE SURVEY | generic site 151 | CONFIRMED | connection point -1618 kW (plus is import), +969 kvar; volts 0.987 to 1.006; busiest transformer 149%; export 1618 kW is 1118 kW over the 500 kW limit: the sola |
| 279 | SITE SURVEY | generic site 152 | CONFIRMED | connection point -3736 kW (plus is import), +2619 kvar; volts 0.981 to 1.000; busiest transformer 666%; export 3736 kW is 3236 kW over the 500 kW limit: the sol |
| 280 | SITE SURVEY | generic site 153 | CONFIRMED | connection point -2022 kW (plus is import), +971 kvar; volts 0.987 to 1.009; busiest transformer 159%; export 2022 kW is 1972 kW over the 50 kW limit: the solar |
| 281 | SITE SURVEY | generic site 154 | CONFIRMED | connection point -1836 kW (plus is import), +485 kvar; volts 0.993 to 1.009; busiest transformer 143%; export 1836 kW is 1336 kW over the 500 kW limit: the sola |
| 282 | SITE SURVEY | generic site 155 | CONFIRMED | connection point -3450 kW (plus is import), +1379 kvar; volts 0.989 to 1.016; busiest transformer 292%; export 3450 kW is 3250 kW over the 200 kW limit: the sol |
| 283 | SITE SURVEY | generic site 156 | CONFIRMED | connection point -103 kW (plus is import), +498 kvar; volts 0.988 to 1.002; busiest transformer 108%; export 103 kW is 103 kW over the 0 kW limit: the solar mus |
| 284 | SITE SURVEY | generic site 157 | CONFIRMED | connection point -2370 kW (plus is import), +1129 kvar; volts 0.994 to 1.017; busiest transformer 412%; export 2370 kW is 2370 kW over the 0 kW limit: the solar |
| 285 | SITE SURVEY | generic site 158 | CONFIRMED | connection point -22 kW (plus is import), +587 kvar; volts 0.987 to 1.000; busiest transformer 47%; export 22 kW is 22 kW over the 0 kW limit: the solar must be |
| 286 | SITE SURVEY | generic site 159 | CONFIRMED | connection point -1422 kW (plus is import), +713 kvar; volts 0.992 to 1.013; busiest transformer 270%; export 1422 kW is 1372 kW over the 50 kW limit: the solar |
| 287 | SITE SURVEY | generic site 160 | CONFIRMED | connection point -888 kW (plus is import), +297 kvar; volts 0.996 to 1.004; busiest transformer 59%; export 888 kW is 838 kW over the 50 kW limit: the solar mus |
| 288 | SITE SURVEY | generic site 161 | CONFIRMED | connection point -541 kW (plus is import), +531 kvar; volts 0.989 to 1.001; busiest transformer 80%; export 541 kW is 41 kW over the 500 kW limit: the solar mus |
| 289 | SITE SURVEY | generic site 162 | CONFIRMED | connection point -1766 kW (plus is import), +651 kvar; volts 0.987 to 1.013; busiest transformer 289%; export 1766 kW is 1766 kW over the 0 kW limit: the solar  |
| 290 | SITE SURVEY | generic site 163 | CONFIRMED | connection point -2426 kW (plus is import), +1284 kvar; volts 0.987 to 1.013; busiest transformer 434%; export 2426 kW is 2226 kW over the 200 kW limit: the sol |
| 291 | SITE SURVEY | generic site 164 | CONFIRMED | connection point -169 kW (plus is import), +261 kvar; volts 0.989 to 1.000; busiest transformer 27%; inside every limit |
| 292 | SITE SURVEY | generic site 165 | CONFIRMED | connection point -603 kW (plus is import), +148 kvar; volts 0.995 to 1.008; busiest transformer 139%; export 603 kW is 403 kW over the 200 kW limit: the solar m |
| 293 | SITE SURVEY | generic site 166 | CONFIRMED | connection point -230 kW (plus is import), +258 kvar; volts 0.993 to 1.002; busiest transformer 60%; inside every limit |
| 294 | SITE SURVEY | generic site 167 | CONFIRMED | connection point -133 kW (plus is import), +248 kvar; volts 0.992 to 1.002; busiest transformer 98%; export 133 kW is 133 kW over the 0 kW limit: the solar must |
| 295 | SITE SURVEY | generic site 168 | CONFIRMED | connection point +369 kW (plus is import), +895 kvar; volts 0.982 to 1.000; busiest transformer 144%; a transformer is at 144% of its rating |
| 296 | SITE SURVEY | generic site 169 | CONFIRMED | connection point -2140 kW (plus is import), +1377 kvar; volts 0.986 to 1.002; busiest transformer 608%; export 2140 kW is 2090 kW over the 50 kW limit: the sola |
| 297 | SITE SURVEY | generic site 170 | CONFIRMED | connection point -4033 kW (plus is import), +2666 kvar; volts 0.980 to 1.000; busiest transformer 591%; export 4033 kW is 4033 kW over the 0 kW limit: the solar |
| 298 | SITE SURVEY | generic site 171 | CONFIRMED | connection point -3337 kW (plus is import), +2077 kvar; volts 0.980 to 1.006; busiest transformer 501%; export 3337 kW is 2837 kW over the 500 kW limit: the sol |
| 299 | SITE SURVEY | generic site 172 | CONFIRMED | connection point -1862 kW (plus is import), +1000 kvar; volts 0.990 to 1.012; busiest transformer 511%; export 1862 kW is 1862 kW over the 0 kW limit: the solar |
| 300 | SITE SURVEY | generic site 173 | CONFIRMED | connection point +12 kW (plus is import), +481 kvar; volts 0.989 to 1.000; busiest transformer 41%; inside every limit |
| 301 | SITE SURVEY | generic site 174 | CONFIRMED | connection point -2238 kW (plus is import), +1926 kvar; volts 0.983 to 1.000; busiest transformer 707%; export 2238 kW is 2238 kW over the 0 kW limit: the solar |
| 302 | SITE SURVEY | generic site 175 | CONFIRMED | connection point -1301 kW (plus is import), +969 kvar; volts 0.988 to 1.012; busiest transformer 446%; export 1301 kW is 801 kW over the 500 kW limit: the solar |
| 303 | SITE SURVEY | generic site 176 | CONFIRMED | connection point +67 kW (plus is import), +102 kvar; volts 0.991 to 1.000; busiest transformer 24%; inside every limit |
| 304 | SITE SURVEY | generic site 177 | CONFIRMED | connection point -94 kW (plus is import), +404 kvar; volts 0.992 to 1.000; busiest transformer 25%; export 94 kW is 94 kW over the 0 kW limit: the solar must be |
| 305 | SITE SURVEY | generic site 178 | CONFIRMED | connection point -1348 kW (plus is import), +512 kvar; volts 0.989 to 1.008; busiest transformer 184%; export 1348 kW is 848 kW over the 500 kW limit: the solar |
| 306 | SITE SURVEY | generic site 179 | CONFIRMED | connection point -5004 kW (plus is import), +5959 kvar; volts 0.882 to 1.000; busiest transformer 960%; export 5004 kW is 5004 kW over the 0 kW limit: the solar |
| 307 | SITE SURVEY | generic site 180 | CONFIRMED | connection point -1137 kW (plus is import), +215 kvar; volts 0.993 to 1.005; busiest transformer 67%; export 1137 kW is 1137 kW over the 0 kW limit: the solar m |
| 308 | SITE SURVEY | generic site 181 | CONFIRMED | connection point -1838 kW (plus is import), +719 kvar; volts 0.989 to 1.018; busiest transformer 311%; export 1838 kW is 1638 kW over the 200 kW limit: the sola |
| 309 | SITE SURVEY | generic site 182 | CONFIRMED | connection point -1156 kW (plus is import), +452 kvar; volts 0.992 to 1.014; busiest transformer 169%; export 1156 kW is 1106 kW over the 50 kW limit: the solar |
| 310 | SITE SURVEY | generic site 183 | CONFIRMED | connection point +7 kW (plus is import), +155 kvar; volts 0.991 to 1.000; busiest transformer 41%; inside every limit |
| 311 | SITE SURVEY | generic site 184 | CONFIRMED | connection point +30 kW (plus is import), +392 kvar; volts 0.991 to 1.000; busiest transformer 23%; inside every limit |
| 312 | SITE SURVEY | generic site 185 | CONFIRMED | connection point -2220 kW (plus is import), +2528 kvar; volts 0.967 to 1.000; busiest transformer 794%; export 2220 kW is 2170 kW over the 50 kW limit: the sola |
| 313 | SITE SURVEY | generic site 186 | CONFIRMED | connection point -992 kW (plus is import), +526 kvar; volts 0.990 to 1.016; busiest transformer 309%; export 992 kW is 942 kW over the 50 kW limit: the solar mu |
| 314 | SITE SURVEY | generic site 187 | CONFIRMED | connection point -1400 kW (plus is import), +572 kvar; volts 0.990 to 1.004; busiest transformer 125%; export 1400 kW is 400 kW over the 1000 kW limit: the sola |
| 315 | SITE SURVEY | generic site 188 | CONFIRMED | connection point -2388 kW (plus is import), +957 kvar; volts 0.991 to 1.012; busiest transformer 212%; export 2388 kW is 2188 kW over the 200 kW limit: the sola |
| 316 | SITE SURVEY | generic site 189 | CONFIRMED | connection point -1758 kW (plus is import), +714 kvar; volts 0.990 to 1.015; busiest transformer 252%; export 1758 kW is 1708 kW over the 50 kW limit: the solar |
| 317 | SITE SURVEY | generic site 190 | CONFIRMED | connection point -545 kW (plus is import), +149 kvar; volts 0.995 to 1.003; busiest transformer 81%; inside every limit |
| 318 | SITE SURVEY | generic site 191 | CONFIRMED | connection point -522 kW (plus is import), +1046 kvar; volts 0.985 to 1.006; busiest transformer 249%; a transformer is at 249% of its rating |
| 319 | SITE SURVEY | generic site 192 | CONFIRMED | connection point -1444 kW (plus is import), +402 kvar; volts 0.996 to 1.010; busiest transformer 118%; export 1444 kW is 1244 kW over the 200 kW limit: the sola |
| 320 | SITE SURVEY | generic site 193 | CONFIRMED | connection point -4579 kW (plus is import), +2792 kvar; volts 0.979 to 1.000; busiest transformer 622%; export 4579 kW is 3579 kW over the 1000 kW limit: the so |
| 321 | SITE SURVEY | generic site 194 | CONFIRMED | connection point -630 kW (plus is import), +963 kvar; volts 0.986 to 1.001; busiest transformer 104%; export 630 kW is 130 kW over the 500 kW limit: the solar m |
| 322 | SITE SURVEY | generic site 195 | CONFIRMED | connection point -315 kW (plus is import), +579 kvar; volts 0.989 to 1.000; busiest transformer 69%; export 315 kW is 315 kW over the 0 kW limit: the solar must |
| 323 | SITE SURVEY | generic site 196 | CONFIRMED | connection point -2101 kW (plus is import), +1145 kvar; volts 0.985 to 1.007; busiest transformer 173%; export 2101 kW is 1101 kW over the 1000 kW limit: the so |
| 324 | SITE SURVEY | generic site 197 | CONFIRMED | connection point -862 kW (plus is import), +928 kvar; volts 0.987 to 1.010; busiest transformer 260%; export 862 kW is 662 kW over the 200 kW limit: the solar m |
| 325 | SITE SURVEY | generic site 198 | CONFIRMED | connection point -1398 kW (plus is import), +419 kvar; volts 0.992 to 1.007; busiest transformer 113%; export 1398 kW is 898 kW over the 500 kW limit: the solar |
| 326 | SITE SURVEY | generic site 199 | CONFIRMED | connection point -1323 kW (plus is import), +560 kvar; volts 0.992 to 1.011; busiest transformer 191%; export 1323 kW is 823 kW over the 500 kW limit: the solar |
| 327 | SITE SURVEY | generic site 200 | CONFIRMED | connection point -920 kW (plus is import), +322 kvar; volts 0.992 to 1.000; busiest transformer 55%; export 920 kW is 870 kW over the 50 kW limit: the solar mus |
| 328 | SITE SURVEY | generic site 201 | CONFIRMED | connection point -1152 kW (plus is import), +263 kvar; volts 0.996 to 1.009; busiest transformer 132%; export 1152 kW is 652 kW over the 500 kW limit: the solar |
| 329 | SITE SURVEY | generic site 202 | REFUTED | connection point -3654 kW (plus is import), +3618 kvar; volts 0.966 to 1.000; busiest transformer 1115%; export 3654 kW is 3154 kW over the 500 kW limit: the so |
| 330 | SITE SURVEY | generic site 203 | CONFIRMED | connection point -513 kW (plus is import), +111 kvar; volts 0.992 to 1.006; busiest transformer 78%; export 513 kW is 463 kW over the 50 kW limit: the solar mus |
| 331 | SITE SURVEY | generic site 204 | CONFIRMED | connection point -571 kW (plus is import), +589 kvar; volts 0.988 to 1.003; busiest transformer 73%; export 571 kW is 371 kW over the 200 kW limit: the solar mu |
| 332 | SITE SURVEY | generic site 205 | CONFIRMED | connection point -1026 kW (plus is import), +574 kvar; volts 0.992 to 1.006; busiest transformer 91%; export 1026 kW is 26 kW over the 1000 kW limit: the solar  |
| 333 | SITE SURVEY | generic site 206 | CONFIRMED | connection point -585 kW (plus is import), +184 kvar; volts 0.991 to 1.010; busiest transformer 156%; a transformer is at 156% of its rating |
| 334 | SITE SURVEY | generic site 207 | CONFIRMED | connection point -1565 kW (plus is import), +849 kvar; volts 0.990 to 1.019; busiest transformer 311%; export 1565 kW is 1365 kW over the 200 kW limit: the sola |
| 335 | SITE SURVEY | generic site 208 | CONFIRMED | connection point -3704 kW (plus is import), +1263 kvar; volts 0.989 to 1.017; busiest transformer 296%; export 3704 kW is 2704 kW over the 1000 kW limit: the so |
| 336 | SITE SURVEY | generic site 209 | CONFIRMED | connection point -1888 kW (plus is import), +955 kvar; volts 0.991 to 1.013; busiest transformer 506%; export 1888 kW is 1888 kW over the 0 kW limit: the solar  |
| 337 | SITE SURVEY | generic site 210 | CONFIRMED | connection point -2772 kW (plus is import), +1040 kvar; volts 0.993 to 1.022; busiest transformer 357%; export 2772 kW is 2572 kW over the 200 kW limit: the sol |
| 338 | SITE SURVEY | generic site 211 | CONFIRMED | connection point -4405 kW (plus is import), +1502 kvar; volts 0.992 to 1.024; busiest transformer 281%; export 4405 kW is 4205 kW over the 200 kW limit: the sol |
| 339 | SITE SURVEY | generic site 212 | CONFIRMED | connection point -787 kW (plus is import), +772 kvar; volts 0.986 to 1.012; busiest transformer 344%; export 787 kW is 787 kW over the 0 kW limit: the solar mus |
| 340 | SITE SURVEY | generic site 213 | CONFIRMED | connection point -909 kW (plus is import), +326 kvar; volts 0.993 to 1.004; busiest transformer 81%; inside every limit |
| 341 | SITE SURVEY | generic site 214 | CONFIRMED | connection point -3760 kW (plus is import), +1995 kvar; volts 0.986 to 1.013; busiest transformer 515%; export 3760 kW is 3760 kW over the 0 kW limit: the solar |
| 342 | SITE SURVEY | generic site 215 | CONFIRMED | connection point -145 kW (plus is import), +93 kvar; volts 0.993 to 1.000; busiest transformer 24%; export 145 kW is 145 kW over the 0 kW limit: the solar must  |
| 343 | SITE SURVEY | generic site 216 | CONFIRMED | connection point -3775 kW (plus is import), +1524 kvar; volts 0.989 to 1.013; busiest transformer 314%; export 3775 kW is 3275 kW over the 500 kW limit: the sol |
| 344 | SITE SURVEY | generic site 217 | CONFIRMED | connection point +90 kW (plus is import), +342 kvar; volts 0.991 to 1.000; busiest transformer 42%; inside every limit |
| 345 | SITE SURVEY | generic site 218 | CONFIRMED | connection point -212 kW (plus is import), +239 kvar; volts 0.993 to 1.001; busiest transformer 54%; inside every limit |
| 346 | SITE SURVEY | generic site 219 | CONFIRMED | connection point -1015 kW (plus is import), +994 kvar; volts 0.986 to 1.012; busiest transformer 422%; export 1015 kW is 1015 kW over the 0 kW limit: the solar  |
| 347 | SITE SURVEY | generic site 220 | CONFIRMED | connection point -2745 kW (plus is import), +1509 kvar; volts 0.990 to 1.015; busiest transformer 489%; export 2745 kW is 2745 kW over the 0 kW limit: the solar |
| 348 | SITE SURVEY | generic site 221 | CONFIRMED | connection point -1405 kW (plus is import), +546 kvar; volts 0.995 to 1.014; busiest transformer 239%; export 1405 kW is 1405 kW over the 0 kW limit: the solar  |
| 349 | SITE SURVEY | generic site 222 | CONFIRMED | connection point -1093 kW (plus is import), +735 kvar; volts 0.988 to 1.006; busiest transformer 130%; export 1093 kW is 93 kW over the 1000 kW limit: the solar |
| 350 | SITE SURVEY | generic site 223 | CONFIRMED | connection point -801 kW (plus is import), +576 kvar; volts 0.990 to 1.012; busiest transformer 292%; export 801 kW is 801 kW over the 0 kW limit: the solar mus |
| 351 | SITE SURVEY | generic site 224 | CONFIRMED | connection point -392 kW (plus is import), +110 kvar; volts 0.996 to 1.002; busiest transformer 59%; export 392 kW is 192 kW over the 200 kW limit: the solar mu |
| 352 | SITE SURVEY | generic site 225 | CONFIRMED | connection point -1537 kW (plus is import), +1053 kvar; volts 0.988 to 1.015; busiest transformer 280%; export 1537 kW is 1337 kW over the 200 kW limit: the sol |
| 353 | SITE SURVEY | generic site 226 | CONFIRMED | connection point -3799 kW (plus is import), +2400 kvar; volts 0.986 to 1.005; busiest transformer 549%; export 3799 kW is 3799 kW over the 0 kW limit: the solar |
| 354 | SITE SURVEY | generic site 227 | CONFIRMED | connection point -558 kW (plus is import), +372 kvar; volts 0.993 to 1.008; busiest transformer 132%; export 558 kW is 58 kW over the 500 kW limit: the solar mu |
| 355 | SITE SURVEY | generic site 228 | CONFIRMED | connection point -3335 kW (plus is import), +1667 kvar; volts 0.989 to 1.015; busiest transformer 252%; export 3335 kW is 2335 kW over the 1000 kW limit: the so |
| 356 | SITE SURVEY | generic site 229 | CONFIRMED | connection point -2085 kW (plus is import), +598 kvar; volts 0.989 to 1.009; busiest transformer 137%; export 2085 kW is 1585 kW over the 500 kW limit: the sola |
| 357 | SITE SURVEY | generic site 230 | CONFIRMED | connection point -1010 kW (plus is import), +909 kvar; volts 0.987 to 1.014; busiest transformer 273%; export 1010 kW is 510 kW over the 500 kW limit: the solar |
| 358 | SITE SURVEY | generic site 231 | REFUTED | connection point -2731 kW (plus is import), +5461 kvar; volts 0.791 to 1.000; busiest transformer 1039%; export 2731 kW is 2231 kW over the 500 kW limit: the so |
| 359 | SITE SURVEY | generic site 232 | CONFIRMED | connection point -721 kW (plus is import), +270 kvar; volts 0.995 to 1.005; busiest transformer 98%; export 721 kW is 521 kW over the 200 kW limit: the solar mu |
| 360 | SITE SURVEY | generic site 233 | CONFIRMED | connection point -1036 kW (plus is import), +814 kvar; volts 0.988 to 1.011; busiest transformer 256%; export 1036 kW is 36 kW over the 1000 kW limit: the solar |
| 361 | SITE SURVEY | generic site 234 | CONFIRMED | connection point -2660 kW (plus is import), +1338 kvar; volts 0.988 to 1.011; busiest transformer 452%; export 2660 kW is 2660 kW over the 0 kW limit: the solar |
| 362 | SITE SURVEY | generic site 235 | CONFIRMED | connection point -64 kW (plus is import), +374 kvar; volts 0.990 to 1.008; busiest transformer 137%; export 64 kW is 14 kW over the 50 kW limit: the solar must  |
| 363 | SITE SURVEY | generic site 236 | CONFIRMED | connection point -2627 kW (plus is import), +811 kvar; volts 0.990 to 1.010; busiest transformer 173%; export 2627 kW is 2627 kW over the 0 kW limit: the solar  |
| 364 | SITE SURVEY | generic site 237 | CONFIRMED | connection point -2250 kW (plus is import), +1296 kvar; volts 0.984 to 1.008; busiest transformer 231%; export 2250 kW is 1250 kW over the 1000 kW limit: the so |
| 365 | SITE SURVEY | generic site 238 | CONFIRMED | connection point -482 kW (plus is import), +710 kvar; volts 0.987 to 1.014; busiest transformer 293%; a transformer is at 293% of its rating |
| 366 | SITE SURVEY | generic site 239 | CONFIRMED | connection point -226 kW (plus is import), +125 kvar; volts 0.994 to 1.000; busiest transformer 39%; export 226 kW is 26 kW over the 200 kW limit: the solar mus |
| 367 | SITE SURVEY | generic site 240 | CONFIRMED | connection point +77 kW (plus is import), +767 kvar; volts 0.985 to 1.000; busiest transformer 59%; inside every limit |
| 368 | SITE SURVEY | generic site 241 | CONFIRMED | connection point -4819 kW (plus is import), +1939 kvar; volts 0.990 to 1.025; busiest transformer 327%; export 4819 kW is 3819 kW over the 1000 kW limit: the so |
| 369 | SITE SURVEY | generic site 242 | CONFIRMED | connection point -1827 kW (plus is import), +636 kvar; volts 0.991 to 1.015; busiest transformer 298%; export 1827 kW is 827 kW over the 1000 kW limit: the sola |
| 370 | SITE SURVEY | generic site 243 | CONFIRMED | connection point -2405 kW (plus is import), +797 kvar; volts 0.992 to 1.015; busiest transformer 304%; export 2405 kW is 2405 kW over the 0 kW limit: the solar  |
| 371 | SITE SURVEY | generic site 244 | CONFIRMED | connection point -1798 kW (plus is import), +935 kvar; volts 0.988 to 1.015; busiest transformer 284%; export 1798 kW is 1798 kW over the 0 kW limit: the solar  |
| 372 | SITE SURVEY | generic site 245 | CONFIRMED | connection point -924 kW (plus is import), +482 kvar; volts 0.991 to 1.010; busiest transformer 184%; export 924 kW is 724 kW over the 200 kW limit: the solar m |
| 373 | SITE SURVEY | generic site 246 | CONFIRMED | connection point -1698 kW (plus is import), +356 kvar; volts 0.998 to 1.012; busiest transformer 126%; export 1698 kW is 1698 kW over the 0 kW limit: the solar  |
| 374 | SITE SURVEY | generic site 247 | CONFIRMED | connection point +48 kW (plus is import), +333 kvar; volts 0.991 to 1.002; busiest transformer 99%; inside every limit |
| 375 | SITE SURVEY | generic site 248 | CONFIRMED | connection point -4962 kW (plus is import), +6326 kvar; volts 0.865 to 1.000; busiest transformer 971%; export 4962 kW is 4912 kW over the 50 kW limit: the sola |
| 376 | SITE SURVEY | generic site 249 | CONFIRMED | connection point -1967 kW (plus is import), +867 kvar; volts 0.989 to 1.006; busiest transformer 145%; export 1967 kW is 1967 kW over the 0 kW limit: the solar  |
| 377 | SITE SURVEY | generic site 250 | CONFIRMED | connection point -2933 kW (plus is import), +1521 kvar; volts 0.988 to 1.013; busiest transformer 414%; export 2933 kW is 2883 kW over the 50 kW limit: the sola |
| 378 | SITE SURVEY | generic site 251 | CONFIRMED | connection point -632 kW (plus is import), +584 kvar; volts 0.988 to 1.006; busiest transformer 174%; export 632 kW is 582 kW over the 50 kW limit: the solar mu |
| 379 | SITE SURVEY | generic site 252 | CONFIRMED | connection point -3195 kW (plus is import), +1190 kvar; volts 0.991 to 1.016; busiest transformer 223%; export 3195 kW is 2195 kW over the 1000 kW limit: the so |
| 380 | SITE SURVEY | generic site 253 | CONFIRMED | connection point -1701 kW (plus is import), +1065 kvar; volts 0.988 to 1.014; busiest transformer 354%; export 1701 kW is 1501 kW over the 200 kW limit: the sol |
| 381 | SITE SURVEY | generic site 254 | CONFIRMED | connection point -107 kW (plus is import), +314 kvar; volts 0.992 to 1.000; busiest transformer 53%; inside every limit |
| 382 | SITE SURVEY | generic site 255 | CONFIRMED | connection point -388 kW (plus is import), +181 kvar; volts 0.993 to 1.004; busiest transformer 116%; a transformer is at 116% of its rating |
| 383 | SITE SURVEY | generic site 256 | CONFIRMED | connection point -3060 kW (plus is import), +753 kvar; volts 0.992 to 1.013; busiest transformer 184%; export 3060 kW is 2060 kW over the 1000 kW limit: the sol |
| 384 | SITE SURVEY | generic site 257 | CONFIRMED | connection point +146 kW (plus is import), +328 kvar; volts 0.989 to 1.000; busiest transformer 24%; inside every limit |
| 385 | SITE SURVEY | generic site 258 | CONFIRMED | connection point -4841 kW (plus is import), +1769 kvar; volts 0.991 to 1.024; busiest transformer 311%; export 4841 kW is 3841 kW over the 1000 kW limit: the so |
| 386 | SITE SURVEY | generic site 259 | CONFIRMED | connection point -1403 kW (plus is import), +315 kvar; volts 0.995 to 1.009; busiest transformer 86%; export 1403 kW is 403 kW over the 1000 kW limit: the solar |
| 387 | SITE SURVEY | generic site 260 | CONFIRMED | connection point -1447 kW (plus is import), +412 kvar; volts 0.993 to 1.011; busiest transformer 178%; export 1447 kW is 1397 kW over the 50 kW limit: the solar |
| 388 | SITE SURVEY | generic site 261 | CONFIRMED | connection point -1617 kW (plus is import), +845 kvar; volts 0.990 to 1.009; busiest transformer 448%; export 1617 kW is 1617 kW over the 0 kW limit: the solar  |
| 389 | SITE SURVEY | generic site 262 | CONFIRMED | connection point -2749 kW (plus is import), +952 kvar; volts 0.989 to 1.013; busiest transformer 231%; export 2749 kW is 2549 kW over the 200 kW limit: the sola |
| 390 | SITE SURVEY | generic site 263 | CONFIRMED | connection point -898 kW (plus is import), +1096 kvar; volts 0.986 to 1.003; busiest transformer 122%; export 898 kW is 848 kW over the 50 kW limit: the solar m |
| 391 | SITE SURVEY | generic site 264 | CONFIRMED | connection point -925 kW (plus is import), +752 kvar; volts 0.987 to 1.008; busiest transformer 193%; export 925 kW is 725 kW over the 200 kW limit: the solar m |
| 392 | SITE SURVEY | generic site 265 | CONFIRMED | connection point -3553 kW (plus is import), +3355 kvar; volts 0.969 to 1.000; busiest transformer 724%; export 3553 kW is 3553 kW over the 0 kW limit: the solar |
| 393 | SITE SURVEY | generic site 266 | CONFIRMED | connection point -151 kW (plus is import), +251 kvar; volts 0.992 to 1.000; busiest transformer 18%; export 151 kW is 151 kW over the 0 kW limit: the solar must |
| 394 | SITE SURVEY | generic site 267 | CONFIRMED | connection point -349 kW (plus is import), +160 kvar; volts 0.993 to 1.008; busiest transformer 114%; a transformer is at 114% of its rating |
| 395 | SITE SURVEY | generic site 268 | CONFIRMED | connection point -2896 kW (plus is import), +1644 kvar; volts 0.985 to 1.009; busiest transformer 235%; export 2896 kW is 2896 kW over the 0 kW limit: the solar |
| 396 | SITE SURVEY | generic site 269 | CONFIRMED | connection point -1063 kW (plus is import), +374 kvar; volts 0.995 to 1.014; busiest transformer 272%; export 1063 kW is 1063 kW over the 0 kW limit: the solar  |
| 397 | SITE SURVEY | generic site 270 | CONFIRMED | connection point -2181 kW (plus is import), +2193 kvar; volts 0.980 to 1.006; busiest transformer 538%; export 2181 kW is 2181 kW over the 0 kW limit: the solar |
| 398 | SITE SURVEY | generic site 271 | CONFIRMED | connection point -1546 kW (plus is import), +904 kvar; volts 0.987 to 1.010; busiest transformer 455%; export 1546 kW is 1346 kW over the 200 kW limit: the sola |
| 399 | SITE SURVEY | generic site 272 | CONFIRMED | connection point -2234 kW (plus is import), +1178 kvar; volts 0.986 to 1.015; busiest transformer 406%; export 2234 kW is 2184 kW over the 50 kW limit: the sola |
| 400 | SITE SURVEY | generic site 273 | CONFIRMED | connection point -1539 kW (plus is import), +368 kvar; volts 0.996 to 1.008; busiest transformer 94%; export 1539 kW is 1339 kW over the 200 kW limit: the solar |
| 401 | SITE SURVEY | generic site 274 | CONFIRMED | connection point +171 kW (plus is import), +354 kvar; volts 0.988 to 1.000; busiest transformer 57%; inside every limit |
| 402 | SITE SURVEY | generic site 275 | CONFIRMED | connection point -4262 kW (plus is import), +2604 kvar; volts 0.981 to 1.003; busiest transformer 596%; export 4262 kW is 4212 kW over the 50 kW limit: the sola |
| 403 | SITE SURVEY | generic site 276 | CONFIRMED | connection point -1093 kW (plus is import), +458 kvar; volts 0.994 to 1.016; busiest transformer 305%; export 1093 kW is 1093 kW over the 0 kW limit: the solar  |
| 404 | SITE SURVEY | generic site 277 | CONFIRMED | connection point -259 kW (plus is import), +204 kvar; volts 0.995 to 1.000; busiest transformer 24%; inside every limit |
| 405 | SITE SURVEY | generic site 278 | CONFIRMED | connection point -1361 kW (plus is import), +520 kvar; volts 0.994 to 1.015; busiest transformer 237%; export 1361 kW is 1361 kW over the 0 kW limit: the solar  |
| 406 | SITE SURVEY | generic site 279 | CONFIRMED | connection point -1000 kW (plus is import), +668 kvar; volts 0.989 to 1.015; busiest transformer 346%; export 1000 kW is 500 kW over the 500 kW limit: the solar |
| 407 | SITE SURVEY | generic site 280 | CONFIRMED | connection point -2160 kW (plus is import), +1574 kvar; volts 0.987 to 1.000; busiest transformer 644%; export 2160 kW is 1660 kW over the 500 kW limit: the sol |
| 408 | SITE SURVEY | generic site 281 | CONFIRMED | connection point -2048 kW (plus is import), +395 kvar; volts 0.998 to 1.009; busiest transformer 111%; export 2048 kW is 1848 kW over the 200 kW limit: the sola |
| 409 | SITE SURVEY | generic site 282 | CONFIRMED | connection point -3361 kW (plus is import), +1913 kvar; volts 0.983 to 1.008; busiest transformer 480%; export 3361 kW is 3311 kW over the 50 kW limit: the sola |
| 410 | SITE SURVEY | generic site 283 | CONFIRMED | connection point -175 kW (plus is import), +681 kvar; volts 0.986 to 1.003; busiest transformer 150%; export 175 kW is 175 kW over the 0 kW limit: the solar mus |
| 411 | SITE SURVEY | generic site 284 | CONFIRMED | connection point -1100 kW (plus is import), +267 kvar; volts 0.991 to 1.009; busiest transformer 134%; export 1100 kW is 900 kW over the 200 kW limit: the solar |
| 412 | SITE SURVEY | generic site 285 | CONFIRMED | connection point -597 kW (plus is import), +414 kvar; volts 0.993 to 1.005; busiest transformer 139%; export 597 kW is 547 kW over the 50 kW limit: the solar mu |
| 413 | SITE SURVEY | generic site 286 | CONFIRMED | connection point -13 kW (plus is import), +470 kvar; volts 0.989 to 1.003; busiest transformer 99%; export 13 kW is 13 kW over the 0 kW limit: the solar must be |
| 414 | SITE SURVEY | generic site 287 | CONFIRMED | connection point -120 kW (plus is import), +366 kvar; volts 0.989 to 1.008; busiest transformer 144%; a transformer is at 144% of its rating |
| 415 | SITE SURVEY | generic site 288 | CONFIRMED | connection point -928 kW (plus is import), +1139 kvar; volts 0.985 to 1.007; busiest transformer 165%; export 928 kW is 428 kW over the 500 kW limit: the solar  |
| 416 | SITE SURVEY | generic site 289 | CONFIRMED | connection point -3028 kW (plus is import), +1795 kvar; volts 0.987 to 1.010; busiest transformer 450%; export 3028 kW is 2978 kW over the 50 kW limit: the sola |
| 417 | SITE SURVEY | generic site 290 | CONFIRMED | connection point -1720 kW (plus is import), +825 kvar; volts 0.991 to 1.016; busiest transformer 263%; export 1720 kW is 1220 kW over the 500 kW limit: the sola |
| 418 | SITE SURVEY | generic site 291 | CONFIRMED | connection point -954 kW (plus is import), +1419 kvar; volts 0.982 to 1.006; busiest transformer 504%; export 954 kW is 454 kW over the 500 kW limit: the solar  |
| 419 | SITE SURVEY | generic site 292 | REFUTED | connection point -4515 kW (plus is import), -1394 kvar; volts 1.000 to 1.526; busiest transformer 1987%; export 4515 kW is 4465 kW over the 50 kW limit: the sol |
| 420 | SITE SURVEY | generic site 293 | CONFIRMED | connection point -652 kW (plus is import), +550 kvar; volts 0.991 to 1.011; busiest transformer 181%; export 652 kW is 152 kW over the 500 kW limit: the solar m |
| 421 | SITE SURVEY | generic site 294 | CONFIRMED | connection point -619 kW (plus is import), +205 kvar; volts 0.994 to 1.002; busiest transformer 49%; export 619 kW is 419 kW over the 200 kW limit: the solar mu |
| 422 | SITE SURVEY | generic site 295 | CONFIRMED | connection point -3528 kW (plus is import), +2571 kvar; volts 0.984 to 1.000; busiest transformer 656%; export 3528 kW is 3528 kW over the 0 kW limit: the solar |
| 423 | SITE SURVEY | generic site 296 | CONFIRMED | connection point -1599 kW (plus is import), +409 kvar; volts 0.993 to 1.012; busiest transformer 193%; export 1599 kW is 1549 kW over the 50 kW limit: the solar |
| 424 | SITE SURVEY | generic site 297 | CONFIRMED | connection point -584 kW (plus is import), +590 kvar; volts 0.989 to 1.002; busiest transformer 88%; export 584 kW is 534 kW over the 50 kW limit: the solar mus |
| 425 | SITE SURVEY | generic site 298 | CONFIRMED | connection point -1804 kW (plus is import), +547 kvar; volts 0.993 to 1.008; busiest transformer 115%; export 1804 kW is 1604 kW over the 200 kW limit: the sola |
| 426 | SITE SURVEY | generic site 299 | CONFIRMED | connection point -4866 kW (plus is import), +1771 kvar; volts 0.990 to 1.016; busiest transformer 315%; export 4866 kW is 4666 kW over the 200 kW limit: the sol |
| 427 | SITE SURVEY | generic site 300 | CONFIRMED | connection point -4093 kW (plus is import), +3085 kvar; volts 0.981 to 1.000; busiest transformer 730%; export 4093 kW is 3893 kW over the 200 kW limit: the sol |
| 428 | SITE SURVEY | generic site 301 | CONFIRMED | connection point -4006 kW (plus is import), +1224 kvar; volts 0.988 to 1.018; busiest transformer 252%; export 4006 kW is 3006 kW over the 1000 kW limit: the so |
| 429 | SITE SURVEY | generic site 302 | CONFIRMED | connection point -3771 kW (plus is import), +2007 kvar; volts 0.981 to 1.004; busiest transformer 510%; export 3771 kW is 3571 kW over the 200 kW limit: the sol |
| 430 | SITE SURVEY | generic site 303 | CONFIRMED | connection point -1920 kW (plus is import), +728 kvar; volts 0.990 to 1.012; busiest transformer 309%; export 1920 kW is 1420 kW over the 500 kW limit: the sola |
| 431 | SITE SURVEY | generic site 304 | CONFIRMED | connection point -289 kW (plus is import), +196 kvar; volts 0.994 to 1.002; busiest transformer 55%; export 289 kW is 289 kW over the 0 kW limit: the solar must |
| 432 | SITE SURVEY | generic site 305 | CONFIRMED | connection point -2601 kW (plus is import), +616 kvar; volts 0.993 to 1.012; busiest transformer 158%; export 2601 kW is 2551 kW over the 50 kW limit: the solar |
| 433 | SITE SURVEY | generic site 306 | CONFIRMED | connection point -4403 kW (plus is import), +1467 kvar; volts 0.993 to 1.024; busiest transformer 285%; export 4403 kW is 3403 kW over the 1000 kW limit: the so |
| 434 | SITE SURVEY | generic site 307 | CONFIRMED | connection point -2040 kW (plus is import), +1253 kvar; volts 0.988 to 1.012; busiest transformer 184%; export 2040 kW is 1840 kW over the 200 kW limit: the sol |
| 435 | SITE SURVEY | generic site 308 | CONFIRMED | connection point +76 kW (plus is import), +405 kvar; volts 0.988 to 1.000; busiest transformer 66%; inside every limit |
| 436 | SITE SURVEY | generic site 309 | CONFIRMED | connection point -227 kW (plus is import), +85 kvar; volts 0.996 to 1.001; busiest transformer 32%; export 227 kW is 177 kW over the 50 kW limit: the solar must |
| 437 | SITE SURVEY | generic site 310 | CONFIRMED | connection point -2628 kW (plus is import), +1574 kvar; volts 0.985 to 1.010; busiest transformer 487%; export 2628 kW is 1628 kW over the 1000 kW limit: the so |
| 438 | SITE SURVEY | generic site 311 | CONFIRMED | connection point -2468 kW (plus is import), +1089 kvar; volts 0.986 to 1.011; busiest transformer 227%; export 2468 kW is 2468 kW over the 0 kW limit: the solar |
| 439 | SITE SURVEY | generic site 312 | CONFIRMED | connection point +223 kW (plus is import), +557 kvar; volts 0.988 to 1.000; busiest transformer 68%; inside every limit |
| 440 | SITE SURVEY | generic site 313 | CONFIRMED | connection point +123 kW (plus is import), +406 kvar; volts 0.988 to 1.000; busiest transformer 29%; inside every limit |
| 441 | SITE SURVEY | generic site 314 | CONFIRMED | connection point -2612 kW (plus is import), +576 kvar; volts 0.995 to 1.006; busiest transformer 147%; export 2612 kW is 2562 kW over the 50 kW limit: the solar |
| 442 | SITE SURVEY | generic site 315 | CONFIRMED | connection point +24 kW (plus is import), +331 kvar; volts 0.989 to 1.000; busiest transformer 60%; inside every limit |
| 443 | SITE SURVEY | generic site 316 | CONFIRMED | connection point -356 kW (plus is import), +126 kvar; volts 0.992 to 1.003; busiest transformer 94%; inside every limit |
| 444 | SITE SURVEY | generic site 317 | CONFIRMED | connection point -699 kW (plus is import), +513 kvar; volts 0.989 to 1.010; busiest transformer 176%; export 699 kW is 499 kW over the 200 kW limit: the solar m |
| 445 | SITE SURVEY | generic site 318 | CONFIRMED | connection point -718 kW (plus is import), +1182 kvar; volts 0.985 to 1.010; busiest transformer 429%; export 718 kW is 218 kW over the 500 kW limit: the solar  |
| 446 | SITE SURVEY | generic site 319 | CONFIRMED | connection point -250 kW (plus is import), +391 kvar; volts 0.988 to 1.010; busiest transformer 169%; a transformer is at 169% of its rating |
| 447 | SITE SURVEY | generic site 320 | CONFIRMED | connection point -3529 kW (plus is import), +1403 kvar; volts 0.986 to 1.012; busiest transformer 243%; export 3529 kW is 3029 kW over the 500 kW limit: the sol |
| 448 | SITE SURVEY | generic site 321 | CONFIRMED | connection point -1044 kW (plus is import), +474 kvar; volts 0.990 to 1.004; busiest transformer 101%; export 1044 kW is 544 kW over the 500 kW limit: the solar |
| 449 | SITE SURVEY | generic site 322 | CONFIRMED | connection point -5275 kW (plus is import), +2394 kvar; volts 0.986 to 1.014; busiest transformer 439%; export 5275 kW is 4275 kW over the 1000 kW limit: the so |
| 450 | SITE SURVEY | generic site 323 | CONFIRMED | connection point -507 kW (plus is import), +938 kvar; volts 0.985 to 1.000; busiest transformer 97%; export 507 kW is 7 kW over the 500 kW limit: the solar must |
| 451 | SITE SURVEY | generic site 324 | CONFIRMED | connection point -409 kW (plus is import), +446 kvar; volts 0.990 to 1.004; busiest transformer 104%; export 409 kW is 359 kW over the 50 kW limit: the solar mu |
| 452 | SITE SURVEY | generic site 325 | CONFIRMED | connection point +73 kW (plus is import), +420 kvar; volts 0.988 to 1.002; busiest transformer 80%; inside every limit |
| 453 | SITE SURVEY | generic site 326 | CONFIRMED | connection point -58 kW (plus is import), +168 kvar; volts 0.996 to 1.000; busiest transformer 14%; inside every limit |
| 454 | SITE SURVEY | generic site 327 | CONFIRMED | connection point -1070 kW (plus is import), +631 kvar; volts 0.990 to 1.014; busiest transformer 232%; export 1070 kW is 1070 kW over the 0 kW limit: the solar  |
| 455 | SITE SURVEY | generic site 328 | CONFIRMED | connection point +267 kW (plus is import), +907 kvar; volts 0.983 to 1.000; busiest transformer 56%; inside every limit |
| 456 | SITE SURVEY | generic site 329 | CONFIRMED | connection point -1491 kW (plus is import), +1774 kvar; volts 0.982 to 1.000; busiest transformer 621%; export 1491 kW is 1491 kW over the 0 kW limit: the solar |
| 457 | SITE SURVEY | generic site 330 | CONFIRMED | connection point -2726 kW (plus is import), +1085 kvar; volts 0.989 to 1.014; busiest transformer 199%; export 2726 kW is 2676 kW over the 50 kW limit: the sola |
| 458 | SITE SURVEY | generic site 331 | CONFIRMED | connection point -4373 kW (plus is import), +3105 kvar; volts 0.975 to 1.000; busiest transformer 635%; export 4373 kW is 3373 kW over the 1000 kW limit: the so |
| 459 | SITE SURVEY | generic site 332 | CONFIRMED | connection point -1607 kW (plus is import), +539 kvar; volts 0.992 to 1.005; busiest transformer 110%; export 1607 kW is 607 kW over the 1000 kW limit: the sola |
| 460 | SITE SURVEY | generic site 333 | CONFIRMED | connection point -582 kW (plus is import), +502 kvar; volts 0.990 to 1.004; busiest transformer 84%; export 582 kW is 382 kW over the 200 kW limit: the solar mu |
| 461 | SITE SURVEY | generic site 334 | CONFIRMED | connection point +163 kW (plus is import), +284 kvar; volts 0.992 to 1.000; busiest transformer 15%; inside every limit |
| 462 | SITE SURVEY | generic site 335 | CONFIRMED | connection point -562 kW (plus is import), +190 kvar; volts 0.993 to 1.012; busiest transformer 156%; export 562 kW is 62 kW over the 500 kW limit: the solar mu |
| 463 | SITE SURVEY | generic site 336 | CONFIRMED | connection point -1300 kW (plus is import), +390 kvar; volts 0.992 to 1.002; busiest transformer 77%; export 1300 kW is 1300 kW over the 0 kW limit: the solar m |
| 464 | SITE SURVEY | generic site 337 | CONFIRMED | connection point -1703 kW (plus is import), +395 kvar; volts 0.993 to 1.005; busiest transformer 122%; export 1703 kW is 1503 kW over the 200 kW limit: the sola |
| 465 | SITE SURVEY | generic site 338 | CONFIRMED | connection point -56 kW (plus is import), +179 kvar; volts 0.996 to 1.000; busiest transformer 15%; inside every limit |
| 466 | SITE SURVEY | generic site 339 | CONFIRMED | connection point +71 kW (plus is import), +154 kvar; volts 0.990 to 1.000; busiest transformer 25%; inside every limit |
| 467 | SITE SURVEY | generic site 340 | CONFIRMED | connection point -1825 kW (plus is import), +717 kvar; volts 0.989 to 1.007; busiest transformer 137%; export 1825 kW is 1825 kW over the 0 kW limit: the solar  |
| 468 | SITE SURVEY | generic site 341 | CONFIRMED | connection point -1213 kW (plus is import), +745 kvar; volts 0.989 to 1.016; busiest transformer 388%; export 1213 kW is 1213 kW over the 0 kW limit: the solar  |
| 469 | SITE SURVEY | generic site 342 | CONFIRMED | connection point -1455 kW (plus is import), +335 kvar; volts 0.994 to 1.004; busiest transformer 101%; export 1455 kW is 455 kW over the 1000 kW limit: the sola |
| 470 | SITE SURVEY | generic site 343 | CONFIRMED | connection point -810 kW (plus is import), +419 kvar; volts 0.990 to 1.003; busiest transformer 81%; export 810 kW is 760 kW over the 50 kW limit: the solar mus |
| 471 | SITE SURVEY | generic site 344 | CONFIRMED | connection point -3714 kW (plus is import), +1820 kvar; volts 0.990 to 1.022; busiest transformer 343%; export 3714 kW is 3664 kW over the 50 kW limit: the sola |
| 472 | SITE SURVEY | generic site 345 | CONFIRMED | connection point -3811 kW (plus is import), +1995 kvar; volts 0.984 to 1.009; busiest transformer 517%; export 3811 kW is 3761 kW over the 50 kW limit: the sola |
| 473 | SITE SURVEY | generic site 346 | CONFIRMED | connection point -3810 kW (plus is import), +1088 kvar; volts 0.995 to 1.016; busiest transformer 229%; export 3810 kW is 3310 kW over the 500 kW limit: the sol |
| 474 | SITE SURVEY | generic site 347 | CONFIRMED | connection point -1372 kW (plus is import), +475 kvar; volts 0.992 to 1.009; busiest transformer 121%; export 1372 kW is 872 kW over the 500 kW limit: the solar |
| 475 | SITE SURVEY | generic site 348 | CONFIRMED | connection point -4787 kW (plus is import), +1873 kvar; volts 0.990 to 1.021; busiest transformer 319%; export 4787 kW is 4737 kW over the 50 kW limit: the sola |
| 476 | SITE SURVEY | generic site 349 | CONFIRMED | connection point -2068 kW (plus is import), +1927 kvar; volts 0.985 to 1.000; busiest transformer 692%; export 2068 kW is 1868 kW over the 200 kW limit: the sol |
| 477 | SITE SURVEY | generic site 350 | CONFIRMED | connection point -2181 kW (plus is import), +852 kvar; volts 0.988 to 1.014; busiest transformer 353%; export 2181 kW is 1681 kW over the 500 kW limit: the sola |
| 478 | SITE SURVEY | generic site 351 | CONFIRMED | connection point -449 kW (plus is import), +1134 kvar; volts 0.984 to 1.005; busiest transformer 209%; a transformer is at 209% of its rating |
| 479 | SITE SURVEY | generic site 352 | CONFIRMED | connection point -51 kW (plus is import), +219 kvar; volts 0.991 to 1.000; busiest transformer 22%; inside every limit |
| 480 | SITE SURVEY | generic site 353 | CONFIRMED | connection point -1088 kW (plus is import), +411 kvar; volts 0.993 to 1.016; busiest transformer 290%; export 1088 kW is 88 kW over the 1000 kW limit: the solar |
| 481 | SITE SURVEY | generic site 354 | CONFIRMED | connection point -955 kW (plus is import), +229 kvar; volts 0.993 to 1.011; busiest transformer 149%; export 955 kW is 755 kW over the 200 kW limit: the solar m |
| 482 | SITE SURVEY | generic site 355 | CONFIRMED | connection point -454 kW (plus is import), +131 kvar; volts 0.993 to 1.009; busiest transformer 120%; a transformer is at 120% of its rating |
| 483 | SITE SURVEY | generic site 356 | CONFIRMED | connection point -413 kW (plus is import), +700 kvar; volts 0.989 to 1.003; busiest transformer 142%; export 413 kW is 413 kW over the 0 kW limit: the solar mus |
| 484 | SITE SURVEY | generic site 357 | CONFIRMED | connection point +92 kW (plus is import), +246 kvar; volts 0.989 to 1.000; busiest transformer 31%; inside every limit |
| 485 | SITE SURVEY | generic site 358 | CONFIRMED | connection point -2249 kW (plus is import), +1169 kvar; volts 0.989 to 1.015; busiest transformer 408%; export 2249 kW is 1749 kW over the 500 kW limit: the sol |
| 486 | SITE SURVEY | generic site 359 | CONFIRMED | connection point +101 kW (plus is import), +260 kvar; volts 0.993 to 1.000; busiest transformer 14%; inside every limit |
| 487 | SITE SURVEY | generic site 360 | CONFIRMED | connection point -83 kW (plus is import), +173 kvar; volts 0.992 to 1.001; busiest transformer 44%; inside every limit |
| 488 | SITE SURVEY | generic site 361 | CONFIRMED | connection point -4480 kW (plus is import), +2933 kvar; volts 0.982 to 1.000; busiest transformer 633%; export 4480 kW is 4430 kW over the 50 kW limit: the sola |
| 489 | SITE SURVEY | generic site 362 | CONFIRMED | connection point -986 kW (plus is import), +1315 kvar; volts 0.985 to 1.011; busiest transformer 338%; export 986 kW is 986 kW over the 0 kW limit: the solar mu |
| 490 | SITE SURVEY | generic site 363 | CONFIRMED | connection point -1282 kW (plus is import), +798 kvar; volts 0.988 to 1.012; busiest transformer 230%; export 1282 kW is 782 kW over the 500 kW limit: the solar |
| 491 | SITE SURVEY | generic site 364 | CONFIRMED | connection point -1720 kW (plus is import), +1186 kvar; volts 0.985 to 1.013; busiest transformer 370%; export 1720 kW is 1720 kW over the 0 kW limit: the solar |
| 492 | SITE SURVEY | generic site 365 | CONFIRMED | connection point +279 kW (plus is import), +512 kvar; volts 0.986 to 1.000; busiest transformer 63%; inside every limit |
| 493 | SITE SURVEY | generic site 366 | CONFIRMED | connection point -812 kW (plus is import), +329 kvar; volts 0.995 to 1.002; busiest transformer 69%; export 812 kW is 812 kW over the 0 kW limit: the solar must |
| 494 | SITE SURVEY | generic site 367 | CONFIRMED | connection point +48 kW (plus is import), +305 kvar; volts 0.988 to 1.000; busiest transformer 26%; inside every limit |
| 495 | SITE SURVEY | generic site 368 | CONFIRMED | connection point -2615 kW (plus is import), +1800 kvar; volts 0.986 to 1.000; busiest transformer 719%; export 2615 kW is 2115 kW over the 500 kW limit: the sol |
| 496 | SITE SURVEY | generic site 369 | CONFIRMED | connection point -1324 kW (plus is import), +1564 kvar; volts 0.981 to 1.002; busiest transformer 567%; export 1324 kW is 1274 kW over the 50 kW limit: the sola |
| 497 | SITE SURVEY | generic site 370 | CONFIRMED | connection point -888 kW (plus is import), +241 kvar; volts 0.995 to 1.015; busiest transformer 218%; export 888 kW is 888 kW over the 0 kW limit: the solar mus |
| 498 | SITE SURVEY | generic site 371 | CONFIRMED | connection point -1746 kW (plus is import), +650 kvar; volts 0.988 to 1.013; busiest transformer 285%; export 1746 kW is 1696 kW over the 50 kW limit: the solar |
| 499 | SITE SURVEY | generic site 372 | CONFIRMED | connection point -247 kW (plus is import), +184 kvar; volts 0.993 to 1.001; busiest transformer 49%; inside every limit |
| 500 | SITE SURVEY | generic site 373 | CONFIRMED | connection point -200 kW (plus is import), +113 kvar; volts 0.991 to 1.001; busiest transformer 63%; inside every limit |
| 501 | SITE SURVEY | generic site 374 | CONFIRMED | connection point -2239 kW (plus is import), +1026 kvar; volts 0.992 to 1.020; busiest transformer 388%; export 2239 kW is 2039 kW over the 200 kW limit: the sol |
| 502 | SITE SURVEY | generic site 375 | CONFIRMED | connection point -500 kW (plus is import), +209 kvar; volts 0.993 to 1.005; busiest transformer 76%; export 500 kW is 450 kW over the 50 kW limit: the solar mus |
| 503 | SITE SURVEY | generic site 376 | CONFIRMED | connection point -2848 kW (plus is import), +2872 kvar; volts 0.944 to 1.000; busiest transformer 873%; export 2848 kW is 1848 kW over the 1000 kW limit: the so |
| 504 | SITE SURVEY | generic site 377 | CONFIRMED | connection point +62 kW (plus is import), +181 kvar; volts 0.993 to 1.000; busiest transformer 41%; inside every limit |
| 505 | SITE SURVEY | generic site 378 | CONFIRMED | connection point -1179 kW (plus is import), +289 kvar; volts 0.993 to 1.010; busiest transformer 139%; export 1179 kW is 1129 kW over the 50 kW limit: the solar |
| 506 | SITE SURVEY | generic site 379 | CONFIRMED | connection point -1704 kW (plus is import), +623 kvar; volts 0.992 to 1.018; busiest transformer 280%; export 1704 kW is 1504 kW over the 200 kW limit: the sola |
| 507 | SITE SURVEY | generic site 380 | CONFIRMED | connection point -416 kW (plus is import), +302 kvar; volts 0.991 to 1.004; busiest transformer 102%; export 416 kW is 216 kW over the 200 kW limit: the solar m |
| 508 | SITE SURVEY | generic site 381 | CONFIRMED | connection point -2350 kW (plus is import), +2309 kvar; volts 0.976 to 1.000; busiest transformer 774%; export 2350 kW is 2350 kW over the 0 kW limit: the solar |
| 509 | SITE SURVEY | generic site 382 | CONFIRMED | connection point -166 kW (plus is import), +83 kvar; volts 0.995 to 1.000; busiest transformer 24%; export 166 kW is 116 kW over the 50 kW limit: the solar must |
| 510 | SITE SURVEY | generic site 383 | CONFIRMED | connection point -1291 kW (plus is import), +700 kvar; volts 0.989 to 1.011; busiest transformer 212%; export 1291 kW is 791 kW over the 500 kW limit: the solar |
| 511 | SITE SURVEY | generic site 384 | CONFIRMED | connection point -2352 kW (plus is import), +1477 kvar; volts 0.986 to 1.011; busiest transformer 455%; export 2352 kW is 1852 kW over the 500 kW limit: the sol |
| 512 | SITE SURVEY | generic site 385 | CONFIRMED | connection point -1164 kW (plus is import), +263 kvar; volts 0.996 to 1.007; busiest transformer 88%; export 1164 kW is 1114 kW over the 50 kW limit: the solar  |
| 513 | SITE SURVEY | generic site 386 | CONFIRMED | connection point -2172 kW (plus is import), +1135 kvar; volts 0.992 to 1.013; busiest transformer 390%; export 2172 kW is 2172 kW over the 0 kW limit: the solar |
| 514 | SITE SURVEY | generic site 387 | CONFIRMED | connection point -1437 kW (plus is import), +351 kvar; volts 0.996 to 1.015; busiest transformer 177%; export 1437 kW is 437 kW over the 1000 kW limit: the sola |
| 515 | SITE SURVEY | generic site 388 | CONFIRMED | connection point -3846 kW (plus is import), +1941 kvar; volts 0.989 to 1.012; busiest transformer 511%; export 3846 kW is 3846 kW over the 0 kW limit: the solar |
| 516 | SITE SURVEY | generic site 389 | CONFIRMED | connection point -3029 kW (plus is import), +1370 kvar; volts 0.990 to 1.018; busiest transformer 408%; export 3029 kW is 2029 kW over the 1000 kW limit: the so |
| 517 | SITE SURVEY | generic site 390 | CONFIRMED | connection point +251 kW (plus is import), +539 kvar; volts 0.987 to 1.000; busiest transformer 32%; inside every limit |
| 518 | SITE SURVEY | generic site 391 | CONFIRMED | connection point -1847 kW (plus is import), +896 kvar; volts 0.991 to 1.018; busiest transformer 339%; export 1847 kW is 1647 kW over the 200 kW limit: the sola |
| 519 | SITE SURVEY | generic site 392 | CONFIRMED | connection point +224 kW (plus is import), +446 kvar; volts 0.990 to 1.000; busiest transformer 66%; inside every limit |
| 520 | SITE SURVEY | generic site 393 | CONFIRMED | connection point -891 kW (plus is import), +432 kvar; volts 0.993 to 1.015; busiest transformer 274%; a transformer is at 274% of its rating |
| 521 | SITE SURVEY | generic site 394 | CONFIRMED | connection point -1187 kW (plus is import), +496 kvar; volts 0.993 to 1.016; busiest transformer 325%; export 1187 kW is 1187 kW over the 0 kW limit: the solar  |
| 522 | SITE SURVEY | generic site 395 | CONFIRMED | connection point -2310 kW (plus is import), +557 kvar; volts 0.994 to 1.009; busiest transformer 132%; export 2310 kW is 2110 kW over the 200 kW limit: the sola |
| 523 | SITE SURVEY | generic site 396 | CONFIRMED | connection point -1038 kW (plus is import), +246 kvar; volts 0.994 to 1.011; busiest transformer 156%; export 1038 kW is 38 kW over the 1000 kW limit: the solar |
| 524 | SITE SURVEY | generic site 397 | CONFIRMED | connection point -203 kW (plus is import), +89 kvar; volts 0.995 to 1.001; busiest transformer 56%; inside every limit |
| 525 | SITE SURVEY | generic site 398 | CONFIRMED | connection point -482 kW (plus is import), +547 kvar; volts 0.990 to 1.007; busiest transformer 133%; export 482 kW is 282 kW over the 200 kW limit: the solar m |
| 526 | SITE SURVEY | generic site 399 | CONFIRMED | connection point -270 kW (plus is import), +124 kvar; volts 0.993 to 1.003; busiest transformer 54%; export 270 kW is 220 kW over the 50 kW limit: the solar mus |
| 527 | SITE SURVEY | generic site 400 | CONFIRMED | connection point -3388 kW (plus is import), +1105 kvar; volts 0.992 to 1.019; busiest transformer 223%; export 3388 kW is 2888 kW over the 500 kW limit: the sol |
| 528 | SITE SURVEY | generic site 401 | CONFIRMED | connection point -778 kW (plus is import), +722 kvar; volts 0.988 to 1.014; busiest transformer 329%; export 778 kW is 278 kW over the 500 kW limit: the solar m |
| 529 | SITE SURVEY | generic site 402 | CONFIRMED | connection point -2938 kW (plus is import), +1367 kvar; volts 0.991 to 1.014; busiest transformer 275%; export 2938 kW is 1938 kW over the 1000 kW limit: the so |
| 530 | SITE SURVEY | generic site 403 | CONFIRMED | connection point -205 kW (plus is import), +336 kvar; volts 0.989 to 1.000; busiest transformer 31%; export 205 kW is 5 kW over the 200 kW limit: the solar must |
| 531 | SITE SURVEY | generic site 404 | CONFIRMED | connection point -1051 kW (plus is import), +315 kvar; volts 0.995 to 1.001; busiest transformer 79%; export 1051 kW is 551 kW over the 500 kW limit: the solar  |
| 532 | SITE SURVEY | generic site 405 | CONFIRMED | connection point -194 kW (plus is import), +151 kvar; volts 0.991 to 1.000; busiest transformer 39%; inside every limit |
| 533 | SITE SURVEY | generic site 406 | CONFIRMED | connection point -1196 kW (plus is import), +605 kvar; volts 0.992 to 1.013; busiest transformer 232%; export 1196 kW is 1196 kW over the 0 kW limit: the solar  |
| 534 | SITE SURVEY | generic site 407 | CONFIRMED | connection point -380 kW (plus is import), +740 kvar; volts 0.987 to 1.000; busiest transformer 74%; export 380 kW is 330 kW over the 50 kW limit: the solar mus |
| 535 | SITE SURVEY | generic site 408 | CONFIRMED | connection point -2492 kW (plus is import), +1116 kvar; volts 0.987 to 1.009; busiest transformer 187%; export 2492 kW is 1992 kW over the 500 kW limit: the sol |
| 536 | SITE SURVEY | generic site 409 | CONFIRMED | connection point -1859 kW (plus is import), +1108 kvar; volts 0.989 to 1.010; busiest transformer 168%; export 1859 kW is 859 kW over the 1000 kW limit: the sol |
| 537 | SITE SURVEY | generic site 410 | CONFIRMED | connection point -32 kW (plus is import), +176 kvar; volts 0.992 to 1.000; busiest transformer 30%; inside every limit |
| 538 | SITE SURVEY | generic site 411 | CONFIRMED | connection point -1113 kW (plus is import), +448 kvar; volts 0.991 to 1.016; busiest transformer 303%; export 1113 kW is 113 kW over the 1000 kW limit: the sola |
| 539 | SITE SURVEY | generic site 412 | CONFIRMED | connection point -1118 kW (plus is import), +321 kvar; volts 0.997 to 1.013; busiest transformer 178%; export 1118 kW is 918 kW over the 200 kW limit: the solar |
| 540 | SITE SURVEY | generic site 413 | CONFIRMED | connection point -3800 kW (plus is import), +2300 kvar; volts 0.983 to 1.003; busiest transformer 539%; export 3800 kW is 3600 kW over the 200 kW limit: the sol |
| 541 | SITE SURVEY | generic site 414 | CONFIRMED | connection point -168 kW (plus is import), +429 kvar; volts 0.989 to 1.000; busiest transformer 78%; inside every limit |
| 542 | SITE SURVEY | generic site 415 | CONFIRMED | connection point -618 kW (plus is import), +989 kvar; volts 0.985 to 1.011; busiest transformer 376%; export 618 kW is 118 kW over the 500 kW limit: the solar m |
| 543 | SITE SURVEY | generic site 416 | CONFIRMED | connection point -1406 kW (plus is import), +482 kvar; volts 0.992 to 1.008; busiest transformer 98%; export 1406 kW is 1356 kW over the 50 kW limit: the solar  |
| 544 | SITE SURVEY | generic site 417 | CONFIRMED | connection point -393 kW (plus is import), +343 kvar; volts 0.993 to 1.007; busiest transformer 170%; export 393 kW is 393 kW over the 0 kW limit: the solar mus |
| 545 | SITE SURVEY | generic site 418 | CONFIRMED | connection point +176 kW (plus is import), +272 kvar; volts 0.991 to 1.000; busiest transformer 28%; inside every limit |
| 546 | SITE SURVEY | generic site 419 | CONFIRMED | connection point +274 kW (plus is import), +453 kvar; volts 0.987 to 1.000; busiest transformer 25%; inside every limit |
| 547 | SITE SURVEY | generic site 420 | CONFIRMED | connection point -325 kW (plus is import), +100 kvar; volts 0.995 to 1.006; busiest transformer 90%; inside every limit |
| 548 | SITE SURVEY | generic site 421 | CONFIRMED | connection point -3691 kW (plus is import), +2160 kvar; volts 0.980 to 1.005; busiest transformer 360%; export 3691 kW is 3491 kW over the 200 kW limit: the sol |
| 549 | SITE SURVEY | generic site 422 | CONFIRMED | connection point -815 kW (plus is import), +551 kvar; volts 0.992 to 1.013; busiest transformer 291%; export 815 kW is 315 kW over the 500 kW limit: the solar m |
| 550 | SITE SURVEY | generic site 423 | CONFIRMED | connection point -3525 kW (plus is import), +2120 kvar; volts 0.986 to 1.005; busiest transformer 605%; export 3525 kW is 3525 kW over the 0 kW limit: the solar |
| 551 | SITE SURVEY | generic site 424 | CONFIRMED | connection point -703 kW (plus is import), +601 kvar; volts 0.988 to 1.010; busiest transformer 193%; export 703 kW is 203 kW over the 500 kW limit: the solar m |
| 552 | SITE SURVEY | generic site 425 | CONFIRMED | connection point -2458 kW (plus is import), +3385 kvar; volts 0.930 to 1.000; busiest transformer 910%; export 2458 kW is 1958 kW over the 500 kW limit: the sol |
| 553 | SITE SURVEY | generic site 426 | CONFIRMED | connection point -1864 kW (plus is import), +731 kvar; volts 0.993 to 1.014; busiest transformer 306%; export 1864 kW is 864 kW over the 1000 kW limit: the sola |
| 554 | SITE SURVEY | generic site 427 | CONFIRMED | connection point -959 kW (plus is import), +512 kvar; volts 0.990 to 1.015; busiest transformer 302%; export 959 kW is 759 kW over the 200 kW limit: the solar m |
| 555 | SITE SURVEY | generic site 428 | CONFIRMED | connection point -607 kW (plus is import), +624 kvar; volts 0.987 to 1.013; busiest transformer 284%; a transformer is at 284% of its rating |
| 556 | SITE SURVEY | generic site 429 | CONFIRMED | connection point -249 kW (plus is import), +550 kvar; volts 0.988 to 1.002; busiest transformer 108%; export 249 kW is 199 kW over the 50 kW limit: the solar mu |
| 557 | SITE SURVEY | generic site 430 | CONFIRMED | connection point -2623 kW (plus is import), +1051 kvar; volts 0.988 to 1.014; busiest transformer 348%; export 2623 kW is 2423 kW over the 200 kW limit: the sol |
| 558 | SITE SURVEY | generic site 431 | CONFIRMED | connection point -708 kW (plus is import), +437 kvar; volts 0.989 to 1.011; busiest transformer 244%; export 708 kW is 708 kW over the 0 kW limit: the solar mus |
| 559 | SITE SURVEY | generic site 432 | CONFIRMED | connection point -1024 kW (plus is import), +658 kvar; volts 0.991 to 1.008; busiest transformer 122%; export 1024 kW is 974 kW over the 50 kW limit: the solar  |
| 560 | SITE SURVEY | generic site 433 | CONFIRMED | connection point -46 kW (plus is import), +223 kvar; volts 0.990 to 1.000; busiest transformer 25%; export 46 kW is 46 kW over the 0 kW limit: the solar must be |
| 561 | SITE SURVEY | generic site 434 | CONFIRMED | connection point -852 kW (plus is import), +400 kvar; volts 0.993 to 1.012; busiest transformer 252%; export 852 kW is 852 kW over the 0 kW limit: the solar mus |
| 562 | SITE SURVEY | generic site 435 | CONFIRMED | connection point -1795 kW (plus is import), +1029 kvar; volts 0.989 to 1.014; busiest transformer 352%; export 1795 kW is 795 kW over the 1000 kW limit: the sol |
| 563 | SITE SURVEY | generic site 436 | CONFIRMED | connection point -936 kW (plus is import), +693 kvar; volts 0.989 to 1.017; busiest transformer 346%; export 936 kW is 436 kW over the 500 kW limit: the solar m |
| 564 | SITE SURVEY | generic site 437 | CONFIRMED | connection point -2623 kW (plus is import), +1307 kvar; volts 0.986 to 1.008; busiest transformer 373%; export 2623 kW is 1623 kW over the 1000 kW limit: the so |
| 565 | SITE SURVEY | generic site 438 | CONFIRMED | connection point -956 kW (plus is import), +309 kvar; volts 0.993 to 1.002; busiest transformer 60%; export 956 kW is 906 kW over the 50 kW limit: the solar mus |
| 566 | SITE SURVEY | generic site 439 | CONFIRMED | connection point -3147 kW (plus is import), +1080 kvar; volts 0.993 to 1.016; busiest transformer 251%; export 3147 kW is 3147 kW over the 0 kW limit: the solar |
| 567 | SITE SURVEY | generic site 440 | CONFIRMED | connection point -462 kW (plus is import), +127 kvar; volts 0.996 to 1.006; busiest transformer 112%; a transformer is at 112% of its rating |
| 568 | SITE SURVEY | generic site 441 | CONFIRMED | connection point -1211 kW (plus is import), +499 kvar; volts 0.991 to 1.006; busiest transformer 109%; export 1211 kW is 211 kW over the 1000 kW limit: the sola |
| 569 | SITE SURVEY | generic site 442 | CONFIRMED | connection point -3860 kW (plus is import), +1424 kvar; volts 0.993 to 1.024; busiest transformer 318%; export 3860 kW is 3360 kW over the 500 kW limit: the sol |
| 570 | SITE SURVEY | generic site 443 | CONFIRMED | connection point -77 kW (plus is import), +742 kvar; volts 0.986 to 1.007; busiest transformer 163%; a transformer is at 163% of its rating |
| 571 | SITE SURVEY | generic site 444 | CONFIRMED | connection point +178 kW (plus is import), +419 kvar; volts 0.989 to 1.000; busiest transformer 56%; inside every limit |
| 572 | SITE SURVEY | generic site 445 | CONFIRMED | connection point -1518 kW (plus is import), +886 kvar; volts 0.990 to 1.015; busiest transformer 258%; export 1518 kW is 1018 kW over the 500 kW limit: the sola |
| 573 | SITE SURVEY | generic site 446 | CONFIRMED | connection point -1520 kW (plus is import), +1950 kvar; volts 0.980 to 1.000; busiest transformer 651%; export 1520 kW is 1470 kW over the 50 kW limit: the sola |
| 574 | SITE SURVEY | generic site 447 | CONFIRMED | connection point -22 kW (plus is import), +332 kvar; volts 0.990 to 1.003; busiest transformer 108%; a transformer is at 108% of its rating |
| 575 | SITE SURVEY | generic site 448 | CONFIRMED | connection point -2334 kW (plus is import), +606 kvar; volts 0.991 to 1.013; busiest transformer 147%; export 2334 kW is 2134 kW over the 200 kW limit: the sola |
| 576 | SITE SURVEY | generic site 449 | CONFIRMED | connection point -352 kW (plus is import), +298 kvar; volts 0.992 to 1.006; busiest transformer 99%; inside every limit |
| 577 | SITE SURVEY | generic site 450 | CONFIRMED | connection point -345 kW (plus is import), +243 kvar; volts 0.994 to 1.000; busiest transformer 31%; export 345 kW is 345 kW over the 0 kW limit: the solar must |
| 578 | SITE SURVEY | generic site 451 | CONFIRMED | connection point -1069 kW (plus is import), +192 kvar; volts 0.992 to 1.005; busiest transformer 60%; export 1069 kW is 1019 kW over the 50 kW limit: the solar  |
| 579 | SITE SURVEY | generic site 452 | CONFIRMED | connection point -745 kW (plus is import), +594 kvar; volts 0.990 to 1.008; busiest transformer 186%; export 745 kW is 245 kW over the 500 kW limit: the solar m |
| 580 | SITE SURVEY | generic site 453 | CONFIRMED | connection point -3511 kW (plus is import), +1039 kvar; volts 0.989 to 1.012; busiest transformer 262%; export 3511 kW is 3011 kW over the 500 kW limit: the sol |
| 581 | SITE SURVEY | generic site 454 | CONFIRMED | connection point -3096 kW (plus is import), +1245 kvar; volts 0.994 to 1.018; busiest transformer 395%; export 3096 kW is 3096 kW over the 0 kW limit: the solar |
| 582 | SITE SURVEY | generic site 455 | CONFIRMED | connection point -1380 kW (plus is import), +981 kvar; volts 0.988 to 1.011; busiest transformer 458%; export 1380 kW is 380 kW over the 1000 kW limit: the sola |
| 583 | SITE SURVEY | generic site 456 | CONFIRMED | connection point +71 kW (plus is import), +1025 kvar; volts 0.983 to 1.008; busiest transformer 300%; a transformer is at 300% of its rating |
| 584 | SITE SURVEY | generic site 457 | CONFIRMED | connection point -3019 kW (plus is import), +2207 kvar; volts 0.985 to 1.002; busiest transformer 585%; export 3019 kW is 2019 kW over the 1000 kW limit: the so |
| 585 | SITE SURVEY | generic site 458 | CONFIRMED | connection point -1672 kW (plus is import), +463 kvar; volts 0.994 to 1.014; busiest transformer 205%; export 1672 kW is 672 kW over the 1000 kW limit: the sola |
| 586 | SITE SURVEY | generic site 459 | CONFIRMED | connection point -3407 kW (plus is import), +2036 kvar; volts 0.988 to 1.009; busiest transformer 594%; export 3407 kW is 2407 kW over the 1000 kW limit: the so |
| 587 | SITE SURVEY | generic site 460 | CONFIRMED | connection point -2106 kW (plus is import), +1081 kvar; volts 0.986 to 1.016; busiest transformer 322%; export 2106 kW is 2106 kW over the 0 kW limit: the solar |
| 588 | SITE SURVEY | generic site 461 | CONFIRMED | connection point -4300 kW (plus is import), +2611 kvar; volts 0.985 to 1.005; busiest transformer 595%; export 4300 kW is 4100 kW over the 200 kW limit: the sol |
| 589 | SITE SURVEY | generic site 462 | CONFIRMED | connection point +72 kW (plus is import), +411 kvar; volts 0.988 to 1.000; busiest transformer 26%; inside every limit |
| 590 | SITE SURVEY | generic site 463 | CONFIRMED | connection point -1638 kW (plus is import), +485 kvar; volts 0.993 to 1.009; busiest transformer 106%; export 1638 kW is 1138 kW over the 500 kW limit: the sola |
| 591 | SITE SURVEY | generic site 464 | CONFIRMED | connection point +74 kW (plus is import), +314 kvar; volts 0.989 to 1.002; busiest transformer 90%; inside every limit |
| 592 | SITE SURVEY | generic site 465 | CONFIRMED | connection point -502 kW (plus is import), +165 kvar; volts 0.995 to 1.006; busiest transformer 86%; export 502 kW is 452 kW over the 50 kW limit: the solar mus |
| 593 | SITE SURVEY | generic site 466 | CONFIRMED | connection point -335 kW (plus is import), +130 kvar; volts 0.996 to 1.000; busiest transformer 51%; export 335 kW is 135 kW over the 200 kW limit: the solar mu |
| 594 | SITE SURVEY | generic site 467 | CONFIRMED | connection point -1378 kW (plus is import), +430 kvar; volts 0.992 to 1.010; busiest transformer 180%; export 1378 kW is 1378 kW over the 0 kW limit: the solar  |
| 595 | SITE SURVEY | generic site 468 | CONFIRMED | connection point -116 kW (plus is import), +301 kvar; volts 0.991 to 1.000; busiest transformer 35%; export 116 kW is 66 kW over the 50 kW limit: the solar must |
| 596 | SITE SURVEY | generic site 469 | CONFIRMED | connection point -927 kW (plus is import), +435 kvar; volts 0.992 to 1.012; busiest transformer 151%; export 927 kW is 427 kW over the 500 kW limit: the solar m |
| 597 | SITE SURVEY | generic site 470 | CONFIRMED | connection point -1487 kW (plus is import), +289 kvar; volts 0.995 to 1.005; busiest transformer 101%; export 1487 kW is 1487 kW over the 0 kW limit: the solar  |
| 598 | SITE SURVEY | generic site 471 | CONFIRMED | connection point -3342 kW (plus is import), +1712 kvar; volts 0.987 to 1.013; busiest transformer 463%; export 3342 kW is 3292 kW over the 50 kW limit: the sola |
| 599 | SITE SURVEY | generic site 472 | CONFIRMED | connection point -383 kW (plus is import), +187 kvar; volts 0.995 to 1.000; busiest transformer 68%; export 383 kW is 183 kW over the 200 kW limit: the solar mu |
| 600 | SITE SURVEY | generic site 473 | CONFIRMED | connection point -1228 kW (plus is import), +392 kvar; volts 0.991 to 1.011; busiest transformer 195%; export 1228 kW is 228 kW over the 1000 kW limit: the sola |
| 601 | SITE SURVEY | generic site 474 | CONFIRMED | connection point -138 kW (plus is import), +163 kvar; volts 0.990 to 1.003; busiest transformer 74%; export 138 kW is 138 kW over the 0 kW limit: the solar must |
| 602 | SITE SURVEY | generic site 475 | CONFIRMED | connection point -523 kW (plus is import), +292 kvar; volts 0.992 to 1.009; busiest transformer 174%; export 523 kW is 523 kW over the 0 kW limit: the solar mus |
| 603 | SITE SURVEY | generic site 476 | CONFIRMED | connection point -1271 kW (plus is import), +764 kvar; volts 0.989 to 1.006; busiest transformer 137%; export 1271 kW is 1271 kW over the 0 kW limit: the solar  |
| 604 | SITE SURVEY | generic site 477 | CONFIRMED | connection point -2144 kW (plus is import), +1083 kvar; volts 0.988 to 1.014; busiest transformer 389%; export 2144 kW is 1644 kW over the 500 kW limit: the sol |
| 605 | SITE SURVEY | generic site 478 | CONFIRMED | connection point -1578 kW (plus is import), +682 kvar; volts 0.991 to 1.012; busiest transformer 150%; export 1578 kW is 578 kW over the 1000 kW limit: the sola |
| 606 | SITE SURVEY | generic site 479 | CONFIRMED | connection point -5288 kW (plus is import), +2419 kvar; volts 0.987 to 1.015; busiest transformer 438%; export 5288 kW is 4288 kW over the 1000 kW limit: the so |
| 607 | SITE SURVEY | generic site 480 | CONFIRMED | connection point -3399 kW (plus is import), +950 kvar; volts 0.988 to 1.009; busiest transformer 205%; export 3399 kW is 3399 kW over the 0 kW limit: the solar  |
| 608 | SITE SURVEY | generic site 481 | CONFIRMED | connection point -912 kW (plus is import), +946 kvar; volts 0.986 to 1.013; busiest transformer 274%; export 912 kW is 912 kW over the 0 kW limit: the solar mus |
| 609 | SITE SURVEY | generic site 482 | CONFIRMED | connection point -4786 kW (plus is import), +1695 kvar; volts 0.991 to 1.023; busiest transformer 309%; export 4786 kW is 4286 kW over the 500 kW limit: the sol |
| 610 | SITE SURVEY | generic site 483 | CONFIRMED | connection point -124 kW (plus is import), +385 kvar; volts 0.991 to 1.005; busiest transformer 141%; export 124 kW is 124 kW over the 0 kW limit: the solar mus |
| 611 | SITE SURVEY | generic site 484 | CONFIRMED | connection point -2656 kW (plus is import), +1354 kvar; volts 0.992 to 1.014; busiest transformer 459%; export 2656 kW is 2156 kW over the 500 kW limit: the sol |
| 612 | SITE SURVEY | generic site 485 | CONFIRMED | connection point -222 kW (plus is import), +397 kvar; volts 0.989 to 1.002; busiest transformer 99%; inside every limit |
| 613 | SITE SURVEY | generic site 486 | CONFIRMED | connection point -432 kW (plus is import), +230 kvar; volts 0.995 to 1.004; busiest transformer 90%; inside every limit |
| 614 | SITE SURVEY | generic site 487 | CONFIRMED | connection point +24 kW (plus is import), +552 kvar; volts 0.990 to 1.000; busiest transformer 40%; inside every limit |
| 615 | SITE SURVEY | generic site 488 | CONFIRMED | connection point +16 kW (plus is import), +375 kvar; volts 0.989 to 1.000; busiest transformer 22%; inside every limit |
| 616 | SITE SURVEY | generic site 489 | CONFIRMED | connection point -419 kW (plus is import), +344 kvar; volts 0.992 to 1.000; busiest transformer 40%; export 419 kW is 219 kW over the 200 kW limit: the solar mu |
| 617 | SITE SURVEY | generic site 490 | CONFIRMED | connection point -1026 kW (plus is import), +749 kvar; volts 0.989 to 1.010; busiest transformer 200%; export 1026 kW is 26 kW over the 1000 kW limit: the solar |
| 618 | SITE SURVEY | generic site 491 | REFUTED | connection point -3605 kW (plus is import), +7723 kvar; volts 0.789 to 1.000; busiest transformer 1435%; export 3605 kW is 3105 kW over the 500 kW limit: the so |
| 619 | SITE SURVEY | generic site 492 | CONFIRMED | connection point -3421 kW (plus is import), +1225 kvar; volts 0.988 to 1.013; busiest transformer 226%; export 3421 kW is 3421 kW over the 0 kW limit: the solar |
| 620 | SITE SURVEY | generic site 493 | CONFIRMED | connection point -256 kW (plus is import), +562 kvar; volts 0.989 to 1.009; busiest transformer 216%; a transformer is at 216% of its rating |
| 621 | SITE SURVEY | generic site 494 | CONFIRMED | connection point -4203 kW (plus is import), +1558 kvar; volts 0.987 to 1.015; busiest transformer 279%; export 4203 kW is 3203 kW over the 1000 kW limit: the so |
| 622 | SITE SURVEY | generic site 495 | CONFIRMED | connection point -4311 kW (plus is import), +3092 kvar; volts 0.979 to 1.000; busiest transformer 641%; export 4311 kW is 3311 kW over the 1000 kW limit: the so |
| 623 | SITE SURVEY | generic site 496 | CONFIRMED | connection point -2897 kW (plus is import), +1394 kvar; volts 0.988 to 1.015; busiest transformer 403%; export 2897 kW is 1897 kW over the 1000 kW limit: the so |
| 624 | SITE SURVEY | generic site 497 | CONFIRMED | connection point -2929 kW (plus is import), +757 kvar; volts 0.997 to 1.017; busiest transformer 173%; export 2929 kW is 2429 kW over the 500 kW limit: the sola |
| 625 | SITE SURVEY | generic site 498 | CONFIRMED | connection point -1710 kW (plus is import), +878 kvar; volts 0.989 to 1.009; busiest transformer 174%; export 1710 kW is 1710 kW over the 0 kW limit: the solar  |
| 626 | SITE SURVEY | generic site 499 | CONFIRMED | connection point -1207 kW (plus is import), +282 kvar; volts 0.992 to 1.004; busiest transformer 69%; export 1207 kW is 1007 kW over the 200 kW limit: the solar |
| 627 | SITE SURVEY | generic site 500 | CONFIRMED | connection point -1788 kW (plus is import), +1560 kvar; volts 0.984 to 1.011; busiest transformer 427%; export 1788 kW is 1738 kW over the 50 kW limit: the sola |
| 628 | SITE SURVEY | generic site 501 | CONFIRMED | connection point -302 kW (plus is import), +550 kvar; volts 0.990 to 1.005; busiest transformer 116%; export 302 kW is 252 kW over the 50 kW limit: the solar mu |
| 629 | SITE SURVEY | generic site 502 | CONFIRMED | connection point -52 kW (plus is import), +455 kvar; volts 0.988 to 1.000; busiest transformer 37%; export 52 kW is 52 kW over the 0 kW limit: the solar must be |
| 630 | SITE SURVEY | generic site 503 | CONFIRMED | connection point -443 kW (plus is import), +197 kvar; volts 0.994 to 1.006; busiest transformer 132%; a transformer is at 132% of its rating |
| 631 | SITE SURVEY | generic site 504 | CONFIRMED | connection point -3689 kW (plus is import), +1068 kvar; volts 0.991 to 1.013; busiest transformer 227%; export 3689 kW is 3639 kW over the 50 kW limit: the sola |
| 632 | SITE SURVEY | generic site 505 | CONFIRMED | connection point -1416 kW (plus is import), +348 kvar; volts 0.992 to 1.009; busiest transformer 109%; export 1416 kW is 416 kW over the 1000 kW limit: the sola |
| 633 | SITE SURVEY | generic site 506 | CONFIRMED | connection point -247 kW (plus is import), +843 kvar; volts 0.986 to 1.003; busiest transformer 102%; a transformer is at 102% of its rating |
| 634 | SITE SURVEY | generic site 507 | CONFIRMED | connection point -1516 kW (plus is import), +839 kvar; volts 0.991 to 1.014; busiest transformer 442%; export 1516 kW is 1316 kW over the 200 kW limit: the sola |
| 635 | SITE SURVEY | generic site 508 | CONFIRMED | connection point -3777 kW (plus is import), +1501 kvar; volts 0.987 to 1.011; busiest transformer 315%; export 3777 kW is 3727 kW over the 50 kW limit: the sola |
| 636 | SITE SURVEY | generic site 509 | CONFIRMED | connection point -2592 kW (plus is import), +1228 kvar; volts 0.991 to 1.015; busiest transformer 439%; export 2592 kW is 1592 kW over the 1000 kW limit: the so |
| 637 | SITE SURVEY | generic site 510 | REFUTED | connection point -3667 kW (plus is import), +4225 kvar; volts 0.969 to 1.000; busiest transformer 1239%; export 3667 kW is 3667 kW over the 0 kW limit: the sola |
| 638 | SITE SURVEY | generic site 511 | CONFIRMED | connection point -1049 kW (plus is import), +202 kvar; volts 0.994 to 1.006; busiest transformer 76%; export 1049 kW is 1049 kW over the 0 kW limit: the solar m |
| 639 | SITE SURVEY | generic site 512 | CONFIRMED | connection point -695 kW (plus is import), +229 kvar; volts 0.996 to 1.002; busiest transformer 87%; export 695 kW is 695 kW over the 0 kW limit: the solar must |
| 640 | SITE SURVEY | generic site 513 | CONFIRMED | connection point -1290 kW (plus is import), +344 kvar; volts 0.992 to 1.013; busiest transformer 200%; export 1290 kW is 1090 kW over the 200 kW limit: the sola |
| 641 | SITE SURVEY | generic site 514 | CONFIRMED | connection point -578 kW (plus is import), +351 kvar; volts 0.993 to 1.002; busiest transformer 63%; export 578 kW is 578 kW over the 0 kW limit: the solar must |
| 642 | SITE SURVEY | generic site 515 | CONFIRMED | connection point -667 kW (plus is import), +371 kvar; volts 0.990 to 1.010; busiest transformer 217%; export 667 kW is 167 kW over the 500 kW limit: the solar m |
| 643 | SITE SURVEY | generic site 516 | CONFIRMED | connection point -1162 kW (plus is import), +1569 kvar; volts 0.983 to 1.001; busiest transformer 550%; export 1162 kW is 662 kW over the 500 kW limit: the sola |
| 644 | SITE SURVEY | generic site 517 | CONFIRMED | connection point -1608 kW (plus is import), +2886 kvar; volts 0.963 to 1.000; busiest transformer 798%; export 1608 kW is 608 kW over the 1000 kW limit: the sol |
| 645 | SITE SURVEY | generic site 518 | CONFIRMED | connection point -3863 kW (plus is import), +1450 kvar; volts 0.991 to 1.018; busiest transformer 313%; export 3863 kW is 3663 kW over the 200 kW limit: the sol |
| 646 | SITE SURVEY | generic site 519 | CONFIRMED | connection point -35 kW (plus is import), +352 kvar; volts 0.991 to 1.000; busiest transformer 38%; inside every limit |
| 647 | SITE SURVEY | generic site 520 | CONFIRMED | connection point -96 kW (plus is import), +118 kvar; volts 0.991 to 1.000; busiest transformer 27%; inside every limit |
| 648 | SITE SURVEY | generic site 521 | CONFIRMED | connection point -270 kW (plus is import), +157 kvar; volts 0.992 to 1.003; busiest transformer 89%; export 270 kW is 70 kW over the 200 kW limit: the solar mus |
| 649 | SITE SURVEY | generic site 522 | CONFIRMED | connection point -1269 kW (plus is import), +451 kvar; volts 0.993 to 1.015; busiest transformer 215%; export 1269 kW is 269 kW over the 1000 kW limit: the sola |
| 650 | SITE SURVEY | generic site 523 | CONFIRMED | connection point -2315 kW (plus is import), +1798 kvar; volts 0.984 to 1.009; busiest transformer 411%; export 2315 kW is 2315 kW over the 0 kW limit: the solar |
| 651 | SITE SURVEY | generic site 524 | CONFIRMED | connection point -1101 kW (plus is import), +302 kvar; volts 0.990 to 1.008; busiest transformer 166%; export 1101 kW is 1051 kW over the 50 kW limit: the solar |
| 652 | SITE SURVEY | generic site 525 | CONFIRMED | connection point -152 kW (plus is import), +1221 kvar; volts 0.982 to 1.006; busiest transformer 247%; a transformer is at 247% of its rating |
| 653 | SITE SURVEY | generic site 526 | CONFIRMED | connection point -890 kW (plus is import), +256 kvar; volts 0.992 to 1.004; busiest transformer 69%; export 890 kW is 890 kW over the 0 kW limit: the solar must |
| 654 | SITE SURVEY | generic site 527 | CONFIRMED | connection point -476 kW (plus is import), +623 kvar; volts 0.989 to 1.004; busiest transformer 135%; export 476 kW is 476 kW over the 0 kW limit: the solar mus |
| 655 | SITE SURVEY | generic site 528 | CONFIRMED | connection point +343 kW (plus is import), +633 kvar; volts 0.986 to 1.004; busiest transformer 150%; a transformer is at 150% of its rating |
| 656 | SITE SURVEY | generic site 529 | CONFIRMED | connection point -5070 kW (plus is import), +2201 kvar; volts 0.988 to 1.017; busiest transformer 417%; export 5070 kW is 4570 kW over the 500 kW limit: the sol |
| 657 | SITE SURVEY | generic site 530 | CONFIRMED | connection point +148 kW (plus is import), +330 kvar; volts 0.990 to 1.000; busiest transformer 79%; inside every limit |
| 658 | SITE SURVEY | generic site 531 | CONFIRMED | connection point -2007 kW (plus is import), +941 kvar; volts 0.990 to 1.017; busiest transformer 294%; export 2007 kW is 1807 kW over the 200 kW limit: the sola |
| 659 | SITE SURVEY | generic site 532 | CONFIRMED | connection point -961 kW (plus is import), +297 kvar; volts 0.995 to 1.007; busiest transformer 123%; export 961 kW is 761 kW over the 200 kW limit: the solar m |
| 660 | SITE SURVEY | generic site 533 | CONFIRMED | connection point -2361 kW (plus is import), +1283 kvar; volts 0.985 to 1.013; busiest transformer 360%; export 2361 kW is 1361 kW over the 1000 kW limit: the so |
| 661 | SITE SURVEY | generic site 534 | CONFIRMED | connection point +177 kW (plus is import), +334 kvar; volts 0.992 to 1.000; busiest transformer 16%; inside every limit |
| 662 | SITE SURVEY | generic site 535 | CONFIRMED | connection point -1483 kW (plus is import), +638 kvar; volts 0.993 to 1.013; busiest transformer 390%; export 1483 kW is 983 kW over the 500 kW limit: the solar |
| 663 | SITE SURVEY | generic site 536 | CONFIRMED | connection point -3205 kW (plus is import), +4123 kvar; volts 0.878 to 1.000; busiest transformer 1005%; export 3205 kW is 3005 kW over the 200 kW limit: the so |
| 664 | SITE SURVEY | generic site 537 | CONFIRMED | connection point -3968 kW (plus is import), +2410 kvar; volts 0.984 to 1.008; busiest transformer 565%; export 3968 kW is 3968 kW over the 0 kW limit: the solar |
| 665 | SITE SURVEY | generic site 538 | CONFIRMED | connection point -640 kW (plus is import), +254 kvar; volts 0.991 to 1.007; busiest transformer 118%; a transformer is at 118% of its rating |
| 666 | SITE SURVEY | generic site 539 | CONFIRMED | connection point -135 kW (plus is import), +251 kvar; volts 0.990 to 1.000; busiest transformer 58%; export 135 kW is 135 kW over the 0 kW limit: the solar must |
| 667 | SITE SURVEY | generic site 540 | CONFIRMED | connection point -2306 kW (plus is import), +1876 kvar; volts 0.980 to 1.000; busiest transformer 706%; export 2306 kW is 1306 kW over the 1000 kW limit: the so |
| 668 | SITE SURVEY | generic site 541 | CONFIRMED | connection point -1172 kW (plus is import), +393 kvar; volts 0.992 to 1.010; busiest transformer 190%; export 1172 kW is 1172 kW over the 0 kW limit: the solar  |
| 669 | SITE SURVEY | generic site 542 | CONFIRMED | connection point -2404 kW (plus is import), +565 kvar; volts 0.994 to 1.014; busiest transformer 149%; export 2404 kW is 1904 kW over the 500 kW limit: the sola |
| 670 | SITE SURVEY | generic site 543 | CONFIRMED | connection point -4190 kW (plus is import), +1839 kvar; volts 0.988 to 1.015; busiest transformer 359%; export 4190 kW is 4140 kW over the 50 kW limit: the sola |
| 671 | SITE SURVEY | generic site 544 | CONFIRMED | connection point -2934 kW (plus is import), +2661 kvar; volts 0.953 to 1.000; busiest transformer 856%; export 2934 kW is 2734 kW over the 200 kW limit: the sol |
| 672 | SITE SURVEY | generic site 545 | CONFIRMED | connection point -746 kW (plus is import), +216 kvar; volts 0.995 to 1.012; busiest transformer 191%; export 746 kW is 746 kW over the 0 kW limit: the solar mus |
| 673 | SITE SURVEY | generic site 546 | CONFIRMED | connection point -857 kW (plus is import), +192 kvar; volts 0.997 to 1.009; busiest transformer 101%; a transformer is at 101% of its rating |
| 674 | SITE SURVEY | generic site 547 | CONFIRMED | connection point -683 kW (plus is import), +213 kvar; volts 0.997 to 1.010; busiest transformer 175%; export 683 kW is 683 kW over the 0 kW limit: the solar mus |
| 675 | SITE SURVEY | generic site 548 | CONFIRMED | connection point +9 kW (plus is import), +94 kvar; volts 0.991 to 1.000; busiest transformer 24%; inside every limit |
| 676 | SITE SURVEY | generic site 549 | CONFIRMED | connection point -2026 kW (plus is import), +1270 kvar; volts 0.985 to 1.014; busiest transformer 404%; export 2026 kW is 1976 kW over the 50 kW limit: the sola |
| 677 | SITE SURVEY | generic site 550 | CONFIRMED | connection point -95 kW (plus is import), +653 kvar; volts 0.989 to 1.000; busiest transformer 69%; inside every limit |
| 678 | SITE SURVEY | generic site 551 | CONFIRMED | connection point -2624 kW (plus is import), +924 kvar; volts 0.993 to 1.020; busiest transformer 226%; export 2624 kW is 2424 kW over the 200 kW limit: the sola |
| 679 | SITE SURVEY | generic site 552 | CONFIRMED | connection point -843 kW (plus is import), +342 kvar; volts 0.992 to 1.013; busiest transformer 236%; a transformer is at 236% of its rating |
| 680 | SITE SURVEY | generic site 553 | CONFIRMED | connection point -1375 kW (plus is import), +750 kvar; volts 0.990 to 1.007; busiest transformer 113%; export 1375 kW is 875 kW over the 500 kW limit: the solar |
| 681 | SITE SURVEY | generic site 554 | CONFIRMED | connection point -154 kW (plus is import), +434 kvar; volts 0.991 to 1.008; busiest transformer 168%; a transformer is at 168% of its rating |
| 682 | SITE SURVEY | generic site 555 | CONFIRMED | connection point -1749 kW (plus is import), +860 kvar; volts 0.992 to 1.016; busiest transformer 474%; export 1749 kW is 749 kW over the 1000 kW limit: the sola |
| 683 | SITE SURVEY | generic site 556 | CONFIRMED | connection point -2784 kW (plus is import), +1140 kvar; volts 0.992 to 1.013; busiest transformer 241%; export 2784 kW is 2734 kW over the 50 kW limit: the sola |
| 684 | SITE SURVEY | generic site 557 | CONFIRMED | connection point -824 kW (plus is import), +348 kvar; volts 0.992 to 1.005; busiest transformer 63%; inside every limit |
| 685 | SITE SURVEY | generic site 558 | CONFIRMED | connection point -1084 kW (plus is import), +524 kvar; volts 0.991 to 1.005; busiest transformer 104%; export 1084 kW is 1034 kW over the 50 kW limit: the solar |
| 686 | SITE SURVEY | generic site 559 | CONFIRMED | connection point -230 kW (plus is import), +315 kvar; volts 0.989 to 1.002; busiest transformer 69%; export 230 kW is 30 kW over the 200 kW limit: the solar mus |
| 687 | SITE SURVEY | generic site 560 | CONFIRMED | connection point -5307 kW (plus is import), +3111 kvar; volts 0.978 to 1.003; busiest transformer 484%; export 5307 kW is 4307 kW over the 1000 kW limit: the so |
| 688 | SITE SURVEY | generic site 561 | CONFIRMED | connection point -3492 kW (plus is import), +2908 kvar; volts 0.975 to 1.000; busiest transformer 685%; export 3492 kW is 3492 kW over the 0 kW limit: the solar |
| 689 | SITE SURVEY | generic site 562 | CONFIRMED | connection point -5130 kW (plus is import), +4428 kvar; volts 0.971 to 1.000; busiest transformer 771%; export 5130 kW is 5130 kW over the 0 kW limit: the solar |
| 690 | SITE SURVEY | generic site 563 | CONFIRMED | connection point -679 kW (plus is import), +726 kvar; volts 0.987 to 1.006; busiest transformer 169%; export 679 kW is 179 kW over the 500 kW limit: the solar m |
| 691 | SITE SURVEY | generic site 564 | CONFIRMED | connection point -2843 kW (plus is import), +1501 kvar; volts 0.988 to 1.009; busiest transformer 486%; export 2843 kW is 1843 kW over the 1000 kW limit: the so |
| 692 | SITE SURVEY | generic site 565 | CONFIRMED | connection point -328 kW (plus is import), +994 kvar; volts 0.984 to 1.004; busiest transformer 120%; export 328 kW is 278 kW over the 50 kW limit: the solar mu |
| 693 | SITE SURVEY | generic site 566 | CONFIRMED | connection point -25 kW (plus is import), +938 kvar; volts 0.984 to 1.007; busiest transformer 194%; a transformer is at 194% of its rating |
| 694 | SITE SURVEY | generic site 567 | CONFIRMED | connection point -1764 kW (plus is import), +363 kvar; volts 0.995 to 1.010; busiest transformer 103%; export 1764 kW is 1714 kW over the 50 kW limit: the solar |
| 695 | SITE SURVEY | generic site 568 | CONFIRMED | connection point -36 kW (plus is import), +113 kvar; volts 0.994 to 1.000; busiest transformer 36%; inside every limit |
| 696 | SITE SURVEY | generic site 569 | CONFIRMED | connection point -1095 kW (plus is import), +1115 kvar; volts 0.986 to 1.010; busiest transformer 454%; export 1095 kW is 1095 kW over the 0 kW limit: the solar |
| 697 | SITE SURVEY | generic site 570 | CONFIRMED | connection point -593 kW (plus is import), +117 kvar; volts 0.997 to 1.004; busiest transformer 66%; export 593 kW is 593 kW over the 0 kW limit: the solar must |
| 698 | SITE SURVEY | generic site 571 | CONFIRMED | connection point -2311 kW (plus is import), +706 kvar; volts 0.990 to 1.012; busiest transformer 190%; export 2311 kW is 1311 kW over the 1000 kW limit: the sol |
| 699 | SITE SURVEY | generic site 572 | CONFIRMED | connection point -1016 kW (plus is import), +338 kvar; volts 0.993 to 1.001; busiest transformer 79%; export 1016 kW is 16 kW over the 1000 kW limit: the solar  |
| 700 | SITE SURVEY | generic site 573 | CONFIRMED | connection point -1561 kW (plus is import), +1196 kvar; volts 0.984 to 1.011; busiest transformer 299%; export 1561 kW is 1361 kW over the 200 kW limit: the sol |
| 701 | SITE SURVEY | generic site 574 | CONFIRMED | connection point -1363 kW (plus is import), +598 kvar; volts 0.994 to 1.016; busiest transformer 251%; export 1363 kW is 863 kW over the 500 kW limit: the solar |
| 702 | SITE SURVEY | generic site 575 | CONFIRMED | connection point -1172 kW (plus is import), +543 kvar; volts 0.991 to 1.008; busiest transformer 115%; export 1172 kW is 172 kW over the 1000 kW limit: the sola |
| 703 | SITE SURVEY | generic site 576 | CONFIRMED | connection point -2291 kW (plus is import), +1894 kvar; volts 0.980 to 1.004; busiest transformer 284%; export 2291 kW is 2241 kW over the 50 kW limit: the sola |
| 704 | SITE SURVEY | generic site 577 | CONFIRMED | connection point -3871 kW (plus is import), +1727 kvar; volts 0.989 to 1.015; busiest transformer 333%; export 3871 kW is 3821 kW over the 50 kW limit: the sola |
| 705 | SITE SURVEY | generic site 578 | CONFIRMED | connection point +280 kW (plus is import), +623 kvar; volts 0.985 to 1.000; busiest transformer 35%; inside every limit |
| 706 | SITE SURVEY | generic site 579 | CONFIRMED | connection point -1266 kW (plus is import), +696 kvar; volts 0.990 to 1.013; busiest transformer 215%; export 1266 kW is 1216 kW over the 50 kW limit: the solar |
| 707 | SITE SURVEY | generic site 580 | CONFIRMED | connection point -1186 kW (plus is import), +850 kvar; volts 0.990 to 1.015; busiest transformer 278%; export 1186 kW is 986 kW over the 200 kW limit: the solar |
| 708 | SITE SURVEY | generic site 581 | CONFIRMED | connection point -2724 kW (plus is import), +2525 kvar; volts 0.965 to 1.000; busiest transformer 828%; export 2724 kW is 2674 kW over the 50 kW limit: the sola |
| 709 | SITE SURVEY | generic site 582 | CONFIRMED | connection point -1156 kW (plus is import), +556 kvar; volts 0.992 to 1.014; busiest transformer 331%; export 1156 kW is 1106 kW over the 50 kW limit: the solar |
| 710 | SITE SURVEY | generic site 583 | CONFIRMED | connection point -419 kW (plus is import), +716 kvar; volts 0.987 to 1.002; busiest transformer 79%; export 419 kW is 419 kW over the 0 kW limit: the solar must |
| 711 | SITE SURVEY | generic site 584 | CONFIRMED | connection point -820 kW (plus is import), +721 kvar; volts 0.988 to 1.003; busiest transformer 92%; export 820 kW is 320 kW over the 500 kW limit: the solar mu |
| 712 | SITE SURVEY | generic site 585 | CONFIRMED | connection point -598 kW (plus is import), +262 kvar; volts 0.994 to 1.009; busiest transformer 177%; export 598 kW is 598 kW over the 0 kW limit: the solar mus |
| 713 | SITE SURVEY | generic site 586 | CONFIRMED | connection point -1420 kW (plus is import), +909 kvar; volts 0.990 to 1.015; busiest transformer 255%; export 1420 kW is 420 kW over the 1000 kW limit: the sola |
| 714 | SITE SURVEY | generic site 587 | CONFIRMED | connection point -1840 kW (plus is import), +1072 kvar; volts 0.987 to 1.008; busiest transformer 193%; export 1840 kW is 1640 kW over the 200 kW limit: the sol |
| 715 | SITE SURVEY | generic site 588 | CONFIRMED | connection point -2215 kW (plus is import), +943 kvar; volts 0.992 to 1.011; busiest transformer 161%; export 2215 kW is 2215 kW over the 0 kW limit: the solar  |
| 716 | SITE SURVEY | generic site 589 | CONFIRMED | connection point -661 kW (plus is import), +203 kvar; volts 0.994 to 1.004; busiest transformer 53%; export 661 kW is 661 kW over the 0 kW limit: the solar must |
| 717 | SITE SURVEY | generic site 590 | CONFIRMED | connection point -136 kW (plus is import), +169 kvar; volts 0.990 to 1.002; busiest transformer 74%; inside every limit |
| 718 | SITE SURVEY | generic site 591 | CONFIRMED | connection point -289 kW (plus is import), +481 kvar; volts 0.989 to 1.000; busiest transformer 60%; export 289 kW is 89 kW over the 200 kW limit: the solar mus |
| 719 | SITE SURVEY | generic site 592 | CONFIRMED | connection point -1573 kW (plus is import), +538 kvar; volts 0.990 to 1.011; busiest transformer 250%; export 1573 kW is 1373 kW over the 200 kW limit: the sola |
| 720 | SITE SURVEY | generic site 593 | CONFIRMED | connection point -16 kW (plus is import), +437 kvar; volts 0.989 to 1.001; busiest transformer 72%; inside every limit |
| 721 | SITE SURVEY | generic site 594 | CONFIRMED | connection point -1645 kW (plus is import), +908 kvar; volts 0.989 to 1.014; busiest transformer 474%; export 1645 kW is 1645 kW over the 0 kW limit: the solar  |
| 722 | SITE SURVEY | generic site 595 | CONFIRMED | connection point -1365 kW (plus is import), +924 kvar; volts 0.988 to 1.009; busiest transformer 439%; export 1365 kW is 1165 kW over the 200 kW limit: the sola |
| 723 | SITE SURVEY | generic site 596 | CONFIRMED | connection point -1824 kW (plus is import), +779 kvar; volts 0.991 to 1.016; busiest transformer 258%; export 1824 kW is 824 kW over the 1000 kW limit: the sola |
| 724 | SITE SURVEY | generic site 597 | CONFIRMED | connection point -351 kW (plus is import), +99 kvar; volts 0.994 to 1.003; busiest transformer 55%; inside every limit |
| 725 | SITE SURVEY | generic site 598 | CONFIRMED | connection point -3335 kW (plus is import), +2290 kvar; volts 0.985 to 1.003; busiest transformer 614%; export 3335 kW is 3335 kW over the 0 kW limit: the solar |
| 726 | SITE SURVEY | generic site 599 | CONFIRMED | connection point -70 kW (plus is import), +508 kvar; volts 0.988 to 1.009; busiest transformer 180%; a transformer is at 180% of its rating |
| 727 | SITE SURVEY | generic site 600 | CONFIRMED | connection point -359 kW (plus is import), +544 kvar; volts 0.988 to 1.003; busiest transformer 115%; export 359 kW is 159 kW over the 200 kW limit: the solar m |
| 728 | SITE SURVEY | generic site 601 | CONFIRMED | connection point -1759 kW (plus is import), +1068 kvar; volts 0.989 to 1.008; busiest transformer 511%; export 1759 kW is 759 kW over the 1000 kW limit: the sol |
| 729 | SITE SURVEY | generic site 602 | CONFIRMED | connection point -1550 kW (plus is import), +600 kvar; volts 0.989 to 1.006; busiest transformer 136%; export 1550 kW is 1500 kW over the 50 kW limit: the solar |
| 730 | SITE SURVEY | generic site 603 | CONFIRMED | connection point -364 kW (plus is import), +400 kvar; volts 0.991 to 1.000; busiest transformer 40%; export 364 kW is 314 kW over the 50 kW limit: the solar mus |
| 731 | SITE SURVEY | generic site 604 | CONFIRMED | connection point -997 kW (plus is import), +294 kvar; volts 0.992 to 1.008; busiest transformer 154%; export 997 kW is 497 kW over the 500 kW limit: the solar m |
| 732 | SITE SURVEY | generic site 605 | CONFIRMED | connection point -1434 kW (plus is import), +855 kvar; volts 0.988 to 1.014; busiest transformer 440%; export 1434 kW is 1434 kW over the 0 kW limit: the solar  |
| 733 | SITE SURVEY | generic site 606 | CONFIRMED | connection point -1663 kW (plus is import), +732 kvar; volts 0.991 to 1.012; busiest transformer 293%; export 1663 kW is 1163 kW over the 500 kW limit: the sola |
| 734 | SITE SURVEY | generic site 607 | CONFIRMED | connection point +40 kW (plus is import), +524 kvar; volts 0.987 to 1.000; busiest transformer 79%; inside every limit |
| 735 | SITE SURVEY | generic site 608 | CONFIRMED | connection point -2600 kW (plus is import), +1104 kvar; volts 0.986 to 1.011; busiest transformer 421%; export 2600 kW is 2400 kW over the 200 kW limit: the sol |
| 736 | SITE SURVEY | generic site 609 | CONFIRMED | connection point -3317 kW (plus is import), +1619 kvar; volts 0.989 to 1.016; busiest transformer 453%; export 3317 kW is 2817 kW over the 500 kW limit: the sol |
| 737 | SITE SURVEY | generic site 610 | CONFIRMED | connection point -3636 kW (plus is import), +2144 kvar; volts 0.987 to 1.010; busiest transformer 522%; export 3636 kW is 3636 kW over the 0 kW limit: the solar |
| 738 | SITE SURVEY | generic site 611 | CONFIRMED | connection point -562 kW (plus is import), +498 kvar; volts 0.991 to 1.003; busiest transformer 66%; export 562 kW is 512 kW over the 50 kW limit: the solar mus |
| 739 | SITE SURVEY | generic site 612 | CONFIRMED | connection point -1652 kW (plus is import), +1200 kvar; volts 0.987 to 1.009; busiest transformer 299%; export 1652 kW is 652 kW over the 1000 kW limit: the sol |
| 740 | SITE SURVEY | generic site 613 | CONFIRMED | connection point -1348 kW (plus is import), +569 kvar; volts 0.991 to 1.007; busiest transformer 101%; export 1348 kW is 848 kW over the 500 kW limit: the solar |
| 741 | SITE SURVEY | generic site 614 | CONFIRMED | connection point -888 kW (plus is import), +376 kvar; volts 0.992 to 1.010; busiest transformer 166%; a transformer is at 166% of its rating |
| 742 | SITE SURVEY | generic site 615 | CONFIRMED | connection point -1378 kW (plus is import), +312 kvar; volts 0.994 to 1.011; busiest transformer 106%; export 1378 kW is 1328 kW over the 50 kW limit: the solar |
| 743 | SITE SURVEY | generic site 616 | CONFIRMED | connection point -1002 kW (plus is import), +294 kvar; volts 0.993 to 1.007; busiest transformer 128%; export 1002 kW is 952 kW over the 50 kW limit: the solar  |
| 744 | SITE SURVEY | generic site 617 | CONFIRMED | connection point -55 kW (plus is import), +733 kvar; volts 0.986 to 1.000; busiest transformer 76%; inside every limit |
| 745 | SITE SURVEY | generic site 618 | CONFIRMED | connection point -137 kW (plus is import), +381 kvar; volts 0.990 to 1.003; busiest transformer 93%; inside every limit |
| 746 | SITE SURVEY | generic site 619 | CONFIRMED | connection point -2865 kW (plus is import), +2282 kvar; volts 0.968 to 1.000; busiest transformer 802%; export 2865 kW is 2665 kW over the 200 kW limit: the sol |
| 747 | SITE SURVEY | generic site 620 | CONFIRMED | connection point +53 kW (plus is import), +222 kvar; volts 0.991 to 1.000; busiest transformer 22%; inside every limit |
| 748 | SITE SURVEY | generic site 621 | CONFIRMED | connection point -2598 kW (plus is import), +1250 kvar; volts 0.988 to 1.015; busiest transformer 369%; export 2598 kW is 2098 kW over the 500 kW limit: the sol |
| 749 | SITE SURVEY | generic site 622 | CONFIRMED | connection point -169 kW (plus is import), +193 kvar; volts 0.990 to 1.002; busiest transformer 46%; inside every limit |
| 750 | SITE SURVEY | generic site 623 | CONFIRMED | connection point -1468 kW (plus is import), +320 kvar; volts 0.993 to 1.007; busiest transformer 110%; export 1468 kW is 1268 kW over the 200 kW limit: the sola |
| 751 | SITE SURVEY | generic site 624 | CONFIRMED | connection point -833 kW (plus is import), +276 kvar; volts 0.992 to 1.014; busiest transformer 221%; export 833 kW is 633 kW over the 200 kW limit: the solar m |
| 752 | SITE SURVEY | generic site 625 | CONFIRMED | connection point -1857 kW (plus is import), +639 kvar; volts 0.993 to 1.009; busiest transformer 126%; export 1857 kW is 1807 kW over the 50 kW limit: the solar |
| 753 | SITE SURVEY | generic site 626 | CONFIRMED | connection point -980 kW (plus is import), +406 kvar; volts 0.994 to 1.017; busiest transformer 277%; export 980 kW is 980 kW over the 0 kW limit: the solar mus |
| 754 | SITE SURVEY | generic site 627 | CONFIRMED | connection point -2162 kW (plus is import), +607 kvar; volts 0.994 to 1.013; busiest transformer 141%; export 2162 kW is 2112 kW over the 50 kW limit: the solar |
| 755 | SITE SURVEY | generic site 628 | CONFIRMED | connection point +280 kW (plus is import), +587 kvar; volts 0.986 to 1.000; busiest transformer 42%; inside every limit |
| 756 | SITE SURVEY | generic site 629 | CONFIRMED | connection point -354 kW (plus is import), +130 kvar; volts 0.993 to 1.001; busiest transformer 45%; export 354 kW is 354 kW over the 0 kW limit: the solar must |
| 757 | SITE SURVEY | generic site 630 | CONFIRMED | connection point -3288 kW (plus is import), +2004 kvar; volts 0.986 to 1.005; busiest transformer 575%; export 3288 kW is 3238 kW over the 50 kW limit: the sola |
| 758 | SITE SURVEY | generic site 631 | CONFIRMED | connection point -5524 kW (plus is import), +2073 kvar; volts 0.981 to 1.005; busiest transformer 347%; export 5524 kW is 5324 kW over the 200 kW limit: the sol |
| 759 | SITE SURVEY | generic site 632 | CONFIRMED | connection point -2138 kW (plus is import), +820 kvar; volts 0.992 to 1.012; busiest transformer 341%; export 2138 kW is 1638 kW over the 500 kW limit: the sola |
| 760 | SITE SURVEY | generic site 633 | CONFIRMED | connection point -460 kW (plus is import), +170 kvar; volts 0.997 to 1.001; busiest transformer 55%; inside every limit |
| 761 | SITE SURVEY | generic site 634 | CONFIRMED | connection point -1176 kW (plus is import), +543 kvar; volts 0.991 to 1.004; busiest transformer 110%; export 1176 kW is 176 kW over the 1000 kW limit: the sola |
| 762 | SITE SURVEY | generic site 635 | CONFIRMED | connection point -2640 kW (plus is import), +1117 kvar; volts 0.989 to 1.014; busiest transformer 424%; export 2640 kW is 2140 kW over the 500 kW limit: the sol |
| 763 | SITE SURVEY | generic site 636 | CONFIRMED | connection point -263 kW (plus is import), +337 kvar; volts 0.992 to 1.009; busiest transformer 156%; export 263 kW is 263 kW over the 0 kW limit: the solar mus |
| 764 | SITE SURVEY | generic site 637 | CONFIRMED | connection point -1789 kW (plus is import), +1030 kvar; volts 0.987 to 1.016; busiest transformer 356%; export 1789 kW is 1739 kW over the 50 kW limit: the sola |
| 765 | SITE SURVEY | generic site 638 | CONFIRMED | connection point -1977 kW (plus is import), +1194 kvar; volts 0.989 to 1.010; busiest transformer 210%; export 1977 kW is 1927 kW over the 50 kW limit: the sola |
| 766 | SITE SURVEY | generic site 639 | CONFIRMED | connection point -1158 kW (plus is import), +1059 kvar; volts 0.986 to 1.011; busiest transformer 308%; export 1158 kW is 1108 kW over the 50 kW limit: the sola |
| 767 | SITE SURVEY | generic site 640 | CONFIRMED | connection point -467 kW (plus is import), +192 kvar; volts 0.996 to 1.002; busiest transformer 81%; inside every limit |
| 768 | SITE SURVEY | generic site 641 | CONFIRMED | connection point -413 kW (plus is import), +447 kvar; volts 0.991 to 1.001; busiest transformer 64%; inside every limit |
| 769 | SITE SURVEY | generic site 642 | CONFIRMED | connection point -4088 kW (plus is import), +1438 kvar; volts 0.992 to 1.018; busiest transformer 269%; export 4088 kW is 4038 kW over the 50 kW limit: the sola |
| 770 | SITE SURVEY | generic site 643 | CONFIRMED | connection point -2447 kW (plus is import), +1462 kvar; volts 0.985 to 1.006; busiest transformer 454%; export 2447 kW is 1447 kW over the 1000 kW limit: the so |
| 771 | SITE SURVEY | generic site 644 | CONFIRMED | connection point -2662 kW (plus is import), +1490 kvar; volts 0.984 to 1.009; busiest transformer 399%; export 2662 kW is 1662 kW over the 1000 kW limit: the so |
| 772 | SITE SURVEY | generic site 645 | CONFIRMED | connection point -56 kW (plus is import), +224 kvar; volts 0.995 to 1.000; busiest transformer 43%; inside every limit |
| 773 | SITE SURVEY | generic site 646 | CONFIRMED | connection point -2136 kW (plus is import), +910 kvar; volts 0.992 to 1.013; busiest transformer 161%; export 2136 kW is 1136 kW over the 1000 kW limit: the sol |
| 774 | SITE SURVEY | generic site 647 | CONFIRMED | connection point -567 kW (plus is import), +1148 kvar; volts 0.983 to 1.012; busiest transformer 408%; a transformer is at 408% of its rating |
| 775 | SITE SURVEY | generic site 648 | CONFIRMED | connection point -2176 kW (plus is import), +1103 kvar; volts 0.987 to 1.013; busiest transformer 389%; export 2176 kW is 1676 kW over the 500 kW limit: the sol |
| 776 | SITE SURVEY | generic site 649 | CONFIRMED | connection point -711 kW (plus is import), +472 kvar; volts 0.990 to 1.014; busiest transformer 257%; export 711 kW is 211 kW over the 500 kW limit: the solar m |
| 777 | SITE SURVEY | generic site 650 | CONFIRMED | connection point -579 kW (plus is import), +479 kvar; volts 0.989 to 1.003; busiest transformer 80%; export 579 kW is 379 kW over the 200 kW limit: the solar mu |
| 778 | SITE SURVEY | generic site 651 | CONFIRMED | connection point -569 kW (plus is import), +137 kvar; volts 0.998 to 1.002; busiest transformer 32%; export 569 kW is 369 kW over the 200 kW limit: the solar mu |
| 779 | SITE SURVEY | generic site 652 | CONFIRMED | connection point -396 kW (plus is import), +290 kvar; volts 0.992 to 1.007; busiest transformer 105%; export 396 kW is 396 kW over the 0 kW limit: the solar mus |
| 780 | SITE SURVEY | generic site 653 | CONFIRMED | connection point -4223 kW (plus is import), +1964 kvar; volts 0.986 to 1.017; busiest transformer 308%; export 4223 kW is 3723 kW over the 500 kW limit: the sol |
| 781 | SITE SURVEY | generic site 654 | CONFIRMED | connection point -35 kW (plus is import), +577 kvar; volts 0.989 to 1.001; busiest transformer 93%; inside every limit |
| 782 | SITE SURVEY | generic site 655 | CONFIRMED | connection point +686 kW (plus is import), +1171 kvar; volts 0.981 to 1.005; busiest transformer 259%; a transformer is at 259% of its rating |
| 783 | SITE SURVEY | generic site 656 | CONFIRMED | connection point -590 kW (plus is import), +777 kvar; volts 0.987 to 1.011; busiest transformer 318%; export 590 kW is 390 kW over the 200 kW limit: the solar m |
| 784 | SITE SURVEY | generic site 657 | CONFIRMED | connection point -924 kW (plus is import), +660 kvar; volts 0.990 to 1.011; busiest transformer 180%; export 924 kW is 424 kW over the 500 kW limit: the solar m |
| 785 | SITE SURVEY | generic site 658 | CONFIRMED | connection point -642 kW (plus is import), +151 kvar; volts 0.995 to 1.009; busiest transformer 101%; export 642 kW is 642 kW over the 0 kW limit: the solar mus |
| 786 | SITE SURVEY | generic site 659 | CONFIRMED | connection point -3002 kW (plus is import), +1880 kvar; volts 0.988 to 1.010; busiest transformer 550%; export 3002 kW is 2002 kW over the 1000 kW limit: the so |
| 787 | SITE SURVEY | generic site 660 | CONFIRMED | connection point -706 kW (plus is import), +202 kvar; volts 0.993 to 1.004; busiest transformer 56%; export 706 kW is 706 kW over the 0 kW limit: the solar must |
| 788 | SITE SURVEY | generic site 661 | CONFIRMED | connection point -3460 kW (plus is import), +1082 kvar; volts 0.994 to 1.016; busiest transformer 264%; export 3460 kW is 2960 kW over the 500 kW limit: the sol |
| 789 | SITE SURVEY | generic site 662 | CONFIRMED | connection point -1656 kW (plus is import), +1170 kvar; volts 0.988 to 1.012; busiest transformer 297%; export 1656 kW is 1456 kW over the 200 kW limit: the sol |
| 790 | SITE SURVEY | generic site 663 | CONFIRMED | connection point -3344 kW (plus is import), +2787 kvar; volts 0.976 to 1.000; busiest transformer 662%; export 3344 kW is 3344 kW over the 0 kW limit: the solar |
| 791 | SITE SURVEY | generic site 664 | CONFIRMED | connection point -2625 kW (plus is import), +1497 kvar; volts 0.988 to 1.012; busiest transformer 216%; export 2625 kW is 2125 kW over the 500 kW limit: the sol |
| 792 | SITE SURVEY | generic site 665 | CONFIRMED | connection point -408 kW (plus is import), +613 kvar; volts 0.989 to 1.001; busiest transformer 82%; export 408 kW is 208 kW over the 200 kW limit: the solar mu |
| 793 | SITE SURVEY | generic site 666 | CONFIRMED | connection point -1166 kW (plus is import), +1037 kvar; volts 0.985 to 1.011; busiest transformer 450%; export 1166 kW is 966 kW over the 200 kW limit: the sola |
| 794 | SITE SURVEY | generic site 667 | CONFIRMED | connection point -1521 kW (plus is import), +394 kvar; volts 0.994 to 1.012; busiest transformer 186%; export 1521 kW is 1471 kW over the 50 kW limit: the solar |
| 795 | SITE SURVEY | generic site 668 | CONFIRMED | connection point -2683 kW (plus is import), +966 kvar; volts 0.992 to 1.015; busiest transformer 222%; export 2683 kW is 1683 kW over the 1000 kW limit: the sol |
| 796 | SITE SURVEY | generic site 669 | CONFIRMED | connection point -2202 kW (plus is import), +682 kvar; volts 0.991 to 1.010; busiest transformer 144%; export 2202 kW is 1202 kW over the 1000 kW limit: the sol |
| 797 | SITE SURVEY | generic site 670 | CONFIRMED | connection point -1699 kW (plus is import), +812 kvar; volts 0.989 to 1.002; busiest transformer 128%; export 1699 kW is 699 kW over the 1000 kW limit: the sola |
| 798 | SITE SURVEY | generic site 671 | CONFIRMED | connection point -3138 kW (plus is import), +1439 kvar; volts 0.991 to 1.017; busiest transformer 239%; export 3138 kW is 3088 kW over the 50 kW limit: the sola |
| 799 | SITE SURVEY | generic site 672 | CONFIRMED | connection point -1563 kW (plus is import), +734 kvar; volts 0.987 to 1.013; busiest transformer 425%; export 1563 kW is 1363 kW over the 200 kW limit: the sola |
| 800 | SITE SURVEY | generic site 673 | CONFIRMED | connection point +172 kW (plus is import), +560 kvar; volts 0.989 to 1.000; busiest transformer 42%; inside every limit |
| 801 | SITE SURVEY | generic site 674 | CONFIRMED | connection point -946 kW (plus is import), +513 kvar; volts 0.991 to 1.006; busiest transformer 103%; export 946 kW is 446 kW over the 500 kW limit: the solar m |
| 802 | SITE SURVEY | generic site 675 | CONFIRMED | connection point -1589 kW (plus is import), +565 kvar; volts 0.989 to 1.013; busiest transformer 215%; export 1589 kW is 1089 kW over the 500 kW limit: the sola |
| 803 | SITE SURVEY | generic site 676 | CONFIRMED | connection point -1030 kW (plus is import), +354 kvar; volts 0.993 to 1.004; busiest transformer 68%; export 1030 kW is 830 kW over the 200 kW limit: the solar  |
| 804 | SITE SURVEY | generic site 677 | CONFIRMED | connection point -5375 kW (plus is import), +2611 kvar; volts 0.977 to 1.006; busiest transformer 452%; export 5375 kW is 5175 kW over the 200 kW limit: the sol |
| 805 | SITE SURVEY | generic site 678 | CONFIRMED | connection point -418 kW (plus is import), +113 kvar; volts 0.998 to 1.003; busiest transformer 63%; export 418 kW is 418 kW over the 0 kW limit: the solar must |
| 806 | SITE SURVEY | generic site 679 | CONFIRMED | connection point -1777 kW (plus is import), +1165 kvar; volts 0.988 to 1.013; busiest transformer 304%; export 1777 kW is 1727 kW over the 50 kW limit: the sola |
| 807 | SITE SURVEY | generic site 680 | CONFIRMED | connection point -3973 kW (plus is import), +1718 kvar; volts 0.990 to 1.013; busiest transformer 278%; export 3973 kW is 3773 kW over the 200 kW limit: the sol |
| 808 | SITE SURVEY | generic site 681 | CONFIRMED | connection point -3445 kW (plus is import), +964 kvar; volts 0.996 to 1.018; busiest transformer 207%; export 3445 kW is 2945 kW over the 500 kW limit: the sola |
| 809 | SITE SURVEY | generic site 682 | CONFIRMED | connection point -2289 kW (plus is import), +799 kvar; volts 0.989 to 1.005; busiest transformer 153%; export 2289 kW is 2089 kW over the 200 kW limit: the sola |
| 810 | SITE SURVEY | generic site 683 | CONFIRMED | connection point -2404 kW (plus is import), +687 kvar; volts 0.997 to 1.013; busiest transformer 185%; export 2404 kW is 1404 kW over the 1000 kW limit: the sol |
| 811 | SITE SURVEY | generic site 684 | CONFIRMED | connection point -3604 kW (plus is import), +1292 kvar; volts 0.993 to 1.017; busiest transformer 291%; export 3604 kW is 3404 kW over the 200 kW limit: the sol |
| 812 | SITE SURVEY | generic site 685 | CONFIRMED | connection point -884 kW (plus is import), +329 kvar; volts 0.992 to 1.014; busiest transformer 243%; export 884 kW is 384 kW over the 500 kW limit: the solar m |
| 813 | SITE SURVEY | generic site 686 | CONFIRMED | connection point -1759 kW (plus is import), +2093 kvar; volts 0.980 to 1.000; busiest transformer 696%; export 1759 kW is 1559 kW over the 200 kW limit: the sol |
| 814 | SITE SURVEY | generic site 687 | CONFIRMED | connection point -113 kW (plus is import), +487 kvar; volts 0.989 to 1.000; busiest transformer 57%; inside every limit |
| 815 | SITE SURVEY | generic site 688 | CONFIRMED | connection point -736 kW (plus is import), +987 kvar; volts 0.986 to 1.008; busiest transformer 255%; a transformer is at 255% of its rating |
| 816 | SITE SURVEY | generic site 689 | CONFIRMED | connection point -1179 kW (plus is import), +1151 kvar; volts 0.986 to 1.009; busiest transformer 318%; export 1179 kW is 979 kW over the 200 kW limit: the sola |
| 817 | SITE SURVEY | generic site 690 | CONFIRMED | connection point -2017 kW (plus is import), +717 kvar; volts 0.992 to 1.010; busiest transformer 137%; export 2017 kW is 1517 kW over the 500 kW limit: the sola |
| 818 | SITE SURVEY | generic site 691 | CONFIRMED | connection point -2224 kW (plus is import), +1304 kvar; volts 0.986 to 1.013; busiest transformer 425%; export 2224 kW is 2024 kW over the 200 kW limit: the sol |
| 819 | SITE SURVEY | generic site 692 | CONFIRMED | connection point -2687 kW (plus is import), +4494 kvar; volts 0.866 to 1.000; busiest transformer 1008%; export 2687 kW is 2187 kW over the 500 kW limit: the so |
| 820 | SITE SURVEY | generic site 693 | CONFIRMED | connection point -39 kW (plus is import), +392 kvar; volts 0.989 to 1.000; busiest transformer 34%; inside every limit |
| 821 | SITE SURVEY | generic site 694 | CONFIRMED | connection point -4304 kW (plus is import), +1396 kvar; volts 0.987 to 1.013; busiest transformer 275%; export 4304 kW is 3304 kW over the 1000 kW limit: the so |
| 822 | SITE SURVEY | generic site 695 | CONFIRMED | connection point -1085 kW (plus is import), +495 kvar; volts 0.991 to 1.005; busiest transformer 102%; export 1085 kW is 885 kW over the 200 kW limit: the solar |
| 823 | SITE SURVEY | generic site 696 | CONFIRMED | connection point -376 kW (plus is import), +372 kvar; volts 0.990 to 1.001; busiest transformer 56%; export 376 kW is 376 kW over the 0 kW limit: the solar must |
| 824 | SITE SURVEY | generic site 697 | CONFIRMED | connection point -316 kW (plus is import), +153 kvar; volts 0.995 to 1.000; busiest transformer 23%; export 316 kW is 316 kW over the 0 kW limit: the solar must |
| 825 | SITE SURVEY | generic site 698 | CONFIRMED | connection point -3355 kW (plus is import), +1745 kvar; volts 0.982 to 1.010; busiest transformer 469%; export 3355 kW is 2855 kW over the 500 kW limit: the sol |
| 826 | SITE SURVEY | generic site 699 | CONFIRMED | connection point -1844 kW (plus is import), +653 kvar; volts 0.996 to 1.016; busiest transformer 293%; export 1844 kW is 844 kW over the 1000 kW limit: the sola |
| 827 | SITE SURVEY | generic site 700 | CONFIRMED | connection point -228 kW (plus is import), +331 kvar; volts 0.991 to 1.006; busiest transformer 143%; export 228 kW is 28 kW over the 200 kW limit: the solar mu |
| 828 | SITE SURVEY | generic site 701 | CONFIRMED | connection point -2036 kW (plus is import), +1876 kvar; volts 0.982 to 1.000; busiest transformer 686%; export 2036 kW is 1836 kW over the 200 kW limit: the sol |
| 829 | SITE SURVEY | generic site 702 | CONFIRMED | connection point -3365 kW (plus is import), +2136 kvar; volts 0.980 to 1.005; busiest transformer 502%; export 3365 kW is 3365 kW over the 0 kW limit: the solar |
| 830 | SITE SURVEY | generic site 703 | CONFIRMED | connection point -301 kW (plus is import), +117 kvar; volts 0.996 to 1.002; busiest transformer 51%; export 301 kW is 251 kW over the 50 kW limit: the solar mus |
| 831 | SITE SURVEY | generic site 704 | CONFIRMED | connection point -252 kW (plus is import), +816 kvar; volts 0.986 to 1.009; busiest transformer 193%; a transformer is at 193% of its rating |
| 832 | SITE SURVEY | generic site 705 | CONFIRMED | connection point -3416 kW (plus is import), +1376 kvar; volts 0.986 to 1.012; busiest transformer 237%; export 3416 kW is 2916 kW over the 500 kW limit: the sol |
| 833 | SITE SURVEY | generic site 706 | CONFIRMED | connection point -3097 kW (plus is import), +1257 kvar; volts 0.991 to 1.013; busiest transformer 220%; export 3097 kW is 2097 kW over the 1000 kW limit: the so |
| 834 | SITE SURVEY | generic site 707 | CONFIRMED | connection point -1162 kW (plus is import), +385 kvar; volts 0.994 to 1.003; busiest transformer 75%; export 1162 kW is 962 kW over the 200 kW limit: the solar  |
| 835 | SITE SURVEY | generic site 708 | CONFIRMED | connection point -216 kW (plus is import), +205 kvar; volts 0.994 to 1.000; busiest transformer 18%; inside every limit |
| 836 | SITE SURVEY | generic site 709 | CONFIRMED | connection point -2547 kW (plus is import), +742 kvar; volts 0.994 to 1.013; busiest transformer 164%; export 2547 kW is 2547 kW over the 0 kW limit: the solar  |
| 837 | SITE SURVEY | generic site 710 | CONFIRMED | connection point -1258 kW (plus is import), +792 kvar; volts 0.991 to 1.006; busiest transformer 141%; export 1258 kW is 758 kW over the 500 kW limit: the solar |
| 838 | SITE SURVEY | generic site 711 | CONFIRMED | connection point -2211 kW (plus is import), +1041 kvar; volts 0.987 to 1.013; busiest transformer 387%; export 2211 kW is 2011 kW over the 200 kW limit: the sol |
| 839 | SITE SURVEY | generic site 712 | CONFIRMED | connection point -2994 kW (plus is import), +933 kvar; volts 0.993 to 1.013; busiest transformer 234%; export 2994 kW is 2994 kW over the 0 kW limit: the solar  |
| 840 | SITE SURVEY | generic site 713 | CONFIRMED | connection point -2045 kW (plus is import), +580 kvar; volts 0.990 to 1.008; busiest transformer 133%; export 2045 kW is 1545 kW over the 500 kW limit: the sola |
| 841 | SITE SURVEY | generic site 714 | REFUTED | connection point -3114 kW (plus is import), +5430 kvar; volts 0.814 to 1.000; busiest transformer 1104%; export 3114 kW is 2114 kW over the 1000 kW limit: the s |
| 842 | SITE SURVEY | generic site 715 | CONFIRMED | connection point -331 kW (plus is import), +599 kvar; volts 0.990 to 1.003; busiest transformer 123%; a transformer is at 123% of its rating |
| 843 | SITE SURVEY | generic site 716 | CONFIRMED | connection point -946 kW (plus is import), +635 kvar; volts 0.990 to 1.012; busiest transformer 324%; a transformer is at 324% of its rating |
| 844 | SITE SURVEY | generic site 717 | CONFIRMED | connection point -2616 kW (plus is import), +891 kvar; volts 0.992 to 1.011; busiest transformer 211%; export 2616 kW is 1616 kW over the 1000 kW limit: the sol |
| 845 | SITE SURVEY | generic site 718 | CONFIRMED | connection point +281 kW (plus is import), +461 kvar; volts 0.988 to 1.000; busiest transformer 58%; inside every limit |
| 846 | SITE SURVEY | generic site 719 | CONFIRMED | connection point -539 kW (plus is import), +787 kvar; volts 0.988 to 1.011; busiest transformer 313%; export 539 kW is 339 kW over the 200 kW limit: the solar m |
| 847 | SITE SURVEY | generic site 720 | CONFIRMED | connection point -1476 kW (plus is import), +1214 kvar; volts 0.986 to 1.011; busiest transformer 294%; export 1476 kW is 1426 kW over the 50 kW limit: the sola |
| 848 | SITE SURVEY | generic site 721 | CONFIRMED | connection point -1809 kW (plus is import), +541 kvar; volts 0.992 to 1.013; busiest transformer 150%; export 1809 kW is 1309 kW over the 500 kW limit: the sola |
| 849 | SITE SURVEY | generic site 722 | CONFIRMED | connection point -2564 kW (plus is import), +1015 kvar; volts 0.991 to 1.014; busiest transformer 227%; export 2564 kW is 2064 kW over the 500 kW limit: the sol |
| 850 | SITE SURVEY | generic site 723 | CONFIRMED | connection point +269 kW (plus is import), +553 kvar; volts 0.986 to 1.000; busiest transformer 88%; inside every limit |
| 851 | SITE SURVEY | generic site 724 | CONFIRMED | connection point -1782 kW (plus is import), +1030 kvar; volts 0.990 to 1.014; busiest transformer 288%; export 1782 kW is 1282 kW over the 500 kW limit: the sol |
| 852 | SITE SURVEY | generic site 725 | CONFIRMED | connection point -50 kW (plus is import), +148 kvar; volts 0.993 to 1.000; busiest transformer 18%; inside every limit |
| 853 | SITE SURVEY | generic site 726 | CONFIRMED | connection point -2331 kW (plus is import), +1508 kvar; volts 0.985 to 1.000; busiest transformer 646%; export 2331 kW is 1831 kW over the 500 kW limit: the sol |
| 854 | SITE SURVEY | generic site 727 | REFUTED | connection point -2803 kW (plus is import), +7777 kvar; volts 0.675 to 1.000; busiest transformer 1175%; export 2803 kW is 2803 kW over the 0 kW limit: the sola |
| 855 | SITE SURVEY | generic site 728 | CONFIRMED | connection point +47 kW (plus is import), +350 kvar; volts 0.989 to 1.000; busiest transformer 24%; inside every limit |
| 856 | SITE SURVEY | generic site 729 | CONFIRMED | connection point -300 kW (plus is import), +740 kvar; volts 0.986 to 1.009; busiest transformer 269%; export 300 kW is 250 kW over the 50 kW limit: the solar mu |
| 857 | SITE SURVEY | generic site 730 | CONFIRMED | connection point -1676 kW (plus is import), +646 kvar; volts 0.993 to 1.008; busiest transformer 144%; export 1676 kW is 1676 kW over the 0 kW limit: the solar  |
| 858 | SITE SURVEY | generic site 731 | CONFIRMED | connection point -3873 kW (plus is import), +1349 kvar; volts 0.988 to 1.017; busiest transformer 256%; export 3873 kW is 3373 kW over the 500 kW limit: the sol |
| 859 | SITE SURVEY | generic site 732 | CONFIRMED | connection point -1577 kW (plus is import), +729 kvar; volts 0.989 to 1.009; busiest transformer 128%; export 1577 kW is 1377 kW over the 200 kW limit: the sola |
| 860 | SITE SURVEY | generic site 733 | CONFIRMED | connection point -3471 kW (plus is import), +1051 kvar; volts 0.989 to 1.013; busiest transformer 215%; export 3471 kW is 3421 kW over the 50 kW limit: the sola |
| 861 | SITE SURVEY | generic site 734 | CONFIRMED | connection point -3142 kW (plus is import), +1223 kvar; volts 0.988 to 1.012; busiest transformer 266%; export 3142 kW is 3092 kW over the 50 kW limit: the sola |
| 862 | SITE SURVEY | generic site 735 | CONFIRMED | connection point -1387 kW (plus is import), +430 kvar; volts 0.997 to 1.010; busiest transformer 96%; export 1387 kW is 1387 kW over the 0 kW limit: the solar m |
| 863 | SITE SURVEY | generic site 736 | CONFIRMED | connection point -1174 kW (plus is import), +597 kvar; volts 0.992 to 1.019; busiest transformer 351%; export 1174 kW is 1174 kW over the 0 kW limit: the solar  |
| 864 | SITE SURVEY | generic site 737 | CONFIRMED | connection point -807 kW (plus is import), +216 kvar; volts 0.993 to 1.004; busiest transformer 50%; export 807 kW is 307 kW over the 500 kW limit: the solar mu |
| 865 | SITE SURVEY | generic site 738 | CONFIRMED | connection point -1131 kW (plus is import), +1118 kvar; volts 0.987 to 1.011; busiest transformer 461%; export 1131 kW is 631 kW over the 500 kW limit: the sola |
| 866 | SITE SURVEY | generic site 739 | CONFIRMED | connection point -342 kW (plus is import), +171 kvar; volts 0.994 to 1.004; busiest transformer 71%; inside every limit |
| 867 | SITE SURVEY | generic site 740 | CONFIRMED | connection point -2385 kW (plus is import), +910 kvar; volts 0.988 to 1.013; busiest transformer 312%; export 2385 kW is 2385 kW over the 0 kW limit: the solar  |
| 868 | SITE SURVEY | generic site 741 | CONFIRMED | connection point -2348 kW (plus is import), +650 kvar; volts 0.994 to 1.016; busiest transformer 183%; export 2348 kW is 1848 kW over the 500 kW limit: the sola |
| 869 | SITE SURVEY | generic site 742 | CONFIRMED | connection point -1876 kW (plus is import), +722 kvar; volts 0.989 to 1.011; busiest transformer 170%; export 1876 kW is 1876 kW over the 0 kW limit: the solar  |
| 870 | SITE SURVEY | generic site 743 | CONFIRMED | connection point -2953 kW (plus is import), +1113 kvar; volts 0.994 to 1.012; busiest transformer 200%; export 2953 kW is 2903 kW over the 50 kW limit: the sola |
| 871 | SITE SURVEY | generic site 744 | CONFIRMED | connection point -1195 kW (plus is import), +502 kvar; volts 0.990 to 1.011; busiest transformer 180%; export 1195 kW is 695 kW over the 500 kW limit: the solar |
| 872 | SITE SURVEY | generic site 745 | CONFIRMED | connection point -2382 kW (plus is import), +607 kvar; volts 0.995 to 1.012; busiest transformer 175%; export 2382 kW is 1382 kW over the 1000 kW limit: the sol |
| 873 | SITE SURVEY | generic site 746 | CONFIRMED | connection point -260 kW (plus is import), +661 kvar; volts 0.986 to 1.004; busiest transformer 130%; a transformer is at 130% of its rating |
| 874 | SITE SURVEY | generic site 747 | CONFIRMED | connection point +150 kW (plus is import), +364 kvar; volts 0.989 to 1.000; busiest transformer 43%; inside every limit |
| 875 | SITE SURVEY | generic site 748 | CONFIRMED | connection point -803 kW (plus is import), +191 kvar; volts 0.992 to 1.006; busiest transformer 63%; inside every limit |
| 876 | SITE SURVEY | generic site 749 | CONFIRMED | connection point -4614 kW (plus is import), +5028 kvar; volts 0.927 to 1.000; busiest transformer 903%; export 4614 kW is 4114 kW over the 500 kW limit: the sol |
| 877 | SITE SURVEY | generic site 750 | CONFIRMED | connection point -2695 kW (plus is import), +742 kvar; volts 0.995 to 1.018; busiest transformer 208%; export 2695 kW is 2645 kW over the 50 kW limit: the solar |
| 878 | SITE SURVEY | generic site 751 | CONFIRMED | connection point -28 kW (plus is import), +838 kvar; volts 0.985 to 1.000; busiest transformer 71%; inside every limit |
| 879 | SITE SURVEY | generic site 752 | CONFIRMED | connection point -1779 kW (plus is import), +1338 kvar; volts 0.985 to 1.004; busiest transformer 568%; export 1779 kW is 1279 kW over the 500 kW limit: the sol |
| 880 | SITE SURVEY | generic site 753 | CONFIRMED | connection point -1106 kW (plus is import), +915 kvar; volts 0.987 to 1.011; busiest transformer 413%; export 1106 kW is 606 kW over the 500 kW limit: the solar |
| 881 | SITE SURVEY | generic site 754 | CONFIRMED | connection point -733 kW (plus is import), +276 kvar; volts 0.996 to 1.000; busiest transformer 57%; export 733 kW is 233 kW over the 500 kW limit: the solar mu |
| 882 | SITE SURVEY | generic site 755 | CONFIRMED | connection point -4206 kW (plus is import), +2569 kvar; volts 0.982 to 1.001; busiest transformer 586%; export 4206 kW is 3206 kW over the 1000 kW limit: the so |
| 883 | SITE SURVEY | generic site 756 | CONFIRMED | connection point -976 kW (plus is import), +432 kvar; volts 0.991 to 1.006; busiest transformer 93%; export 976 kW is 926 kW over the 50 kW limit: the solar mus |
| 884 | SITE SURVEY | generic site 757 | CONFIRMED | connection point -168 kW (plus is import), +485 kvar; volts 0.988 to 1.002; busiest transformer 91%; inside every limit |
| 885 | SITE SURVEY | generic site 758 | CONFIRMED | connection point -253 kW (plus is import), +373 kvar; volts 0.992 to 1.006; busiest transformer 157%; export 253 kW is 203 kW over the 50 kW limit: the solar mu |
| 886 | SITE SURVEY | generic site 759 | CONFIRMED | connection point -801 kW (plus is import), +210 kvar; volts 0.997 to 1.008; busiest transformer 124%; export 801 kW is 801 kW over the 0 kW limit: the solar mus |
| 887 | SITE SURVEY | generic site 760 | CONFIRMED | connection point -2104 kW (plus is import), +1153 kvar; volts 0.988 to 1.005; busiest transformer 560%; export 2104 kW is 1904 kW over the 200 kW limit: the sol |
| 888 | SITE SURVEY | generic site 761 | CONFIRMED | connection point -190 kW (plus is import), +395 kvar; volts 0.990 to 1.007; busiest transformer 157%; a transformer is at 157% of its rating |
| 889 | SITE SURVEY | generic site 762 | CONFIRMED | connection point -2266 kW (plus is import), +1093 kvar; volts 0.989 to 1.017; busiest transformer 331%; export 2266 kW is 2266 kW over the 0 kW limit: the solar |
| 890 | SITE SURVEY | generic site 763 | CONFIRMED | connection point -1089 kW (plus is import), +931 kvar; volts 0.987 to 1.010; busiest transformer 411%; export 1089 kW is 589 kW over the 500 kW limit: the solar |
| 891 | SITE SURVEY | generic site 764 | REFUTED | connection point -3782 kW (plus is import), +6548 kvar; volts 0.839 to 1.000; busiest transformer 1368%; export 3782 kW is 3732 kW over the 50 kW limit: the sol |
| 892 | SITE SURVEY | generic site 765 | CONFIRMED | connection point +50 kW (plus is import), +177 kvar; volts 0.994 to 1.000; busiest transformer 20%; inside every limit |
| 893 | SITE SURVEY | generic site 766 | CONFIRMED | connection point -1071 kW (plus is import), +406 kvar; volts 0.996 to 1.003; busiest transformer 69%; export 1071 kW is 1071 kW over the 0 kW limit: the solar m |
| 894 | SITE SURVEY | generic site 767 | CONFIRMED | connection point -2663 kW (plus is import), +1771 kvar; volts 0.986 to 1.012; busiest transformer 295%; export 2663 kW is 2663 kW over the 0 kW limit: the solar |
| 895 | SITE SURVEY | generic site 768 | CONFIRMED | connection point -92 kW (plus is import), +255 kvar; volts 0.992 to 1.000; busiest transformer 19%; export 92 kW is 92 kW over the 0 kW limit: the solar must be |
| 896 | SITE SURVEY | generic site 769 | CONFIRMED | connection point -1427 kW (plus is import), +401 kvar; volts 0.996 to 1.013; busiest transformer 218%; export 1427 kW is 1377 kW over the 50 kW limit: the solar |
| 897 | SITE SURVEY | generic site 770 | CONFIRMED | connection point -2215 kW (plus is import), +987 kvar; volts 0.993 to 1.016; busiest transformer 373%; export 2215 kW is 2165 kW over the 50 kW limit: the solar |
| 898 | SITE SURVEY | generic site 771 | CONFIRMED | connection point -1241 kW (plus is import), +541 kvar; volts 0.994 to 1.014; busiest transformer 339%; export 1241 kW is 1041 kW over the 200 kW limit: the sola |
| 899 | SITE SURVEY | generic site 772 | CONFIRMED | connection point -386 kW (plus is import), +183 kvar; volts 0.995 to 1.000; busiest transformer 25%; export 386 kW is 336 kW over the 50 kW limit: the solar mus |
| 900 | SITE SURVEY | generic site 773 | CONFIRMED | connection point -507 kW (plus is import), +459 kvar; volts 0.991 to 1.007; busiest transformer 143%; export 507 kW is 457 kW over the 50 kW limit: the solar mu |
| 901 | SITE SURVEY | generic site 774 | CONFIRMED | connection point -2034 kW (plus is import), +662 kvar; volts 0.994 to 1.017; busiest transformer 257%; export 2034 kW is 1534 kW over the 500 kW limit: the sola |
| 902 | SITE SURVEY | generic site 775 | CONFIRMED | connection point -452 kW (plus is import), +519 kvar; volts 0.989 to 1.003; busiest transformer 80%; export 452 kW is 252 kW over the 200 kW limit: the solar mu |
| 903 | SITE SURVEY | generic site 776 | CONFIRMED | connection point +122 kW (plus is import), +513 kvar; volts 0.989 to 1.000; busiest transformer 37%; inside every limit |
| 904 | SITE SURVEY | generic site 777 | CONFIRMED | connection point -1926 kW (plus is import), +960 kvar; volts 0.989 to 1.010; busiest transformer 505%; export 1926 kW is 1726 kW over the 200 kW limit: the sola |
| 905 | SITE SURVEY | generic site 778 | CONFIRMED | connection point -654 kW (plus is import), +169 kvar; volts 0.992 to 1.007; busiest transformer 84%; export 654 kW is 604 kW over the 50 kW limit: the solar mus |
| 906 | SITE SURVEY | generic site 779 | CONFIRMED | connection point -1593 kW (plus is import), +1065 kvar; volts 0.988 to 1.008; busiest transformer 154%; export 1593 kW is 1093 kW over the 500 kW limit: the sol |
| 907 | SITE SURVEY | generic site 780 | CONFIRMED | connection point -261 kW (plus is import), +298 kvar; volts 0.993 to 1.000; busiest transformer 63%; inside every limit |
| 908 | SITE SURVEY | generic site 781 | CONFIRMED | connection point -52 kW (plus is import), +272 kvar; volts 0.993 to 1.001; busiest transformer 59%; inside every limit |
| 909 | SITE SURVEY | generic site 782 | CONFIRMED | connection point -3013 kW (plus is import), +1735 kvar; volts 0.983 to 1.003; busiest transformer 527%; export 3013 kW is 2963 kW over the 50 kW limit: the sola |
| 910 | SITE SURVEY | generic site 783 | CONFIRMED | connection point -2896 kW (plus is import), +1228 kvar; volts 0.991 to 1.014; busiest transformer 207%; export 2896 kW is 2896 kW over the 0 kW limit: the solar |
| 911 | SITE SURVEY | generic site 784 | CONFIRMED | connection point -1986 kW (plus is import), +1091 kvar; volts 0.989 to 1.011; busiest transformer 371%; export 1986 kW is 1936 kW over the 50 kW limit: the sola |
| 912 | SITE SURVEY | generic site 785 | CONFIRMED | connection point -3427 kW (plus is import), +1628 kvar; volts 0.987 to 1.014; busiest transformer 458%; export 3427 kW is 2427 kW over the 1000 kW limit: the so |
| 913 | SITE SURVEY | generic site 786 | CONFIRMED | connection point -636 kW (plus is import), +748 kvar; volts 0.988 to 1.009; busiest transformer 177%; export 636 kW is 586 kW over the 50 kW limit: the solar mu |
| 914 | SITE SURVEY | generic site 787 | CONFIRMED | connection point -1502 kW (plus is import), +514 kvar; volts 0.993 to 1.008; busiest transformer 108%; export 1502 kW is 1502 kW over the 0 kW limit: the solar  |
| 915 | SITE SURVEY | generic site 788 | CONFIRMED | connection point -1506 kW (plus is import), +847 kvar; volts 0.990 to 1.008; busiest transformer 156%; export 1506 kW is 1506 kW over the 0 kW limit: the solar  |
| 916 | SITE SURVEY | generic site 789 | CONFIRMED | connection point -1863 kW (plus is import), +607 kvar; volts 0.994 to 1.017; busiest transformer 242%; export 1863 kW is 1663 kW over the 200 kW limit: the sola |
| 917 | SITE SURVEY | generic site 790 | CONFIRMED | connection point -2936 kW (plus is import), +2795 kvar; volts 0.950 to 1.000; busiest transformer 872%; export 2936 kW is 2736 kW over the 200 kW limit: the sol |
| 918 | SITE SURVEY | generic site 791 | CONFIRMED | connection point -2555 kW (plus is import), +2401 kvar; volts 0.970 to 1.000; busiest transformer 801%; export 2555 kW is 2555 kW over the 0 kW limit: the solar |
| 919 | SITE SURVEY | generic site 792 | CONFIRMED | connection point -3856 kW (plus is import), +1596 kvar; volts 0.992 to 1.016; busiest transformer 322%; export 3856 kW is 3856 kW over the 0 kW limit: the solar |
| 920 | SITE SURVEY | generic site 793 | CONFIRMED | connection point +286 kW (plus is import), +1097 kvar; volts 0.983 to 1.005; busiest transformer 287%; a transformer is at 287% of its rating |
| 921 | SITE SURVEY | generic site 794 | CONFIRMED | connection point -1767 kW (plus is import), +552 kvar; volts 0.991 to 1.004; busiest transformer 139%; export 1767 kW is 1567 kW over the 200 kW limit: the sola |
| 922 | SITE SURVEY | generic site 795 | CONFIRMED | connection point -1070 kW (plus is import), +632 kvar; volts 0.992 to 1.014; busiest transformer 340%; export 1070 kW is 570 kW over the 500 kW limit: the solar |
| 923 | SITE SURVEY | generic site 796 | CONFIRMED | connection point -1310 kW (plus is import), +1099 kvar; volts 0.986 to 1.006; busiest transformer 142%; export 1310 kW is 1260 kW over the 50 kW limit: the sola |
| 924 | SITE SURVEY | generic site 797 | CONFIRMED | connection point -1564 kW (plus is import), +799 kvar; volts 0.990 to 1.012; busiest transformer 164%; export 1564 kW is 1564 kW over the 0 kW limit: the solar  |
| 925 | SITE SURVEY | generic site 798 | CONFIRMED | connection point -3895 kW (plus is import), +1930 kvar; volts 0.982 to 1.006; busiest transformer 511%; export 3895 kW is 2895 kW over the 1000 kW limit: the so |
| 926 | SITE SURVEY | generic site 799 | REFUTED | connection point -5057 kW (plus is import), +4605 kvar; volts 0.964 to 1.083; busiest transformer 1694%; export 5057 kW is 4857 kW over the 200 kW limit: the so |
| 927 | SITE SURVEY | generic site 800 | CONFIRMED | connection point -3556 kW (plus is import), +1451 kvar; volts 0.991 to 1.018; busiest transformer 300%; export 3556 kW is 2556 kW over the 1000 kW limit: the so |
| 928 | SITE SURVEY | generic site 801 | CONFIRMED | connection point -790 kW (plus is import), +152 kvar; volts 0.997 to 1.006; busiest transformer 57%; inside every limit |
| 929 | SITE SURVEY | generic site 802 | CONFIRMED | connection point -3963 kW (plus is import), +3212 kvar; volts 0.976 to 1.000; busiest transformer 735%; export 3963 kW is 3963 kW over the 0 kW limit: the solar |
| 930 | SITE SURVEY | generic site 803 | CONFIRMED | connection point -792 kW (plus is import), +202 kvar; volts 0.993 to 1.008; busiest transformer 121%; a transformer is at 121% of its rating |
| 931 | SITE SURVEY | generic site 804 | CONFIRMED | connection point +101 kW (plus is import), +315 kvar; volts 0.991 to 1.005; busiest transformer 92%; inside every limit |
| 932 | SITE SURVEY | generic site 805 | CONFIRMED | connection point -578 kW (plus is import), +640 kvar; volts 0.989 to 1.000; busiest transformer 68%; export 578 kW is 528 kW over the 50 kW limit: the solar mus |
| 933 | SITE SURVEY | generic site 806 | CONFIRMED | connection point -589 kW (plus is import), +670 kvar; volts 0.988 to 1.003; busiest transformer 99%; export 589 kW is 589 kW over the 0 kW limit: the solar must |
| 934 | SITE SURVEY | generic site 807 | CONFIRMED | connection point -447 kW (plus is import), +401 kvar; volts 0.989 to 1.005; busiest transformer 105%; export 447 kW is 397 kW over the 50 kW limit: the solar mu |
| 935 | SITE SURVEY | generic site 808 | CONFIRMED | connection point -2317 kW (plus is import), +894 kvar; volts 0.993 to 1.013; busiest transformer 200%; export 2317 kW is 2117 kW over the 200 kW limit: the sola |
| 936 | SITE SURVEY | generic site 809 | CONFIRMED | connection point -178 kW (plus is import), +212 kvar; volts 0.994 to 1.000; busiest transformer 27%; export 178 kW is 178 kW over the 0 kW limit: the solar must |
| 937 | SITE SURVEY | generic site 810 | REFUTED | connection point -3322 kW (plus is import), +6319 kvar; volts 0.802 to 1.000; busiest transformer 1229%; export 3322 kW is 3272 kW over the 50 kW limit: the sol |
| 938 | SITE SURVEY | generic site 811 | CONFIRMED | connection point -252 kW (plus is import), +163 kvar; volts 0.991 to 1.001; busiest transformer 28%; export 252 kW is 252 kW over the 0 kW limit: the solar must |
| 939 | SITE SURVEY | generic site 812 | CONFIRMED | connection point -1341 kW (plus is import), +401 kvar; volts 0.992 to 1.009; busiest transformer 166%; export 1341 kW is 1291 kW over the 50 kW limit: the solar |
| 940 | SITE SURVEY | generic site 813 | CONFIRMED | connection point -755 kW (plus is import), +423 kvar; volts 0.990 to 1.003; busiest transformer 81%; export 755 kW is 555 kW over the 200 kW limit: the solar mu |
| 941 | SITE SURVEY | generic site 814 | CONFIRMED | connection point -481 kW (plus is import), +685 kvar; volts 0.987 to 1.012; busiest transformer 283%; a transformer is at 283% of its rating |
| 942 | SITE SURVEY | generic site 815 | CONFIRMED | connection point -700 kW (plus is import), +135 kvar; volts 0.998 to 1.004; busiest transformer 49%; export 700 kW is 650 kW over the 50 kW limit: the solar mus |
| 943 | SITE SURVEY | generic site 816 | CONFIRMED | connection point -352 kW (plus is import), +181 kvar; volts 0.996 to 1.002; busiest transformer 59%; inside every limit |
| 944 | SITE SURVEY | generic site 817 | CONFIRMED | connection point -79 kW (plus is import), +324 kvar; volts 0.991 to 1.000; busiest transformer 53%; inside every limit |
| 945 | SITE SURVEY | generic site 818 | CONFIRMED | connection point -1841 kW (plus is import), +762 kvar; volts 0.994 to 1.015; busiest transformer 311%; export 1841 kW is 841 kW over the 1000 kW limit: the sola |
| 946 | SITE SURVEY | generic site 819 | CONFIRMED | connection point -680 kW (plus is import), +323 kvar; volts 0.993 to 1.007; busiest transformer 110%; export 680 kW is 180 kW over the 500 kW limit: the solar m |
| 947 | SITE SURVEY | generic site 820 | CONFIRMED | connection point +80 kW (plus is import), +296 kvar; volts 0.989 to 1.000; busiest transformer 42%; inside every limit |
| 948 | SITE SURVEY | generic site 821 | CONFIRMED | connection point -1925 kW (plus is import), +778 kvar; volts 0.992 to 1.013; busiest transformer 176%; export 1925 kW is 1925 kW over the 0 kW limit: the solar  |
| 949 | SITE SURVEY | generic site 822 | CONFIRMED | connection point -307 kW (plus is import), +179 kvar; volts 0.994 to 1.000; busiest transformer 29%; inside every limit |
| 950 | SITE SURVEY | generic site 823 | CONFIRMED | connection point -2624 kW (plus is import), +2238 kvar; volts 0.974 to 1.000; busiest transformer 780%; export 2624 kW is 2424 kW over the 200 kW limit: the sol |
| 951 | SITE SURVEY | generic site 824 | CONFIRMED | connection point -413 kW (plus is import), +658 kvar; volts 0.988 to 1.012; busiest transformer 268%; export 413 kW is 213 kW over the 200 kW limit: the solar m |
| 952 | SITE SURVEY | generic site 825 | CONFIRMED | connection point -1070 kW (plus is import), +429 kvar; volts 0.990 to 1.009; busiest transformer 154%; export 1070 kW is 1020 kW over the 50 kW limit: the solar |
| 953 | SITE SURVEY | generic site 826 | CONFIRMED | connection point -3791 kW (plus is import), +1166 kvar; volts 0.990 to 1.009; busiest transformer 232%; export 3791 kW is 3741 kW over the 50 kW limit: the sola |
| 954 | SITE SURVEY | generic site 827 | CONFIRMED | connection point -738 kW (plus is import), +413 kvar; volts 0.993 to 1.000; busiest transformer 73%; export 738 kW is 238 kW over the 500 kW limit: the solar mu |
| 955 | SITE SURVEY | generic site 828 | CONFIRMED | connection point -1050 kW (plus is import), +349 kvar; volts 0.992 to 1.009; busiest transformer 172%; export 1050 kW is 1050 kW over the 0 kW limit: the solar  |
| 956 | SITE SURVEY | generic site 829 | CONFIRMED | connection point -1173 kW (plus is import), +375 kvar; volts 0.994 to 1.015; busiest transformer 287%; export 1173 kW is 973 kW over the 200 kW limit: the solar |
| 957 | SITE SURVEY | generic site 830 | CONFIRMED | connection point -25 kW (plus is import), +120 kvar; volts 0.995 to 1.000; busiest transformer 14%; inside every limit |
| 958 | SITE SURVEY | generic site 831 | CONFIRMED | connection point -70 kW (plus is import), +368 kvar; volts 0.988 to 1.000; busiest transformer 27%; inside every limit |
| 959 | SITE SURVEY | generic site 832 | CONFIRMED | connection point -1547 kW (plus is import), +810 kvar; volts 0.991 to 1.005; busiest transformer 124%; export 1547 kW is 1497 kW over the 50 kW limit: the solar |
| 960 | SITE SURVEY | generic site 833 | CONFIRMED | connection point -3509 kW (plus is import), +1080 kvar; volts 0.992 to 1.018; busiest transformer 225%; export 3509 kW is 2509 kW over the 1000 kW limit: the so |
| 961 | SITE SURVEY | generic site 834 | CONFIRMED | connection point -1484 kW (plus is import), +680 kvar; volts 0.989 to 1.012; busiest transformer 219%; export 1484 kW is 984 kW over the 500 kW limit: the solar |
| 962 | SITE SURVEY | generic site 835 | CONFIRMED | connection point -4260 kW (plus is import), +2463 kvar; volts 0.982 to 1.003; busiest transformer 579%; export 4260 kW is 4060 kW over the 200 kW limit: the sol |
| 963 | SITE SURVEY | generic site 836 | CONFIRMED | connection point -1094 kW (plus is import), +460 kvar; volts 0.990 to 1.015; busiest transformer 302%; export 1094 kW is 1094 kW over the 0 kW limit: the solar  |
| 964 | SITE SURVEY | generic site 837 | CONFIRMED | connection point -4327 kW (plus is import), +1820 kvar; volts 0.988 to 1.010; busiest transformer 296%; export 4327 kW is 4277 kW over the 50 kW limit: the sola |
| 965 | SITE SURVEY | generic site 838 | CONFIRMED | connection point -2044 kW (plus is import), +1682 kvar; volts 0.982 to 1.010; busiest transformer 465%; export 2044 kW is 1994 kW over the 50 kW limit: the sola |
| 966 | SITE SURVEY | generic site 839 | CONFIRMED | connection point -1567 kW (plus is import), +1186 kvar; volts 0.986 to 1.007; busiest transformer 516%; export 1567 kW is 1067 kW over the 500 kW limit: the sol |
| 967 | SITE SURVEY | generic site 840 | CONFIRMED | connection point -1002 kW (plus is import), +497 kvar; volts 0.992 to 1.000; busiest transformer 74%; export 1002 kW is 502 kW over the 500 kW limit: the solar  |
| 968 | SITE SURVEY | generic site 841 | CONFIRMED | connection point -5631 kW (plus is import), +2975 kvar; volts 0.978 to 1.005; busiest transformer 485%; export 5631 kW is 5631 kW over the 0 kW limit: the solar |
| 969 | SITE SURVEY | generic site 842 | CONFIRMED | connection point -641 kW (plus is import), +186 kvar; volts 0.997 to 1.003; busiest transformer 41%; export 641 kW is 641 kW over the 0 kW limit: the solar must |
| 970 | SITE SURVEY | generic site 843 | CONFIRMED | connection point -4308 kW (plus is import), +3375 kvar; volts 0.973 to 1.000; busiest transformer 769%; export 4308 kW is 4308 kW over the 0 kW limit: the solar |
| 971 | SITE SURVEY | generic site 844 | CONFIRMED | connection point -4462 kW (plus is import), +1633 kvar; volts 0.988 to 1.014; busiest transformer 291%; export 4462 kW is 4462 kW over the 0 kW limit: the solar |
| 972 | SITE SURVEY | generic site 845 | CONFIRMED | connection point -534 kW (plus is import), +182 kvar; volts 0.993 to 1.002; busiest transformer 68%; export 534 kW is 334 kW over the 200 kW limit: the solar mu |
| 973 | SITE SURVEY | generic site 846 | CONFIRMED | connection point +96 kW (plus is import), +155 kvar; volts 0.992 to 1.000; busiest transformer 17%; inside every limit |
| 974 | SITE SURVEY | generic site 847 | CONFIRMED | connection point -2177 kW (plus is import), +1044 kvar; volts 0.989 to 1.016; busiest transformer 214%; export 2177 kW is 1677 kW over the 500 kW limit: the sol |
| 975 | SITE SURVEY | generic site 848 | CONFIRMED | connection point +24 kW (plus is import), +867 kvar; volts 0.985 to 1.005; busiest transformer 176%; a transformer is at 176% of its rating |
| 976 | SITE SURVEY | generic site 849 | CONFIRMED | connection point -1022 kW (plus is import), +330 kvar; volts 0.991 to 1.012; busiest transformer 255%; export 1022 kW is 822 kW over the 200 kW limit: the solar |
| 977 | SITE SURVEY | generic site 850 | CONFIRMED | connection point -737 kW (plus is import), +1352 kvar; volts 0.984 to 1.008; busiest transformer 469%; export 737 kW is 537 kW over the 200 kW limit: the solar  |
| 978 | SITE SURVEY | generic site 851 | CONFIRMED | connection point -602 kW (plus is import), +944 kvar; volts 0.986 to 1.010; busiest transformer 359%; a transformer is at 359% of its rating |
| 979 | SITE SURVEY | generic site 852 | REFUTED | connection point -5055 kW (plus is import), +7622 kvar; volts 0.812 to 1.000; busiest transformer 1020%; export 5055 kW is 5055 kW over the 0 kW limit: the sola |
| 980 | SITE SURVEY | generic site 853 | CONFIRMED | connection point -540 kW (plus is import), +547 kvar; volts 0.989 to 1.004; busiest transformer 128%; export 540 kW is 540 kW over the 0 kW limit: the solar mus |
| 981 | SITE SURVEY | generic site 854 | CONFIRMED | connection point +290 kW (plus is import), +892 kvar; volts 0.984 to 1.000; busiest transformer 56%; inside every limit |
| 982 | SITE SURVEY | generic site 855 | CONFIRMED | connection point -1628 kW (plus is import), +726 kvar; volts 0.992 to 1.018; busiest transformer 433%; export 1628 kW is 1578 kW over the 50 kW limit: the solar |
| 983 | SITE SURVEY | generic site 856 | CONFIRMED | connection point -1433 kW (plus is import), +471 kvar; volts 0.995 to 1.011; busiest transformer 229%; export 1433 kW is 1433 kW over the 0 kW limit: the solar  |
| 984 | SITE SURVEY | generic site 857 | CONFIRMED | connection point -3219 kW (plus is import), +994 kvar; volts 0.994 to 1.016; busiest transformer 248%; export 3219 kW is 3219 kW over the 0 kW limit: the solar  |
| 985 | SITE SURVEY | generic site 858 | CONFIRMED | connection point -3688 kW (plus is import), +1359 kvar; volts 0.989 to 1.016; busiest transformer 299%; export 3688 kW is 3188 kW over the 500 kW limit: the sol |
| 986 | SITE SURVEY | generic site 859 | CONFIRMED | connection point -1261 kW (plus is import), +785 kvar; volts 0.987 to 1.007; busiest transformer 120%; export 1261 kW is 1211 kW over the 50 kW limit: the solar |
| 987 | SITE SURVEY | generic site 860 | CONFIRMED | connection point -2141 kW (plus is import), +812 kvar; volts 0.993 to 1.014; busiest transformer 343%; export 2141 kW is 1941 kW over the 200 kW limit: the sola |
| 988 | SITE SURVEY | generic site 861 | CONFIRMED | connection point -2436 kW (plus is import), +924 kvar; volts 0.993 to 1.010; busiest transformer 206%; export 2436 kW is 1936 kW over the 500 kW limit: the sola |
| 989 | SITE SURVEY | generic site 862 | CONFIRMED | connection point -765 kW (plus is import), +647 kvar; volts 0.988 to 1.011; busiest transformer 208%; export 765 kW is 715 kW over the 50 kW limit: the solar mu |
| 990 | SITE SURVEY | generic site 863 | CONFIRMED | connection point -1535 kW (plus is import), +798 kvar; volts 0.990 to 1.007; busiest transformer 154%; export 1535 kW is 1485 kW over the 50 kW limit: the solar |
| 991 | SITE SURVEY | generic site 864 | CONFIRMED | connection point -1478 kW (plus is import), +378 kvar; volts 0.995 to 1.012; busiest transformer 119%; export 1478 kW is 1428 kW over the 50 kW limit: the solar |
| 992 | SITE SURVEY | generic site 865 | CONFIRMED | connection point -2566 kW (plus is import), +931 kvar; volts 0.993 to 1.015; busiest transformer 217%; export 2566 kW is 2516 kW over the 50 kW limit: the solar |
| 993 | SITE SURVEY | generic site 866 | CONFIRMED | connection point -426 kW (plus is import), +108 kvar; volts 0.998 to 1.004; busiest transformer 99%; inside every limit |
| 994 | SITE SURVEY | generic site 867 | CONFIRMED | connection point -4712 kW (plus is import), +1605 kvar; volts 0.986 to 1.012; busiest transformer 301%; export 4712 kW is 4212 kW over the 500 kW limit: the sol |
| 995 | SITE SURVEY | generic site 868 | CONFIRMED | connection point -1786 kW (plus is import), +553 kvar; volts 0.989 to 1.006; busiest transformer 143%; export 1786 kW is 1786 kW over the 0 kW limit: the solar  |
| 996 | SITE SURVEY | generic site 869 | CONFIRMED | connection point -890 kW (plus is import), +917 kvar; volts 0.987 to 1.012; busiest transformer 389%; export 890 kW is 690 kW over the 200 kW limit: the solar m |
| 997 | SITE SURVEY | generic site 870 | CONFIRMED | connection point +239 kW (plus is import), +471 kvar; volts 0.990 to 1.000; busiest transformer 17%; inside every limit |
| 998 | SITE SURVEY | generic site 871 | CONFIRMED | connection point -2720 kW (plus is import), +699 kvar; volts 0.997 to 1.014; busiest transformer 161%; export 2720 kW is 1720 kW over the 1000 kW limit: the sol |
| 999 | SITE SURVEY | generic site 872 | CONFIRMED | connection point -939 kW (plus is import), +943 kvar; volts 0.986 to 1.001; busiest transformer 112%; export 939 kW is 939 kW over the 0 kW limit: the solar mus |
| 1000 | SITE SURVEY | generic site 873 | CONFIRMED | connection point -1236 kW (plus is import), +608 kvar; volts 0.992 to 1.014; busiest transformer 196%; export 1236 kW is 1036 kW over the 200 kW limit: the sola |
| 1001 | SITE SURVEY | generic site 874 | CONFIRMED | connection point -1810 kW (plus is import), +1043 kvar; volts 0.988 to 1.010; busiest transformer 514%; export 1810 kW is 1610 kW over the 200 kW limit: the sol |
| 1002 | SITE SURVEY | generic site 875 | CONFIRMED | connection point +260 kW (plus is import), +554 kvar; volts 0.987 to 1.000; busiest transformer 34%; inside every limit |
| 1003 | SITE SURVEY | generic site 876 | CONFIRMED | connection point -1765 kW (plus is import), +1655 kvar; volts 0.984 to 1.001; busiest transformer 627%; export 1765 kW is 1765 kW over the 0 kW limit: the solar |
| 1004 | SITE SURVEY | generic site 877 | CONFIRMED | connection point -635 kW (plus is import), +376 kvar; volts 0.989 to 1.002; busiest transformer 59%; export 635 kW is 585 kW over the 50 kW limit: the solar mus |
| 1005 | SITE SURVEY | generic site 878 | CONFIRMED | connection point -425 kW (plus is import), +826 kvar; volts 0.987 to 1.007; busiest transformer 170%; export 425 kW is 225 kW over the 200 kW limit: the solar m |
| 1006 | SITE SURVEY | generic site 879 | CONFIRMED | connection point -502 kW (plus is import), +212 kvar; volts 0.995 to 1.007; busiest transformer 98%; export 502 kW is 502 kW over the 0 kW limit: the solar must |
| 1007 | SITE SURVEY | generic site 880 | CONFIRMED | connection point -4 kW (plus is import), +252 kvar; volts 0.991 to 1.000; busiest transformer 22%; inside every limit |
| 1008 | SITE SURVEY | generic site 881 | CONFIRMED | connection point -3025 kW (plus is import), +1008 kvar; volts 0.992 to 1.013; busiest transformer 198%; export 3025 kW is 3025 kW over the 0 kW limit: the solar |
| 1009 | SITE SURVEY | generic site 882 | CONFIRMED | connection point -520 kW (plus is import), +278 kvar; volts 0.996 to 1.000; busiest transformer 33%; export 520 kW is 470 kW over the 50 kW limit: the solar mus |
| 1010 | SITE SURVEY | generic site 883 | CONFIRMED | connection point +16 kW (plus is import), +499 kvar; volts 0.988 to 1.001; busiest transformer 99%; inside every limit |
| 1011 | SITE SURVEY | generic site 884 | CONFIRMED | connection point -1794 kW (plus is import), +1052 kvar; volts 0.987 to 1.013; busiest transformer 354%; export 1794 kW is 1744 kW over the 50 kW limit: the sola |
| 1012 | SITE SURVEY | generic site 885 | CONFIRMED | connection point -1998 kW (plus is import), +542 kvar; volts 0.997 to 1.012; busiest transformer 150%; export 1998 kW is 1948 kW over the 50 kW limit: the solar |
| 1013 | SITE SURVEY | generic site 886 | CONFIRMED | connection point -1017 kW (plus is import), +429 kvar; volts 0.993 to 1.007; busiest transformer 147%; export 1017 kW is 1017 kW over the 0 kW limit: the solar  |
| 1014 | SITE SURVEY | generic site 887 | CONFIRMED | connection point -2413 kW (plus is import), +1581 kvar; volts 0.985 to 1.007; busiest transformer 467%; export 2413 kW is 2363 kW over the 50 kW limit: the sola |
| 1015 | SITE SURVEY | generic site 888 | CONFIRMED | connection point -1974 kW (plus is import), +454 kvar; volts 0.994 to 1.010; busiest transformer 144%; export 1974 kW is 1474 kW over the 500 kW limit: the sola |
| 1016 | SITE SURVEY | generic site 889 | CONFIRMED | connection point +54 kW (plus is import), +583 kvar; volts 0.987 to 1.000; busiest transformer 50%; inside every limit |
| 1017 | SITE SURVEY | generic site 890 | CONFIRMED | connection point -994 kW (plus is import), +292 kvar; volts 0.996 to 1.001; busiest transformer 57%; export 994 kW is 494 kW over the 500 kW limit: the solar mu |
| 1018 | SITE SURVEY | generic site 891 | CONFIRMED | connection point -538 kW (plus is import), +738 kvar; volts 0.988 to 1.010; busiest transformer 205%; export 538 kW is 538 kW over the 0 kW limit: the solar mus |
| 1019 | SITE SURVEY | generic site 892 | CONFIRMED | connection point -1385 kW (plus is import), +571 kvar; volts 0.992 to 1.014; busiest transformer 243%; export 1385 kW is 385 kW over the 1000 kW limit: the sola |
| 1020 | SITE SURVEY | generic site 893 | CONFIRMED | connection point -3023 kW (plus is import), +1308 kvar; volts 0.992 to 1.020; busiest transformer 403%; export 3023 kW is 2823 kW over the 200 kW limit: the sol |
| 1021 | SITE SURVEY | generic site 894 | CONFIRMED | connection point -2375 kW (plus is import), +942 kvar; volts 0.988 to 1.015; busiest transformer 385%; export 2375 kW is 2175 kW over the 200 kW limit: the sola |
| 1022 | SITE SURVEY | generic site 895 | CONFIRMED | connection point -2953 kW (plus is import), +1858 kvar; volts 0.983 to 1.006; busiest transformer 542%; export 2953 kW is 1953 kW over the 1000 kW limit: the so |
| 1023 | SITE SURVEY | generic site 896 | CONFIRMED | connection point -1324 kW (plus is import), +353 kvar; volts 0.992 to 1.006; busiest transformer 86%; export 1324 kW is 1324 kW over the 0 kW limit: the solar m |
| 1024 | SITE SURVEY | generic site 897 | CONFIRMED | connection point -356 kW (plus is import), +126 kvar; volts 0.993 to 1.001; busiest transformer 29%; export 356 kW is 356 kW over the 0 kW limit: the solar must |
| 1025 | SITE SURVEY | generic site 898 | CONFIRMED | connection point -2765 kW (plus is import), +786 kvar; volts 0.993 to 1.012; busiest transformer 212%; export 2765 kW is 2715 kW over the 50 kW limit: the solar |
| 1026 | SITE SURVEY | generic site 899 | CONFIRMED | connection point -4102 kW (plus is import), +2602 kvar; volts 0.981 to 1.000; busiest transformer 586%; export 4102 kW is 3102 kW over the 1000 kW limit: the so |
| 1027 | SITE SURVEY | generic site 900 | CONFIRMED | connection point -340 kW (plus is import), +534 kvar; volts 0.990 to 1.009; busiest transformer 219%; a transformer is at 219% of its rating |
| 1028 | SITE SURVEY | generic site 901 | CONFIRMED | connection point -1999 kW (plus is import), +627 kvar; volts 0.990 to 1.010; busiest transformer 164%; export 1999 kW is 1799 kW over the 200 kW limit: the sola |
| 1029 | SITE SURVEY | generic site 902 | CONFIRMED | connection point -308 kW (plus is import), +447 kvar; volts 0.990 to 1.002; busiest transformer 115%; a transformer is at 115% of its rating |
| 1030 | SITE SURVEY | generic site 903 | CONFIRMED | connection point -23 kW (plus is import), +72 kvar; volts 0.995 to 1.000; busiest transformer 14%; inside every limit |
| 1031 | SITE SURVEY | generic site 904 | CONFIRMED | connection point -594 kW (plus is import), +578 kvar; volts 0.989 to 1.002; busiest transformer 72%; export 594 kW is 594 kW over the 0 kW limit: the solar must |
| 1032 | SITE SURVEY | generic site 905 | CONFIRMED | connection point -1456 kW (plus is import), +1295 kvar; volts 0.983 to 1.008; busiest transformer 304%; export 1456 kW is 1406 kW over the 50 kW limit: the sola |
| 1033 | SITE SURVEY | generic site 906 | CONFIRMED | connection point -116 kW (plus is import), +171 kvar; volts 0.991 to 1.000; busiest transformer 25%; inside every limit |
| 1034 | SITE SURVEY | generic site 907 | CONFIRMED | connection point -1086 kW (plus is import), +1201 kvar; volts 0.984 to 1.012; busiest transformer 326%; export 1086 kW is 86 kW over the 1000 kW limit: the sola |
| 1035 | SITE SURVEY | generic site 908 | CONFIRMED | connection point -2252 kW (plus is import), +1149 kvar; volts 0.988 to 1.012; busiest transformer 331%; export 2252 kW is 2202 kW over the 50 kW limit: the sola |
| 1036 | SITE SURVEY | generic site 909 | CONFIRMED | connection point -1740 kW (plus is import), +500 kvar; volts 0.993 to 1.008; busiest transformer 136%; export 1740 kW is 1240 kW over the 500 kW limit: the sola |
| 1037 | SITE SURVEY | generic site 910 | CONFIRMED | connection point -1374 kW (plus is import), +992 kvar; volts 0.987 to 1.012; busiest transformer 263%; export 1374 kW is 1324 kW over the 50 kW limit: the solar |
| 1038 | SITE SURVEY | generic site 911 | CONFIRMED | connection point -860 kW (plus is import), +726 kvar; volts 0.987 to 1.009; busiest transformer 223%; export 860 kW is 360 kW over the 500 kW limit: the solar m |
| 1039 | SITE SURVEY | generic site 912 | CONFIRMED | connection point -2570 kW (plus is import), +1170 kvar; volts 0.992 to 1.019; busiest transformer 360%; export 2570 kW is 1570 kW over the 1000 kW limit: the so |
| 1040 | SITE SURVEY | generic site 913 | CONFIRMED | connection point -1275 kW (plus is import), +272 kvar; volts 0.995 to 1.003; busiest transformer 69%; export 1275 kW is 1075 kW over the 200 kW limit: the solar |
| 1041 | SITE SURVEY | generic site 914 | CONFIRMED | connection point -1041 kW (plus is import), +249 kvar; volts 0.993 to 1.005; busiest transformer 63%; export 1041 kW is 841 kW over the 200 kW limit: the solar  |
| 1042 | SITE SURVEY | generic site 915 | CONFIRMED | connection point -364 kW (plus is import), +258 kvar; volts 0.991 to 1.000; busiest transformer 65%; export 364 kW is 164 kW over the 200 kW limit: the solar mu |
| 1043 | SITE SURVEY | generic site 916 | CONFIRMED | connection point -7356 kW (plus is import), +4003 kvar; volts 0.968 to 1.000; busiest transformer 505%; export 7356 kW is 6356 kW over the 1000 kW limit: the so |
| 1044 | SITE SURVEY | generic site 917 | CONFIRMED | connection point -899 kW (plus is import), +1252 kvar; volts 0.984 to 1.010; busiest transformer 468%; export 899 kW is 699 kW over the 200 kW limit: the solar  |
| 1045 | SITE SURVEY | generic site 918 | CONFIRMED | connection point -3786 kW (plus is import), +1839 kvar; volts 0.986 to 1.011; busiest transformer 340%; export 3786 kW is 3286 kW over the 500 kW limit: the sol |
| 1046 | SITE SURVEY | generic site 919 | CONFIRMED | connection point -2957 kW (plus is import), +1496 kvar; volts 0.988 to 1.010; busiest transformer 227%; export 2957 kW is 2957 kW over the 0 kW limit: the solar |
| 1047 | SITE SURVEY | generic site 920 | CONFIRMED | connection point -916 kW (plus is import), +776 kvar; volts 0.988 to 1.012; busiest transformer 241%; export 916 kW is 866 kW over the 50 kW limit: the solar mu |
| 1048 | SITE SURVEY | generic site 921 | CONFIRMED | connection point -27 kW (plus is import), +330 kvar; volts 0.991 to 1.000; busiest transformer 53%; inside every limit |
| 1049 | SITE SURVEY | generic site 922 | CONFIRMED | connection point -137 kW (plus is import), +417 kvar; volts 0.988 to 1.000; busiest transformer 28%; inside every limit |
| 1050 | SITE SURVEY | generic site 923 | CONFIRMED | connection point -448 kW (plus is import), +1091 kvar; volts 0.984 to 1.003; busiest transformer 138%; a transformer is at 138% of its rating |
| 1051 | SITE SURVEY | generic site 924 | CONFIRMED | connection point -1462 kW (plus is import), +697 kvar; volts 0.991 to 1.015; busiest transformer 227%; export 1462 kW is 1262 kW over the 200 kW limit: the sola |
| 1052 | SITE SURVEY | generic site 925 | CONFIRMED | connection point +25 kW (plus is import), +126 kvar; volts 0.990 to 1.000; busiest transformer 26%; inside every limit |
| 1053 | SITE SURVEY | generic site 926 | CONFIRMED | connection point -2786 kW (plus is import), +1183 kvar; volts 0.992 to 1.016; busiest transformer 246%; export 2786 kW is 2286 kW over the 500 kW limit: the sol |
| 1054 | SITE SURVEY | generic site 927 | CONFIRMED | connection point -380 kW (plus is import), +718 kvar; volts 0.987 to 1.010; busiest transformer 276%; export 380 kW is 330 kW over the 50 kW limit: the solar mu |
| 1055 | SITE SURVEY | generic site 928 | CONFIRMED | connection point -3000 kW (plus is import), +988 kvar; volts 0.994 to 1.020; busiest transformer 201%; export 3000 kW is 2950 kW over the 50 kW limit: the solar |
| 1056 | SITE SURVEY | generic site 929 | CONFIRMED | connection point -2698 kW (plus is import), +1906 kvar; volts 0.983 to 1.000; busiest transformer 737%; export 2698 kW is 2648 kW over the 50 kW limit: the sola |
| 1057 | SITE SURVEY | generic site 930 | CONFIRMED | connection point -996 kW (plus is import), +668 kvar; volts 0.990 to 1.008; busiest transformer 185%; export 996 kW is 796 kW over the 200 kW limit: the solar m |
| 1058 | SITE SURVEY | generic site 931 | CONFIRMED | connection point -1373 kW (plus is import), +1688 kvar; volts 0.982 to 1.009; busiest transformer 418%; export 1373 kW is 1323 kW over the 50 kW limit: the sola |
| 1059 | SITE SURVEY | generic site 932 | CONFIRMED | connection point -2956 kW (plus is import), +2964 kvar; volts 0.938 to 1.000; busiest transformer 892%; export 2956 kW is 2456 kW over the 500 kW limit: the sol |
| 1060 | SITE SURVEY | generic site 933 | CONFIRMED | connection point -1098 kW (plus is import), +774 kvar; volts 0.988 to 1.012; busiest transformer 379%; export 1098 kW is 1048 kW over the 50 kW limit: the solar |
| 1061 | SITE SURVEY | generic site 934 | CONFIRMED | connection point -1201 kW (plus is import), +478 kvar; volts 0.992 to 1.012; busiest transformer 177%; export 1201 kW is 201 kW over the 1000 kW limit: the sola |
| 1062 | SITE SURVEY | generic site 935 | CONFIRMED | connection point -4069 kW (plus is import), +3077 kvar; volts 0.977 to 1.000; busiest transformer 620%; export 4069 kW is 3869 kW over the 200 kW limit: the sol |
| 1063 | SITE SURVEY | generic site 936 | CONFIRMED | connection point -2577 kW (plus is import), +616 kvar; volts 0.996 to 1.010; busiest transformer 184%; export 2577 kW is 2527 kW over the 50 kW limit: the solar |
| 1064 | SITE SURVEY | generic site 937 | CONFIRMED | connection point -542 kW (plus is import), +624 kvar; volts 0.988 to 1.000; busiest transformer 65%; export 542 kW is 342 kW over the 200 kW limit: the solar mu |
| 1065 | SITE SURVEY | generic site 938 | CONFIRMED | connection point -617 kW (plus is import), +492 kvar; volts 0.992 to 1.006; busiest transformer 156%; export 617 kW is 617 kW over the 0 kW limit: the solar mus |
| 1066 | SITE SURVEY | generic site 939 | CONFIRMED | connection point -374 kW (plus is import), +112 kvar; volts 0.996 to 1.005; busiest transformer 94%; export 374 kW is 174 kW over the 200 kW limit: the solar mu |
| 1067 | SITE SURVEY | generic site 940 | CONFIRMED | connection point -1571 kW (plus is import), +757 kvar; volts 0.990 to 1.006; busiest transformer 122%; export 1571 kW is 1571 kW over the 0 kW limit: the solar  |
| 1068 | SITE SURVEY | generic site 941 | CONFIRMED | connection point +262 kW (plus is import), +481 kvar; volts 0.988 to 1.000; busiest transformer 49%; inside every limit |
| 1069 | SITE SURVEY | generic site 942 | CONFIRMED | connection point -4170 kW (plus is import), +1835 kvar; volts 0.983 to 1.011; busiest transformer 355%; export 4170 kW is 3970 kW over the 200 kW limit: the sol |
| 1070 | SITE SURVEY | generic site 943 | CONFIRMED | connection point -3768 kW (plus is import), +1640 kvar; volts 0.988 to 1.016; busiest transformer 322%; export 3768 kW is 3268 kW over the 500 kW limit: the sol |
| 1071 | SITE SURVEY | generic site 944 | CONFIRMED | connection point -353 kW (plus is import), +176 kvar; volts 0.992 to 1.000; busiest transformer 48%; export 353 kW is 353 kW over the 0 kW limit: the solar must |
| 1072 | SITE SURVEY | generic site 945 | CONFIRMED | connection point -2292 kW (plus is import), +1048 kvar; volts 0.991 to 1.018; busiest transformer 330%; export 2292 kW is 2292 kW over the 0 kW limit: the solar |
| 1073 | SITE SURVEY | generic site 946 | CONFIRMED | connection point -725 kW (plus is import), +135 kvar; volts 0.996 to 1.004; busiest transformer 79%; export 725 kW is 525 kW over the 200 kW limit: the solar mu |
| 1074 | SITE SURVEY | generic site 947 | CONFIRMED | connection point +181 kW (plus is import), +296 kvar; volts 0.989 to 1.000; busiest transformer 32%; inside every limit |
| 1075 | SITE SURVEY | generic site 948 | CONFIRMED | connection point -2538 kW (plus is import), +706 kvar; volts 0.995 to 1.017; busiest transformer 164%; export 2538 kW is 2538 kW over the 0 kW limit: the solar  |
| 1076 | SITE SURVEY | generic site 949 | CONFIRMED | connection point +82 kW (plus is import), +522 kvar; volts 0.987 to 1.000; busiest transformer 74%; inside every limit |
| 1077 | SITE SURVEY | generic site 950 | CONFIRMED | connection point -1133 kW (plus is import), +504 kvar; volts 0.989 to 1.011; busiest transformer 209%; export 1133 kW is 933 kW over the 200 kW limit: the solar |
| 1078 | SITE SURVEY | generic site 951 | CONFIRMED | connection point -1971 kW (plus is import), +1030 kvar; volts 0.987 to 1.015; busiest transformer 367%; export 1971 kW is 1921 kW over the 50 kW limit: the sola |
| 1079 | SITE SURVEY | generic site 952 | CONFIRMED | connection point -682 kW (plus is import), +153 kvar; volts 0.992 to 1.009; busiest transformer 159%; export 682 kW is 682 kW over the 0 kW limit: the solar mus |
| 1080 | SITE SURVEY | generic site 953 | CONFIRMED | connection point -283 kW (plus is import), +150 kvar; volts 0.994 to 1.000; busiest transformer 25%; inside every limit |
| 1081 | SITE SURVEY | generic site 954 | CONFIRMED | connection point -1231 kW (plus is import), +269 kvar; volts 0.994 to 1.007; busiest transformer 75%; export 1231 kW is 1181 kW over the 50 kW limit: the solar  |
| 1082 | SITE SURVEY | generic site 955 | CONFIRMED | connection point -1199 kW (plus is import), +813 kvar; volts 0.989 to 1.009; busiest transformer 218%; export 1199 kW is 199 kW over the 1000 kW limit: the sola |
| 1083 | SITE SURVEY | generic site 956 | REFUTED | connection point -3808 kW (plus is import), +5554 kvar; volts 0.861 to 1.000; busiest transformer 1260%; export 3808 kW is 2808 kW over the 1000 kW limit: the s |
| 1084 | SITE SURVEY | generic site 957 | CONFIRMED | connection point -2268 kW (plus is import), +922 kvar; volts 0.992 to 1.020; busiest transformer 372%; export 2268 kW is 2068 kW over the 200 kW limit: the sola |
| 1085 | SITE SURVEY | generic site 958 | CONFIRMED | connection point -212 kW (plus is import), +579 kvar; volts 0.987 to 1.001; busiest transformer 69%; inside every limit |
| 1086 | SITE SURVEY | generic site 959 | CONFIRMED | connection point -3189 kW (plus is import), +1045 kvar; volts 0.994 to 1.016; busiest transformer 209%; export 3189 kW is 2989 kW over the 200 kW limit: the sol |
| 1087 | SITE SURVEY | generic site 960 | CONFIRMED | connection point -1564 kW (plus is import), +817 kvar; volts 0.988 to 1.009; busiest transformer 161%; export 1564 kW is 1364 kW over the 200 kW limit: the sola |
| 1088 | SITE SURVEY | generic site 961 | CONFIRMED | connection point -2695 kW (plus is import), +2205 kvar; volts 0.981 to 1.001; busiest transformer 567%; export 2695 kW is 2645 kW over the 50 kW limit: the sola |
| 1089 | SITE SURVEY | generic site 962 | CONFIRMED | connection point -2006 kW (plus is import), +1061 kvar; volts 0.986 to 1.012; busiest transformer 372%; export 2006 kW is 1806 kW over the 200 kW limit: the sol |
| 1090 | SITE SURVEY | generic site 963 | CONFIRMED | connection point -1827 kW (plus is import), +869 kvar; volts 0.990 to 1.016; busiest transformer 275%; export 1827 kW is 827 kW over the 1000 kW limit: the sola |
| 1091 | SITE SURVEY | generic site 964 | CONFIRMED | connection point -2897 kW (plus is import), +1346 kvar; volts 0.990 to 1.014; busiest transformer 221%; export 2897 kW is 2397 kW over the 500 kW limit: the sol |
| 1092 | SITE SURVEY | generic site 965 | CONFIRMED | connection point -279 kW (plus is import), +283 kvar; volts 0.991 to 1.000; busiest transformer 40%; inside every limit |
| 1093 | SITE SURVEY | generic site 966 | CONFIRMED | connection point -558 kW (plus is import), +232 kvar; volts 0.994 to 1.003; busiest transformer 79%; export 558 kW is 358 kW over the 200 kW limit: the solar mu |
| 1094 | SITE SURVEY | generic site 967 | CONFIRMED | connection point +4 kW (plus is import), +620 kvar; volts 0.987 to 1.000; busiest transformer 45%; inside every limit |
| 1095 | SITE SURVEY | generic site 968 | CONFIRMED | connection point -1124 kW (plus is import), +645 kvar; volts 0.990 to 1.012; busiest transformer 195%; export 1124 kW is 624 kW over the 500 kW limit: the solar |
| 1096 | SITE SURVEY | generic site 969 | CONFIRMED | connection point -569 kW (plus is import), +1040 kvar; volts 0.984 to 1.009; busiest transformer 377%; export 569 kW is 69 kW over the 500 kW limit: the solar m |
| 1097 | SITE SURVEY | generic site 970 | CONFIRMED | connection point -592 kW (plus is import), +1428 kvar; volts 0.982 to 1.003; busiest transformer 463%; a transformer is at 463% of its rating |
| 1098 | SITE SURVEY | generic site 971 | CONFIRMED | connection point -210 kW (plus is import), +300 kvar; volts 0.989 to 1.004; busiest transformer 126%; export 210 kW is 210 kW over the 0 kW limit: the solar mus |
| 1099 | SITE SURVEY | generic site 972 | CONFIRMED | connection point -2305 kW (plus is import), +2661 kvar; volts 0.958 to 1.000; busiest transformer 811%; export 2305 kW is 2255 kW over the 50 kW limit: the sola |
| 1100 | SITE SURVEY | generic site 973 | CONFIRMED | connection point -1686 kW (plus is import), +393 kvar; volts 0.992 to 1.009; busiest transformer 105%; export 1686 kW is 1686 kW over the 0 kW limit: the solar  |
| 1101 | SITE SURVEY | generic site 974 | CONFIRMED | connection point -22 kW (plus is import), +520 kvar; volts 0.989 to 1.000; busiest transformer 82%; inside every limit |
| 1102 | SITE SURVEY | generic site 975 | CONFIRMED | connection point -1814 kW (plus is import), +936 kvar; volts 0.992 to 1.012; busiest transformer 492%; export 1814 kW is 1614 kW over the 200 kW limit: the sola |
| 1103 | SITE SURVEY | generic site 976 | CONFIRMED | connection point -1966 kW (plus is import), +1141 kvar; volts 0.986 to 1.004; busiest transformer 170%; export 1966 kW is 1466 kW over the 500 kW limit: the sol |
| 1104 | SITE SURVEY | generic site 977 | CONFIRMED | connection point -5386 kW (plus is import), +1919 kvar; volts 0.989 to 1.017; busiest transformer 335%; export 5386 kW is 4386 kW over the 1000 kW limit: the so |
| 1105 | SITE SURVEY | generic site 978 | CONFIRMED | connection point -2699 kW (plus is import), +817 kvar; volts 0.996 to 1.019; busiest transformer 217%; export 2699 kW is 1699 kW over the 1000 kW limit: the sol |
| 1106 | SITE SURVEY | generic site 979 | CONFIRMED | connection point -3758 kW (plus is import), +1174 kvar; volts 0.988 to 1.012; busiest transformer 283%; export 3758 kW is 3258 kW over the 500 kW limit: the sol |
| 1107 | SITE SURVEY | generic site 980 | CONFIRMED | connection point -826 kW (plus is import), +508 kvar; volts 0.989 to 1.006; busiest transformer 145%; export 826 kW is 776 kW over the 50 kW limit: the solar mu |
| 1108 | SITE SURVEY | generic site 981 | CONFIRMED | connection point -675 kW (plus is import), +240 kvar; volts 0.993 to 1.006; busiest transformer 93%; export 675 kW is 475 kW over the 200 kW limit: the solar mu |
| 1109 | SITE SURVEY | generic site 982 | CONFIRMED | connection point -1416 kW (plus is import), +1179 kvar; volts 0.986 to 1.008; busiest transformer 503%; export 1416 kW is 916 kW over the 500 kW limit: the sola |
| 1110 | SITE SURVEY | generic site 983 | CONFIRMED | connection point -4976 kW (plus is import), +1866 kvar; volts 0.990 to 1.017; busiest transformer 321%; export 4976 kW is 4476 kW over the 500 kW limit: the sol |
| 1111 | SITE SURVEY | generic site 984 | CONFIRMED | connection point -3599 kW (plus is import), +2200 kvar; volts 0.982 to 1.008; busiest transformer 527%; export 3599 kW is 2599 kW over the 1000 kW limit: the so |
| 1112 | SITE SURVEY | generic site 985 | CONFIRMED | connection point -807 kW (plus is import), +464 kvar; volts 0.992 to 1.014; busiest transformer 266%; export 807 kW is 607 kW over the 200 kW limit: the solar m |
| 1113 | SITE SURVEY | generic site 986 | CONFIRMED | connection point -1195 kW (plus is import), +390 kvar; volts 0.993 to 1.015; busiest transformer 299%; export 1195 kW is 695 kW over the 500 kW limit: the solar |
| 1114 | SITE SURVEY | generic site 987 | CONFIRMED | connection point +135 kW (plus is import), +469 kvar; volts 0.988 to 1.001; busiest transformer 82%; inside every limit |
| 1115 | SITE SURVEY | generic site 988 | CONFIRMED | connection point -1771 kW (plus is import), +1334 kvar; volts 0.985 to 1.005; busiest transformer 567%; export 1771 kW is 771 kW over the 1000 kW limit: the sol |
| 1116 | SITE SURVEY | generic site 989 | CONFIRMED | connection point -2215 kW (plus is import), +1273 kvar; volts 0.989 to 1.017; busiest transformer 351%; export 2215 kW is 2015 kW over the 200 kW limit: the sol |
| 1117 | SITE SURVEY | generic site 990 | CONFIRMED | connection point -3678 kW (plus is import), +1712 kvar; volts 0.984 to 1.008; busiest transformer 271%; export 3678 kW is 3178 kW over the 500 kW limit: the sol |
| 1118 | SITE SURVEY | generic site 991 | CONFIRMED | connection point -321 kW (plus is import), +381 kvar; volts 0.990 to 1.000; busiest transformer 49%; inside every limit |
| 1119 | SITE SURVEY | generic site 992 | CONFIRMED | connection point -1257 kW (plus is import), +428 kvar; volts 0.991 to 1.011; busiest transformer 172%; export 1257 kW is 757 kW over the 500 kW limit: the solar |
| 1120 | SITE SURVEY | generic site 993 | CONFIRMED | connection point -196 kW (plus is import), +135 kvar; volts 0.996 to 1.000; busiest transformer 13%; inside every limit |
| 1121 | SITE SURVEY | generic site 994 | CONFIRMED | connection point -2205 kW (plus is import), +543 kvar; volts 0.995 to 1.012; busiest transformer 130%; export 2205 kW is 1705 kW over the 500 kW limit: the sola |
| 1122 | SITE SURVEY | generic site 995 | CONFIRMED | connection point -2642 kW (plus is import), +665 kvar; volts 0.995 to 1.012; busiest transformer 156%; export 2642 kW is 2592 kW over the 50 kW limit: the solar |
| 1123 | SITE SURVEY | generic site 996 | CONFIRMED | connection point -1898 kW (plus is import), +821 kvar; volts 0.991 to 1.009; busiest transformer 141%; export 1898 kW is 1848 kW over the 50 kW limit: the solar |
| 1124 | SITE SURVEY | generic site 997 | CONFIRMED | connection point -2682 kW (plus is import), +894 kvar; volts 0.987 to 1.010; busiest transformer 221%; export 2682 kW is 1682 kW over the 1000 kW limit: the sol |
| 1125 | SITE SURVEY | generic site 998 | CONFIRMED | connection point -2635 kW (plus is import), +876 kvar; volts 0.993 to 1.019; busiest transformer 220%; export 2635 kW is 2635 kW over the 0 kW limit: the solar  |
| 1126 | SITE SURVEY | generic site 999 | CONFIRMED | connection point -437 kW (plus is import), +630 kvar; volts 0.988 to 1.000; busiest transformer 66%; export 437 kW is 387 kW over the 50 kW limit: the solar mus |
| 1127 | SITE SURVEY | generic site 1000 | CONFIRMED | connection point -4353 kW (plus is import), +2699 kvar; volts 0.983 to 1.000; busiest transformer 608%; export 4353 kW is 4303 kW over the 50 kW limit: the sola |
| 1128 | SITE SURVEY | generic site 1001 | CONFIRMED | connection point -88 kW (plus is import), +1120 kvar; volts 0.983 to 1.011; busiest transformer 346%; a transformer is at 346% of its rating |
| 1129 | SITE SURVEY | generic site 1002 | REFUTED | connection point -3727 kW (plus is import), +3622 kvar; volts 0.975 to 1.000; busiest transformer 1153%; export 3727 kW is 3527 kW over the 200 kW limit: the so |
| 1130 | SITE SURVEY | generic site 1003 | CONFIRMED | connection point -971 kW (plus is import), +652 kvar; volts 0.992 to 1.009; busiest transformer 181%; export 971 kW is 921 kW over the 50 kW limit: the solar mu |
| 1131 | SITE SURVEY | generic site 1004 | CONFIRMED | connection point -1379 kW (plus is import), +1087 kvar; volts 0.986 to 1.007; busiest transformer 475%; export 1379 kW is 1379 kW over the 0 kW limit: the solar |
| 1132 | SITE SURVEY | generic site 1005 | CONFIRMED | connection point -2761 kW (plus is import), +1247 kvar; volts 0.985 to 1.008; busiest transformer 205%; export 2761 kW is 2761 kW over the 0 kW limit: the solar |
| 1133 | SITE SURVEY | generic site 1006 | CONFIRMED | connection point +85 kW (plus is import), +342 kvar; volts 0.991 to 1.000; busiest transformer 53%; inside every limit |
| 1134 | SITE SURVEY | generic site 1007 | CONFIRMED | connection point -1007 kW (plus is import), +922 kvar; volts 0.987 to 1.011; busiest transformer 403%; export 1007 kW is 957 kW over the 50 kW limit: the solar  |
| 1135 | SITE SURVEY | generic site 1008 | CONFIRMED | connection point -1202 kW (plus is import), +666 kvar; volts 0.990 to 1.008; busiest transformer 130%; export 1202 kW is 1152 kW over the 50 kW limit: the solar |
| 1136 | SITE SURVEY | generic site 1009 | CONFIRMED | connection point -271 kW (plus is import), +282 kvar; volts 0.992 to 1.003; busiest transformer 83%; export 271 kW is 271 kW over the 0 kW limit: the solar must |
| 1137 | SITE SURVEY | generic site 1010 | CONFIRMED | connection point -2001 kW (plus is import), +1942 kvar; volts 0.983 to 1.000; busiest transformer 692%; export 2001 kW is 1951 kW over the 50 kW limit: the sola |
| 1138 | SITE SURVEY | generic site 1011 | CONFIRMED | connection point -6 kW (plus is import), +377 kvar; volts 0.989 to 1.000; busiest transformer 27%; inside every limit |
| 1139 | SITE SURVEY | generic site 1012 | CONFIRMED | connection point -1917 kW (plus is import), +638 kvar; volts 0.992 to 1.013; busiest transformer 300%; export 1917 kW is 917 kW over the 1000 kW limit: the sola |
| 1140 | SITE SURVEY | generic site 1013 | CONFIRMED | connection point -2608 kW (plus is import), +1872 kvar; volts 0.986 to 1.000; busiest transformer 730%; export 2608 kW is 2558 kW over the 50 kW limit: the sola |
| 1141 | SITE SURVEY | generic site 1014 | CONFIRMED | connection point -558 kW (plus is import), +680 kvar; volts 0.988 to 1.001; busiest transformer 94%; export 558 kW is 358 kW over the 200 kW limit: the solar mu |
| 1142 | SITE SURVEY | generic site 1015 | CONFIRMED | connection point -1665 kW (plus is import), +538 kvar; volts 0.992 to 1.012; busiest transformer 211%; export 1665 kW is 1465 kW over the 200 kW limit: the sola |
| 1143 | SITE SURVEY | generic site 1016 | CONFIRMED | connection point -457 kW (plus is import), +632 kvar; volts 0.988 to 1.003; busiest transformer 134%; a transformer is at 134% of its rating |
| 1144 | SITE SURVEY | generic site 1017 | CONFIRMED | connection point -2101 kW (plus is import), +1637 kvar; volts 0.987 to 1.000; busiest transformer 650%; export 2101 kW is 1601 kW over the 500 kW limit: the sol |
| 1145 | SITE SURVEY | generic site 1018 | CONFIRMED | connection point -2190 kW (plus is import), +811 kvar; volts 0.991 to 1.012; busiest transformer 187%; export 2190 kW is 2140 kW over the 50 kW limit: the solar |
| 1146 | SITE SURVEY | generic site 1019 | CONFIRMED | connection point -524 kW (plus is import), +205 kvar; volts 0.996 to 1.001; busiest transformer 41%; export 524 kW is 324 kW over the 200 kW limit: the solar mu |
| 1147 | SITE SURVEY | generic site 1020 | CONFIRMED | connection point -618 kW (plus is import), +119 kvar; volts 0.995 to 1.006; busiest transformer 88%; inside every limit |
| 1148 | SITE SURVEY | generic site 1021 | CONFIRMED | connection point -1765 kW (plus is import), +803 kvar; volts 0.988 to 1.010; busiest transformer 172%; export 1765 kW is 1565 kW over the 200 kW limit: the sola |
| 1149 | SITE SURVEY | generic site 1022 | CONFIRMED | connection point -151 kW (plus is import), +381 kvar; volts 0.989 to 1.000; busiest transformer 41%; inside every limit |
| 1150 | SITE SURVEY | generic site 1023 | CONFIRMED | connection point -101 kW (plus is import), +520 kvar; volts 0.990 to 1.000; busiest transformer 57%; export 101 kW is 51 kW over the 50 kW limit: the solar must |
| 1151 | SITE SURVEY | generic site 1024 | CONFIRMED | connection point -316 kW (plus is import), +722 kvar; volts 0.987 to 1.002; busiest transformer 75%; export 316 kW is 116 kW over the 200 kW limit: the solar mu |
| 1152 | SITE SURVEY | generic site 1025 | CONFIRMED | connection point -687 kW (plus is import), +275 kvar; volts 0.993 to 1.014; busiest transformer 202%; export 687 kW is 687 kW over the 0 kW limit: the solar mus |
| 1153 | SITE SURVEY | generic site 1026 | CONFIRMED | connection point -32 kW (plus is import), +163 kvar; volts 0.994 to 1.000; busiest transformer 29%; inside every limit |
| 1154 | SITE SURVEY | generic site 1027 | CONFIRMED | connection point -537 kW (plus is import), +199 kvar; volts 0.995 to 1.007; busiest transformer 146%; a transformer is at 146% of its rating |
| 1155 | SITE SURVEY | generic site 1028 | CONFIRMED | connection point -2998 kW (plus is import), +741 kvar; volts 0.990 to 1.012; busiest transformer 180%; export 2998 kW is 2998 kW over the 0 kW limit: the solar  |
| 1156 | SITE SURVEY | generic site 1029 | CONFIRMED | connection point +488 kW (plus is import), +735 kvar; volts 0.985 to 1.000; busiest transformer 41%; inside every limit |
| 1157 | SITE SURVEY | generic site 1030 | CONFIRMED | connection point -803 kW (plus is import), +284 kvar; volts 0.992 to 1.002; busiest transformer 63%; export 803 kW is 303 kW over the 500 kW limit: the solar mu |
| 1158 | SITE SURVEY | generic site 1031 | CONFIRMED | connection point -3449 kW (plus is import), +1431 kvar; volts 0.992 to 1.019; busiest transformer 245%; export 3449 kW is 3399 kW over the 50 kW limit: the sola |
| 1159 | SITE SURVEY | generic site 1032 | CONFIRMED | connection point -1820 kW (plus is import), +529 kvar; volts 0.990 to 1.005; busiest transformer 117%; export 1820 kW is 1620 kW over the 200 kW limit: the sola |
| 1160 | SITE SURVEY | generic site 1033 | CONFIRMED | connection point -1212 kW (plus is import), +685 kvar; volts 0.991 to 1.005; busiest transformer 105%; export 1212 kW is 1012 kW over the 200 kW limit: the sola |
| 1161 | SITE SURVEY | generic site 1034 | CONFIRMED | connection point -2894 kW (plus is import), +889 kvar; volts 0.992 to 1.009; busiest transformer 182%; export 2894 kW is 2844 kW over the 50 kW limit: the solar |
| 1162 | SITE SURVEY | generic site 1035 | CONFIRMED | connection point -4727 kW (plus is import), +1645 kvar; volts 0.992 to 1.020; busiest transformer 299%; export 4727 kW is 4527 kW over the 200 kW limit: the sol |
| 1163 | SITE SURVEY | generic site 1036 | CONFIRMED | connection point -769 kW (plus is import), +519 kvar; volts 0.991 to 1.007; busiest transformer 145%; export 769 kW is 769 kW over the 0 kW limit: the solar mus |
| 1164 | SITE SURVEY | generic site 1037 | CONFIRMED | connection point -613 kW (plus is import), +259 kvar; volts 0.992 to 1.013; busiest transformer 186%; a transformer is at 186% of its rating |
| 1165 | SITE SURVEY | generic site 1038 | CONFIRMED | connection point -157 kW (plus is import), +102 kvar; volts 0.996 to 1.002; busiest transformer 59%; inside every limit |
| 1166 | SITE SURVEY | generic site 1039 | CONFIRMED | connection point -2169 kW (plus is import), +1004 kvar; volts 0.988 to 1.014; busiest transformer 378%; export 2169 kW is 2119 kW over the 50 kW limit: the sola |
| 1167 | SITE SURVEY | generic site 1040 | CONFIRMED | connection point -447 kW (plus is import), +385 kvar; volts 0.989 to 1.005; busiest transformer 122%; a transformer is at 122% of its rating |
| 1168 | SITE SURVEY | generic site 1041 | CONFIRMED | connection point -3231 kW (plus is import), +3753 kvar; volts 0.898 to 1.000; busiest transformer 981%; export 3231 kW is 3231 kW over the 0 kW limit: the solar |
| 1169 | SITE SURVEY | generic site 1042 | CONFIRMED | connection point +87 kW (plus is import), +193 kvar; volts 0.992 to 1.000; busiest transformer 25%; inside every limit |
| 1170 | SITE SURVEY | generic site 1043 | CONFIRMED | connection point +164 kW (plus is import), +432 kvar; volts 0.988 to 1.000; busiest transformer 56%; inside every limit |
| 1171 | SITE SURVEY | generic site 1044 | CONFIRMED | connection point -3743 kW (plus is import), +2337 kvar; volts 0.984 to 1.000; busiest transformer 642%; export 3743 kW is 2743 kW over the 1000 kW limit: the so |
| 1172 | SITE SURVEY | generic site 1045 | CONFIRMED | connection point -4217 kW (plus is import), +1463 kvar; volts 0.993 to 1.017; busiest transformer 271%; export 4217 kW is 4217 kW over the 0 kW limit: the solar |
| 1173 | SITE SURVEY | generic site 1046 | CONFIRMED | connection point -629 kW (plus is import), +694 kvar; volts 0.988 to 1.008; busiest transformer 197%; export 629 kW is 129 kW over the 500 kW limit: the solar m |
| 1174 | SITE SURVEY | generic site 1047 | CONFIRMED | connection point -797 kW (plus is import), +180 kvar; volts 0.994 to 1.003; busiest transformer 59%; export 797 kW is 797 kW over the 0 kW limit: the solar must |
| 1175 | SITE SURVEY | generic site 1048 | CONFIRMED | connection point -1033 kW (plus is import), +272 kvar; volts 0.996 to 1.012; busiest transformer 132%; export 1033 kW is 983 kW over the 50 kW limit: the solar  |
| 1176 | SITE SURVEY | generic site 1049 | CONFIRMED | connection point -2505 kW (plus is import), +979 kvar; volts 0.994 to 1.012; busiest transformer 174%; export 2505 kW is 2505 kW over the 0 kW limit: the solar  |
| 1177 | SITE SURVEY | generic site 1050 | CONFIRMED | connection point -1018 kW (plus is import), +625 kvar; volts 0.991 to 1.014; busiest transformer 331%; export 1018 kW is 518 kW over the 500 kW limit: the solar |
| 1178 | SITE SURVEY | generic site 1051 | CONFIRMED | connection point -400 kW (plus is import), +102 kvar; volts 0.996 to 1.007; busiest transformer 100%; a transformer is at 100% of its rating |
| 1179 | SITE SURVEY | generic site 1052 | CONFIRMED | connection point -526 kW (plus is import), +211 kvar; volts 0.996 to 1.007; busiest transformer 98%; inside every limit |
| 1180 | SITE SURVEY | generic site 1053 | CONFIRMED | connection point -1723 kW (plus is import), +1021 kvar; volts 0.989 to 1.010; busiest transformer 187%; export 1723 kW is 723 kW over the 1000 kW limit: the sol |
| 1181 | SITE SURVEY | generic site 1054 | CONFIRMED | connection point -2733 kW (plus is import), +639 kvar; volts 0.995 to 1.009; busiest transformer 157%; export 2733 kW is 1733 kW over the 1000 kW limit: the sol |
| 1182 | SITE SURVEY | generic site 1055 | CONFIRMED | connection point -402 kW (plus is import), +105 kvar; volts 0.995 to 1.003; busiest transformer 59%; inside every limit |
| 1183 | SITE SURVEY | generic site 1056 | CONFIRMED | connection point +12 kW (plus is import), +141 kvar; volts 0.990 to 1.000; busiest transformer 24%; inside every limit |
| 1184 | SITE SURVEY | generic site 1057 | REFUTED | connection point -3191 kW (plus is import), +9071 kvar; volts 0.780 to 1.000; busiest transformer 1594%; export 3191 kW is 2191 kW over the 1000 kW limit: the s |
| 1185 | SITE SURVEY | generic site 1058 | CONFIRMED | connection point -1173 kW (plus is import), +786 kvar; volts 0.989 to 1.015; busiest transformer 395%; export 1173 kW is 1123 kW over the 50 kW limit: the solar |
| 1186 | SITE SURVEY | generic site 1059 | CONFIRMED | connection point -308 kW (plus is import), +94 kvar; volts 0.995 to 1.003; busiest transformer 77%; export 308 kW is 308 kW over the 0 kW limit: the solar must  |
| 1187 | SITE SURVEY | generic site 1060 | CONFIRMED | connection point -384 kW (plus is import), +175 kvar; volts 0.996 to 1.000; busiest transformer 27%; inside every limit |
| 1188 | SITE SURVEY | generic site 1061 | CONFIRMED | connection point -3103 kW (plus is import), +1825 kvar; volts 0.987 to 1.004; busiest transformer 542%; export 3103 kW is 2603 kW over the 500 kW limit: the sol |
| 1189 | SITE SURVEY | generic site 1062 | CONFIRMED | connection point -227 kW (plus is import), +105 kvar; volts 0.995 to 1.002; busiest transformer 68%; export 227 kW is 227 kW over the 0 kW limit: the solar must |
| 1190 | SITE SURVEY | generic site 1063 | CONFIRMED | connection point -1018 kW (plus is import), +507 kvar; volts 0.989 to 1.002; busiest transformer 78%; export 1018 kW is 18 kW over the 1000 kW limit: the solar  |
| 1191 | SITE SURVEY | generic site 1064 | CONFIRMED | connection point -1021 kW (plus is import), +305 kvar; volts 0.992 to 1.005; busiest transformer 69%; export 1021 kW is 1021 kW over the 0 kW limit: the solar m |
| 1192 | SITE SURVEY | generic site 1065 | CONFIRMED | connection point -4619 kW (plus is import), +1822 kvar; volts 0.984 to 1.012; busiest transformer 375%; export 4619 kW is 4419 kW over the 200 kW limit: the sol |
| 1193 | SITE SURVEY | generic site 1066 | CONFIRMED | connection point -5014 kW (plus is import), +1879 kvar; volts 0.984 to 1.012; busiest transformer 322%; export 5014 kW is 4964 kW over the 50 kW limit: the sola |
| 1194 | SITE SURVEY | generic site 1067 | CONFIRMED | connection point -758 kW (plus is import), +266 kvar; volts 0.991 to 1.002; busiest transformer 50%; export 758 kW is 258 kW over the 500 kW limit: the solar mu |
| 1195 | SITE SURVEY | generic site 1068 | CONFIRMED | connection point -1993 kW (plus is import), +847 kvar; volts 0.992 to 1.017; busiest transformer 281%; export 1993 kW is 1993 kW over the 0 kW limit: the solar  |
| 1196 | SITE SURVEY | generic site 1069 | CONFIRMED | connection point -2564 kW (plus is import), +773 kvar; volts 0.991 to 1.010; busiest transformer 198%; export 2564 kW is 2514 kW over the 50 kW limit: the solar |
| 1197 | SITE SURVEY | generic site 1070 | CONFIRMED | connection point -2254 kW (plus is import), +1308 kvar; volts 0.987 to 1.004; busiest transformer 607%; export 2254 kW is 2204 kW over the 50 kW limit: the sola |
| 1198 | SITE SURVEY | generic site 1071 | CONFIRMED | connection point -318 kW (plus is import), +211 kvar; volts 0.992 to 1.000; busiest transformer 27%; inside every limit |
| 1199 | SITE SURVEY | generic site 1072 | CONFIRMED | connection point -5740 kW (plus is import), +2997 kvar; volts 0.983 to 1.014; busiest transformer 494%; export 5740 kW is 5690 kW over the 50 kW limit: the sola |
| 1200 | SITE SURVEY | generic site 1073 | CONFIRMED | connection point -1003 kW (plus is import), +326 kvar; volts 0.993 to 1.015; busiest transformer 257%; export 1003 kW is 953 kW over the 50 kW limit: the solar  |
| 1201 | SITE SURVEY | generic site 1074 | CONFIRMED | connection point -218 kW (plus is import), +613 kvar; volts 0.987 to 1.000; busiest transformer 60%; inside every limit |
| 1202 | SITE SURVEY | generic site 1075 | CONFIRMED | connection point -1774 kW (plus is import), +467 kvar; volts 0.989 to 1.007; busiest transformer 112%; export 1774 kW is 1574 kW over the 200 kW limit: the sola |
| 1203 | SITE SURVEY | generic site 1076 | CONFIRMED | connection point +250 kW (plus is import), +587 kvar; volts 0.987 to 1.003; busiest transformer 100%; inside every limit |
| 1204 | SITE SURVEY | generic site 1077 | CONFIRMED | connection point -2207 kW (plus is import), +1076 kvar; volts 0.992 to 1.017; busiest transformer 326%; export 2207 kW is 2207 kW over the 0 kW limit: the solar |
| 1205 | SITE SURVEY | generic site 1078 | CONFIRMED | connection point -101 kW (plus is import), +92 kvar; volts 0.994 to 1.001; busiest transformer 45%; inside every limit |
| 1206 | SITE SURVEY | generic site 1079 | CONFIRMED | connection point -3954 kW (plus is import), +1572 kvar; volts 0.984 to 1.015; busiest transformer 332%; export 3954 kW is 2954 kW over the 1000 kW limit: the so |
| 1207 | SITE SURVEY | generic site 1080 | CONFIRMED | connection point -3223 kW (plus is import), +1642 kvar; volts 0.984 to 1.009; busiest transformer 444%; export 3223 kW is 2223 kW over the 1000 kW limit: the so |
| 1208 | SITE SURVEY | generic site 1081 | CONFIRMED | connection point -2065 kW (plus is import), +777 kvar; volts 0.989 to 1.011; busiest transformer 150%; export 2065 kW is 2015 kW over the 50 kW limit: the solar |
| 1209 | SITE SURVEY | generic site 1082 | CONFIRMED | connection point -1689 kW (plus is import), +417 kvar; volts 0.991 to 1.005; busiest transformer 101%; export 1689 kW is 1639 kW over the 50 kW limit: the solar |
| 1210 | SITE SURVEY | generic site 1083 | CONFIRMED | connection point -1171 kW (plus is import), +259 kvar; volts 0.998 to 1.011; busiest transformer 137%; export 1171 kW is 171 kW over the 1000 kW limit: the sola |
| 1211 | SITE SURVEY | generic site 1084 | CONFIRMED | connection point -2137 kW (plus is import), +1131 kvar; volts 0.985 to 1.010; busiest transformer 218%; export 2137 kW is 2087 kW over the 50 kW limit: the sola |
| 1212 | SITE SURVEY | generic site 1085 | CONFIRMED | connection point -4067 kW (plus is import), +2965 kvar; volts 0.975 to 1.000; busiest transformer 718%; export 4067 kW is 4067 kW over the 0 kW limit: the solar |
| 1213 | SITE SURVEY | generic site 1086 | CONFIRMED | connection point -2214 kW (plus is import), +1427 kvar; volts 0.984 to 1.010; busiest transformer 249%; export 2214 kW is 2214 kW over the 0 kW limit: the solar |
| 1214 | SITE SURVEY | generic site 1087 | CONFIRMED | connection point -495 kW (plus is import), +235 kvar; volts 0.991 to 1.009; busiest transformer 158%; export 495 kW is 445 kW over the 50 kW limit: the solar mu |
| 1215 | SITE SURVEY | generic site 1088 | CONFIRMED | connection point -2056 kW (plus is import), +783 kvar; volts 0.993 to 1.015; busiest transformer 278%; export 2056 kW is 1056 kW over the 1000 kW limit: the sol |
| 1216 | SITE SURVEY | generic site 1089 | CONFIRMED | connection point -119 kW (plus is import), +312 kvar; volts 0.990 to 1.000; busiest transformer 31%; inside every limit |
| 1217 | SITE SURVEY | generic site 1090 | CONFIRMED | connection point -294 kW (plus is import), +432 kvar; volts 0.990 to 1.005; busiest transformer 119%; a transformer is at 119% of its rating |
| 1218 | SITE SURVEY | generic site 1091 | CONFIRMED | connection point +111 kW (plus is import), +244 kvar; volts 0.991 to 1.000; busiest transformer 56%; inside every limit |
| 1219 | SITE SURVEY | generic site 1092 | CONFIRMED | connection point -2552 kW (plus is import), +1498 kvar; volts 0.984 to 1.012; busiest transformer 395%; export 2552 kW is 2352 kW over the 200 kW limit: the sol |
| 1220 | SITE SURVEY | generic site 1093 | CONFIRMED | connection point -2523 kW (plus is import), +1263 kvar; volts 0.992 to 1.014; busiest transformer 438%; export 2523 kW is 2323 kW over the 200 kW limit: the sol |
| 1221 | SITE SURVEY | generic site 1094 | CONFIRMED | connection point -3051 kW (plus is import), +1055 kvar; volts 0.988 to 1.010; busiest transformer 206%; export 3051 kW is 3051 kW over the 0 kW limit: the solar |
| 1222 | SITE SURVEY | generic site 1095 | CONFIRMED | connection point -473 kW (plus is import), +434 kvar; volts 0.991 to 1.004; busiest transformer 131%; export 473 kW is 423 kW over the 50 kW limit: the solar mu |
| 1223 | SITE SURVEY | generic site 1096 | CONFIRMED | connection point -4985 kW (plus is import), +2432 kvar; volts 0.986 to 1.014; busiest transformer 431%; export 4985 kW is 4785 kW over the 200 kW limit: the sol |
| 1224 | SITE SURVEY | generic site 1097 | REFUTED | connection point -3844 kW (plus is import), +6669 kvar; volts 0.840 to 1.000; busiest transformer 1392%; export 3844 kW is 3844 kW over the 0 kW limit: the sola |
| 1225 | SITE SURVEY | generic site 1098 | CONFIRMED | connection point -2699 kW (plus is import), +963 kvar; volts 0.988 to 1.014; busiest transformer 339%; export 2699 kW is 2699 kW over the 0 kW limit: the solar  |
| 1226 | SITE SURVEY | generic site 1099 | CONFIRMED | connection point -1755 kW (plus is import), +844 kvar; volts 0.992 to 1.014; busiest transformer 468%; export 1755 kW is 1705 kW over the 50 kW limit: the solar |
| 1227 | SITE SURVEY | generic site 1100 | CONFIRMED | connection point +33 kW (plus is import), +113 kvar; volts 0.994 to 1.000; busiest transformer 11%; inside every limit |
| 1228 | SITE SURVEY | generic site 1101 | CONFIRMED | connection point -425 kW (plus is import), +438 kvar; volts 0.991 to 1.000; busiest transformer 46%; inside every limit |
| 1229 | SITE SURVEY | generic site 1102 | CONFIRMED | connection point -4691 kW (plus is import), +1870 kvar; volts 0.983 to 1.008; busiest transformer 314%; export 4691 kW is 3691 kW over the 1000 kW limit: the so |
| 1230 | SITE SURVEY | generic site 1103 | CONFIRMED | connection point -1452 kW (plus is import), +567 kvar; volts 0.993 to 1.007; busiest transformer 105%; export 1452 kW is 1402 kW over the 50 kW limit: the solar |
| 1231 | SITE SURVEY | generic site 1104 | CONFIRMED | connection point -701 kW (plus is import), +561 kvar; volts 0.988 to 1.008; busiest transformer 180%; export 701 kW is 501 kW over the 200 kW limit: the solar m |
| 1232 | SITE SURVEY | generic site 1105 | CONFIRMED | connection point -1127 kW (plus is import), +1187 kvar; volts 0.984 to 1.010; busiest transformer 478%; export 1127 kW is 627 kW over the 500 kW limit: the sola |
| 1233 | SITE SURVEY | generic site 1106 | CONFIRMED | connection point -2587 kW (plus is import), +697 kvar; volts 0.995 to 1.012; busiest transformer 161%; export 2587 kW is 2537 kW over the 50 kW limit: the solar |
| 1234 | SITE SURVEY | generic site 1107 | CONFIRMED | connection point -515 kW (plus is import), +687 kvar; volts 0.988 to 1.012; busiest transformer 288%; export 515 kW is 15 kW over the 500 kW limit: the solar mu |
| 1235 | SITE SURVEY | generic site 1108 | CONFIRMED | connection point -416 kW (plus is import), +480 kvar; volts 0.989 to 1.003; busiest transformer 110%; export 416 kW is 366 kW over the 50 kW limit: the solar mu |
| 1236 | SITE SURVEY | generic site 1109 | CONFIRMED | connection point -1677 kW (plus is import), +922 kvar; volts 0.988 to 1.012; busiest transformer 475%; export 1677 kW is 1177 kW over the 500 kW limit: the sola |
| 1237 | SITE SURVEY | generic site 1110 | CONFIRMED | connection point -1395 kW (plus is import), +582 kvar; volts 0.993 to 1.010; busiest transformer 132%; export 1395 kW is 895 kW over the 500 kW limit: the solar |
| 1238 | SITE SURVEY | generic site 1111 | CONFIRMED | connection point -1212 kW (plus is import), +303 kvar; volts 0.994 to 1.012; busiest transformer 183%; export 1212 kW is 1162 kW over the 50 kW limit: the solar |
| 1239 | SITE SURVEY | generic site 1112 | CONFIRMED | connection point +133 kW (plus is import), +274 kvar; volts 0.993 to 1.000; busiest transformer 27%; inside every limit |
| 1240 | SITE SURVEY | generic site 1113 | CONFIRMED | connection point -399 kW (plus is import), +104 kvar; volts 0.993 to 1.008; busiest transformer 101%; a transformer is at 101% of its rating |
| 1241 | SITE SURVEY | generic site 1114 | CONFIRMED | connection point +307 kW (plus is import), +746 kvar; volts 0.984 to 1.000; busiest transformer 54%; inside every limit |
| 1242 | SITE SURVEY | generic site 1115 | CONFIRMED | connection point -125 kW (plus is import), +376 kvar; volts 0.990 to 1.006; busiest transformer 141%; a transformer is at 141% of its rating |
| 1243 | SITE SURVEY | generic site 1116 | CONFIRMED | connection point -3588 kW (plus is import), +1911 kvar; volts 0.985 to 1.007; busiest transformer 276%; export 3588 kW is 3588 kW over the 0 kW limit: the solar |
| 1244 | SITE SURVEY | generic site 1117 | CONFIRMED | connection point -4368 kW (plus is import), +1679 kvar; volts 0.991 to 1.018; busiest transformer 350%; export 4368 kW is 3368 kW over the 1000 kW limit: the so |
| 1245 | SITE SURVEY | generic site 1118 | CONFIRMED | connection point -383 kW (plus is import), +465 kvar; volts 0.991 to 1.005; busiest transformer 133%; export 383 kW is 183 kW over the 200 kW limit: the solar m |
| 1246 | SITE SURVEY | generic site 1119 | CONFIRMED | connection point -1331 kW (plus is import), +268 kvar; volts 0.996 to 1.003; busiest transformer 72%; export 1331 kW is 1281 kW over the 50 kW limit: the solar  |
| 1247 | SITE SURVEY | generic site 1120 | CONFIRMED | connection point -281 kW (plus is import), +517 kvar; volts 0.988 to 1.000; busiest transformer 52%; inside every limit |
| 1248 | SITE SURVEY | generic site 1121 | CONFIRMED | connection point -1532 kW (plus is import), +796 kvar; volts 0.992 to 1.015; busiest transformer 436%; export 1532 kW is 1332 kW over the 200 kW limit: the sola |
| 1249 | SITE SURVEY | generic site 1122 | CONFIRMED | connection point -500 kW (plus is import), +603 kvar; volts 0.989 to 1.005; busiest transformer 134%; export 500 kW is 450 kW over the 50 kW limit: the solar mu |
| 1250 | SITE SURVEY | generic site 1123 | CONFIRMED | connection point -1582 kW (plus is import), +308 kvar; volts 0.995 to 1.010; busiest transformer 94%; export 1582 kW is 582 kW over the 1000 kW limit: the solar |
| 1251 | SITE SURVEY | generic site 1124 | CONFIRMED | connection point -147 kW (plus is import), +166 kvar; volts 0.993 to 1.000; busiest transformer 20%; inside every limit |
| 1252 | SITE SURVEY | generic site 1125 | CONFIRMED | connection point -2359 kW (plus is import), +760 kvar; volts 0.989 to 1.015; busiest transformer 293%; export 2359 kW is 2159 kW over the 200 kW limit: the sola |
| 1253 | SITE SURVEY | generic site 1126 | CONFIRMED | connection point -2781 kW (plus is import), +664 kvar; volts 0.994 to 1.009; busiest transformer 159%; export 2781 kW is 2731 kW over the 50 kW limit: the solar |
| 1254 | SITE SURVEY | generic site 1127 | CONFIRMED | connection point -878 kW (plus is import), +752 kvar; volts 0.987 to 1.003; busiest transformer 117%; a transformer is at 117% of its rating |
| 1255 | SITE SURVEY | generic site 1128 | CONFIRMED | connection point -469 kW (plus is import), +255 kvar; volts 0.994 to 1.001; busiest transformer 39%; inside every limit |
| 1256 | SITE SURVEY | generic site 1129 | CONFIRMED | connection point -406 kW (plus is import), +832 kvar; volts 0.986 to 1.010; busiest transformer 210%; a transformer is at 210% of its rating |
| 1257 | SITE SURVEY | generic site 1130 | CONFIRMED | connection point -3138 kW (plus is import), +1645 kvar; volts 0.984 to 1.006; busiest transformer 522%; export 3138 kW is 3088 kW over the 50 kW limit: the sola |
| 1258 | SITE SURVEY | generic site 1131 | CONFIRMED | connection point -186 kW (plus is import), +112 kvar; volts 0.996 to 1.005; busiest transformer 70%; inside every limit |
| 1259 | SITE SURVEY | generic site 1132 | CONFIRMED | connection point -4101 kW (plus is import), +1226 kvar; volts 0.986 to 1.012; busiest transformer 254%; export 4101 kW is 3901 kW over the 200 kW limit: the sol |
| 1260 | SITE SURVEY | generic site 1133 | CONFIRMED | connection point -2183 kW (plus is import), +2100 kvar; volts 0.980 to 1.000; busiest transformer 729%; export 2183 kW is 1683 kW over the 500 kW limit: the sol |
| 1261 | SITE SURVEY | generic site 1134 | CONFIRMED | connection point -472 kW (plus is import), +427 kvar; volts 0.990 to 1.000; busiest transformer 46%; export 472 kW is 272 kW over the 200 kW limit: the solar mu |
| 1262 | SITE SURVEY | generic site 1135 | CONFIRMED | connection point -4171 kW (plus is import), +1472 kvar; volts 0.993 to 1.022; busiest transformer 272%; export 4171 kW is 3971 kW over the 200 kW limit: the sol |
| 1263 | SITE SURVEY | generic site 1136 | CONFIRMED | connection point -237 kW (plus is import), +107 kvar; volts 0.995 to 1.004; busiest transformer 74%; inside every limit |
| 1264 | SITE SURVEY | generic site 1137 | CONFIRMED | connection point -3125 kW (plus is import), +3139 kvar; volts 0.930 to 1.000; busiest transformer 921%; export 3125 kW is 3125 kW over the 0 kW limit: the solar |
| 1265 | SITE SURVEY | generic site 1138 | CONFIRMED | connection point -2321 kW (plus is import), +1685 kvar; volts 0.986 to 1.000; busiest transformer 673%; export 2321 kW is 2321 kW over the 0 kW limit: the solar |
| 1266 | SITE SURVEY | generic site 1139 | CONFIRMED | connection point -1303 kW (plus is import), +226 kvar; volts 0.998 to 1.008; busiest transformer 74%; export 1303 kW is 303 kW over the 1000 kW limit: the solar |
| 1267 | SITE SURVEY | generic site 1140 | CONFIRMED | connection point -1337 kW (plus is import), +593 kvar; volts 0.991 to 1.014; busiest transformer 242%; export 1337 kW is 1287 kW over the 50 kW limit: the solar |
| 1268 | SITE SURVEY | generic site 1141 | CONFIRMED | connection point -1855 kW (plus is import), +882 kvar; volts 0.992 to 1.020; busiest transformer 338%; export 1855 kW is 1355 kW over the 500 kW limit: the sola |
| 1269 | SITE SURVEY | generic site 1142 | CONFIRMED | connection point -1785 kW (plus is import), +334 kvar; volts 0.999 to 1.010; busiest transformer 96%; export 1785 kW is 1785 kW over the 0 kW limit: the solar m |
| 1270 | SITE SURVEY | generic site 1143 | CONFIRMED | connection point -4509 kW (plus is import), +1842 kvar; volts 0.988 to 1.011; busiest transformer 366%; export 4509 kW is 4009 kW over the 500 kW limit: the sol |
| 1271 | SITE SURVEY | generic site 1144 | CONFIRMED | connection point -3349 kW (plus is import), +1350 kvar; volts 0.991 to 1.020; busiest transformer 287%; export 3349 kW is 3149 kW over the 200 kW limit: the sol |
| 1272 | SITE SURVEY | generic site 1145 | CONFIRMED | connection point -1255 kW (plus is import), +331 kvar; volts 0.992 to 1.005; busiest transformer 78%; export 1255 kW is 255 kW over the 1000 kW limit: the solar |
| 1273 | SITE SURVEY | generic site 1146 | CONFIRMED | connection point -3390 kW (plus is import), +2055 kvar; volts 0.980 to 1.005; busiest transformer 499%; export 3390 kW is 3340 kW over the 50 kW limit: the sola |
| 1274 | SITE SURVEY | generic site 1147 | CONFIRMED | connection point -82 kW (plus is import), +391 kvar; volts 0.988 to 1.000; busiest transformer 34%; export 82 kW is 32 kW over the 50 kW limit: the solar must b |
| 1275 | SITE SURVEY | generic site 1148 | CONFIRMED | connection point -2556 kW (plus is import), +764 kvar; volts 0.995 to 1.013; busiest transformer 166%; export 2556 kW is 1556 kW over the 1000 kW limit: the sol |
| 1276 | SITE SURVEY | generic site 1149 | CONFIRMED | connection point -695 kW (plus is import), +693 kvar; volts 0.987 to 1.008; busiest transformer 203%; export 695 kW is 645 kW over the 50 kW limit: the solar mu |
| 1277 | SITE SURVEY | generic site 1150 | CONFIRMED | connection point -999 kW (plus is import), +587 kvar; volts 0.988 to 1.007; busiest transformer 208%; export 999 kW is 799 kW over the 200 kW limit: the solar m |
| 1278 | SITE SURVEY | generic site 1151 | CONFIRMED | connection point +79 kW (plus is import), +384 kvar; volts 0.990 to 1.000; busiest transformer 20%; inside every limit |
| 1279 | SITE SURVEY | generic site 1152 | CONFIRMED | connection point -4022 kW (plus is import), +1927 kvar; volts 0.986 to 1.017; busiest transformer 362%; export 4022 kW is 3822 kW over the 200 kW limit: the sol |
| 1280 | SITE SURVEY | generic site 1153 | CONFIRMED | connection point -257 kW (plus is import), +233 kvar; volts 0.991 to 1.002; busiest transformer 71%; export 257 kW is 257 kW over the 0 kW limit: the solar must |
| 1281 | SITE SURVEY | generic site 1154 | CONFIRMED | connection point -1131 kW (plus is import), +573 kvar; volts 0.991 to 1.004; busiest transformer 90%; export 1131 kW is 631 kW over the 500 kW limit: the solar  |
| 1282 | SITE SURVEY | generic site 1155 | CONFIRMED | connection point -3012 kW (plus is import), +760 kvar; volts 0.994 to 1.013; busiest transformer 176%; export 3012 kW is 2962 kW over the 50 kW limit: the solar |
| 1283 | SITE SURVEY | generic site 1156 | CONFIRMED | connection point -91 kW (plus is import), +585 kvar; volts 0.988 to 1.000; busiest transformer 66%; inside every limit |
| 1284 | SITE SURVEY | generic site 1157 | CONFIRMED | connection point -185 kW (plus is import), +581 kvar; volts 0.988 to 1.000; busiest transformer 63%; inside every limit |
| 1285 | SITE SURVEY | generic site 1158 | CONFIRMED | connection point -2742 kW (plus is import), +3200 kvar; volts 0.937 to 1.000; busiest transformer 908%; export 2742 kW is 2692 kW over the 50 kW limit: the sola |
| 1286 | SITE SURVEY | generic site 1159 | CONFIRMED | connection point -2058 kW (plus is import), +482 kvar; volts 0.991 to 1.009; busiest transformer 150%; export 2058 kW is 1058 kW over the 1000 kW limit: the sol |
| 1287 | SITE SURVEY | generic site 1160 | CONFIRMED | connection point -3138 kW (plus is import), +1893 kvar; volts 0.987 to 1.011; busiest transformer 559%; export 3138 kW is 3138 kW over the 0 kW limit: the solar |
| 1288 | SITE SURVEY | generic site 1161 | CONFIRMED | connection point -2187 kW (plus is import), +860 kvar; volts 0.992 to 1.016; busiest transformer 294%; export 2187 kW is 1687 kW over the 500 kW limit: the sola |
| 1289 | SITE SURVEY | generic site 1162 | CONFIRMED | connection point -371 kW (plus is import), +586 kvar; volts 0.988 to 1.002; busiest transformer 119%; a transformer is at 119% of its rating |
| 1290 | SITE SURVEY | generic site 1163 | CONFIRMED | connection point -482 kW (plus is import), +119 kvar; volts 0.995 to 1.005; busiest transformer 61%; export 482 kW is 482 kW over the 0 kW limit: the solar must |
| 1291 | SITE SURVEY | generic site 1164 | CONFIRMED | connection point -680 kW (plus is import), +246 kvar; volts 0.991 to 1.007; busiest transformer 100%; export 680 kW is 680 kW over the 0 kW limit: the solar mus |
| 1292 | SITE SURVEY | generic site 1165 | CONFIRMED | connection point -771 kW (plus is import), +1196 kvar; volts 0.985 to 1.008; busiest transformer 297%; export 771 kW is 571 kW over the 200 kW limit: the solar  |
| 1293 | SITE SURVEY | generic site 1166 | CONFIRMED | connection point +1 kW (plus is import), +534 kvar; volts 0.987 to 1.000; busiest transformer 42%; inside every limit |
| 1294 | SITE SURVEY | generic site 1167 | CONFIRMED | connection point -2637 kW (plus is import), +1762 kvar; volts 0.984 to 1.006; busiest transformer 424%; export 2637 kW is 2637 kW over the 0 kW limit: the solar |
| 1295 | SITE SURVEY | generic site 1168 | CONFIRMED | connection point -388 kW (plus is import), +869 kvar; volts 0.985 to 1.001; busiest transformer 88%; export 388 kW is 188 kW over the 200 kW limit: the solar mu |
| 1296 | SITE SURVEY | generic site 1169 | CONFIRMED | connection point -3147 kW (plus is import), +4039 kvar; volts 0.880 to 1.000; busiest transformer 994%; export 3147 kW is 3097 kW over the 50 kW limit: the sola |
| 1297 | SITE SURVEY | generic site 1170 | CONFIRMED | connection point -489 kW (plus is import), +191 kvar; volts 0.997 to 1.001; busiest transformer 37%; export 489 kW is 289 kW over the 200 kW limit: the solar mu |
| 1298 | SITE SURVEY | generic site 1171 | CONFIRMED | connection point +317 kW (plus is import), +613 kvar; volts 0.985 to 1.000; busiest transformer 43%; inside every limit |
| 1299 | SITE SURVEY | generic site 1172 | CONFIRMED | connection point +100 kW (plus is import), +752 kvar; volts 0.984 to 1.002; busiest transformer 141%; a transformer is at 141% of its rating |
| 1300 | SITE SURVEY | generic site 1173 | CONFIRMED | connection point -210 kW (plus is import), +332 kvar; volts 0.991 to 1.002; busiest transformer 85%; inside every limit |
| 1301 | SITE SURVEY | generic site 1174 | CONFIRMED | connection point -148 kW (plus is import), +200 kvar; volts 0.994 to 1.000; busiest transformer 23%; inside every limit |
| 1302 | SITE SURVEY | generic site 1175 | CONFIRMED | connection point -2880 kW (plus is import), +856 kvar; volts 0.994 to 1.018; busiest transformer 230%; export 2880 kW is 2680 kW over the 200 kW limit: the sola |
| 1303 | SITE SURVEY | generic site 1176 | CONFIRMED | connection point -594 kW (plus is import), +1088 kvar; volts 0.985 to 1.010; busiest transformer 392%; a transformer is at 392% of its rating |
| 1304 | SITE SURVEY | generic site 1177 | CONFIRMED | connection point -718 kW (plus is import), +359 kvar; volts 0.992 to 1.008; busiest transformer 143%; export 718 kW is 218 kW over the 500 kW limit: the solar m |
| 1305 | SITE SURVEY | generic site 1178 | CONFIRMED | connection point -3711 kW (plus is import), +1548 kvar; volts 0.991 to 1.014; busiest transformer 312%; export 3711 kW is 3511 kW over the 200 kW limit: the sol |
| 1306 | SITE SURVEY | generic site 1179 | CONFIRMED | connection point -1129 kW (plus is import), +654 kvar; volts 0.989 to 1.009; busiest transformer 232%; export 1129 kW is 629 kW over the 500 kW limit: the solar |
| 1307 | SITE SURVEY | generic site 1180 | CONFIRMED | connection point -4263 kW (plus is import), +1392 kvar; volts 0.993 to 1.011; busiest transformer 264%; export 4263 kW is 4213 kW over the 50 kW limit: the sola |
| 1308 | SITE SURVEY | generic site 1181 | CONFIRMED | connection point -806 kW (plus is import), +439 kvar; volts 0.991 to 1.013; busiest transformer 260%; export 806 kW is 756 kW over the 50 kW limit: the solar mu |
| 1309 | SITE SURVEY | generic site 1182 | CONFIRMED | connection point +13 kW (plus is import), +758 kvar; volts 0.986 to 1.007; busiest transformer 233%; a transformer is at 233% of its rating |
| 1310 | SITE SURVEY | generic site 1183 | CONFIRMED | connection point -1172 kW (plus is import), +677 kvar; volts 0.990 to 1.010; busiest transformer 240%; export 1172 kW is 1122 kW over the 50 kW limit: the solar |
| 1311 | SITE SURVEY | generic site 1184 | CONFIRMED | connection point -366 kW (plus is import), +705 kvar; volts 0.987 to 1.003; busiest transformer 94%; export 366 kW is 366 kW over the 0 kW limit: the solar must |
| 1312 | SITE SURVEY | generic site 1185 | CONFIRMED | connection point -1120 kW (plus is import), +361 kvar; volts 0.993 to 1.010; busiest transformer 182%; export 1120 kW is 620 kW over the 500 kW limit: the solar |
| 1313 | SITE SURVEY | generic site 1186 | CONFIRMED | connection point -539 kW (plus is import), +369 kvar; volts 0.990 to 1.004; busiest transformer 101%; export 539 kW is 339 kW over the 200 kW limit: the solar m |
| 1314 | SITE SURVEY | generic site 1187 | CONFIRMED | connection point -1801 kW (plus is import), +841 kvar; volts 0.991 to 1.010; busiest transformer 143%; export 1801 kW is 1601 kW over the 200 kW limit: the sola |
| 1315 | SITE SURVEY | generic site 1188 | CONFIRMED | connection point -3745 kW (plus is import), +2844 kvar; volts 0.980 to 1.000; busiest transformer 695%; export 3745 kW is 3545 kW over the 200 kW limit: the sol |
| 1316 | SITE SURVEY | generic site 1189 | CONFIRMED | connection point -3752 kW (plus is import), +1271 kvar; volts 0.994 to 1.022; busiest transformer 247%; export 3752 kW is 3552 kW over the 200 kW limit: the sol |
| 1317 | SITE SURVEY | generic site 1190 | CONFIRMED | connection point -2438 kW (plus is import), +912 kvar; volts 0.990 to 1.009; busiest transformer 166%; export 2438 kW is 2388 kW over the 50 kW limit: the solar |
| 1318 | SITE SURVEY | generic site 1191 | CONFIRMED | connection point +33 kW (plus is import), +386 kvar; volts 0.989 to 1.000; busiest transformer 56%; inside every limit |
| 1319 | SITE SURVEY | generic site 1192 | CONFIRMED | connection point -2450 kW (plus is import), +1080 kvar; volts 0.991 to 1.013; busiest transformer 223%; export 2450 kW is 2400 kW over the 50 kW limit: the sola |
| 1320 | SITE SURVEY | generic site 1193 | CONFIRMED | connection point -2695 kW (plus is import), +719 kvar; volts 0.991 to 1.010; busiest transformer 166%; export 2695 kW is 2645 kW over the 50 kW limit: the solar |
| 1321 | SITE SURVEY | generic site 1194 | CONFIRMED | connection point -1475 kW (plus is import), +960 kvar; volts 0.986 to 1.014; busiest transformer 319%; export 1475 kW is 475 kW over the 1000 kW limit: the sola |
| 1322 | SITE SURVEY | generic site 1195 | CONFIRMED | connection point -2474 kW (plus is import), +1151 kvar; volts 0.990 to 1.015; busiest transformer 415%; export 2474 kW is 1474 kW over the 1000 kW limit: the so |
| 1323 | SITE SURVEY | generic site 1196 | CONFIRMED | connection point -2400 kW (plus is import), +779 kvar; volts 0.990 to 1.014; busiest transformer 298%; export 2400 kW is 2200 kW over the 200 kW limit: the sola |
| 1324 | SITE SURVEY | generic site 1197 | CONFIRMED | connection point -427 kW (plus is import), +586 kvar; volts 0.990 to 1.009; busiest transformer 244%; a transformer is at 244% of its rating |
| 1325 | SITE SURVEY | generic site 1198 | CONFIRMED | connection point -82 kW (plus is import), +581 kvar; volts 0.990 to 1.000; busiest transformer 43%; inside every limit |
| 1326 | SITE SURVEY | generic site 1199 | CONFIRMED | connection point -445 kW (plus is import), +530 kvar; volts 0.990 to 1.002; busiest transformer 61%; inside every limit |
| 1327 | SITE SURVEY | generic site 1200 | CONFIRMED | connection point -2732 kW (plus is import), +2253 kvar; volts 0.972 to 1.000; busiest transformer 793%; export 2732 kW is 2682 kW over the 50 kW limit: the sola |
| 1328 | SITE SURVEY | generic site 1201 | CONFIRMED | connection point -158 kW (plus is import), +234 kvar; volts 0.990 to 1.004; busiest transformer 102%; a transformer is at 102% of its rating |
| 1329 | SITE SURVEY | generic site 1202 | CONFIRMED | connection point -174 kW (plus is import), +337 kvar; volts 0.989 to 1.002; busiest transformer 69%; inside every limit |
| 1330 | SITE SURVEY | generic site 1203 | CONFIRMED | connection point -1531 kW (plus is import), +1228 kvar; volts 0.989 to 1.013; busiest transformer 358%; export 1531 kW is 1331 kW over the 200 kW limit: the sol |
| 1331 | SITE SURVEY | generic site 1204 | CONFIRMED | connection point -1876 kW (plus is import), +772 kvar; volts 0.988 to 1.013; busiest transformer 267%; export 1876 kW is 1876 kW over the 0 kW limit: the solar  |
| 1332 | SITE SURVEY | generic site 1205 | CONFIRMED | connection point -1964 kW (plus is import), +1229 kvar; volts 0.986 to 1.004; busiest transformer 175%; export 1964 kW is 1964 kW over the 0 kW limit: the solar |
| 1333 | SITE SURVEY | generic site 1206 | CONFIRMED | connection point +97 kW (plus is import), +332 kvar; volts 0.988 to 1.000; busiest transformer 47%; inside every limit |
| 1334 | SITE SURVEY | generic site 1207 | CONFIRMED | connection point -3214 kW (plus is import), +1732 kvar; volts 0.986 to 1.009; busiest transformer 545%; export 3214 kW is 2214 kW over the 1000 kW limit: the so |
| 1335 | SITE SURVEY | generic site 1208 | CONFIRMED | connection point -857 kW (plus is import), +171 kvar; volts 0.994 to 1.004; busiest transformer 60%; export 857 kW is 807 kW over the 50 kW limit: the solar mus |
| 1336 | SITE SURVEY | generic site 1209 | CONFIRMED | connection point -2998 kW (plus is import), +2483 kvar; volts 0.976 to 1.000; busiest transformer 613%; export 2998 kW is 1998 kW over the 1000 kW limit: the so |
| 1337 | SITE SURVEY | generic site 1210 | CONFIRMED | connection point -981 kW (plus is import), +373 kvar; volts 0.993 to 1.013; busiest transformer 266%; export 981 kW is 781 kW over the 200 kW limit: the solar m |
| 1338 | SITE SURVEY | generic site 1211 | CONFIRMED | connection point -1365 kW (plus is import), +629 kvar; volts 0.990 to 1.016; busiest transformer 380%; export 1365 kW is 1315 kW over the 50 kW limit: the solar |
| 1339 | SITE SURVEY | generic site 1212 | CONFIRMED | connection point -2686 kW (plus is import), +1955 kvar; volts 0.983 to 1.007; busiest transformer 448%; export 2686 kW is 2186 kW over the 500 kW limit: the sol |
| 1340 | SITE SURVEY | generic site 1213 | CONFIRMED | connection point -799 kW (plus is import), +830 kvar; volts 0.990 to 1.010; busiest transformer 197%; export 799 kW is 299 kW over the 500 kW limit: the solar m |
| 1341 | SITE SURVEY | generic site 1214 | CONFIRMED | connection point -1413 kW (plus is import), +387 kvar; volts 0.994 to 1.007; busiest transformer 109%; export 1413 kW is 913 kW over the 500 kW limit: the solar |
| 1342 | SITE SURVEY | generic site 1215 | CONFIRMED | connection point -1275 kW (plus is import), +584 kvar; volts 0.991 to 1.004; busiest transformer 98%; export 1275 kW is 1075 kW over the 200 kW limit: the solar |
| 1343 | SITE SURVEY | generic site 1216 | CONFIRMED | connection point -2425 kW (plus is import), +2068 kvar; volts 0.979 to 1.000; busiest transformer 740%; export 2425 kW is 1425 kW over the 1000 kW limit: the so |
| 1344 | SITE SURVEY | generic site 1217 | CONFIRMED | connection point +229 kW (plus is import), +341 kvar; volts 0.988 to 1.000; busiest transformer 24%; inside every limit |
| 1345 | SITE SURVEY | generic site 1218 | CONFIRMED | connection point -1361 kW (plus is import), +674 kvar; volts 0.993 to 1.016; busiest transformer 266%; export 1361 kW is 861 kW over the 500 kW limit: the solar |
| 1346 | SITE SURVEY | generic site 1219 | CONFIRMED | connection point -3448 kW (plus is import), +1530 kvar; volts 0.986 to 1.008; busiest transformer 246%; export 3448 kW is 3448 kW over the 0 kW limit: the solar |
| 1347 | SITE SURVEY | generic site 1220 | CONFIRMED | connection point -1945 kW (plus is import), +867 kvar; volts 0.989 to 1.012; busiest transformer 276%; export 1945 kW is 945 kW over the 1000 kW limit: the sola |
| 1348 | SITE SURVEY | generic site 1221 | CONFIRMED | connection point -1504 kW (plus is import), +296 kvar; volts 0.995 to 1.006; busiest transformer 101%; export 1504 kW is 1304 kW over the 200 kW limit: the sola |
| 1349 | SITE SURVEY | generic site 1222 | CONFIRMED | connection point -731 kW (plus is import), +846 kvar; volts 0.986 to 1.012; busiest transformer 355%; export 731 kW is 531 kW over the 200 kW limit: the solar m |
| 1350 | SITE SURVEY | generic site 1223 | CONFIRMED | connection point -537 kW (plus is import), +797 kvar; volts 0.988 to 1.010; busiest transformer 313%; export 537 kW is 537 kW over the 0 kW limit: the solar mus |
| 1351 | SITE SURVEY | generic site 1224 | CONFIRMED | connection point -572 kW (plus is import), +235 kvar; volts 0.994 to 1.005; busiest transformer 102%; export 572 kW is 572 kW over the 0 kW limit: the solar mus |
| 1352 | SITE SURVEY | generic site 1225 | CONFIRMED | connection point -2737 kW (plus is import), +1193 kvar; volts 0.991 to 1.015; busiest transformer 367%; export 2737 kW is 2537 kW over the 200 kW limit: the sol |
| 1353 | SITE SURVEY | generic site 1226 | CONFIRMED | connection point -2342 kW (plus is import), +780 kvar; volts 0.992 to 1.012; busiest transformer 194%; export 2342 kW is 2342 kW over the 0 kW limit: the solar  |
| 1354 | SITE SURVEY | generic site 1227 | CONFIRMED | connection point +206 kW (plus is import), +552 kvar; volts 0.987 to 1.000; busiest transformer 30%; inside every limit |
| 1355 | SITE SURVEY | generic site 1228 | CONFIRMED | connection point -662 kW (plus is import), +187 kvar; volts 0.993 to 1.006; busiest transformer 87%; export 662 kW is 662 kW over the 0 kW limit: the solar must |
| 1356 | SITE SURVEY | generic site 1229 | CONFIRMED | connection point -1578 kW (plus is import), +308 kvar; volts 0.997 to 1.009; busiest transformer 110%; export 1578 kW is 578 kW over the 1000 kW limit: the sola |
| 1357 | SITE SURVEY | generic site 1230 | CONFIRMED | connection point -3141 kW (plus is import), +1956 kvar; volts 0.985 to 1.009; busiest transformer 479%; export 3141 kW is 2641 kW over the 500 kW limit: the sol |
| 1358 | SITE SURVEY | generic site 1231 | CONFIRMED | connection point -3174 kW (plus is import), +966 kvar; volts 0.991 to 1.013; busiest transformer 204%; export 3174 kW is 2674 kW over the 500 kW limit: the sola |
| 1359 | SITE SURVEY | generic site 1232 | CONFIRMED | connection point -1245 kW (plus is import), +647 kvar; volts 0.989 to 1.003; busiest transformer 98%; export 1245 kW is 1195 kW over the 50 kW limit: the solar  |
| 1360 | SITE SURVEY | generic site 1233 | CONFIRMED | connection point -800 kW (plus is import), +420 kvar; volts 0.992 to 1.003; busiest transformer 82%; export 800 kW is 750 kW over the 50 kW limit: the solar mus |
| 1361 | SITE SURVEY | generic site 1234 | CONFIRMED | connection point -845 kW (plus is import), +598 kvar; volts 0.989 to 1.005; busiest transformer 88%; export 845 kW is 845 kW over the 0 kW limit: the solar must |
| 1362 | SITE SURVEY | generic site 1235 | CONFIRMED | connection point -3940 kW (plus is import), +1440 kvar; volts 0.991 to 1.020; busiest transformer 321%; export 3940 kW is 3940 kW over the 0 kW limit: the solar |
| 1363 | SITE SURVEY | generic site 1236 | CONFIRMED | connection point +398 kW (plus is import), +748 kvar; volts 0.985 to 1.003; busiest transformer 173%; a transformer is at 173% of its rating |
| 1364 | SITE SURVEY | generic site 1237 | CONFIRMED | connection point -1819 kW (plus is import), +573 kvar; volts 0.993 to 1.012; busiest transformer 231%; export 1819 kW is 819 kW over the 1000 kW limit: the sola |
| 1365 | SITE SURVEY | generic site 1238 | CONFIRMED | connection point -172 kW (plus is import), +133 kvar; volts 0.996 to 1.000; busiest transformer 17%; export 172 kW is 122 kW over the 50 kW limit: the solar mus |
| 1366 | SITE SURVEY | generic site 1239 | CONFIRMED | connection point -715 kW (plus is import), +195 kvar; volts 0.994 to 1.011; busiest transformer 177%; export 715 kW is 515 kW over the 200 kW limit: the solar m |
| 1367 | SITE SURVEY | generic site 1240 | CONFIRMED | connection point -4044 kW (plus is import), +1406 kvar; volts 0.989 to 1.016; busiest transformer 266%; export 4044 kW is 4044 kW over the 0 kW limit: the solar |
| 1368 | SITE SURVEY | generic site 1241 | CONFIRMED | connection point +34 kW (plus is import), +815 kvar; volts 0.986 to 1.003; busiest transformer 130%; a transformer is at 130% of its rating |
| 1369 | SITE SURVEY | generic site 1242 | CONFIRMED | connection point -890 kW (plus is import), +194 kvar; volts 0.994 to 1.003; busiest transformer 50%; export 890 kW is 840 kW over the 50 kW limit: the solar mus |
| 1370 | SITE SURVEY | generic site 1243 | CONFIRMED | connection point +60 kW (plus is import), +616 kvar; volts 0.986 to 1.000; busiest transformer 41%; inside every limit |
| 1371 | SITE SURVEY | generic site 1244 | CONFIRMED | connection point -3933 kW (plus is import), +1356 kvar; volts 0.991 to 1.017; busiest transformer 310%; export 3933 kW is 3883 kW over the 50 kW limit: the sola |
| 1372 | SITE SURVEY | generic site 1245 | CONFIRMED | connection point -2510 kW (plus is import), +1505 kvar; volts 0.987 to 1.014; busiest transformer 469%; export 2510 kW is 2010 kW over the 500 kW limit: the sol |
| 1373 | SITE SURVEY | generic site 1246 | CONFIRMED | connection point +78 kW (plus is import), +179 kvar; volts 0.994 to 1.000; busiest transformer 41%; inside every limit |
| 1374 | SITE SURVEY | generic site 1247 | CONFIRMED | connection point -5539 kW (plus is import), +4506 kvar; volts 0.959 to 1.000; busiest transformer 785%; export 5539 kW is 5539 kW over the 0 kW limit: the solar |
| 1375 | SITE SURVEY | generic site 1248 | CONFIRMED | connection point -4978 kW (plus is import), +3586 kvar; volts 0.975 to 1.000; busiest transformer 703%; export 4978 kW is 3978 kW over the 1000 kW limit: the so |
| 1376 | SITE SURVEY | generic site 1249 | CONFIRMED | connection point -5816 kW (plus is import), +2869 kvar; volts 0.983 to 1.013; busiest transformer 486%; export 5816 kW is 4816 kW over the 1000 kW limit: the so |
| 1377 | SITE SURVEY | generic site 1250 | CONFIRMED | connection point -2021 kW (plus is import), +651 kvar; volts 0.993 to 1.013; busiest transformer 251%; export 2021 kW is 2021 kW over the 0 kW limit: the solar  |
| 1378 | SITE SURVEY | generic site 1251 | CONFIRMED | connection point -5545 kW (plus is import), +4637 kvar; volts 0.963 to 1.000; busiest transformer 800%; export 5545 kW is 4545 kW over the 1000 kW limit: the so |
| 1379 | SITE SURVEY | generic site 1252 | CONFIRMED | connection point -4570 kW (plus is import), +3192 kvar; volts 0.976 to 1.000; busiest transformer 653%; export 4570 kW is 3570 kW over the 1000 kW limit: the so |
| 1380 | SITE SURVEY | generic site 1253 | CONFIRMED | connection point -430 kW (plus is import), +592 kvar; volts 0.989 to 1.000; busiest transformer 77%; export 430 kW is 380 kW over the 50 kW limit: the solar mus |
| 1381 | SITE SURVEY | generic site 1254 | CONFIRMED | connection point -238 kW (plus is import), +691 kvar; volts 0.987 to 1.010; busiest transformer 251%; a transformer is at 251% of its rating |
| 1382 | SITE SURVEY | generic site 1255 | CONFIRMED | connection point -1784 kW (plus is import), +892 kvar; volts 0.991 to 1.013; busiest transformer 482%; export 1784 kW is 1734 kW over the 50 kW limit: the solar |
| 1383 | SITE SURVEY | generic site 1256 | CONFIRMED | connection point +276 kW (plus is import), +479 kvar; volts 0.988 to 1.000; busiest transformer 57%; inside every limit |
| 1384 | SITE SURVEY | generic site 1257 | CONFIRMED | connection point -3738 kW (plus is import), +1411 kvar; volts 0.992 to 1.019; busiest transformer 310%; export 3738 kW is 3688 kW over the 50 kW limit: the sola |
| 1385 | SITE SURVEY | generic site 1258 | CONFIRMED | connection point -1910 kW (plus is import), +408 kvar; volts 0.996 to 1.011; busiest transformer 112%; export 1910 kW is 1860 kW over the 50 kW limit: the solar |
| 1386 | SITE SURVEY | generic site 1259 | CONFIRMED | connection point -1500 kW (plus is import), +612 kvar; volts 0.994 to 1.013; busiest transformer 143%; export 1500 kW is 1300 kW over the 200 kW limit: the sola |
| 1387 | SITE SURVEY | generic site 1260 | CONFIRMED | connection point -539 kW (plus is import), +144 kvar; volts 0.995 to 1.007; busiest transformer 131%; export 539 kW is 339 kW over the 200 kW limit: the solar m |
| 1388 | SITE SURVEY | generic site 1261 | CONFIRMED | connection point -901 kW (plus is import), +229 kvar; volts 0.996 to 1.009; busiest transformer 115%; export 901 kW is 701 kW over the 200 kW limit: the solar m |
| 1389 | SITE SURVEY | generic site 1262 | CONFIRMED | connection point -663 kW (plus is import), +297 kvar; volts 0.994 to 1.002; busiest transformer 62%; export 663 kW is 663 kW over the 0 kW limit: the solar must |
| 1390 | SITE SURVEY | generic site 1263 | CONFIRMED | connection point -1127 kW (plus is import), +1141 kvar; volts 0.985 to 1.001; busiest transformer 134%; export 1127 kW is 127 kW over the 1000 kW limit: the sol |
| 1391 | SITE SURVEY | generic site 1264 | CONFIRMED | connection point -1262 kW (plus is import), +280 kvar; volts 0.993 to 1.006; busiest transformer 93%; export 1262 kW is 1062 kW over the 200 kW limit: the solar |
| 1392 | SITE SURVEY | generic site 1265 | CONFIRMED | connection point -738 kW (plus is import), +201 kvar; volts 0.995 to 1.011; busiest transformer 181%; a transformer is at 181% of its rating |
| 1393 | SITE SURVEY | generic site 1266 | CONFIRMED | connection point -2719 kW (plus is import), +3364 kvar; volts 0.927 to 1.000; busiest transformer 919%; export 2719 kW is 1719 kW over the 1000 kW limit: the so |
| 1394 | SITE SURVEY | generic site 1267 | CONFIRMED | connection point -185 kW (plus is import), +277 kvar; volts 0.993 to 1.000; busiest transformer 29%; inside every limit |
| 1395 | SITE SURVEY | generic site 1268 | CONFIRMED | connection point -146 kW (plus is import), +141 kvar; volts 0.995 to 1.004; busiest transformer 72%; export 146 kW is 146 kW over the 0 kW limit: the solar must |
| 1396 | SITE SURVEY | generic site 1269 | CONFIRMED | connection point -615 kW (plus is import), +562 kvar; volts 0.989 to 1.005; busiest transformer 94%; export 615 kW is 565 kW over the 50 kW limit: the solar mus |
| 1397 | SITE SURVEY | generic site 1270 | CONFIRMED | connection point -2784 kW (plus is import), +856 kvar; volts 0.992 to 1.016; busiest transformer 180%; export 2784 kW is 2784 kW over the 0 kW limit: the solar  |
| 1398 | SITE SURVEY | generic site 1271 | CONFIRMED | connection point -43 kW (plus is import), +192 kvar; volts 0.990 to 1.001; busiest transformer 66%; inside every limit |
| 1399 | SITE SURVEY | generic site 1272 | CONFIRMED | connection point -1614 kW (plus is import), +299 kvar; volts 0.995 to 1.009; busiest transformer 95%; export 1614 kW is 1114 kW over the 500 kW limit: the solar |
| 1400 | SITE SURVEY | generic site 1273 | CONFIRMED | connection point -1468 kW (plus is import), +1091 kvar; volts 0.986 to 1.003; busiest transformer 145%; export 1468 kW is 968 kW over the 500 kW limit: the sola |
| 1401 | SITE SURVEY | generic site 1274 | CONFIRMED | connection point -705 kW (plus is import), +213 kvar; volts 0.995 to 1.010; busiest transformer 175%; export 705 kW is 655 kW over the 50 kW limit: the solar mu |
| 1402 | SITE SURVEY | generic site 1275 | CONFIRMED | connection point -4701 kW (plus is import), +3273 kvar; volts 0.973 to 1.000; busiest transformer 664%; export 4701 kW is 4501 kW over the 200 kW limit: the sol |
| 1403 | SITE SURVEY | generic site 1276 | CONFIRMED | connection point +79 kW (plus is import), +208 kvar; volts 0.993 to 1.000; busiest transformer 28%; inside every limit |
| 1404 | SITE SURVEY | generic site 1277 | CONFIRMED | connection point -1714 kW (plus is import), +439 kvar; volts 0.992 to 1.006; busiest transformer 127%; export 1714 kW is 1214 kW over the 500 kW limit: the sola |
| 1405 | SITE SURVEY | generic site 1278 | CONFIRMED | connection point -1104 kW (plus is import), +205 kvar; volts 0.997 to 1.004; busiest transformer 73%; export 1104 kW is 904 kW over the 200 kW limit: the solar  |
| 1406 | SITE SURVEY | generic site 1279 | CONFIRMED | connection point -2261 kW (plus is import), +2829 kvar; volts 0.957 to 1.000; busiest transformer 834%; export 2261 kW is 2261 kW over the 0 kW limit: the solar |
| 1407 | SITE SURVEY | generic site 1280 | CONFIRMED | connection point -148 kW (plus is import), +533 kvar; volts 0.989 to 1.004; busiest transformer 125%; export 148 kW is 148 kW over the 0 kW limit: the solar mus |
| 1408 | SITE SURVEY | generic site 1281 | CONFIRMED | connection point -2029 kW (plus is import), +601 kvar; volts 0.991 to 1.016; busiest transformer 248%; export 2029 kW is 1829 kW over the 200 kW limit: the sola |
| 1409 | SITE SURVEY | generic site 1282 | CONFIRMED | connection point +27 kW (plus is import), +120 kvar; volts 0.995 to 1.000; busiest transformer 12%; inside every limit |
| 1410 | SITE SURVEY | generic site 1283 | CONFIRMED | connection point -1724 kW (plus is import), +777 kvar; volts 0.991 to 1.014; busiest transformer 448%; export 1724 kW is 1524 kW over the 200 kW limit: the sola |
| 1411 | SITE SURVEY | generic site 1284 | CONFIRMED | connection point -3873 kW (plus is import), +2525 kvar; volts 0.984 to 1.000; busiest transformer 667%; export 3873 kW is 2873 kW over the 1000 kW limit: the so |
| 1412 | SITE SURVEY | generic site 1285 | CONFIRMED | connection point -2237 kW (plus is import), +535 kvar; volts 0.997 to 1.017; busiest transformer 169%; export 2237 kW is 1237 kW over the 1000 kW limit: the sol |
| 1413 | SITE SURVEY | generic site 1286 | CONFIRMED | connection point -1140 kW (plus is import), +333 kvar; volts 0.993 to 1.008; busiest transformer 147%; export 1140 kW is 940 kW over the 200 kW limit: the solar |
| 1414 | SITE SURVEY | generic site 1287 | CONFIRMED | connection point -869 kW (plus is import), +506 kvar; volts 0.990 to 1.008; busiest transformer 182%; export 869 kW is 369 kW over the 500 kW limit: the solar m |
| 1415 | SITE SURVEY | generic site 1288 | CONFIRMED | connection point -3904 kW (plus is import), +2059 kvar; volts 0.988 to 1.012; busiest transformer 522%; export 3904 kW is 3704 kW over the 200 kW limit: the sol |
| 1416 | SITE SURVEY | generic site 1289 | CONFIRMED | connection point -2601 kW (plus is import), +2100 kvar; volts 0.978 to 1.000; busiest transformer 758%; export 2601 kW is 1601 kW over the 1000 kW limit: the so |
| 1417 | SITE SURVEY | generic site 1290 | CONFIRMED | connection point -1808 kW (plus is import), +1644 kvar; volts 0.982 to 1.005; busiest transformer 362%; export 1808 kW is 808 kW over the 1000 kW limit: the sol |
| 1418 | SITE SURVEY | generic site 1291 | CONFIRMED | connection point -669 kW (plus is import), +655 kvar; volts 0.990 to 1.006; busiest transformer 104%; export 669 kW is 469 kW over the 200 kW limit: the solar m |
| 1419 | SITE SURVEY | generic site 1292 | CONFIRMED | connection point -1691 kW (plus is import), +849 kvar; volts 0.989 to 1.015; busiest transformer 263%; export 1691 kW is 1191 kW over the 500 kW limit: the sola |
| 1420 | SITE SURVEY | generic site 1293 | CONFIRMED | connection point -288 kW (plus is import), +295 kvar; volts 0.990 to 1.007; busiest transformer 142%; a transformer is at 142% of its rating |
| 1421 | SITE SURVEY | generic site 1294 | CONFIRMED | connection point -2103 kW (plus is import), +450 kvar; volts 0.993 to 1.009; busiest transformer 125%; export 2103 kW is 2053 kW over the 50 kW limit: the solar |
| 1422 | SITE SURVEY | generic site 1295 | CONFIRMED | connection point -517 kW (plus is import), +268 kvar; volts 0.991 to 1.007; busiest transformer 108%; a transformer is at 108% of its rating |
| 1423 | SITE SURVEY | generic site 1296 | CONFIRMED | connection point -2613 kW (plus is import), +2057 kvar; volts 0.978 to 1.000; busiest transformer 752%; export 2613 kW is 2413 kW over the 200 kW limit: the sol |
| 1424 | SITE SURVEY | generic site 1297 | CONFIRMED | connection point +314 kW (plus is import), +475 kvar; volts 0.987 to 1.000; busiest transformer 46%; inside every limit |
| 1425 | SITE SURVEY | generic site 1298 | CONFIRMED | connection point -370 kW (plus is import), +298 kvar; volts 0.991 to 1.002; busiest transformer 92%; inside every limit |
| 1426 | SITE SURVEY | generic site 1299 | CONFIRMED | connection point -1311 kW (plus is import), +732 kvar; volts 0.990 to 1.006; busiest transformer 137%; export 1311 kW is 811 kW over the 500 kW limit: the solar |
| 1427 | SITE SURVEY | generic site 1300 | CONFIRMED | connection point +214 kW (plus is import), +326 kvar; volts 0.989 to 1.000; busiest transformer 22%; inside every limit |
| 1428 | SITE SURVEY | generic site 1301 | CONFIRMED | connection point -77 kW (plus is import), +810 kvar; volts 0.985 to 1.006; busiest transformer 173%; a transformer is at 173% of its rating |
| 1429 | SITE SURVEY | generic site 1302 | CONFIRMED | connection point -97 kW (plus is import), +646 kvar; volts 0.987 to 1.000; busiest transformer 59%; inside every limit |
| 1430 | SITE SURVEY | generic site 1303 | CONFIRMED | connection point -1877 kW (plus is import), +595 kvar; volts 0.992 to 1.014; busiest transformer 234%; export 1877 kW is 877 kW over the 1000 kW limit: the sola |
| 1431 | SITE SURVEY | generic site 1304 | CONFIRMED | connection point -2559 kW (plus is import), +1131 kvar; volts 0.989 to 1.015; busiest transformer 347%; export 2559 kW is 2509 kW over the 50 kW limit: the sola |
| 1432 | SITE SURVEY | generic site 1305 | CONFIRMED | connection point -2178 kW (plus is import), +576 kvar; volts 0.993 to 1.011; busiest transformer 167%; export 2178 kW is 2128 kW over the 50 kW limit: the solar |
| 1433 | SITE SURVEY | generic site 1306 | CONFIRMED | connection point -3480 kW (plus is import), +2147 kvar; volts 0.983 to 1.004; busiest transformer 508%; export 3480 kW is 2480 kW over the 1000 kW limit: the so |
| 1434 | SITE SURVEY | generic site 1307 | CONFIRMED | connection point -646 kW (plus is import), +461 kvar; volts 0.989 to 1.006; busiest transformer 129%; export 646 kW is 446 kW over the 200 kW limit: the solar m |
| 1435 | SITE SURVEY | generic site 1308 | CONFIRMED | connection point -781 kW (plus is import), +507 kvar; volts 0.989 to 1.002; busiest transformer 75%; export 781 kW is 731 kW over the 50 kW limit: the solar mus |
| 1436 | SITE SURVEY | generic site 1309 | CONFIRMED | connection point -915 kW (plus is import), +852 kvar; volts 0.986 to 1.004; busiest transformer 129%; export 915 kW is 715 kW over the 200 kW limit: the solar m |
| 1437 | SITE SURVEY | generic site 1310 | CONFIRMED | connection point -1022 kW (plus is import), +692 kvar; volts 0.989 to 1.003; busiest transformer 94%; export 1022 kW is 22 kW over the 1000 kW limit: the solar  |
| 1438 | SITE SURVEY | generic site 1311 | CONFIRMED | connection point -1229 kW (plus is import), +301 kvar; volts 0.994 to 1.010; busiest transformer 180%; export 1229 kW is 229 kW over the 1000 kW limit: the sola |
| 1439 | SITE SURVEY | generic site 1312 | CONFIRMED | connection point -4158 kW (plus is import), +1433 kvar; volts 0.985 to 1.012; busiest transformer 264%; export 4158 kW is 3658 kW over the 500 kW limit: the sol |
| 1440 | SITE SURVEY | generic site 1313 | CONFIRMED | connection point -2062 kW (plus is import), +813 kvar; volts 0.991 to 1.011; busiest transformer 151%; export 2062 kW is 1062 kW over the 1000 kW limit: the sol |
| 1441 | SITE SURVEY | generic site 1314 | CONFIRMED | connection point -1007 kW (plus is import), +689 kvar; volts 0.990 to 1.014; busiest transformer 350%; export 1007 kW is 957 kW over the 50 kW limit: the solar  |
| 1442 | SITE SURVEY | generic site 1315 | CONFIRMED | connection point -2354 kW (plus is import), +1123 kvar; volts 0.988 to 1.017; busiest transformer 410%; export 2354 kW is 1354 kW over the 1000 kW limit: the so |
| 1443 | SITE SURVEY | generic site 1316 | CONFIRMED | connection point -601 kW (plus is import), +179 kvar; volts 0.995 to 1.004; busiest transformer 93%; inside every limit |
| 1444 | SITE SURVEY | generic site 1317 | CONFIRMED | connection point -2678 kW (plus is import), +1169 kvar; volts 0.988 to 1.009; busiest transformer 360%; export 2678 kW is 2478 kW over the 200 kW limit: the sol |
| 1445 | SITE SURVEY | generic site 1318 | CONFIRMED | connection point -1647 kW (plus is import), +1158 kvar; volts 0.985 to 1.011; busiest transformer 357%; export 1647 kW is 647 kW over the 1000 kW limit: the sol |
| 1446 | SITE SURVEY | generic site 1319 | CONFIRMED | connection point -2214 kW (plus is import), +1012 kvar; volts 0.987 to 1.013; busiest transformer 376%; export 2214 kW is 1214 kW over the 1000 kW limit: the so |
| 1447 | SITE SURVEY | generic site 1320 | CONFIRMED | connection point -186 kW (plus is import), +183 kvar; volts 0.992 to 1.000; busiest transformer 52%; inside every limit |
| 1448 | SITE SURVEY | generic site 1321 | CONFIRMED | connection point -1611 kW (plus is import), +896 kvar; volts 0.989 to 1.006; busiest transformer 167%; export 1611 kW is 1611 kW over the 0 kW limit: the solar  |
| 1449 | SITE SURVEY | generic site 1322 | CONFIRMED | connection point -895 kW (plus is import), +415 kvar; volts 0.992 to 1.012; busiest transformer 145%; export 895 kW is 895 kW over the 0 kW limit: the solar mus |
| 1450 | SITE SURVEY | generic site 1323 | CONFIRMED | connection point -327 kW (plus is import), +454 kvar; volts 0.989 to 1.001; busiest transformer 61%; export 327 kW is 277 kW over the 50 kW limit: the solar mus |
| 1451 | SITE SURVEY | generic site 1324 | CONFIRMED | connection point -1522 kW (plus is import), +737 kvar; volts 0.992 to 1.017; busiest transformer 287%; export 1522 kW is 522 kW over the 1000 kW limit: the sola |
| 1452 | SITE SURVEY | generic site 1325 | CONFIRMED | connection point -2096 kW (plus is import), +1618 kvar; volts 0.986 to 1.007; busiest transformer 252%; export 2096 kW is 1096 kW over the 1000 kW limit: the so |
| 1453 | SITE SURVEY | generic site 1326 | CONFIRMED | connection point -2739 kW (plus is import), +1064 kvar; volts 0.987 to 1.015; busiest transformer 352%; export 2739 kW is 2689 kW over the 50 kW limit: the sola |
| 1454 | SITE SURVEY | generic site 1327 | CONFIRMED | connection point -136 kW (plus is import), +406 kvar; volts 0.991 to 1.000; busiest transformer 28%; export 136 kW is 136 kW over the 0 kW limit: the solar must |
| 1455 | SITE SURVEY | generic site 1328 | CONFIRMED | connection point -532 kW (plus is import), +383 kvar; volts 0.990 to 1.004; busiest transformer 106%; export 532 kW is 332 kW over the 200 kW limit: the solar m |
| 1456 | SITE SURVEY | generic site 1329 | CONFIRMED | connection point -2523 kW (plus is import), +2005 kvar; volts 0.978 to 1.000; busiest transformer 740%; export 2523 kW is 2473 kW over the 50 kW limit: the sola |
| 1457 | SITE SURVEY | generic site 1330 | CONFIRMED | connection point -938 kW (plus is import), +339 kvar; volts 0.993 to 1.003; busiest transformer 76%; export 938 kW is 438 kW over the 500 kW limit: the solar mu |
| 1458 | SITE SURVEY | generic site 1331 | CONFIRMED | connection point -1136 kW (plus is import), +811 kvar; volts 0.991 to 1.004; busiest transformer 111%; export 1136 kW is 636 kW over the 500 kW limit: the solar |
| 1459 | SITE SURVEY | generic site 1332 | CONFIRMED | connection point -161 kW (plus is import), +123 kvar; volts 0.995 to 1.003; busiest transformer 67%; inside every limit |
| 1460 | SITE SURVEY | generic site 1333 | CONFIRMED | connection point -4363 kW (plus is import), +1390 kvar; volts 0.991 to 1.019; busiest transformer 277%; export 4363 kW is 4363 kW over the 0 kW limit: the solar |
| 1461 | SITE SURVEY | generic site 1334 | CONFIRMED | connection point -2365 kW (plus is import), +1189 kvar; volts 0.988 to 1.007; busiest transformer 227%; export 2365 kW is 2365 kW over the 0 kW limit: the solar |
| 1462 | SITE SURVEY | generic site 1335 | CONFIRMED | connection point -1481 kW (plus is import), +1021 kvar; volts 0.985 to 1.009; busiest transformer 181%; export 1481 kW is 1281 kW over the 200 kW limit: the sol |
| 1463 | SITE SURVEY | generic site 1336 | CONFIRMED | connection point -763 kW (plus is import), +516 kvar; volts 0.992 to 1.004; busiest transformer 90%; inside every limit |
| 1464 | SITE SURVEY | generic site 1337 | CONFIRMED | connection point -3238 kW (plus is import), +1869 kvar; volts 0.988 to 1.010; busiest transformer 468%; export 3238 kW is 2738 kW over the 500 kW limit: the sol |
| 1465 | SITE SURVEY | generic site 1338 | CONFIRMED | connection point +375 kW (plus is import), +964 kvar; volts 0.983 to 1.000; busiest transformer 65%; inside every limit |
| 1466 | SITE SURVEY | generic site 1339 | CONFIRMED | connection point -4880 kW (plus is import), +1692 kvar; volts 0.991 to 1.023; busiest transformer 307%; export 4880 kW is 4880 kW over the 0 kW limit: the solar |
| 1467 | SITE SURVEY | generic site 1340 | CONFIRMED | connection point -1905 kW (plus is import), +1309 kvar; volts 0.985 to 1.001; busiest transformer 572%; export 1905 kW is 905 kW over the 1000 kW limit: the sol |
| 1468 | SITE SURVEY | generic site 1341 | CONFIRMED | connection point -1185 kW (plus is import), +575 kvar; volts 0.990 to 1.008; busiest transformer 185%; export 1185 kW is 1135 kW over the 50 kW limit: the solar |
| 1469 | SITE SURVEY | generic site 1342 | CONFIRMED | connection point -4231 kW (plus is import), +1851 kvar; volts 0.985 to 1.016; busiest transformer 362%; export 4231 kW is 4231 kW over the 0 kW limit: the solar |
| 1470 | SITE SURVEY | generic site 1343 | CONFIRMED | connection point -465 kW (plus is import), +312 kvar; volts 0.992 to 1.006; busiest transformer 113%; export 465 kW is 265 kW over the 200 kW limit: the solar m |
| 1471 | SITE SURVEY | generic site 1344 | CONFIRMED | connection point -4093 kW (plus is import), +1471 kvar; volts 0.992 to 1.021; busiest transformer 329%; export 4093 kW is 3893 kW over the 200 kW limit: the sol |
| 1472 | SITE SURVEY | generic site 1345 | CONFIRMED | connection point -1123 kW (plus is import), +279 kvar; volts 0.994 to 1.012; busiest transformer 141%; export 1123 kW is 123 kW over the 1000 kW limit: the sola |
| 1473 | SITE SURVEY | generic site 1346 | CONFIRMED | connection point -2283 kW (plus is import), +1013 kvar; volts 0.992 to 1.017; busiest transformer 385%; export 2283 kW is 2083 kW over the 200 kW limit: the sol |
| 1474 | SITE SURVEY | generic site 1347 | CONFIRMED | connection point -1500 kW (plus is import), +521 kvar; volts 0.990 to 1.006; busiest transformer 106%; export 1500 kW is 1000 kW over the 500 kW limit: the sola |
| 1475 | SITE SURVEY | generic site 1348 | CONFIRMED | connection point -1801 kW (plus is import), +606 kvar; volts 0.996 to 1.015; busiest transformer 237%; export 1801 kW is 801 kW over the 1000 kW limit: the sola |
| 1476 | SITE SURVEY | generic site 1349 | CONFIRMED | connection point -1426 kW (plus is import), +342 kvar; volts 0.993 to 1.012; busiest transformer 168%; export 1426 kW is 1426 kW over the 0 kW limit: the solar  |
| 1477 | SITE SURVEY | generic site 1350 | CONFIRMED | connection point -2356 kW (plus is import), +783 kvar; volts 0.993 to 1.019; busiest transformer 299%; export 2356 kW is 2306 kW over the 50 kW limit: the solar |
| 1478 | SITE SURVEY | generic site 1351 | CONFIRMED | connection point -433 kW (plus is import), +301 kvar; volts 0.993 to 1.002; busiest transformer 99%; inside every limit |
| 1479 | SITE SURVEY | generic site 1352 | CONFIRMED | connection point -2829 kW (plus is import), +793 kvar; volts 0.991 to 1.012; busiest transformer 212%; export 2829 kW is 2329 kW over the 500 kW limit: the sola |
| 1480 | SITE SURVEY | generic site 1353 | CONFIRMED | connection point -1376 kW (plus is import), +472 kvar; volts 0.991 to 1.008; busiest transformer 97%; export 1376 kW is 876 kW over the 500 kW limit: the solar  |
| 1481 | SITE SURVEY | generic site 1354 | CONFIRMED | connection point +59 kW (plus is import), +561 kvar; volts 0.988 to 1.008; busiest transformer 175%; a transformer is at 175% of its rating |
| 1482 | SITE SURVEY | generic site 1355 | CONFIRMED | connection point -3191 kW (plus is import), +4379 kvar; volts 0.857 to 1.000; busiest transformer 1015%; export 3191 kW is 3191 kW over the 0 kW limit: the sola |
| 1483 | SITE SURVEY | generic site 1356 | CONFIRMED | connection point -723 kW (plus is import), +536 kvar; volts 0.989 to 1.011; busiest transformer 269%; export 723 kW is 523 kW over the 200 kW limit: the solar m |
| 1484 | SITE SURVEY | generic site 1357 | CONFIRMED | connection point -2257 kW (plus is import), +1119 kvar; volts 0.991 to 1.016; busiest transformer 397%; export 2257 kW is 2057 kW over the 200 kW limit: the sol |
| 1485 | SITE SURVEY | generic site 1358 | CONFIRMED | connection point -45 kW (plus is import), +92 kvar; volts 0.994 to 1.000; busiest transformer 26%; inside every limit |
| 1486 | SITE SURVEY | generic site 1359 | CONFIRMED | connection point -2590 kW (plus is import), +1947 kvar; volts 0.982 to 1.000; busiest transformer 738%; export 2590 kW is 2390 kW over the 200 kW limit: the sol |
| 1487 | SITE SURVEY | generic site 1360 | CONFIRMED | connection point -1884 kW (plus is import), +1083 kvar; volts 0.990 to 1.017; busiest transformer 307%; export 1884 kW is 1884 kW over the 0 kW limit: the solar |
| 1488 | SITE SURVEY | generic site 1361 | CONFIRMED | connection point -186 kW (plus is import), +244 kvar; volts 0.994 to 1.000; busiest transformer 23%; inside every limit |
| 1489 | SITE SURVEY | generic site 1362 | CONFIRMED | connection point -5295 kW (plus is import), +2559 kvar; volts 0.982 to 1.007; busiest transformer 371%; export 5295 kW is 5095 kW over the 200 kW limit: the sol |
| 1490 | SITE SURVEY | generic site 1363 | CONFIRMED | connection point -420 kW (plus is import), +266 kvar; volts 0.993 to 1.004; busiest transformer 96%; inside every limit |
| 1491 | SITE SURVEY | generic site 1364 | CONFIRMED | connection point -2491 kW (plus is import), +1102 kvar; volts 0.986 to 1.007; busiest transformer 186%; export 2491 kW is 2491 kW over the 0 kW limit: the solar |
| 1492 | SITE SURVEY | generic site 1365 | CONFIRMED | connection point -1257 kW (plus is import), +833 kvar; volts 0.987 to 1.011; busiest transformer 229%; export 1257 kW is 1057 kW over the 200 kW limit: the sola |
| 1493 | SITE SURVEY | generic site 1366 | CONFIRMED | connection point -23 kW (plus is import), +296 kvar; volts 0.992 to 1.005; busiest transformer 104%; a transformer is at 104% of its rating |
| 1494 | SITE SURVEY | generic site 1367 | CONFIRMED | connection point -530 kW (plus is import), +494 kvar; volts 0.991 to 1.010; busiest transformer 234%; a transformer is at 234% of its rating |
| 1495 | SITE SURVEY | generic site 1368 | CONFIRMED | connection point -930 kW (plus is import), +406 kvar; volts 0.992 to 1.000; busiest transformer 64%; export 930 kW is 930 kW over the 0 kW limit: the solar must |
| 1496 | SITE SURVEY | generic site 1369 | CONFIRMED | connection point -1193 kW (plus is import), +911 kvar; volts 0.988 to 1.014; busiest transformer 426%; export 1193 kW is 993 kW over the 200 kW limit: the solar |
| 1497 | SITE SURVEY | generic site 1370 | CONFIRMED | connection point -1321 kW (plus is import), +758 kvar; volts 0.989 to 1.005; busiest transformer 118%; export 1321 kW is 821 kW over the 500 kW limit: the solar |
| 1498 | SITE SURVEY | generic site 1371 | CONFIRMED | connection point -1067 kW (plus is import), +600 kvar; volts 0.990 to 1.008; busiest transformer 176%; export 1067 kW is 1017 kW over the 50 kW limit: the solar |
| 1499 | SITE SURVEY | generic site 1372 | REFUTED | connection point -3303 kW (plus is import), +6144 kvar; volts 0.830 to 1.000; busiest transformer 1253%; export 3303 kW is 3103 kW over the 200 kW limit: the so |
| 1500 | SITE SURVEY | generic site 1373 | CONFIRMED | connection point +37 kW (plus is import), +227 kvar; volts 0.991 to 1.000; busiest transformer 40%; inside every limit |
| 1501 | SITE SURVEY | generic site 1374 | CONFIRMED | connection point -639 kW (plus is import), +286 kvar; volts 0.993 to 1.010; busiest transformer 188%; export 639 kW is 639 kW over the 0 kW limit: the solar mus |
| 1502 | SITE SURVEY | generic site 1375 | CONFIRMED | connection point -1636 kW (plus is import), +343 kvar; volts 0.995 to 1.011; busiest transformer 123%; export 1636 kW is 1636 kW over the 0 kW limit: the solar  |
| 1503 | SITE SURVEY | generic site 1376 | CONFIRMED | connection point +187 kW (plus is import), +617 kvar; volts 0.985 to 1.003; busiest transformer 111%; a transformer is at 111% of its rating |
| 1504 | SITE SURVEY | generic site 1377 | CONFIRMED | connection point -1645 kW (plus is import), +572 kvar; volts 0.993 to 1.018; busiest transformer 268%; export 1645 kW is 645 kW over the 1000 kW limit: the sola |
| 1505 | SITE SURVEY | generic site 1378 | CONFIRMED | connection point -787 kW (plus is import), +206 kvar; volts 0.993 to 1.009; busiest transformer 122%; export 787 kW is 787 kW over the 0 kW limit: the solar mus |
| 1506 | SITE SURVEY | generic site 1379 | CONFIRMED | connection point -2568 kW (plus is import), +911 kvar; volts 0.993 to 1.016; busiest transformer 180%; export 2568 kW is 2568 kW over the 0 kW limit: the solar  |
| 1507 | SITE SURVEY | generic site 1380 | CONFIRMED | connection point -309 kW (plus is import), +776 kvar; volts 0.986 to 1.000; busiest transformer 90%; export 309 kW is 259 kW over the 50 kW limit: the solar mus |
| 1508 | SITE SURVEY | generic site 1381 | CONFIRMED | connection point -2160 kW (plus is import), +836 kvar; volts 0.992 to 1.017; busiest transformer 353%; export 2160 kW is 1960 kW over the 200 kW limit: the sola |
| 1509 | SITE SURVEY | generic site 1382 | CONFIRMED | connection point +171 kW (plus is import), +667 kvar; volts 0.986 to 1.000; busiest transformer 90%; inside every limit |
| 1510 | SITE SURVEY | generic site 1383 | CONFIRMED | connection point -481 kW (plus is import), +224 kvar; volts 0.991 to 1.007; busiest transformer 146%; export 481 kW is 431 kW over the 50 kW limit: the solar mu |
| 1511 | SITE SURVEY | generic site 1384 | CONFIRMED | connection point -3099 kW (plus is import), +999 kvar; volts 0.989 to 1.012; busiest transformer 205%; export 3099 kW is 2899 kW over the 200 kW limit: the sola |
| 1512 | SITE SURVEY | generic site 1385 | CONFIRMED | connection point -150 kW (plus is import), +238 kvar; volts 0.991 to 1.006; busiest transformer 105%; a transformer is at 105% of its rating |
| 1513 | SITE SURVEY | generic site 1386 | CONFIRMED | connection point -110 kW (plus is import), +543 kvar; volts 0.989 to 1.004; busiest transformer 103%; export 110 kW is 110 kW over the 0 kW limit: the solar mus |
| 1514 | SITE SURVEY | generic site 1387 | CONFIRMED | connection point -225 kW (plus is import), +826 kvar; volts 0.986 to 1.000; busiest transformer 75%; export 225 kW is 175 kW over the 50 kW limit: the solar mus |
| 1515 | SITE SURVEY | generic site 1388 | CONFIRMED | connection point -1538 kW (plus is import), +733 kvar; volts 0.989 to 1.016; busiest transformer 288%; export 1538 kW is 538 kW over the 1000 kW limit: the sola |
| 1516 | SITE SURVEY | generic site 1389 | CONFIRMED | connection point +181 kW (plus is import), +314 kvar; volts 0.989 to 1.000; busiest transformer 25%; inside every limit |
| 1517 | SITE SURVEY | generic site 1390 | CONFIRMED | connection point -154 kW (plus is import), +294 kvar; volts 0.989 to 1.007; busiest transformer 125%; a transformer is at 125% of its rating |
| 1518 | SITE SURVEY | generic site 1391 | CONFIRMED | connection point -2953 kW (plus is import), +1160 kvar; volts 0.993 to 1.019; busiest transformer 377%; export 2953 kW is 2903 kW over the 50 kW limit: the sola |
| 1519 | SITE SURVEY | generic site 1392 | CONFIRMED | connection point -66 kW (plus is import), +421 kvar; volts 0.989 to 1.000; busiest transformer 72%; inside every limit |
| 1520 | SITE SURVEY | generic site 1393 | CONFIRMED | connection point -2213 kW (plus is import), +1155 kvar; volts 0.988 to 1.017; busiest transformer 402%; export 2213 kW is 2013 kW over the 200 kW limit: the sol |
| 1521 | SITE SURVEY | generic site 1394 | CONFIRMED | connection point -1759 kW (plus is import), +738 kvar; volts 0.989 to 1.016; busiest transformer 304%; export 1759 kW is 759 kW over the 1000 kW limit: the sola |
| 1522 | SITE SURVEY | generic site 1395 | CONFIRMED | connection point -2249 kW (plus is import), +3253 kvar; volts 0.938 to 1.000; busiest transformer 882%; export 2249 kW is 2249 kW over the 0 kW limit: the solar |
| 1523 | SITE SURVEY | generic site 1396 | CONFIRMED | connection point -1479 kW (plus is import), +322 kvar; volts 0.994 to 1.006; busiest transformer 104%; export 1479 kW is 979 kW over the 500 kW limit: the solar |
| 1524 | SITE SURVEY | generic site 1397 | CONFIRMED | connection point -835 kW (plus is import), +194 kvar; volts 0.996 to 1.008; busiest transformer 102%; export 835 kW is 635 kW over the 200 kW limit: the solar m |
| 1525 | SITE SURVEY | generic site 1398 | CONFIRMED | connection point -2234 kW (plus is import), +809 kvar; volts 0.991 to 1.014; busiest transformer 288%; export 2234 kW is 1734 kW over the 500 kW limit: the sola |
| 1526 | SITE SURVEY | generic site 1399 | CONFIRMED | connection point -295 kW (plus is import), +603 kvar; volts 0.987 to 1.000; busiest transformer 75%; inside every limit |
| 1527 | SITE SURVEY | generic site 1400 | CONFIRMED | connection point -1305 kW (plus is import), +543 kvar; volts 0.992 to 1.002; busiest transformer 91%; export 1305 kW is 1255 kW over the 50 kW limit: the solar  |
| 1528 | SITE SURVEY | generic site 1401 | CONFIRMED | connection point -2774 kW (plus is import), +2213 kvar; volts 0.981 to 1.007; busiest transformer 482%; export 2774 kW is 2574 kW over the 200 kW limit: the sol |
| 1529 | SITE SURVEY | generic site 1402 | CONFIRMED | connection point -3570 kW (plus is import), +1055 kvar; volts 0.994 to 1.012; busiest transformer 219%; export 3570 kW is 3520 kW over the 50 kW limit: the sola |
| 1530 | SITE SURVEY | generic site 1403 | CONFIRMED | connection point -781 kW (plus is import), +467 kvar; volts 0.990 to 1.007; busiest transformer 137%; export 781 kW is 781 kW over the 0 kW limit: the solar mus |
| 1531 | SITE SURVEY | generic site 1404 | CONFIRMED | connection point +246 kW (plus is import), +743 kvar; volts 0.988 to 1.000; busiest transformer 122%; a transformer is at 122% of its rating |
| 1532 | SITE SURVEY | generic site 1405 | CONFIRMED | connection point -1537 kW (plus is import), +761 kvar; volts 0.994 to 1.017; busiest transformer 430%; export 1537 kW is 1337 kW over the 200 kW limit: the sola |
| 1533 | SITE SURVEY | generic site 1406 | CONFIRMED | connection point -1507 kW (plus is import), +690 kvar; volts 0.992 to 1.018; busiest transformer 409%; export 1507 kW is 1007 kW over the 500 kW limit: the sola |
| 1534 | SITE SURVEY | generic site 1407 | CONFIRMED | connection point -702 kW (plus is import), +175 kvar; volts 0.996 to 1.007; busiest transformer 108%; export 702 kW is 652 kW over the 50 kW limit: the solar mu |
| 1535 | SITE SURVEY | generic site 1408 | CONFIRMED | connection point -1918 kW (plus is import), +1076 kvar; volts 0.986 to 1.006; busiest transformer 527%; export 1918 kW is 918 kW over the 1000 kW limit: the sol |
| 1536 | SITE SURVEY | generic site 1409 | CONFIRMED | connection point -2352 kW (plus is import), +568 kvar; volts 0.993 to 1.014; busiest transformer 175%; export 2352 kW is 2152 kW over the 200 kW limit: the sola |
| 1537 | SITE SURVEY | generic site 1410 | CONFIRMED | connection point -274 kW (plus is import), +312 kvar; volts 0.990 to 1.002; busiest transformer 86%; export 274 kW is 274 kW over the 0 kW limit: the solar must |
| 1538 | SITE SURVEY | generic site 1411 | CONFIRMED | connection point -3590 kW (plus is import), +1452 kvar; volts 0.991 to 1.015; busiest transformer 252%; export 3590 kW is 2590 kW over the 1000 kW limit: the so |
| 1539 | SITE SURVEY | generic site 1412 | CONFIRMED | connection point -2051 kW (plus is import), +1395 kvar; volts 0.987 to 1.013; busiest transformer 356%; export 2051 kW is 1551 kW over the 500 kW limit: the sol |
| 1540 | SITE SURVEY | generic site 1413 | CONFIRMED | connection point -2471 kW (plus is import), +1256 kvar; volts 0.991 to 1.013; busiest transformer 429%; export 2471 kW is 1471 kW over the 1000 kW limit: the so |
| 1541 | SITE SURVEY | generic site 1414 | REFUTED | connection point -3087 kW (plus is import), +5718 kvar; volts 0.769 to 1.000; busiest transformer 1065%; export 3087 kW is 2087 kW over the 1000 kW limit: the s |
| 1542 | SITE SURVEY | generic site 1415 | CONFIRMED | connection point -4512 kW (plus is import), +1771 kvar; volts 0.991 to 1.021; busiest transformer 306%; export 4512 kW is 4312 kW over the 200 kW limit: the sol |
| 1543 | SITE SURVEY | generic site 1416 | CONFIRMED | connection point -1202 kW (plus is import), +350 kvar; volts 0.996 to 1.004; busiest transformer 91%; export 1202 kW is 1202 kW over the 0 kW limit: the solar m |
| 1544 | SITE SURVEY | generic site 1417 | CONFIRMED | connection point -1889 kW (plus is import), +1506 kvar; volts 0.985 to 1.003; busiest transformer 609%; export 1889 kW is 1389 kW over the 500 kW limit: the sol |
| 1545 | SITE SURVEY | generic site 1418 | CONFIRMED | connection point -3194 kW (plus is import), +1358 kvar; volts 0.985 to 1.012; busiest transformer 277%; export 3194 kW is 2694 kW over the 500 kW limit: the sol |
| 1546 | SITE SURVEY | generic site 1419 | CONFIRMED | connection point -890 kW (plus is import), +732 kvar; volts 0.989 to 1.000; busiest transformer 90%; export 890 kW is 840 kW over the 50 kW limit: the solar mus |
| 1547 | SITE SURVEY | generic site 1420 | CONFIRMED | connection point -763 kW (plus is import), +1409 kvar; volts 0.983 to 1.004; busiest transformer 477%; a transformer is at 477% of its rating |
| 1548 | SITE SURVEY | generic site 1421 | CONFIRMED | connection point -1007 kW (plus is import), +171 kvar; volts 0.999 to 1.005; busiest transformer 55%; export 1007 kW is 957 kW over the 50 kW limit: the solar m |
| 1549 | SITE SURVEY | generic site 1422 | CONFIRMED | connection point -462 kW (plus is import), +201 kvar; volts 0.991 to 1.000; busiest transformer 39%; inside every limit |
| 1550 | SITE SURVEY | generic site 1423 | CONFIRMED | connection point +80 kW (plus is import), +790 kvar; volts 0.985 to 1.000; busiest transformer 116%; a transformer is at 116% of its rating |
| 1551 | SITE SURVEY | generic site 1424 | CONFIRMED | connection point -992 kW (plus is import), +326 kvar; volts 0.994 to 1.003; busiest transformer 63%; export 992 kW is 942 kW over the 50 kW limit: the solar mus |
| 1552 | SITE SURVEY | generic site 1425 | CONFIRMED | connection point -518 kW (plus is import), +261 kvar; volts 0.992 to 1.006; busiest transformer 107%; export 518 kW is 468 kW over the 50 kW limit: the solar mu |
| 1553 | SITE SURVEY | generic site 1426 | CONFIRMED | connection point -2351 kW (plus is import), +594 kvar; volts 0.996 to 1.008; busiest transformer 137%; export 2351 kW is 1351 kW over the 1000 kW limit: the sol |
| 1554 | SITE SURVEY | generic site 1427 | CONFIRMED | connection point +339 kW (plus is import), +1063 kvar; volts 0.983 to 1.000; busiest transformer 86%; inside every limit |
| 1555 | SITE SURVEY | generic site 1428 | CONFIRMED | connection point -4761 kW (plus is import), +1930 kvar; volts 0.986 to 1.015; busiest transformer 383%; export 4761 kW is 4261 kW over the 500 kW limit: the sol |
| 1556 | SITE SURVEY | generic site 1429 | CONFIRMED | connection point -1697 kW (plus is import), +346 kvar; volts 0.994 to 1.002; busiest transformer 90%; export 1697 kW is 1197 kW over the 500 kW limit: the solar |
| 1557 | SITE SURVEY | generic site 1430 | CONFIRMED | connection point -5245 kW (plus is import), +3135 kvar; volts 0.980 to 1.006; busiest transformer 485%; export 5245 kW is 5045 kW over the 200 kW limit: the sol |
| 1558 | SITE SURVEY | generic site 1431 | CONFIRMED | connection point -1936 kW (plus is import), +1103 kvar; volts 0.987 to 1.016; busiest transformer 375%; export 1936 kW is 1436 kW over the 500 kW limit: the sol |
| 1559 | SITE SURVEY | generic site 1432 | CONFIRMED | connection point -1629 kW (plus is import), +508 kvar; volts 0.992 to 1.013; busiest transformer 207%; export 1629 kW is 1579 kW over the 50 kW limit: the solar |
| 1560 | SITE SURVEY | generic site 1433 | CONFIRMED | connection point -1328 kW (plus is import), +927 kvar; volts 0.990 to 1.010; busiest transformer 165%; export 1328 kW is 1128 kW over the 200 kW limit: the sola |
| 1561 | SITE SURVEY | generic site 1434 | CONFIRMED | connection point -360 kW (plus is import), +123 kvar; volts 0.996 to 1.005; busiest transformer 65%; inside every limit |
| 1562 | SITE SURVEY | generic site 1435 | CONFIRMED | connection point -1074 kW (plus is import), +628 kvar; volts 0.991 to 1.011; busiest transformer 339%; export 1074 kW is 1074 kW over the 0 kW limit: the solar  |
| 1563 | SITE SURVEY | generic site 1436 | CONFIRMED | connection point -979 kW (plus is import), +1297 kvar; volts 0.984 to 1.003; busiest transformer 175%; export 979 kW is 779 kW over the 200 kW limit: the solar  |
| 1564 | SITE SURVEY | generic site 1437 | CONFIRMED | connection point -1779 kW (plus is import), +436 kvar; volts 0.993 to 1.007; busiest transformer 110%; export 1779 kW is 1279 kW over the 500 kW limit: the sola |
| 1565 | SITE SURVEY | generic site 1438 | CONFIRMED | connection point +161 kW (plus is import), +520 kvar; volts 0.987 to 1.000; busiest transformer 66%; inside every limit |
| 1566 | SITE SURVEY | generic site 1439 | CONFIRMED | connection point -2346 kW (plus is import), +1970 kvar; volts 0.984 to 1.000; busiest transformer 719%; export 2346 kW is 2146 kW over the 200 kW limit: the sol |
| 1567 | SITE SURVEY | generic site 1440 | CONFIRMED | connection point -537 kW (plus is import), +492 kvar; volts 0.990 to 1.000; busiest transformer 54%; export 537 kW is 487 kW over the 50 kW limit: the solar mus |
| 1568 | SITE SURVEY | generic site 1441 | CONFIRMED | connection point -2845 kW (plus is import), +2784 kvar; volts 0.951 to 1.000; busiest transformer 864%; export 2845 kW is 1845 kW over the 1000 kW limit: the so |
| 1569 | SITE SURVEY | generic site 1442 | CONFIRMED | connection point -1349 kW (plus is import), +693 kvar; volts 0.990 to 1.013; busiest transformer 220%; export 1349 kW is 849 kW over the 500 kW limit: the solar |
| 1570 | SITE SURVEY | generic site 1443 | CONFIRMED | connection point +21 kW (plus is import), +295 kvar; volts 0.990 to 1.000; busiest transformer 41%; inside every limit |
| 1571 | SITE SURVEY | generic site 1444 | CONFIRMED | connection point -2125 kW (plus is import), +1323 kvar; volts 0.987 to 1.011; busiest transformer 414%; export 2125 kW is 1625 kW over the 500 kW limit: the sol |
| 1572 | SITE SURVEY | generic site 1445 | CONFIRMED | connection point -1426 kW (plus is import), +519 kvar; volts 0.994 to 1.013; busiest transformer 237%; export 1426 kW is 926 kW over the 500 kW limit: the solar |
| 1573 | SITE SURVEY | generic site 1446 | CONFIRMED | connection point +115 kW (plus is import), +297 kvar; volts 0.991 to 1.000; busiest transformer 76%; inside every limit |
| 1574 | SITE SURVEY | generic site 1447 | CONFIRMED | connection point -770 kW (plus is import), +312 kvar; volts 0.994 to 1.001; busiest transformer 66%; inside every limit |
| 1575 | SITE SURVEY | generic site 1448 | CONFIRMED | connection point -1309 kW (plus is import), +676 kvar; volts 0.990 to 1.014; busiest transformer 379%; export 1309 kW is 1309 kW over the 0 kW limit: the solar  |
| 1576 | SITE SURVEY | generic site 1449 | CONFIRMED | connection point -562 kW (plus is import), +302 kvar; volts 0.991 to 1.011; busiest transformer 190%; a transformer is at 190% of its rating |
| 1577 | SITE SURVEY | generic site 1450 | CONFIRMED | connection point -2163 kW (plus is import), +773 kvar; volts 0.995 to 1.015; busiest transformer 155%; export 2163 kW is 1163 kW over the 1000 kW limit: the sol |
| 1578 | SITE SURVEY | generic site 1451 | CONFIRMED | connection point -2673 kW (plus is import), +986 kvar; volts 0.992 to 1.017; busiest transformer 339%; export 2673 kW is 2473 kW over the 200 kW limit: the sola |
| 1579 | SITE SURVEY | generic site 1452 | CONFIRMED | connection point -1644 kW (plus is import), +706 kvar; volts 0.992 to 1.016; busiest transformer 239%; export 1644 kW is 1144 kW over the 500 kW limit: the sola |
| 1580 | SITE SURVEY | generic site 1453 | CONFIRMED | connection point -1320 kW (plus is import), +341 kvar; volts 0.996 to 1.005; busiest transformer 97%; export 1320 kW is 820 kW over the 500 kW limit: the solar  |
| 1581 | SITE SURVEY | generic site 1454 | CONFIRMED | connection point -829 kW (plus is import), +1068 kvar; volts 0.987 to 1.011; busiest transformer 419%; export 829 kW is 329 kW over the 500 kW limit: the solar  |
| 1582 | SITE SURVEY | generic site 1455 | CONFIRMED | connection point +191 kW (plus is import), +533 kvar; volts 0.987 to 1.006; busiest transformer 148%; a transformer is at 148% of its rating |
| 1583 | SITE SURVEY | generic site 1456 | CONFIRMED | connection point -1307 kW (plus is import), +517 kvar; volts 0.989 to 1.012; busiest transformer 232%; export 1307 kW is 307 kW over the 1000 kW limit: the sola |
| 1584 | SITE SURVEY | generic site 1457 | CONFIRMED | connection point -1558 kW (plus is import), +445 kvar; volts 0.993 to 1.015; busiest transformer 238%; export 1558 kW is 1558 kW over the 0 kW limit: the solar  |
| 1585 | SITE SURVEY | generic site 1458 | CONFIRMED | connection point -1161 kW (plus is import), +545 kvar; volts 0.990 to 1.002; busiest transformer 107%; export 1161 kW is 1111 kW over the 50 kW limit: the solar |
| 1586 | SITE SURVEY | generic site 1459 | CONFIRMED | connection point -114 kW (plus is import), +283 kvar; volts 0.990 to 1.004; busiest transformer 111%; a transformer is at 111% of its rating |
| 1587 | SITE SURVEY | generic site 1460 | CONFIRMED | connection point -3455 kW (plus is import), +2223 kvar; volts 0.980 to 1.003; busiest transformer 516%; export 3455 kW is 2455 kW over the 1000 kW limit: the so |
| 1588 | SITE SURVEY | generic site 1461 | CONFIRMED | connection point -871 kW (plus is import), +285 kvar; volts 0.992 to 1.015; busiest transformer 228%; export 871 kW is 821 kW over the 50 kW limit: the solar mu |
| 1589 | SITE SURVEY | generic site 1462 | CONFIRMED | connection point -1197 kW (plus is import), +753 kvar; volts 0.990 to 1.015; busiest transformer 389%; export 1197 kW is 697 kW over the 500 kW limit: the solar |
| 1590 | SITE SURVEY | generic site 1463 | CONFIRMED | connection point -2760 kW (plus is import), +1328 kvar; volts 0.991 to 1.013; busiest transformer 210%; export 2760 kW is 1760 kW over the 1000 kW limit: the so |
| 1591 | SITE SURVEY | generic site 1464 | CONFIRMED | connection point -3216 kW (plus is import), +1098 kvar; volts 0.988 to 1.011; busiest transformer 258%; export 3216 kW is 3016 kW over the 200 kW limit: the sol |
| 1592 | SITE SURVEY | generic site 1465 | CONFIRMED | connection point -1836 kW (plus is import), +929 kvar; volts 0.990 to 1.016; busiest transformer 339%; export 1836 kW is 836 kW over the 1000 kW limit: the sola |
| 1593 | SITE SURVEY | generic site 1466 | CONFIRMED | connection point +137 kW (plus is import), +551 kvar; volts 0.987 to 1.000; busiest transformer 45%; inside every limit |
| 1594 | SITE SURVEY | generic site 1467 | CONFIRMED | connection point -2574 kW (plus is import), +1971 kvar; volts 0.982 to 1.000; busiest transformer 736%; export 2574 kW is 2574 kW over the 0 kW limit: the solar |
| 1595 | SITE SURVEY | generic site 1468 | CONFIRMED | connection point -3261 kW (plus is import), +1475 kvar; volts 0.990 to 1.011; busiest transformer 238%; export 3261 kW is 3061 kW over the 200 kW limit: the sol |
| 1596 | SITE SURVEY | generic site 1469 | CONFIRMED | connection point -489 kW (plus is import), +153 kvar; volts 0.996 to 1.002; busiest transformer 74%; export 489 kW is 289 kW over the 200 kW limit: the solar mu |
| 1597 | SITE SURVEY | generic site 1470 | CONFIRMED | connection point -2612 kW (plus is import), +791 kvar; volts 0.992 to 1.017; busiest transformer 212%; export 2612 kW is 2112 kW over the 500 kW limit: the sola |
| 1598 | SITE SURVEY | generic site 1471 | CONFIRMED | connection point -379 kW (plus is import), +144 kvar; volts 0.995 to 1.008; busiest transformer 113%; a transformer is at 113% of its rating |
| 1599 | SITE SURVEY | generic site 1472 | CONFIRMED | connection point -1100 kW (plus is import), +289 kvar; volts 0.991 to 1.008; busiest transformer 90%; export 1100 kW is 100 kW over the 1000 kW limit: the solar |
| 1600 | SITE SURVEY | generic site 1473 | CONFIRMED | connection point -524 kW (plus is import), +291 kvar; volts 0.993 to 1.000; busiest transformer 34%; export 524 kW is 524 kW over the 0 kW limit: the solar must |
| 1601 | SITE SURVEY | generic site 1474 | CONFIRMED | connection point -1323 kW (plus is import), +358 kvar; volts 0.993 to 1.007; busiest transformer 99%; export 1323 kW is 1323 kW over the 0 kW limit: the solar m |
| 1602 | SITE SURVEY | generic site 1475 | CONFIRMED | connection point -821 kW (plus is import), +236 kvar; volts 0.996 to 1.004; busiest transformer 52%; export 821 kW is 771 kW over the 50 kW limit: the solar mus |
| 1603 | SITE SURVEY | generic site 1476 | CONFIRMED | connection point -60 kW (plus is import), +413 kvar; volts 0.988 to 1.007; busiest transformer 147%; export 60 kW is 10 kW over the 50 kW limit: the solar must  |
| 1604 | SITE SURVEY | generic site 1477 | CONFIRMED | connection point +404 kW (plus is import), +671 kvar; volts 0.985 to 1.000; busiest transformer 95%; inside every limit |
| 1605 | SITE SURVEY | generic site 1478 | CONFIRMED | connection point -4476 kW (plus is import), +2578 kvar; volts 0.977 to 1.000; busiest transformer 595%; export 4476 kW is 3476 kW over the 1000 kW limit: the so |
| 1606 | SITE SURVEY | generic site 1479 | CONFIRMED | connection point -970 kW (plus is import), +236 kvar; volts 0.993 to 1.004; busiest transformer 73%; export 970 kW is 470 kW over the 500 kW limit: the solar mu |
| 1607 | SITE SURVEY | generic site 1480 | CONFIRMED | connection point -2133 kW (plus is import), +1461 kvar; volts 0.988 to 1.000; busiest transformer 619%; export 2133 kW is 1633 kW over the 500 kW limit: the sol |
| 1608 | SITE SURVEY | generic site 1481 | CONFIRMED | connection point -847 kW (plus is import), +376 kvar; volts 0.990 to 1.013; busiest transformer 249%; export 847 kW is 647 kW over the 200 kW limit: the solar m |
| 1609 | SITE SURVEY | generic site 1482 | CONFIRMED | connection point -851 kW (plus is import), +380 kvar; volts 0.993 to 1.001; busiest transformer 74%; export 851 kW is 801 kW over the 50 kW limit: the solar mus |
| 1610 | SITE SURVEY | generic site 1483 | CONFIRMED | connection point -2128 kW (plus is import), +882 kvar; volts 0.991 to 1.017; busiest transformer 355%; export 2128 kW is 1628 kW over the 500 kW limit: the sola |
| 1611 | SITE SURVEY | generic site 1484 | CONFIRMED | connection point +54 kW (plus is import), +227 kvar; volts 0.993 to 1.000; busiest transformer 33%; inside every limit |
| 1612 | SITE SURVEY | generic site 1485 | CONFIRMED | connection point -2380 kW (plus is import), +1147 kvar; volts 0.988 to 1.011; busiest transformer 228%; export 2380 kW is 2330 kW over the 50 kW limit: the sola |
| 1613 | SITE SURVEY | generic site 1486 | CONFIRMED | connection point -420 kW (plus is import), +1040 kvar; volts 0.984 to 1.004; busiest transformer 132%; export 420 kW is 370 kW over the 50 kW limit: the solar m |
| 1614 | SITE SURVEY | generic site 1487 | CONFIRMED | connection point -7029 kW (plus is import), +3473 kvar; volts 0.975 to 1.000; busiest transformer 466%; export 7029 kW is 6529 kW over the 500 kW limit: the sol |
| 1615 | SITE SURVEY | generic site 1488 | CONFIRMED | connection point -1191 kW (plus is import), +402 kvar; volts 0.991 to 1.006; busiest transformer 82%; export 1191 kW is 191 kW over the 1000 kW limit: the solar |
| 1616 | SITE SURVEY | generic site 1489 | CONFIRMED | connection point -1334 kW (plus is import), +336 kvar; volts 0.992 to 1.010; busiest transformer 107%; export 1334 kW is 1134 kW over the 200 kW limit: the sola |
| 1617 | SITE SURVEY | generic site 1490 | CONFIRMED | connection point -3753 kW (plus is import), +1200 kvar; volts 0.991 to 1.017; busiest transformer 286%; export 3753 kW is 3753 kW over the 0 kW limit: the solar |
| 1618 | SITE SURVEY | generic site 1491 | CONFIRMED | connection point -61 kW (plus is import), +221 kvar; volts 0.992 to 1.000; busiest transformer 18%; inside every limit |
| 1619 | SITE SURVEY | generic site 1492 | CONFIRMED | connection point +203 kW (plus is import), +408 kvar; volts 0.988 to 1.001; busiest transformer 97%; inside every limit |
| 1620 | SITE SURVEY | generic site 1493 | REFUTED | connection point -2758 kW (plus is import), +5667 kvar; volts 0.802 to 1.000; busiest transformer 1093%; export 2758 kW is 1758 kW over the 1000 kW limit: the s |
| 1621 | SITE SURVEY | generic site 1494 | CONFIRMED | connection point -1175 kW (plus is import), +486 kvar; volts 0.992 to 1.017; busiest transformer 322%; export 1175 kW is 1175 kW over the 0 kW limit: the solar  |
| 1622 | SITE SURVEY | generic site 1495 | CONFIRMED | connection point -1147 kW (plus is import), +645 kvar; volts 0.990 to 1.009; busiest transformer 126%; export 1147 kW is 647 kW over the 500 kW limit: the solar |
| 1623 | SITE SURVEY | generic site 1496 | CONFIRMED | connection point -2912 kW (plus is import), +1074 kvar; volts 0.992 to 1.015; busiest transformer 197%; export 2912 kW is 2712 kW over the 200 kW limit: the sol |
| 1624 | SITE SURVEY | generic site 1497 | CONFIRMED | connection point -345 kW (plus is import), +161 kvar; volts 0.991 to 1.000; busiest transformer 30%; export 345 kW is 145 kW over the 200 kW limit: the solar mu |
| 1625 | SITE SURVEY | generic site 1498 | CONFIRMED | connection point -1788 kW (plus is import), +595 kvar; volts 0.992 to 1.011; busiest transformer 230%; export 1788 kW is 1788 kW over the 0 kW limit: the solar  |
| 1626 | SITE SURVEY | generic site 1499 | CONFIRMED | connection point -908 kW (plus is import), +468 kvar; volts 0.991 to 1.014; busiest transformer 278%; export 908 kW is 708 kW over the 200 kW limit: the solar m |
| 1627 | SITE SURVEY | generic site 1500 | CONFIRMED | connection point -449 kW (plus is import), +361 kvar; volts 0.990 to 1.004; busiest transformer 96%; inside every limit |
| 1628 | SITE SURVEY | generic site 1501 | CONFIRMED | connection point -851 kW (plus is import), +1299 kvar; volts 0.984 to 1.008; busiest transformer 321%; a transformer is at 321% of its rating |
| 1629 | SITE SURVEY | generic site 1502 | CONFIRMED | connection point -367 kW (plus is import), +360 kvar; volts 0.992 to 1.000; busiest transformer 51%; inside every limit |
| 1630 | SITE SURVEY | generic site 1503 | CONFIRMED | connection point +154 kW (plus is import), +408 kvar; volts 0.988 to 1.000; busiest transformer 25%; inside every limit |
| 1631 | SITE SURVEY | generic site 1504 | CONFIRMED | connection point -3361 kW (plus is import), +1473 kvar; volts 0.985 to 1.008; busiest transformer 241%; export 3361 kW is 3361 kW over the 0 kW limit: the solar |
| 1632 | SITE SURVEY | generic site 1505 | CONFIRMED | connection point -76 kW (plus is import), +94 kvar; volts 0.991 to 1.000; busiest transformer 39%; inside every limit |
| 1633 | SITE SURVEY | generic site 1506 | CONFIRMED | connection point -1819 kW (plus is import), +856 kvar; volts 0.989 to 1.012; busiest transformer 479%; export 1819 kW is 1619 kW over the 200 kW limit: the sola |
| 1634 | SITE SURVEY | generic site 1507 | CONFIRMED | connection point -1174 kW (plus is import), +286 kvar; volts 0.993 to 1.006; busiest transformer 87%; export 1174 kW is 1124 kW over the 50 kW limit: the solar  |
| 1635 | SITE SURVEY | generic site 1508 | CONFIRMED | connection point -3228 kW (plus is import), +884 kvar; volts 0.988 to 1.010; busiest transformer 197%; export 3228 kW is 3228 kW over the 0 kW limit: the solar  |
| 1636 | SITE SURVEY | generic site 1509 | CONFIRMED | connection point -511 kW (plus is import), +440 kvar; volts 0.990 to 1.008; busiest transformer 143%; a transformer is at 143% of its rating |
| 1637 | SITE SURVEY | generic site 1510 | CONFIRMED | connection point -2197 kW (plus is import), +668 kvar; volts 0.994 to 1.016; busiest transformer 178%; export 2197 kW is 2147 kW over the 50 kW limit: the solar |
| 1638 | SITE SURVEY | generic site 1511 | CONFIRMED | connection point -2478 kW (plus is import), +934 kvar; volts 0.989 to 1.015; busiest transformer 326%; export 2478 kW is 1478 kW over the 1000 kW limit: the sol |
| 1639 | SITE SURVEY | generic site 1512 | CONFIRMED | connection point -1019 kW (plus is import), +675 kvar; volts 0.988 to 1.007; busiest transformer 124%; export 1019 kW is 519 kW over the 500 kW limit: the solar |
| 1640 | SITE SURVEY | generic site 1513 | CONFIRMED | connection point -1810 kW (plus is import), +1021 kvar; volts 0.989 to 1.016; busiest transformer 351%; export 1810 kW is 810 kW over the 1000 kW limit: the sol |
| 1641 | SITE SURVEY | generic site 1514 | CONFIRMED | connection point -1301 kW (plus is import), +467 kvar; volts 0.993 to 1.014; busiest transformer 219%; export 1301 kW is 1101 kW over the 200 kW limit: the sola |
| 1642 | SITE SURVEY | generic site 1515 | CONFIRMED | connection point -3505 kW (plus is import), +2516 kvar; volts 0.977 to 1.000; busiest transformer 551%; export 3505 kW is 3005 kW over the 500 kW limit: the sol |
| 1643 | SITE SURVEY | generic site 1516 | CONFIRMED | connection point -2057 kW (plus is import), +1064 kvar; volts 0.986 to 1.005; busiest transformer 540%; export 2057 kW is 1057 kW over the 1000 kW limit: the so |
| 1644 | SITE SURVEY | generic site 1517 | CONFIRMED | connection point -1740 kW (plus is import), +589 kvar; volts 0.996 to 1.015; busiest transformer 153%; export 1740 kW is 1740 kW over the 0 kW limit: the solar  |
| 1645 | SITE SURVEY | generic site 1518 | CONFIRMED | connection point -2437 kW (plus is import), +689 kvar; volts 0.992 to 1.011; busiest transformer 187%; export 2437 kW is 2437 kW over the 0 kW limit: the solar  |
| 1646 | SITE SURVEY | generic site 1519 | CONFIRMED | connection point -1925 kW (plus is import), +528 kvar; volts 0.998 to 1.017; busiest transformer 230%; export 1925 kW is 1725 kW over the 200 kW limit: the sola |
| 1647 | SITE SURVEY | generic site 1520 | CONFIRMED | connection point -710 kW (plus is import), +711 kvar; volts 0.989 to 1.000; busiest transformer 80%; export 710 kW is 660 kW over the 50 kW limit: the solar mus |
| 1648 | SITE SURVEY | generic site 1521 | CONFIRMED | connection point -980 kW (plus is import), +174 kvar; volts 0.997 to 1.007; busiest transformer 70%; export 980 kW is 980 kW over the 0 kW limit: the solar must |
| 1649 | SITE SURVEY | generic site 1522 | CONFIRMED | connection point -1786 kW (plus is import), +1291 kvar; volts 0.986 to 1.005; busiest transformer 563%; export 1786 kW is 1586 kW over the 200 kW limit: the sol |
| 1650 | SITE SURVEY | generic site 1523 | CONFIRMED | connection point -1936 kW (plus is import), +975 kvar; volts 0.986 to 1.011; busiest transformer 515%; export 1936 kW is 1936 kW over the 0 kW limit: the solar  |
| 1651 | SITE SURVEY | generic site 1524 | CONFIRMED | connection point -100 kW (plus is import), +100 kvar; volts 0.993 to 1.000; busiest transformer 20%; inside every limit |
| 1652 | SITE SURVEY | generic site 1525 | CONFIRMED | connection point -4835 kW (plus is import), +1778 kvar; volts 0.983 to 1.013; busiest transformer 313%; export 4835 kW is 4785 kW over the 50 kW limit: the sola |
| 1653 | SITE SURVEY | generic site 1526 | CONFIRMED | connection point -1961 kW (plus is import), +980 kvar; volts 0.987 to 1.011; busiest transformer 292%; export 1961 kW is 1461 kW over the 500 kW limit: the sola |
| 1654 | SITE SURVEY | generic site 1527 | CONFIRMED | connection point -2851 kW (plus is import), +2801 kvar; volts 0.949 to 1.000; busiest transformer 869%; export 2851 kW is 2851 kW over the 0 kW limit: the solar |
| 1655 | SITE SURVEY | generic site 1528 | CONFIRMED | connection point +184 kW (plus is import), +354 kvar; volts 0.991 to 1.000; busiest transformer 22%; inside every limit |
| 1656 | SITE SURVEY | generic site 1529 | CONFIRMED | connection point +17 kW (plus is import), +398 kvar; volts 0.991 to 1.000; busiest transformer 33%; inside every limit |
| 1657 | SITE SURVEY | generic site 1530 | CONFIRMED | connection point -1036 kW (plus is import), +277 kvar; volts 0.995 to 1.007; busiest transformer 125%; export 1036 kW is 836 kW over the 200 kW limit: the solar |
| 1658 | SITE SURVEY | generic site 1531 | CONFIRMED | connection point -1674 kW (plus is import), +1220 kvar; volts 0.987 to 1.007; busiest transformer 536%; export 1674 kW is 1474 kW over the 200 kW limit: the sol |
| 1659 | SITE SURVEY | generic site 1532 | CONFIRMED | connection point -2014 kW (plus is import), +918 kvar; volts 0.991 to 1.013; busiest transformer 292%; export 2014 kW is 1514 kW over the 500 kW limit: the sola |
| 1660 | SITE SURVEY | generic site 1533 | CONFIRMED | connection point +369 kW (plus is import), +712 kvar; volts 0.986 to 1.000; busiest transformer 103%; a transformer is at 103% of its rating |
| 1661 | SITE SURVEY | generic site 1534 | CONFIRMED | connection point -21 kW (plus is import), +427 kvar; volts 0.989 to 1.000; busiest transformer 32%; inside every limit |
| 1662 | SITE SURVEY | generic site 1535 | CONFIRMED | connection point +87 kW (plus is import), +223 kvar; volts 0.994 to 1.000; busiest transformer 32%; inside every limit |
| 1663 | SITE SURVEY | generic site 1536 | CONFIRMED | connection point -307 kW (plus is import), +193 kvar; volts 0.994 to 1.000; busiest transformer 29%; export 307 kW is 257 kW over the 50 kW limit: the solar mus |
| 1664 | SITE SURVEY | generic site 1537 | CONFIRMED | connection point -2878 kW (plus is import), +1454 kvar; volts 0.987 to 1.015; busiest transformer 407%; export 2878 kW is 2378 kW over the 500 kW limit: the sol |
| 1665 | SITE SURVEY | generic site 1538 | CONFIRMED | connection point -758 kW (plus is import), +242 kvar; volts 0.994 to 1.004; busiest transformer 64%; export 758 kW is 558 kW over the 200 kW limit: the solar mu |
| 1666 | SITE SURVEY | generic site 1539 | CONFIRMED | connection point +13 kW (plus is import), +164 kvar; volts 0.992 to 1.000; busiest transformer 21%; inside every limit |
| 1667 | SITE SURVEY | generic site 1540 | CONFIRMED | connection point -272 kW (plus is import), +121 kvar; volts 0.994 to 1.006; busiest transformer 87%; export 272 kW is 222 kW over the 50 kW limit: the solar mus |
| 1668 | SITE SURVEY | generic site 1541 | CONFIRMED | connection point -1452 kW (plus is import), +480 kvar; volts 0.994 to 1.013; busiest transformer 194%; export 1452 kW is 1252 kW over the 200 kW limit: the sola |
| 1669 | SITE SURVEY | generic site 1542 | CONFIRMED | connection point -827 kW (plus is import), +365 kvar; volts 0.991 to 1.015; busiest transformer 246%; export 827 kW is 627 kW over the 200 kW limit: the solar m |
| 1670 | SITE SURVEY | generic site 1543 | CONFIRMED | connection point -2336 kW (plus is import), +558 kvar; volts 0.993 to 1.009; busiest transformer 167%; export 2336 kW is 1336 kW over the 1000 kW limit: the sol |
| 1671 | SITE SURVEY | generic site 1544 | CONFIRMED | connection point -596 kW (plus is import), +286 kvar; volts 0.994 to 1.010; busiest transformer 187%; export 596 kW is 546 kW over the 50 kW limit: the solar mu |
| 1672 | SITE SURVEY | generic site 1545 | CONFIRMED | connection point -387 kW (plus is import), +239 kvar; volts 0.993 to 1.004; busiest transformer 73%; inside every limit |
| 1673 | SITE SURVEY | generic site 1546 | CONFIRMED | connection point -1820 kW (plus is import), +443 kvar; volts 0.997 to 1.015; busiest transformer 138%; export 1820 kW is 820 kW over the 1000 kW limit: the sola |
| 1674 | SITE SURVEY | generic site 1547 | CONFIRMED | connection point -4692 kW (plus is import), +1757 kvar; volts 0.990 to 1.019; busiest transformer 307%; export 4692 kW is 4642 kW over the 50 kW limit: the sola |
| 1675 | SITE SURVEY | generic site 1548 | CONFIRMED | connection point -1013 kW (plus is import), +739 kvar; volts 0.989 to 1.014; busiest transformer 359%; export 1013 kW is 513 kW over the 500 kW limit: the solar |
| 1676 | SITE SURVEY | generic site 1549 | CONFIRMED | connection point +312 kW (plus is import), +631 kvar; volts 0.987 to 1.000; busiest transformer 38%; inside every limit |
| 1677 | SITE SURVEY | generic site 1550 | CONFIRMED | connection point -1933 kW (plus is import), +692 kvar; volts 0.993 to 1.010; busiest transformer 135%; export 1933 kW is 1883 kW over the 50 kW limit: the solar |
| 1678 | SITE SURVEY | generic site 1551 | CONFIRMED | connection point +23 kW (plus is import), +548 kvar; volts 0.987 to 1.008; busiest transformer 175%; a transformer is at 175% of its rating |
| 1679 | SITE SURVEY | generic site 1552 | CONFIRMED | connection point -1358 kW (plus is import), +323 kvar; volts 0.997 to 1.010; busiest transformer 108%; export 1358 kW is 1158 kW over the 200 kW limit: the sola |
| 1680 | SITE SURVEY | generic site 1553 | CONFIRMED | connection point -172 kW (plus is import), +586 kvar; volts 0.991 to 1.002; busiest transformer 109%; a transformer is at 109% of its rating |
| 1681 | SITE SURVEY | generic site 1554 | CONFIRMED | connection point -1858 kW (plus is import), +1074 kvar; volts 0.989 to 1.013; busiest transformer 530%; export 1858 kW is 858 kW over the 1000 kW limit: the sol |
| 1682 | SITE SURVEY | generic site 1555 | CONFIRMED | connection point -1072 kW (plus is import), +296 kvar; volts 0.992 to 1.006; busiest transformer 70%; export 1072 kW is 1022 kW over the 50 kW limit: the solar  |
| 1683 | SITE SURVEY | generic site 1556 | CONFIRMED | connection point -1928 kW (plus is import), +873 kvar; volts 0.991 to 1.013; busiest transformer 274%; export 1928 kW is 1878 kW over the 50 kW limit: the solar |
| 1684 | SITE SURVEY | generic site 1557 | CONFIRMED | connection point -1663 kW (plus is import), +383 kvar; volts 0.994 to 1.009; busiest transformer 123%; export 1663 kW is 663 kW over the 1000 kW limit: the sola |
| 1685 | SITE SURVEY | generic site 1558 | CONFIRMED | connection point -786 kW (plus is import), +242 kvar; volts 0.995 to 1.011; busiest transformer 198%; export 786 kW is 586 kW over the 200 kW limit: the solar m |
| 1686 | SITE SURVEY | generic site 1559 | CONFIRMED | connection point -21 kW (plus is import), +707 kvar; volts 0.987 to 1.000; busiest transformer 67%; inside every limit |
| 1687 | SITE SURVEY | generic site 1560 | CONFIRMED | connection point -238 kW (plus is import), +904 kvar; volts 0.985 to 1.000; busiest transformer 97%; export 238 kW is 188 kW over the 50 kW limit: the solar mus |
| 1688 | SITE SURVEY | generic site 1561 | REFUTED | connection point -6167 kW (plus is import), +2046 kvar; volts 0.990 to 1.407; busiest transformer 2300%; export 6167 kW is 6167 kW over the 0 kW limit: the sola |
| 1689 | SITE SURVEY | generic site 1562 | CONFIRMED | connection point -1418 kW (plus is import), +703 kvar; volts 0.992 to 1.014; busiest transformer 398%; export 1418 kW is 1418 kW over the 0 kW limit: the solar  |
| 1690 | SITE SURVEY | generic site 1563 | CONFIRMED | connection point +327 kW (plus is import), +516 kvar; volts 0.987 to 1.003; busiest transformer 116%; a transformer is at 116% of its rating |
| 1691 | SITE SURVEY | generic site 1564 | CONFIRMED | connection point -513 kW (plus is import), +108 kvar; volts 0.994 to 1.009; busiest transformer 122%; a transformer is at 122% of its rating |
| 1692 | SITE SURVEY | generic site 1565 | CONFIRMED | connection point -2529 kW (plus is import), +2981 kvar; volts 0.945 to 1.000; busiest transformer 867%; export 2529 kW is 2479 kW over the 50 kW limit: the sola |
| 1693 | SITE SURVEY | generic site 1566 | CONFIRMED | connection point -459 kW (plus is import), +321 kvar; volts 0.990 to 1.000; busiest transformer 36%; export 459 kW is 409 kW over the 50 kW limit: the solar mus |
| 1694 | SITE SURVEY | generic site 1567 | CONFIRMED | connection point -2257 kW (plus is import), +897 kvar; volts 0.990 to 1.011; busiest transformer 200%; export 2257 kW is 1757 kW over the 500 kW limit: the sola |
| 1695 | SITE SURVEY | generic site 1568 | CONFIRMED | connection point -2937 kW (plus is import), +1051 kvar; volts 0.987 to 1.008; busiest transformer 194%; export 2937 kW is 1937 kW over the 1000 kW limit: the so |
| 1696 | SITE SURVEY | generic site 1569 | CONFIRMED | connection point -2458 kW (plus is import), +872 kvar; volts 0.990 to 1.011; busiest transformer 209%; export 2458 kW is 2458 kW over the 0 kW limit: the solar  |
| 1697 | SITE SURVEY | generic site 1570 | CONFIRMED | connection point -261 kW (plus is import), +104 kvar; volts 0.994 to 1.001; busiest transformer 70%; inside every limit |
| 1698 | SITE SURVEY | generic site 1571 | CONFIRMED | connection point -460 kW (plus is import), +193 kvar; volts 0.993 to 1.006; busiest transformer 90%; inside every limit |
| 1699 | SITE SURVEY | generic site 1572 | CONFIRMED | connection point -1773 kW (plus is import), +1077 kvar; volts 0.988 to 1.007; busiest transformer 191%; export 1773 kW is 1573 kW over the 200 kW limit: the sol |
| 1700 | SITE SURVEY | generic site 1573 | CONFIRMED | connection point -2061 kW (plus is import), +1290 kvar; volts 0.986 to 1.012; busiest transformer 341%; export 2061 kW is 1061 kW over the 1000 kW limit: the so |
| 1701 | SITE SURVEY | generic site 1574 | CONFIRMED | connection point -832 kW (plus is import), +657 kvar; volts 0.989 to 1.012; busiest transformer 215%; a transformer is at 215% of its rating |
| 1702 | SITE SURVEY | generic site 1575 | CONFIRMED | connection point -1598 kW (plus is import), +373 kvar; volts 0.994 to 1.010; busiest transformer 119%; export 1598 kW is 1398 kW over the 200 kW limit: the sola |
| 1703 | SITE SURVEY | generic site 1576 | CONFIRMED | connection point -1178 kW (plus is import), +1038 kvar; volts 0.985 to 1.012; busiest transformer 309%; export 1178 kW is 978 kW over the 200 kW limit: the sola |
| 1704 | SITE SURVEY | generic site 1577 | CONFIRMED | connection point -1232 kW (plus is import), +1801 kvar; volts 0.980 to 1.005; busiest transformer 350%; export 1232 kW is 1032 kW over the 200 kW limit: the sol |
| 1705 | SITE SURVEY | generic site 1578 | CONFIRMED | connection point -3700 kW (plus is import), +1254 kvar; volts 0.991 to 1.016; busiest transformer 294%; export 3700 kW is 3700 kW over the 0 kW limit: the solar |
| 1706 | SITE SURVEY | generic site 1579 | CONFIRMED | connection point -648 kW (plus is import), +178 kvar; volts 0.994 to 1.006; busiest transformer 102%; export 648 kW is 148 kW over the 500 kW limit: the solar m |
| 1707 | SITE SURVEY | generic site 1580 | CONFIRMED | connection point -1401 kW (plus is import), +975 kvar; volts 0.988 to 1.011; busiest transformer 257%; export 1401 kW is 1351 kW over the 50 kW limit: the solar |
| 1708 | SITE SURVEY | generic site 1581 | CONFIRMED | connection point -2998 kW (plus is import), +1459 kvar; volts 0.990 to 1.012; busiest transformer 412%; export 2998 kW is 1998 kW over the 1000 kW limit: the so |
| 1709 | SITE SURVEY | generic site 1582 | CONFIRMED | connection point -226 kW (plus is import), +237 kvar; volts 0.990 to 1.002; busiest transformer 70%; inside every limit |
| 1710 | SITE SURVEY | generic site 1583 | CONFIRMED | connection point -2277 kW (plus is import), +1998 kvar; volts 0.983 to 1.000; busiest transformer 726%; export 2277 kW is 2277 kW over the 0 kW limit: the solar |
| 1711 | SITE SURVEY | generic site 1584 | CONFIRMED | connection point -5104 kW (plus is import), +3736 kvar; volts 0.977 to 1.000; busiest transformer 726%; export 5104 kW is 5104 kW over the 0 kW limit: the solar |
| 1712 | SITE SURVEY | generic site 1585 | CONFIRMED | connection point -4409 kW (plus is import), +1580 kvar; volts 0.992 to 1.014; busiest transformer 283%; export 4409 kW is 4209 kW over the 200 kW limit: the sol |
| 1713 | SITE SURVEY | generic site 1586 | CONFIRMED | connection point -184 kW (plus is import), +235 kvar; volts 0.992 to 1.000; busiest transformer 30%; inside every limit |
| 1714 | SITE SURVEY | generic site 1587 | CONFIRMED | connection point -313 kW (plus is import), +99 kvar; volts 0.996 to 1.000; busiest transformer 46%; inside every limit |
| 1715 | SITE SURVEY | generic site 1588 | CONFIRMED | connection point -1316 kW (plus is import), +499 kvar; volts 0.991 to 1.012; busiest transformer 188%; export 1316 kW is 816 kW over the 500 kW limit: the solar |
| 1716 | SITE SURVEY | generic site 1589 | CONFIRMED | connection point -1920 kW (plus is import), +526 kvar; volts 0.994 to 1.008; busiest transformer 114%; export 1920 kW is 1920 kW over the 0 kW limit: the solar  |
| 1717 | SITE SURVEY | generic site 1590 | CONFIRMED | connection point -656 kW (plus is import), +198 kvar; volts 0.996 to 1.006; busiest transformer 85%; export 656 kW is 156 kW over the 500 kW limit: the solar mu |
| 1718 | SITE SURVEY | generic site 1591 | CONFIRMED | connection point -31 kW (plus is import), +616 kvar; volts 0.987 to 1.000; busiest transformer 47%; inside every limit |
| 1719 | SITE SURVEY | generic site 1592 | CONFIRMED | connection point -787 kW (plus is import), +400 kvar; volts 0.992 to 1.007; busiest transformer 157%; export 787 kW is 787 kW over the 0 kW limit: the solar mus |
| 1720 | SITE SURVEY | generic site 1593 | CONFIRMED | connection point -1973 kW (plus is import), +1219 kvar; volts 0.991 to 1.007; busiest transformer 564%; export 1973 kW is 1923 kW over the 50 kW limit: the sola |
| 1721 | SITE SURVEY | generic site 1594 | CONFIRMED | connection point -660 kW (plus is import), +509 kvar; volts 0.988 to 1.004; busiest transformer 89%; export 660 kW is 660 kW over the 0 kW limit: the solar must |
| 1722 | SITE SURVEY | generic site 1595 | CONFIRMED | connection point -1799 kW (plus is import), +958 kvar; volts 0.988 to 1.010; busiest transformer 494%; export 1799 kW is 1749 kW over the 50 kW limit: the solar |
| 1723 | SITE SURVEY | generic site 1596 | CONFIRMED | connection point -930 kW (plus is import), +177 kvar; volts 0.996 to 1.005; busiest transformer 102%; export 930 kW is 930 kW over the 0 kW limit: the solar mus |
| 1724 | SITE SURVEY | generic site 1597 | CONFIRMED | connection point -116 kW (plus is import), +1040 kvar; volts 0.983 to 1.004; busiest transformer 214%; a transformer is at 214% of its rating |
| 1725 | SITE SURVEY | generic site 1598 | CONFIRMED | connection point -1371 kW (plus is import), +1231 kvar; volts 0.985 to 1.008; busiest transformer 510%; export 1371 kW is 1171 kW over the 200 kW limit: the sol |
| 1726 | SITE SURVEY | generic site 1599 | CONFIRMED | connection point -3261 kW (plus is import), +1398 kvar; volts 0.990 to 1.016; busiest transformer 283%; export 3261 kW is 2761 kW over the 500 kW limit: the sol |
| 1727 | SITE SURVEY | generic site 1600 | CONFIRMED | connection point -485 kW (plus is import), +291 kvar; volts 0.992 to 1.000; busiest transformer 34%; export 485 kW is 485 kW over the 0 kW limit: the solar must |
| 1728 | SITE SURVEY | generic site 1601 | CONFIRMED | connection point -2308 kW (plus is import), +1139 kvar; volts 0.988 to 1.015; busiest transformer 407%; export 2308 kW is 2258 kW over the 50 kW limit: the sola |
| 1729 | SITE SURVEY | generic site 1602 | CONFIRMED | connection point -1614 kW (plus is import), +1115 kvar; volts 0.988 to 1.009; busiest transformer 510%; export 1614 kW is 1114 kW over the 500 kW limit: the sol |
| 1730 | SITE SURVEY | generic site 1603 | CONFIRMED | connection point -147 kW (plus is import), +754 kvar; volts 0.987 to 1.000; busiest transformer 62%; inside every limit |
| 1731 | SITE SURVEY | generic site 1604 | CONFIRMED | connection point -188 kW (plus is import), +197 kvar; volts 0.991 to 1.000; busiest transformer 50%; export 188 kW is 138 kW over the 50 kW limit: the solar mus |
| 1732 | SITE SURVEY | generic site 1605 | CONFIRMED | connection point -881 kW (plus is import), +370 kvar; volts 0.991 to 1.009; busiest transformer 162%; export 881 kW is 681 kW over the 200 kW limit: the solar m |
| 1733 | SITE SURVEY | generic site 1606 | CONFIRMED | connection point -455 kW (plus is import), +803 kvar; volts 0.987 to 1.000; busiest transformer 77%; export 455 kW is 405 kW over the 50 kW limit: the solar mus |
| 1734 | SITE SURVEY | generic site 1607 | CONFIRMED | connection point -2228 kW (plus is import), +523 kvar; volts 0.996 to 1.013; busiest transformer 135%; export 2228 kW is 2178 kW over the 50 kW limit: the solar |
| 1735 | SITE SURVEY | generic site 1608 | CONFIRMED | connection point -1570 kW (plus is import), +379 kvar; volts 0.997 to 1.009; busiest transformer 95%; export 1570 kW is 570 kW over the 1000 kW limit: the solar |
| 1736 | SITE SURVEY | generic site 1609 | CONFIRMED | connection point -4340 kW (plus is import), +3490 kvar; volts 0.969 to 1.000; busiest transformer 780%; export 4340 kW is 4290 kW over the 50 kW limit: the sola |
| 1737 | SITE SURVEY | generic site 1610 | CONFIRMED | connection point -435 kW (plus is import), +282 kvar; volts 0.993 to 1.002; busiest transformer 51%; inside every limit |
| 1738 | SITE SURVEY | generic site 1611 | CONFIRMED | connection point -1124 kW (plus is import), +524 kvar; volts 0.990 to 1.008; busiest transformer 170%; export 1124 kW is 624 kW over the 500 kW limit: the solar |
| 1739 | SITE SURVEY | generic site 1612 | CONFIRMED | connection point -308 kW (plus is import), +315 kvar; volts 0.992 to 1.000; busiest transformer 39%; export 308 kW is 308 kW over the 0 kW limit: the solar must |
| 1740 | SITE SURVEY | generic site 1613 | CONFIRMED | connection point -127 kW (plus is import), +265 kvar; volts 0.990 to 1.000; busiest transformer 51%; inside every limit |
| 1741 | SITE SURVEY | generic site 1614 | CONFIRMED | connection point -641 kW (plus is import), +183 kvar; volts 0.996 to 1.007; busiest transformer 105%; a transformer is at 105% of its rating |
| 1742 | SITE SURVEY | generic site 1615 | CONFIRMED | connection point -2941 kW (plus is import), +813 kvar; volts 0.990 to 1.012; busiest transformer 227%; export 2941 kW is 2441 kW over the 500 kW limit: the sola |
| 1743 | SITE SURVEY | generic site 1616 | CONFIRMED | connection point -562 kW (plus is import), +769 kvar; volts 0.989 to 1.006; busiest transformer 204%; export 562 kW is 562 kW over the 0 kW limit: the solar mus |
| 1744 | SITE SURVEY | generic site 1617 | CONFIRMED | connection point -3425 kW (plus is import), +1439 kvar; volts 0.988 to 1.014; busiest transformer 300%; export 3425 kW is 3425 kW over the 0 kW limit: the solar |
| 1745 | SITE SURVEY | generic site 1618 | REFUTED | connection point -3520 kW (plus is import), +4442 kvar; volts 0.912 to 1.000; busiest transformer 1145%; export 3520 kW is 2520 kW over the 1000 kW limit: the s |
| 1746 | SITE SURVEY | generic site 1619 | CONFIRMED | connection point -1656 kW (plus is import), +528 kvar; volts 0.992 to 1.016; busiest transformer 263%; export 1656 kW is 1156 kW over the 500 kW limit: the sola |
| 1747 | SITE SURVEY | generic site 1620 | CONFIRMED | connection point -864 kW (plus is import), +168 kvar; volts 0.998 to 1.007; busiest transformer 95%; export 864 kW is 864 kW over the 0 kW limit: the solar must |
| 1748 | SITE SURVEY | generic site 1621 | CONFIRMED | connection point -2278 kW (plus is import), +744 kvar; volts 0.996 to 1.019; busiest transformer 283%; export 2278 kW is 1778 kW over the 500 kW limit: the sola |
| 1749 | SITE SURVEY | generic site 1622 | CONFIRMED | connection point -984 kW (plus is import), +1124 kvar; volts 0.985 to 1.008; busiest transformer 443%; export 984 kW is 484 kW over the 500 kW limit: the solar  |
| 1750 | SITE SURVEY | generic site 1623 | CONFIRMED | connection point -1287 kW (plus is import), +757 kvar; volts 0.987 to 1.010; busiest transformer 264%; export 1287 kW is 787 kW over the 500 kW limit: the solar |
| 1751 | SITE SURVEY | generic site 1624 | CONFIRMED | connection point -1036 kW (plus is import), +315 kvar; volts 0.991 to 1.003; busiest transformer 67%; export 1036 kW is 836 kW over the 200 kW limit: the solar  |
| 1752 | SITE SURVEY | generic site 1625 | CONFIRMED | connection point -2771 kW (plus is import), +1301 kvar; volts 0.985 to 1.008; busiest transformer 454%; export 2771 kW is 2771 kW over the 0 kW limit: the solar |
| 1753 | SITE SURVEY | generic site 1626 | CONFIRMED | connection point -915 kW (plus is import), +417 kvar; volts 0.992 to 1.000; busiest transformer 63%; export 915 kW is 715 kW over the 200 kW limit: the solar mu |
| 1754 | SITE SURVEY | generic site 1627 | CONFIRMED | connection point -1093 kW (plus is import), +473 kvar; volts 0.991 to 1.005; busiest transformer 86%; export 1093 kW is 593 kW over the 500 kW limit: the solar  |
| 1755 | SITE SURVEY | generic site 1628 | CONFIRMED | connection point -116 kW (plus is import), +328 kvar; volts 0.992 to 1.000; busiest transformer 21%; inside every limit |
| 1756 | SITE SURVEY | generic site 1629 | CONFIRMED | connection point -2179 kW (plus is import), +1138 kvar; volts 0.990 to 1.017; busiest transformer 333%; export 2179 kW is 2179 kW over the 0 kW limit: the solar |
| 1757 | SITE SURVEY | generic site 1630 | CONFIRMED | connection point -1197 kW (plus is import), +290 kvar; volts 0.994 to 1.008; busiest transformer 140%; export 1197 kW is 197 kW over the 1000 kW limit: the sola |
| 1758 | SITE SURVEY | generic site 1631 | CONFIRMED | connection point -621 kW (plus is import), +150 kvar; volts 0.994 to 1.005; busiest transformer 77%; export 621 kW is 421 kW over the 200 kW limit: the solar mu |
| 1759 | SITE SURVEY | generic site 1632 | CONFIRMED | connection point -2164 kW (plus is import), +581 kvar; volts 0.995 to 1.010; busiest transformer 161%; export 2164 kW is 2114 kW over the 50 kW limit: the solar |
| 1760 | SITE SURVEY | generic site 1633 | CONFIRMED | connection point -4779 kW (plus is import), +1963 kvar; volts 0.985 to 1.014; busiest transformer 386%; export 4779 kW is 4579 kW over the 200 kW limit: the sol |
| 1761 | SITE SURVEY | generic site 1634 | CONFIRMED | connection point +415 kW (plus is import), +696 kvar; volts 0.986 to 1.000; busiest transformer 75%; inside every limit |
| 1762 | SITE SURVEY | generic site 1635 | CONFIRMED | connection point +483 kW (plus is import), +1002 kvar; volts 0.981 to 1.000; busiest transformer 60%; inside every limit |
| 1763 | SITE SURVEY | generic site 1636 | CONFIRMED | connection point -89 kW (plus is import), +253 kvar; volts 0.990 to 1.000; busiest transformer 28%; inside every limit |
| 1764 | SITE SURVEY | generic site 1637 | CONFIRMED | connection point -110 kW (plus is import), +1178 kvar; volts 0.982 to 1.006; busiest transformer 354%; a transformer is at 354% of its rating |
| 1765 | SITE SURVEY | generic site 1638 | CONFIRMED | connection point -4617 kW (plus is import), +4113 kvar; volts 0.947 to 1.000; busiest transformer 839%; export 4617 kW is 4417 kW over the 200 kW limit: the sol |
| 1766 | SITE SURVEY | generic site 1639 | CONFIRMED | connection point -148 kW (plus is import), +91 kvar; volts 0.995 to 1.000; busiest transformer 22%; export 148 kW is 148 kW over the 0 kW limit: the solar must  |
| 1767 | SITE SURVEY | generic site 1640 | CONFIRMED | connection point -1852 kW (plus is import), +1432 kvar; volts 0.986 to 1.012; busiest transformer 415%; export 1852 kW is 1652 kW over the 200 kW limit: the sol |
| 1768 | SITE SURVEY | generic site 1641 | CONFIRMED | connection point -744 kW (plus is import), +1269 kvar; volts 0.985 to 1.006; busiest transformer 171%; export 744 kW is 544 kW over the 200 kW limit: the solar  |
| 1769 | SITE SURVEY | generic site 1642 | CONFIRMED | connection point -2547 kW (plus is import), +918 kvar; volts 0.990 to 1.012; busiest transformer 218%; export 2547 kW is 2497 kW over the 50 kW limit: the solar |
| 1770 | SITE SURVEY | generic site 1643 | CONFIRMED | connection point -2423 kW (plus is import), +2954 kvar; volts 0.950 to 1.000; busiest transformer 857%; export 2423 kW is 1423 kW over the 1000 kW limit: the so |
| 1771 | SITE SURVEY | generic site 1644 | CONFIRMED | connection point -1873 kW (plus is import), +434 kvar; volts 0.991 to 1.009; busiest transformer 115%; export 1873 kW is 1873 kW over the 0 kW limit: the solar  |
| 1772 | SITE SURVEY | generic site 1645 | CONFIRMED | connection point -488 kW (plus is import), +616 kvar; volts 0.989 to 1.000; busiest transformer 84%; export 488 kW is 488 kW over the 0 kW limit: the solar must |
| 1773 | SITE SURVEY | generic site 1646 | CONFIRMED | connection point -3 kW (plus is import), +450 kvar; volts 0.989 to 1.003; busiest transformer 93%; inside every limit |
| 1774 | SITE SURVEY | generic site 1647 | CONFIRMED | connection point -98 kW (plus is import), +452 kvar; volts 0.989 to 1.000; busiest transformer 38%; export 98 kW is 98 kW over the 0 kW limit: the solar must be |
| 1775 | SITE SURVEY | generic site 1648 | CONFIRMED | connection point -747 kW (plus is import), +245 kvar; volts 0.993 to 1.013; busiest transformer 201%; a transformer is at 201% of its rating |
| 1776 | SITE SURVEY | generic site 1649 | CONFIRMED | connection point -3641 kW (plus is import), +1294 kvar; volts 0.988 to 1.014; busiest transformer 241%; export 3641 kW is 3441 kW over the 200 kW limit: the sol |
| 1777 | SITE SURVEY | generic site 1650 | CONFIRMED | connection point -1724 kW (plus is import), +1194 kvar; volts 0.986 to 1.005; busiest transformer 530%; export 1724 kW is 1524 kW over the 200 kW limit: the sol |
| 1778 | SITE SURVEY | generic site 1651 | CONFIRMED | connection point -333 kW (plus is import), +176 kvar; volts 0.991 to 1.002; busiest transformer 56%; export 333 kW is 283 kW over the 50 kW limit: the solar mus |
| 1779 | SITE SURVEY | generic site 1652 | CONFIRMED | connection point -2553 kW (plus is import), +804 kvar; volts 0.991 to 1.011; busiest transformer 207%; export 2553 kW is 2503 kW over the 50 kW limit: the solar |
| 1780 | SITE SURVEY | generic site 1653 | CONFIRMED | connection point -854 kW (plus is import), +728 kvar; volts 0.988 to 1.010; busiest transformer 190%; export 854 kW is 654 kW over the 200 kW limit: the solar m |
| 1781 | SITE SURVEY | generic site 1654 | CONFIRMED | connection point -883 kW (plus is import), +303 kvar; volts 0.990 to 1.002; busiest transformer 59%; inside every limit |
| 1782 | SITE SURVEY | generic site 1655 | CONFIRMED | connection point -1709 kW (plus is import), +1026 kvar; volts 0.989 to 1.011; busiest transformer 503%; export 1709 kW is 1209 kW over the 500 kW limit: the sol |
| 1783 | SITE SURVEY | generic site 1656 | CONFIRMED | connection point -961 kW (plus is import), +1170 kvar; volts 0.985 to 1.005; busiest transformer 166%; export 961 kW is 461 kW over the 500 kW limit: the solar  |
| 1784 | SITE SURVEY | generic site 1657 | CONFIRMED | connection point +480 kW (plus is import), +793 kvar; volts 0.986 to 1.000; busiest transformer 39%; inside every limit |
| 1785 | SITE SURVEY | generic site 1658 | CONFIRMED | connection point -1834 kW (plus is import), +1066 kvar; volts 0.989 to 1.012; busiest transformer 200%; export 1834 kW is 1334 kW over the 500 kW limit: the sol |
| 1786 | SITE SURVEY | generic site 1659 | CONFIRMED | connection point -372 kW (plus is import), +410 kvar; volts 0.990 to 1.012; busiest transformer 196%; export 372 kW is 172 kW over the 200 kW limit: the solar m |
| 1787 | SITE SURVEY | generic site 1660 | CONFIRMED | connection point -2035 kW (plus is import), +2501 kvar; volts 0.972 to 1.000; busiest transformer 779%; export 2035 kW is 2035 kW over the 0 kW limit: the solar |
| 1788 | SITE SURVEY | generic site 1661 | CONFIRMED | connection point +198 kW (plus is import), +578 kvar; volts 0.986 to 1.002; busiest transformer 150%; a transformer is at 150% of its rating |
| 1789 | SITE SURVEY | generic site 1662 | CONFIRMED | connection point -708 kW (plus is import), +665 kvar; volts 0.988 to 1.002; busiest transformer 101%; a transformer is at 101% of its rating |
| 1790 | SITE SURVEY | generic site 1663 | CONFIRMED | connection point -5013 kW (plus is import), +3359 kvar; volts 0.975 to 1.000; busiest transformer 685%; export 5013 kW is 5013 kW over the 0 kW limit: the solar |
| 1791 | SITE SURVEY | generic site 1664 | CONFIRMED | connection point -3277 kW (plus is import), +2230 kvar; volts 0.984 to 1.000; busiest transformer 602%; export 3277 kW is 2777 kW over the 500 kW limit: the sol |
| 1792 | SITE SURVEY | generic site 1665 | CONFIRMED | connection point -925 kW (plus is import), +627 kvar; volts 0.991 to 1.004; busiest transformer 94%; export 925 kW is 725 kW over the 200 kW limit: the solar mu |
| 1793 | SITE SURVEY | generic site 1666 | CONFIRMED | connection point -4076 kW (plus is import), +1873 kvar; volts 0.986 to 1.014; busiest transformer 354%; export 4076 kW is 3076 kW over the 1000 kW limit: the so |
| 1794 | SITE SURVEY | generic site 1667 | CONFIRMED | connection point -732 kW (plus is import), +1046 kvar; volts 0.985 to 1.008; busiest transformer 221%; export 732 kW is 682 kW over the 50 kW limit: the solar m |
| 1795 | SITE SURVEY | generic site 1668 | CONFIRMED | connection point +20 kW (plus is import), +866 kvar; volts 0.984 to 1.007; busiest transformer 260%; a transformer is at 260% of its rating |
| 1796 | SITE SURVEY | generic site 1669 | CONFIRMED | connection point -413 kW (plus is import), +599 kvar; volts 0.988 to 1.000; busiest transformer 77%; export 413 kW is 413 kW over the 0 kW limit: the solar must |
| 1797 | SITE SURVEY | generic site 1670 | CONFIRMED | connection point -2523 kW (plus is import), +1269 kvar; volts 0.989 to 1.013; busiest transformer 242%; export 2523 kW is 2323 kW over the 200 kW limit: the sol |
| 1798 | SITE SURVEY | generic site 1671 | CONFIRMED | connection point +116 kW (plus is import), +432 kvar; volts 0.987 to 1.000; busiest transformer 56%; inside every limit |
| 1799 | SITE SURVEY | generic site 1672 | CONFIRMED | connection point -2160 kW (plus is import), +998 kvar; volts 0.995 to 1.015; busiest transformer 370%; export 2160 kW is 1160 kW over the 1000 kW limit: the sol |
| 1800 | SITE SURVEY | generic site 1673 | CONFIRMED | connection point -21 kW (plus is import), +427 kvar; volts 0.988 to 1.000; busiest transformer 85%; inside every limit |
| 1801 | SITE SURVEY | generic site 1674 | CONFIRMED | connection point -1949 kW (plus is import), +1007 kvar; volts 0.987 to 1.007; busiest transformer 162%; export 1949 kW is 1749 kW over the 200 kW limit: the sol |
| 1802 | SITE SURVEY | generic site 1675 | CONFIRMED | connection point -1440 kW (plus is import), +462 kvar; volts 0.991 to 1.006; busiest transformer 96%; export 1440 kW is 440 kW over the 1000 kW limit: the solar |
| 1803 | SITE SURVEY | generic site 1676 | CONFIRMED | connection point -519 kW (plus is import), +192 kvar; volts 0.992 to 1.010; busiest transformer 149%; a transformer is at 149% of its rating |
| 1804 | SITE SURVEY | generic site 1677 | CONFIRMED | connection point +55 kW (plus is import), +1149 kvar; volts 0.982 to 1.005; busiest transformer 223%; a transformer is at 223% of its rating |
| 1805 | SITE SURVEY | generic site 1678 | CONFIRMED | connection point -1170 kW (plus is import), +521 kvar; volts 0.990 to 1.004; busiest transformer 90%; export 1170 kW is 970 kW over the 200 kW limit: the solar  |
| 1806 | SITE SURVEY | generic site 1679 | CONFIRMED | connection point -623 kW (plus is import), +128 kvar; volts 0.996 to 1.006; busiest transformer 91%; export 623 kW is 123 kW over the 500 kW limit: the solar mu |
| 1807 | SITE SURVEY | generic site 1680 | CONFIRMED | connection point -164 kW (plus is import), +323 kvar; volts 0.989 to 1.000; busiest transformer 57%; inside every limit |
| 1808 | SITE SURVEY | generic site 1681 | CONFIRMED | connection point -2713 kW (plus is import), +2022 kvar; volts 0.978 to 1.000; busiest transformer 755%; export 2713 kW is 2713 kW over the 0 kW limit: the solar |
| 1809 | SITE SURVEY | generic site 1682 | CONFIRMED | connection point -511 kW (plus is import), +526 kvar; volts 0.988 to 1.002; busiest transformer 64%; export 511 kW is 11 kW over the 500 kW limit: the solar mus |
| 1810 | SITE SURVEY | generic site 1683 | CONFIRMED | connection point -4130 kW (plus is import), +3135 kvar; volts 0.977 to 1.000; busiest transformer 737%; export 4130 kW is 3630 kW over the 500 kW limit: the sol |
| 1811 | SITE SURVEY | generic site 1684 | CONFIRMED | connection point -549 kW (plus is import), +754 kvar; volts 0.987 to 1.002; busiest transformer 88%; export 549 kW is 499 kW over the 50 kW limit: the solar mus |
| 1812 | SITE SURVEY | generic site 1685 | CONFIRMED | connection point -529 kW (plus is import), +700 kvar; volts 0.987 to 1.007; busiest transformer 189%; export 529 kW is 329 kW over the 200 kW limit: the solar m |
| 1813 | SITE SURVEY | generic site 1686 | CONFIRMED | connection point +2 kW (plus is import), +243 kvar; volts 0.990 to 1.000; busiest transformer 25%; inside every limit |
| 1814 | SITE SURVEY | generic site 1687 | CONFIRMED | connection point -1340 kW (plus is import), +860 kvar; volts 0.987 to 1.010; busiest transformer 237%; export 1340 kW is 1340 kW over the 0 kW limit: the solar  |
| 1815 | SITE SURVEY | generic site 1688 | CONFIRMED | connection point -4681 kW (plus is import), +3472 kvar; volts 0.974 to 1.000; busiest transformer 686%; export 4681 kW is 3681 kW over the 1000 kW limit: the so |
| 1816 | SITE SURVEY | generic site 1689 | CONFIRMED | connection point -4480 kW (plus is import), +1995 kvar; volts 0.982 to 1.010; busiest transformer 317%; export 4480 kW is 3480 kW over the 1000 kW limit: the so |
| 1817 | SITE SURVEY | generic site 1690 | CONFIRMED | connection point -207 kW (plus is import), +233 kvar; volts 0.993 to 1.003; busiest transformer 103%; a transformer is at 103% of its rating |
| 1818 | SITE SURVEY | generic site 1691 | CONFIRMED | connection point -775 kW (plus is import), +476 kvar; volts 0.993 to 1.010; busiest transformer 173%; export 775 kW is 775 kW over the 0 kW limit: the solar mus |
| 1819 | SITE SURVEY | generic site 1692 | REFUTED | connection point -4864 kW (plus is import), -5166 kvar; volts 1.000 to 1.877; busiest transformer 3153%; export 4864 kW is 4814 kW over the 50 kW limit: the sol |
| 1820 | SITE SURVEY | generic site 1693 | REFUTED | connection point -2706 kW (plus is import), +13810 kvar; volts 0.882 to 1.047; busiest transformer 3197%; export 2706 kW is 2706 kW over the 0 kW limit: the sol |
| 1821 | SITE SURVEY | generic site 1694 | CONFIRMED | connection point -684 kW (plus is import), +768 kvar; volts 0.987 to 1.011; busiest transformer 224%; a transformer is at 224% of its rating |
| 1822 | SITE SURVEY | generic site 1695 | CONFIRMED | connection point -1137 kW (plus is import), +211 kvar; volts 0.998 to 1.004; busiest transformer 60%; export 1137 kW is 937 kW over the 200 kW limit: the solar  |
| 1823 | SITE SURVEY | generic site 1696 | CONFIRMED | connection point -1857 kW (plus is import), +664 kvar; volts 0.988 to 1.013; busiest transformer 300%; export 1857 kW is 1857 kW over the 0 kW limit: the solar  |
| 1824 | SITE SURVEY | generic site 1697 | CONFIRMED | connection point -1240 kW (plus is import), +868 kvar; volts 0.987 to 1.010; busiest transformer 233%; export 1240 kW is 740 kW over the 500 kW limit: the solar |
| 1825 | SITE SURVEY | generic site 1698 | CONFIRMED | connection point -1243 kW (plus is import), +481 kvar; volts 0.991 to 1.006; busiest transformer 91%; export 1243 kW is 743 kW over the 500 kW limit: the solar  |
| 1826 | SITE SURVEY | generic site 1699 | CONFIRMED | connection point +561 kW (plus is import), +902 kvar; volts 0.983 to 1.000; busiest transformer 40%; inside every limit |
| 1827 | SITE SURVEY | generic site 1700 | CONFIRMED | connection point -1282 kW (plus is import), +1187 kvar; volts 0.984 to 1.009; busiest transformer 492%; export 1282 kW is 1232 kW over the 50 kW limit: the sola |
| 1828 | SITE SURVEY | generic site 1701 | CONFIRMED | connection point -2419 kW (plus is import), +1389 kvar; volts 0.987 to 1.013; busiest transformer 450%; export 2419 kW is 2369 kW over the 50 kW limit: the sola |
| 1829 | SITE SURVEY | generic site 1702 | CONFIRMED | connection point -3113 kW (plus is import), +2985 kvar; volts 0.938 to 1.000; busiest transformer 904%; export 3113 kW is 3113 kW over the 0 kW limit: the solar |
| 1830 | SITE SURVEY | generic site 1703 | CONFIRMED | connection point -1242 kW (plus is import), +709 kvar; volts 0.988 to 1.009; busiest transformer 254%; export 1242 kW is 742 kW over the 500 kW limit: the solar |
| 1831 | SITE SURVEY | generic site 1704 | CONFIRMED | connection point -3143 kW (plus is import), +2094 kvar; volts 0.980 to 1.000; busiest transformer 573%; export 3143 kW is 2643 kW over the 500 kW limit: the sol |
| 1832 | SITE SURVEY | generic site 1705 | CONFIRMED | connection point +20 kW (plus is import), +913 kvar; volts 0.984 to 1.000; busiest transformer 77%; inside every limit |
| 1833 | SITE SURVEY | generic site 1706 | CONFIRMED | connection point -1793 kW (plus is import), +843 kvar; volts 0.991 to 1.008; busiest transformer 141%; export 1793 kW is 1593 kW over the 200 kW limit: the sola |
| 1834 | SITE SURVEY | generic site 1707 | CONFIRMED | connection point -1545 kW (plus is import), +332 kvar; volts 0.992 to 1.007; busiest transformer 94%; export 1545 kW is 1495 kW over the 50 kW limit: the solar  |
| 1835 | SITE SURVEY | generic site 1708 | CONFIRMED | connection point -343 kW (plus is import), +276 kvar; volts 0.990 to 1.008; busiest transformer 145%; export 343 kW is 343 kW over the 0 kW limit: the solar mus |
| 1836 | SITE SURVEY | generic site 1709 | CONFIRMED | connection point -554 kW (plus is import), +1318 kvar; volts 0.983 to 1.008; busiest transformer 444%; export 554 kW is 54 kW over the 500 kW limit: the solar m |
| 1837 | SITE SURVEY | generic site 1710 | CONFIRMED | connection point -5466 kW (plus is import), +4648 kvar; volts 0.960 to 1.000; busiest transformer 794%; export 5466 kW is 5466 kW over the 0 kW limit: the solar |
| 1838 | SITE SURVEY | generic site 1711 | CONFIRMED | connection point -6011 kW (plus is import), +2703 kvar; volts 0.985 to 1.018; busiest transformer 406%; export 6011 kW is 5961 kW over the 50 kW limit: the sola |
| 1839 | SITE SURVEY | generic site 1712 | CONFIRMED | connection point -1893 kW (plus is import), +1141 kvar; volts 0.985 to 1.005; busiest transformer 166%; export 1893 kW is 1393 kW over the 500 kW limit: the sol |
| 1840 | SITE SURVEY | generic site 1713 | CONFIRMED | connection point +419 kW (plus is import), +825 kvar; volts 0.984 to 1.000; busiest transformer 123%; a transformer is at 123% of its rating |
| 1841 | SITE SURVEY | generic site 1714 | CONFIRMED | connection point -153 kW (plus is import), +398 kvar; volts 0.990 to 1.009; busiest transformer 157%; export 153 kW is 153 kW over the 0 kW limit: the solar mus |
| 1842 | SITE SURVEY | generic site 1715 | CONFIRMED | connection point -388 kW (plus is import), +552 kvar; volts 0.989 to 1.000; busiest transformer 53%; inside every limit |
| 1843 | SITE SURVEY | generic site 1716 | CONFIRMED | connection point -72 kW (plus is import), +54 kvar; volts 0.996 to 1.000; busiest transformer 26%; export 72 kW is 72 kW over the 0 kW limit: the solar must be  |
| 1844 | SITE SURVEY | generic site 1717 | REFUTED | connection point -3862 kW (plus is import), +7794 kvar; volts 0.806 to 1.000; busiest transformer 1499%; export 3862 kW is 2862 kW over the 1000 kW limit: the s |
| 1845 | SITE SURVEY | generic site 1718 | CONFIRMED | connection point -1802 kW (plus is import), +903 kvar; volts 0.989 to 1.011; busiest transformer 272%; export 1802 kW is 1602 kW over the 200 kW limit: the sola |
| 1846 | SITE SURVEY | generic site 1719 | CONFIRMED | connection point -1635 kW (plus is import), +729 kvar; volts 0.990 to 1.009; busiest transformer 131%; export 1635 kW is 1135 kW over the 500 kW limit: the sola |
| 1847 | SITE SURVEY | generic site 1720 | CONFIRMED | connection point -2110 kW (plus is import), +1300 kvar; volts 0.987 to 1.000; busiest transformer 587%; export 2110 kW is 2110 kW over the 0 kW limit: the solar |
| 1848 | SITE SURVEY | generic site 1721 | CONFIRMED | connection point -3623 kW (plus is import), +3617 kvar; volts 0.969 to 1.000; busiest transformer 756%; export 3623 kW is 3423 kW over the 200 kW limit: the sol |
| 1849 | SITE SURVEY | generic site 1722 | CONFIRMED | connection point -405 kW (plus is import), +917 kvar; volts 0.986 to 1.000; busiest transformer 91%; inside every limit |
| 1850 | SITE SURVEY | generic site 1723 | CONFIRMED | connection point -1079 kW (plus is import), +307 kvar; volts 0.994 to 1.012; busiest transformer 171%; export 1079 kW is 579 kW over the 500 kW limit: the solar |
| 1851 | SITE SURVEY | generic site 1724 | CONFIRMED | connection point -586 kW (plus is import), +182 kvar; volts 0.996 to 1.000; busiest transformer 43%; export 586 kW is 586 kW over the 0 kW limit: the solar must |
| 1852 | SITE SURVEY | generic site 1725 | CONFIRMED | connection point -84 kW (plus is import), +190 kvar; volts 0.990 to 1.003; busiest transformer 77%; export 84 kW is 34 kW over the 50 kW limit: the solar must b |
| 1853 | SITE SURVEY | generic site 1726 | CONFIRMED | connection point -1387 kW (plus is import), +408 kvar; volts 0.993 to 1.007; busiest transformer 113%; export 1387 kW is 887 kW over the 500 kW limit: the solar |
| 1854 | SITE SURVEY | generic site 1727 | CONFIRMED | connection point -3924 kW (plus is import), +1187 kvar; volts 0.991 to 1.016; busiest transformer 245%; export 3924 kW is 3424 kW over the 500 kW limit: the sol |
| 1855 | SITE SURVEY | generic site 1728 | CONFIRMED | connection point -2536 kW (plus is import), +1755 kvar; volts 0.981 to 1.000; busiest transformer 699%; export 2536 kW is 1536 kW over the 1000 kW limit: the so |
| 1856 | SITE SURVEY | generic site 1729 | CONFIRMED | connection point -3884 kW (plus is import), +1326 kvar; volts 0.986 to 1.012; busiest transformer 304%; export 3884 kW is 3884 kW over the 0 kW limit: the solar |
| 1857 | SITE SURVEY | generic site 1730 | CONFIRMED | connection point -347 kW (plus is import), +308 kvar; volts 0.994 to 1.000; busiest transformer 42%; export 347 kW is 347 kW over the 0 kW limit: the solar must |
| 1858 | SITE SURVEY | generic site 1731 | CONFIRMED | connection point -2357 kW (plus is import), +1017 kvar; volts 0.992 to 1.016; busiest transformer 393%; export 2357 kW is 1857 kW over the 500 kW limit: the sol |
| 1859 | SITE SURVEY | generic site 1732 | CONFIRMED | connection point -469 kW (plus is import), +396 kvar; volts 0.992 to 1.009; busiest transformer 200%; a transformer is at 200% of its rating |
| 1860 | SITE SURVEY | generic site 1733 | CONFIRMED | connection point -72 kW (plus is import), +266 kvar; volts 0.990 to 1.002; busiest transformer 63%; inside every limit |
| 1861 | SITE SURVEY | generic site 1734 | CONFIRMED | connection point +61 kW (plus is import), +319 kvar; volts 0.992 to 1.000; busiest transformer 14%; inside every limit |
| 1862 | SITE SURVEY | generic site 1735 | CONFIRMED | connection point -4006 kW (plus is import), +1542 kvar; volts 0.992 to 1.020; busiest transformer 273%; export 4006 kW is 3956 kW over the 50 kW limit: the sola |
| 1863 | SITE SURVEY | generic site 1736 | CONFIRMED | connection point -1099 kW (plus is import), +182 kvar; volts 0.998 to 1.006; busiest transformer 61%; export 1099 kW is 1049 kW over the 50 kW limit: the solar  |
| 1864 | SITE SURVEY | generic site 1737 | CONFIRMED | connection point -222 kW (plus is import), +197 kvar; volts 0.991 to 1.001; busiest transformer 48%; export 222 kW is 172 kW over the 50 kW limit: the solar mus |
| 1865 | SITE SURVEY | generic site 1738 | CONFIRMED | connection point -1804 kW (plus is import), +1398 kvar; volts 0.986 to 1.003; busiest transformer 582%; export 1804 kW is 804 kW over the 1000 kW limit: the sol |
| 1866 | SITE SURVEY | generic site 1739 | CONFIRMED | connection point -1457 kW (plus is import), +415 kvar; volts 0.992 to 1.011; busiest transformer 183%; export 1457 kW is 1257 kW over the 200 kW limit: the sola |
| 1867 | SITE SURVEY | generic site 1740 | CONFIRMED | connection point -4306 kW (plus is import), +3396 kvar; volts 0.978 to 1.000; busiest transformer 773%; export 4306 kW is 3306 kW over the 1000 kW limit: the so |
| 1868 | SITE SURVEY | generic site 1741 | CONFIRMED | connection point -1968 kW (plus is import), +1149 kvar; volts 0.986 to 1.010; busiest transformer 377%; export 1968 kW is 1968 kW over the 0 kW limit: the solar |
| 1869 | SITE SURVEY | generic site 1742 | CONFIRMED | connection point +128 kW (plus is import), +226 kvar; volts 0.990 to 1.000; busiest transformer 44%; inside every limit |
| 1870 | SITE SURVEY | generic site 1743 | CONFIRMED | connection point -2011 kW (plus is import), +1535 kvar; volts 0.985 to 1.007; busiest transformer 434%; export 2011 kW is 1811 kW over the 200 kW limit: the sol |
| 1871 | SITE SURVEY | generic site 1744 | CONFIRMED | connection point -3703 kW (plus is import), +1064 kvar; volts 0.995 to 1.017; busiest transformer 226%; export 3703 kW is 3203 kW over the 500 kW limit: the sol |
| 1872 | SITE SURVEY | generic site 1745 | CONFIRMED | connection point -91 kW (plus is import), +604 kvar; volts 0.988 to 1.000; busiest transformer 60%; export 91 kW is 91 kW over the 0 kW limit: the solar must be |
| 1873 | SITE SURVEY | generic site 1746 | CONFIRMED | connection point -908 kW (plus is import), +308 kvar; volts 0.992 to 1.010; busiest transformer 154%; a transformer is at 154% of its rating |
| 1874 | SITE SURVEY | generic site 1747 | CONFIRMED | connection point -591 kW (plus is import), +344 kvar; volts 0.992 to 1.010; busiest transformer 135%; export 591 kW is 591 kW over the 0 kW limit: the solar mus |
| 1875 | SITE SURVEY | generic site 1748 | CONFIRMED | connection point -1403 kW (plus is import), +918 kvar; volts 0.987 to 1.005; busiest transformer 163%; export 1403 kW is 903 kW over the 500 kW limit: the solar |
| 1876 | SITE SURVEY | generic site 1749 | CONFIRMED | connection point -500 kW (plus is import), +697 kvar; volts 0.987 to 1.009; busiest transformer 194%; export 500 kW is 500 kW over the 0 kW limit: the solar mus |
| 1877 | SITE SURVEY | generic site 1750 | CONFIRMED | connection point -1608 kW (plus is import), +430 kvar; volts 0.996 to 1.008; busiest transformer 103%; export 1608 kW is 1408 kW over the 200 kW limit: the sola |
| 1878 | SITE SURVEY | generic site 1751 | CONFIRMED | connection point -1093 kW (plus is import), +272 kvar; volts 0.991 to 1.011; busiest transformer 166%; export 1093 kW is 593 kW over the 500 kW limit: the solar |
| 1879 | SITE SURVEY | generic site 1752 | CONFIRMED | connection point -362 kW (plus is import), +239 kvar; volts 0.990 to 1.000; busiest transformer 78%; export 362 kW is 312 kW over the 50 kW limit: the solar mus |
| 1880 | SITE SURVEY | generic site 1753 | CONFIRMED | connection point -443 kW (plus is import), +192 kvar; volts 0.995 to 1.003; busiest transformer 68%; export 443 kW is 393 kW over the 50 kW limit: the solar mus |
| 1881 | SITE SURVEY | generic site 1754 | CONFIRMED | connection point -2250 kW (plus is import), +821 kvar; volts 0.991 to 1.013; busiest transformer 351%; export 2250 kW is 2250 kW over the 0 kW limit: the solar  |
| 1882 | SITE SURVEY | generic site 1755 | CONFIRMED | connection point -3941 kW (plus is import), +1355 kvar; volts 0.989 to 1.017; busiest transformer 312%; export 3941 kW is 3891 kW over the 50 kW limit: the sola |
| 1883 | SITE SURVEY | generic site 1756 | CONFIRMED | connection point -3030 kW (plus is import), +1671 kvar; volts 0.984 to 1.011; busiest transformer 439%; export 3030 kW is 2830 kW over the 200 kW limit: the sol |
| 1884 | SITE SURVEY | generic site 1757 | CONFIRMED | connection point -3909 kW (plus is import), +1460 kvar; volts 0.991 to 1.021; busiest transformer 322%; export 3909 kW is 3709 kW over the 200 kW limit: the sol |
| 1885 | SITE SURVEY | generic site 1758 | CONFIRMED | connection point -1263 kW (plus is import), +580 kvar; volts 0.994 to 1.010; busiest transformer 188%; export 1263 kW is 763 kW over the 500 kW limit: the solar |
| 1886 | SITE SURVEY | generic site 1759 | CONFIRMED | connection point -3350 kW (plus is import), +1232 kvar; volts 0.990 to 1.011; busiest transformer 228%; export 3350 kW is 3150 kW over the 200 kW limit: the sol |
| 1887 | SITE SURVEY | generic site 1760 | CONFIRMED | connection point -1012 kW (plus is import), +888 kvar; volts 0.986 to 1.011; busiest transformer 266%; export 1012 kW is 812 kW over the 200 kW limit: the solar |
| 1888 | SITE SURVEY | generic site 1761 | CONFIRMED | connection point -303 kW (plus is import), +233 kvar; volts 0.992 to 1.000; busiest transformer 29%; export 303 kW is 253 kW over the 50 kW limit: the solar mus |
| 1889 | SITE SURVEY | generic site 1762 | CONFIRMED | connection point -1169 kW (plus is import), +803 kvar; volts 0.989 to 1.011; busiest transformer 391%; export 1169 kW is 669 kW over the 500 kW limit: the solar |
| 1890 | SITE SURVEY | generic site 1763 | CONFIRMED | connection point -3768 kW (plus is import), +1758 kvar; volts 0.986 to 1.012; busiest transformer 334%; export 3768 kW is 3718 kW over the 50 kW limit: the sola |
| 1891 | SITE SURVEY | generic site 1764 | CONFIRMED | connection point -865 kW (plus is import), +235 kvar; volts 0.994 to 1.008; busiest transformer 131%; export 865 kW is 365 kW over the 500 kW limit: the solar m |
| 1892 | SITE SURVEY | generic site 1765 | CONFIRMED | connection point -1417 kW (plus is import), +637 kvar; volts 0.988 to 1.014; busiest transformer 262%; export 1417 kW is 917 kW over the 500 kW limit: the solar |
| 1893 | SITE SURVEY | generic site 1766 | CONFIRMED | connection point -305 kW (plus is import), +225 kvar; volts 0.993 to 1.000; busiest transformer 28%; inside every limit |
| 1894 | SITE SURVEY | generic site 1767 | CONFIRMED | connection point -2918 kW (plus is import), +1061 kvar; volts 0.993 to 1.013; busiest transformer 195%; export 2918 kW is 2918 kW over the 0 kW limit: the solar |
| 1895 | SITE SURVEY | generic site 1768 | CONFIRMED | connection point -2356 kW (plus is import), +1102 kvar; volts 0.988 to 1.011; busiest transformer 224%; export 2356 kW is 1856 kW over the 500 kW limit: the sol |
| 1896 | SITE SURVEY | generic site 1769 | CONFIRMED | connection point -1257 kW (plus is import), +344 kvar; volts 0.993 to 1.007; busiest transformer 97%; export 1257 kW is 1057 kW over the 200 kW limit: the solar |
| 1897 | SITE SURVEY | generic site 1770 | CONFIRMED | connection point -1872 kW (plus is import), +850 kvar; volts 0.988 to 1.013; busiest transformer 273%; export 1872 kW is 1672 kW over the 200 kW limit: the sola |
| 1898 | SITE SURVEY | generic site 1771 | CONFIRMED | connection point -783 kW (plus is import), +251 kvar; volts 0.994 to 1.013; busiest transformer 205%; export 783 kW is 583 kW over the 200 kW limit: the solar m |
| 1899 | SITE SURVEY | generic site 1772 | CONFIRMED | connection point -134 kW (plus is import), +268 kvar; volts 0.991 to 1.000; busiest transformer 27%; inside every limit |
| 1900 | SITE SURVEY | generic site 1773 | CONFIRMED | connection point -2492 kW (plus is import), +1415 kvar; volts 0.988 to 1.010; busiest transformer 453%; export 2492 kW is 1492 kW over the 1000 kW limit: the so |
| 1901 | SITE SURVEY | generic site 1774 | CONFIRMED | connection point -5173 kW (plus is import), +1926 kvar; volts 0.990 to 1.024; busiest transformer 335%; export 5173 kW is 4173 kW over the 1000 kW limit: the so |
| 1902 | SITE SURVEY | generic site 1775 | CONFIRMED | connection point -1704 kW (plus is import), +1021 kvar; volts 0.991 to 1.014; busiest transformer 504%; export 1704 kW is 1704 kW over the 0 kW limit: the solar |
| 1903 | SITE SURVEY | generic site 1776 | CONFIRMED | connection point -1952 kW (plus is import), +901 kvar; volts 0.988 to 1.009; busiest transformer 156%; export 1952 kW is 1752 kW over the 200 kW limit: the sola |
| 1904 | SITE SURVEY | generic site 1777 | CONFIRMED | connection point -1167 kW (plus is import), +846 kvar; volts 0.988 to 1.013; busiest transformer 406%; export 1167 kW is 967 kW over the 200 kW limit: the solar |
| 1905 | SITE SURVEY | generic site 1778 | CONFIRMED | connection point -2574 kW (plus is import), +1037 kvar; volts 0.992 to 1.013; busiest transformer 232%; export 2574 kW is 2374 kW over the 200 kW limit: the sol |
| 1906 | SITE SURVEY | generic site 1779 | REFUTED | connection point -4256 kW (plus is import), +289 kvar; volts 0.999 to 1.310; busiest transformer 1442%; export 4256 kW is 4206 kW over the 50 kW limit: the sola |
| 1907 | SITE SURVEY | generic site 1780 | CONFIRMED | connection point -1435 kW (plus is import), +828 kvar; volts 0.987 to 1.006; busiest transformer 130%; export 1435 kW is 935 kW over the 500 kW limit: the solar |
| 1908 | SITE SURVEY | generic site 1781 | CONFIRMED | connection point -1334 kW (plus is import), +315 kvar; volts 0.992 to 1.003; busiest transformer 94%; export 1334 kW is 334 kW over the 1000 kW limit: the solar |
| 1909 | SITE SURVEY | generic site 1782 | CONFIRMED | connection point -1840 kW (plus is import), +533 kvar; volts 0.997 to 1.017; busiest transformer 226%; export 1840 kW is 1640 kW over the 200 kW limit: the sola |
| 1910 | SITE SURVEY | generic site 1783 | CONFIRMED | connection point -2190 kW (plus is import), +855 kvar; volts 0.991 to 1.008; busiest transformer 189%; export 2190 kW is 2190 kW over the 0 kW limit: the solar  |
| 1911 | SITE SURVEY | generic site 1784 | CONFIRMED | connection point -473 kW (plus is import), +103 kvar; volts 0.998 to 1.005; busiest transformer 104%; a transformer is at 104% of its rating |
| 1912 | SITE SURVEY | generic site 1785 | REFUTED | connection point -1937 kW (plus is import), +8905 kvar; volts 0.637 to 1.000; busiest transformer 1206%; export 1937 kW is 1937 kW over the 0 kW limit: the sola |
| 1913 | SITE SURVEY | generic site 1786 | CONFIRMED | connection point -2833 kW (plus is import), +1553 kvar; volts 0.991 to 1.013; busiest transformer 495%; export 2833 kW is 2783 kW over the 50 kW limit: the sola |
| 1914 | SITE SURVEY | generic site 1787 | CONFIRMED | connection point -85 kW (plus is import), +182 kvar; volts 0.995 to 1.000; busiest transformer 29%; inside every limit |
| 1915 | SITE SURVEY | generic site 1788 | CONFIRMED | connection point -2333 kW (plus is import), +1201 kvar; volts 0.986 to 1.012; busiest transformer 414%; export 2333 kW is 1333 kW over the 1000 kW limit: the so |
| 1916 | SITE SURVEY | generic site 1789 | CONFIRMED | connection point -732 kW (plus is import), +983 kvar; volts 0.985 to 1.010; busiest transformer 384%; export 732 kW is 682 kW over the 50 kW limit: the solar mu |
| 1917 | SITE SURVEY | generic site 1790 | CONFIRMED | connection point -370 kW (plus is import), +486 kvar; volts 0.989 to 1.000; busiest transformer 45%; export 370 kW is 170 kW over the 200 kW limit: the solar mu |
| 1918 | SITE SURVEY | generic site 1791 | CONFIRMED | connection point -4339 kW (plus is import), +4824 kvar; volts 0.928 to 1.000; busiest transformer 874%; export 4339 kW is 4289 kW over the 50 kW limit: the sola |
| 1919 | SITE SURVEY | generic site 1792 | CONFIRMED | connection point -2202 kW (plus is import), +1405 kvar; volts 0.988 to 1.010; busiest transformer 241%; export 2202 kW is 1702 kW over the 500 kW limit: the sol |
| 1920 | SITE SURVEY | generic site 1793 | CONFIRMED | connection point +14 kW (plus is import), +128 kvar; volts 0.995 to 1.000; busiest transformer 13%; inside every limit |
| 1921 | SITE SURVEY | generic site 1794 | CONFIRMED | connection point -1453 kW (plus is import), +337 kvar; volts 0.995 to 1.009; busiest transformer 111%; export 1453 kW is 453 kW over the 1000 kW limit: the sola |
| 1922 | SITE SURVEY | generic site 1795 | CONFIRMED | connection point -711 kW (plus is import), +137 kvar; volts 0.998 to 1.006; busiest transformer 96%; export 711 kW is 711 kW over the 0 kW limit: the solar must |
| 1923 | SITE SURVEY | generic site 1796 | CONFIRMED | connection point -2233 kW (plus is import), +697 kvar; volts 0.993 to 1.013; busiest transformer 181%; export 2233 kW is 1733 kW over the 500 kW limit: the sola |
| 1924 | SITE SURVEY | generic site 1797 | CONFIRMED | connection point -180 kW (plus is import), +351 kvar; volts 0.990 to 1.004; busiest transformer 138%; a transformer is at 138% of its rating |
| 1925 | SITE SURVEY | generic site 1798 | CONFIRMED | connection point -2590 kW (plus is import), +802 kvar; volts 0.993 to 1.012; busiest transformer 169%; export 2590 kW is 2540 kW over the 50 kW limit: the solar |
| 1926 | SITE SURVEY | generic site 1799 | CONFIRMED | connection point -280 kW (plus is import), +175 kvar; volts 0.992 to 1.004; busiest transformer 67%; export 280 kW is 230 kW over the 50 kW limit: the solar mus |
| 1927 | SITE SURVEY | generic site 1800 | CONFIRMED | connection point -2437 kW (plus is import), +1224 kvar; volts 0.988 to 1.015; busiest transformer 429%; export 2437 kW is 2237 kW over the 200 kW limit: the sol |
| 1928 | SITE SURVEY | generic site 1801 | CONFIRMED | connection point -1687 kW (plus is import), +297 kvar; volts 0.999 to 1.006; busiest transformer 90%; export 1687 kW is 1687 kW over the 0 kW limit: the solar m |
| 1929 | SITE SURVEY | generic site 1802 | CONFIRMED | connection point -5363 kW (plus is import), +2447 kvar; volts 0.980 to 1.013; busiest transformer 374%; export 5363 kW is 5363 kW over the 0 kW limit: the solar |
| 1930 | SITE SURVEY | generic site 1803 | CONFIRMED | connection point -3014 kW (plus is import), +1555 kvar; volts 0.985 to 1.008; busiest transformer 508%; export 3014 kW is 2514 kW over the 500 kW limit: the sol |
| 1931 | SITE SURVEY | generic site 1804 | CONFIRMED | connection point -389 kW (plus is import), +479 kvar; volts 0.989 to 1.007; busiest transformer 140%; a transformer is at 140% of its rating |
| 1932 | SITE SURVEY | generic site 1805 | CONFIRMED | connection point -2982 kW (plus is import), +3941 kvar; volts 0.894 to 1.000; busiest transformer 985%; export 2982 kW is 2932 kW over the 50 kW limit: the sola |
| 1933 | SITE SURVEY | generic site 1806 | CONFIRMED | connection point -1268 kW (plus is import), +523 kvar; volts 0.991 to 1.012; busiest transformer 224%; export 1268 kW is 268 kW over the 1000 kW limit: the sola |
| 1934 | SITE SURVEY | generic site 1807 | CONFIRMED | connection point -1284 kW (plus is import), +739 kvar; volts 0.991 to 1.012; busiest transformer 264%; export 1284 kW is 1284 kW over the 0 kW limit: the solar  |
| 1935 | SITE SURVEY | generic site 1808 | CONFIRMED | connection point -1390 kW (plus is import), +245 kvar; volts 0.996 to 1.008; busiest transformer 76%; export 1390 kW is 890 kW over the 500 kW limit: the solar  |
| 1936 | SITE SURVEY | generic site 1809 | CONFIRMED | connection point -1371 kW (plus is import), +1135 kvar; volts 0.985 to 1.010; busiest transformer 331%; export 1371 kW is 871 kW over the 500 kW limit: the sola |
| 1937 | SITE SURVEY | generic site 1810 | CONFIRMED | connection point -555 kW (plus is import), +149 kvar; volts 0.993 to 1.010; busiest transformer 142%; a transformer is at 142% of its rating |
| 1938 | SITE SURVEY | generic site 1811 | CONFIRMED | connection point -1677 kW (plus is import), +781 kvar; volts 0.989 to 1.017; busiest transformer 308%; export 1677 kW is 1477 kW over the 200 kW limit: the sola |
| 1939 | SITE SURVEY | generic site 1812 | CONFIRMED | connection point -1578 kW (plus is import), +958 kvar; volts 0.990 to 1.017; busiest transformer 328%; export 1578 kW is 1378 kW over the 200 kW limit: the sola |
| 1940 | SITE SURVEY | generic site 1813 | CONFIRMED | connection point -1312 kW (plus is import), +584 kvar; volts 0.990 to 1.013; busiest transformer 245%; export 1312 kW is 1262 kW over the 50 kW limit: the solar |
| 1941 | SITE SURVEY | generic site 1814 | CONFIRMED | connection point -3921 kW (plus is import), +2423 kvar; volts 0.986 to 1.012; busiest transformer 567%; export 3921 kW is 3871 kW over the 50 kW limit: the sola |
| 1942 | SITE SURVEY | generic site 1815 | CONFIRMED | connection point -1356 kW (plus is import), +432 kvar; volts 0.993 to 1.014; busiest transformer 217%; export 1356 kW is 1156 kW over the 200 kW limit: the sola |
| 1943 | SITE SURVEY | generic site 1816 | CONFIRMED | connection point -1378 kW (plus is import), +519 kvar; volts 0.990 to 1.009; busiest transformer 190%; export 1378 kW is 1328 kW over the 50 kW limit: the solar |
| 1944 | SITE SURVEY | generic site 1817 | CONFIRMED | connection point -3998 kW (plus is import), +1569 kvar; volts 0.987 to 1.012; busiest transformer 274%; export 3998 kW is 2998 kW over the 1000 kW limit: the so |
| 1945 | SITE SURVEY | generic site 1818 | CONFIRMED | connection point -382 kW (plus is import), +214 kvar; volts 0.993 to 1.005; busiest transformer 127%; a transformer is at 127% of its rating |
| 1946 | SITE SURVEY | generic site 1819 | CONFIRMED | connection point -260 kW (plus is import), +473 kvar; volts 0.988 to 1.000; busiest transformer 46%; export 260 kW is 210 kW over the 50 kW limit: the solar mus |
| 1947 | SITE SURVEY | generic site 1820 | CONFIRMED | connection point -621 kW (plus is import), +309 kvar; volts 0.992 to 1.003; busiest transformer 97%; inside every limit |
| 1948 | SITE SURVEY | generic site 1821 | CONFIRMED | connection point -641 kW (plus is import), +689 kvar; volts 0.987 to 1.006; busiest transformer 196%; export 641 kW is 441 kW over the 200 kW limit: the solar m |
| 1949 | SITE SURVEY | generic site 1822 | REFUTED | connection point -5442 kW (plus is import), +8315 kvar; volts 0.940 to 1.079; busiest transformer 2370%; export 5442 kW is 5392 kW over the 50 kW limit: the sol |
| 1950 | SITE SURVEY | generic site 1823 | CONFIRMED | connection point -517 kW (plus is import), +323 kvar; volts 0.992 to 1.002; busiest transformer 89%; export 517 kW is 17 kW over the 500 kW limit: the solar mus |
| 1951 | SITE SURVEY | generic site 1824 | CONFIRMED | connection point -1439 kW (plus is import), +545 kvar; volts 0.989 to 1.012; busiest transformer 360%; export 1439 kW is 1239 kW over the 200 kW limit: the sola |
| 1952 | SITE SURVEY | generic site 1825 | CONFIRMED | connection point -1487 kW (plus is import), +698 kvar; volts 0.991 to 1.014; busiest transformer 277%; export 1487 kW is 1287 kW over the 200 kW limit: the sola |
| 1953 | SITE SURVEY | generic site 1826 | CONFIRMED | connection point -2875 kW (plus is import), +1926 kvar; volts 0.986 to 1.012; busiest transformer 459%; export 2875 kW is 2875 kW over the 0 kW limit: the solar |
| 1954 | SITE SURVEY | generic site 1827 | CONFIRMED | connection point -2128 kW (plus is import), +701 kvar; volts 0.990 to 1.011; busiest transformer 175%; export 2128 kW is 2078 kW over the 50 kW limit: the solar |
| 1955 | SITE SURVEY | generic site 1828 | CONFIRMED | connection point -4494 kW (plus is import), +2088 kvar; volts 0.981 to 1.008; busiest transformer 322%; export 4494 kW is 3494 kW over the 1000 kW limit: the so |
| 1956 | SITE SURVEY | generic site 1829 | CONFIRMED | connection point -726 kW (plus is import), +399 kvar; volts 0.991 to 1.002; busiest transformer 76%; export 726 kW is 226 kW over the 500 kW limit: the solar mu |
| 1957 | SITE SURVEY | generic site 1830 | CONFIRMED | connection point -3665 kW (plus is import), +2178 kvar; volts 0.984 to 1.005; busiest transformer 521%; export 3665 kW is 2665 kW over the 1000 kW limit: the so |
| 1958 | SITE SURVEY | generic site 1831 | CONFIRMED | connection point -3190 kW (plus is import), +1382 kvar; volts 0.991 to 1.016; busiest transformer 418%; export 3190 kW is 2690 kW over the 500 kW limit: the sol |
| 1959 | SITE SURVEY | generic site 1832 | CONFIRMED | connection point -2161 kW (plus is import), +1444 kvar; volts 0.985 to 1.012; busiest transformer 439%; export 2161 kW is 2161 kW over the 0 kW limit: the solar |
| 1960 | SITE SURVEY | generic site 1833 | CONFIRMED | connection point -1183 kW (plus is import), +1067 kvar; volts 0.990 to 1.011; busiest transformer 308%; export 1183 kW is 183 kW over the 1000 kW limit: the sol |
| 1961 | SITE SURVEY | generic site 1834 | CONFIRMED | connection point -2099 kW (plus is import), +766 kvar; volts 0.993 to 1.011; busiest transformer 179%; export 2099 kW is 2099 kW over the 0 kW limit: the solar  |
| 1962 | SITE SURVEY | generic site 1835 | CONFIRMED | connection point -5392 kW (plus is import), +2760 kvar; volts 0.984 to 1.017; busiest transformer 464%; export 5392 kW is 5192 kW over the 200 kW limit: the sol |
| 1963 | SITE SURVEY | generic site 1836 | CONFIRMED | connection point -2452 kW (plus is import), +679 kvar; volts 0.994 to 1.018; busiest transformer 195%; export 2452 kW is 1952 kW over the 500 kW limit: the sola |
| 1964 | SITE SURVEY | generic site 1837 | CONFIRMED | connection point -2752 kW (plus is import), +1437 kvar; volts 0.987 to 1.016; busiest transformer 401%; export 2752 kW is 2752 kW over the 0 kW limit: the solar |
| 1965 | SITE SURVEY | generic site 1838 | CONFIRMED | connection point -299 kW (plus is import), +176 kvar; volts 0.996 to 1.003; busiest transformer 100%; export 299 kW is 99 kW over the 200 kW limit: the solar mu |
| 1966 | SITE SURVEY | generic site 1839 | CONFIRMED | connection point -2385 kW (plus is import), +492 kvar; volts 0.995 to 1.006; busiest transformer 131%; export 2385 kW is 2385 kW over the 0 kW limit: the solar  |
| 1967 | SITE SURVEY | generic site 1840 | CONFIRMED | connection point -3895 kW (plus is import), +3781 kvar; volts 0.962 to 1.000; busiest transformer 782%; export 3895 kW is 3895 kW over the 0 kW limit: the solar |
| 1968 | SITE SURVEY | generic site 1841 | CONFIRMED | connection point -3729 kW (plus is import), +2446 kvar; volts 0.983 to 1.000; busiest transformer 647%; export 3729 kW is 3679 kW over the 50 kW limit: the sola |
| 1969 | SITE SURVEY | generic site 1842 | CONFIRMED | connection point -1210 kW (plus is import), +311 kvar; volts 0.993 to 1.007; busiest transformer 92%; export 1210 kW is 210 kW over the 1000 kW limit: the solar |
| 1970 | SITE SURVEY | generic site 1843 | CONFIRMED | connection point +139 kW (plus is import), +400 kvar; volts 0.988 to 1.000; busiest transformer 55%; inside every limit |
| 1971 | SITE SURVEY | generic site 1844 | CONFIRMED | connection point -2872 kW (plus is import), +2362 kvar; volts 0.967 to 1.000; busiest transformer 814%; export 2872 kW is 2822 kW over the 50 kW limit: the sola |
| 1972 | SITE SURVEY | generic site 1845 | CONFIRMED | connection point -1882 kW (plus is import), +471 kvar; volts 0.993 to 1.013; busiest transformer 146%; export 1882 kW is 1882 kW over the 0 kW limit: the solar  |
| 1973 | SITE SURVEY | generic site 1846 | CONFIRMED | connection point -4714 kW (plus is import), +5258 kvar; volts 0.909 to 1.000; busiest transformer 913%; export 4714 kW is 4214 kW over the 500 kW limit: the sol |
| 1974 | SITE SURVEY | generic site 1847 | CONFIRMED | connection point -1454 kW (plus is import), +333 kvar; volts 0.994 to 1.008; busiest transformer 111%; export 1454 kW is 1454 kW over the 0 kW limit: the solar  |
| 1975 | SITE SURVEY | generic site 1848 | CONFIRMED | connection point -1239 kW (plus is import), +1549 kvar; volts 0.982 to 1.008; busiest transformer 389%; export 1239 kW is 739 kW over the 500 kW limit: the sola |
| 1976 | SITE SURVEY | generic site 1849 | CONFIRMED | connection point -456 kW (plus is import), +216 kvar; volts 0.995 to 1.011; busiest transformer 149%; export 456 kW is 456 kW over the 0 kW limit: the solar mus |
| 1977 | SITE SURVEY | generic site 1850 | CONFIRMED | connection point -1162 kW (plus is import), +898 kvar; volts 0.989 to 1.013; busiest transformer 233%; export 1162 kW is 1112 kW over the 50 kW limit: the solar |
| 1978 | SITE SURVEY | generic site 1851 | CONFIRMED | connection point +208 kW (plus is import), +308 kvar; volts 0.988 to 1.000; busiest transformer 29%; inside every limit |
| 1979 | SITE SURVEY | generic site 1852 | CONFIRMED | connection point -1469 kW (plus is import), +273 kvar; volts 0.992 to 1.009; busiest transformer 86%; export 1469 kW is 1469 kW over the 0 kW limit: the solar m |
| 1980 | SITE SURVEY | generic site 1853 | CONFIRMED | connection point -958 kW (plus is import), +341 kvar; volts 0.995 to 1.015; busiest transformer 256%; export 958 kW is 758 kW over the 200 kW limit: the solar m |
| 1981 | SITE SURVEY | generic site 1854 | CONFIRMED | connection point -1025 kW (plus is import), +515 kvar; volts 0.991 to 1.015; busiest transformer 310%; export 1025 kW is 975 kW over the 50 kW limit: the solar  |
| 1982 | SITE SURVEY | generic site 1855 | CONFIRMED | connection point -1305 kW (plus is import), +797 kvar; volts 0.987 to 1.006; busiest transformer 146%; export 1305 kW is 305 kW over the 1000 kW limit: the sola |
| 1983 | SITE SURVEY | generic site 1856 | CONFIRMED | connection point -2043 kW (plus is import), +841 kvar; volts 0.993 to 1.015; busiest transformer 189%; export 2043 kW is 1043 kW over the 1000 kW limit: the sol |
| 1984 | SITE SURVEY | generic site 1857 | CONFIRMED | connection point -2177 kW (plus is import), +513 kvar; volts 0.995 to 1.007; busiest transformer 127%; export 2177 kW is 1177 kW over the 1000 kW limit: the sol |
| 1985 | SITE SURVEY | generic site 1858 | CONFIRMED | connection point -881 kW (plus is import), +1261 kvar; volts 0.985 to 1.007; busiest transformer 461%; a transformer is at 461% of its rating |
| 1986 | SITE SURVEY | generic site 1859 | CONFIRMED | connection point -5147 kW (plus is import), +2292 kvar; volts 0.980 to 1.011; busiest transformer 426%; export 5147 kW is 4647 kW over the 500 kW limit: the sol |
| 1987 | SITE SURVEY | generic site 1860 | CONFIRMED | connection point -5442 kW (plus is import), +2870 kvar; volts 0.984 to 1.017; busiest transformer 473%; export 5442 kW is 5392 kW over the 50 kW limit: the sola |
| 1988 | SITE SURVEY | generic site 1861 | CONFIRMED | connection point -2549 kW (plus is import), +2295 kvar; volts 0.972 to 1.000; busiest transformer 783%; export 2549 kW is 2349 kW over the 200 kW limit: the sol |
| 1989 | SITE SURVEY | generic site 1862 | CONFIRMED | connection point -756 kW (plus is import), +449 kvar; volts 0.993 to 1.002; busiest transformer 65%; export 756 kW is 556 kW over the 200 kW limit: the solar mu |
| 1990 | SITE SURVEY | generic site 1863 | CONFIRMED | connection point -2601 kW (plus is import), +2039 kvar; volts 0.977 to 1.000; busiest transformer 747%; export 2601 kW is 1601 kW over the 1000 kW limit: the so |
| 1991 | SITE SURVEY | generic site 1864 | CONFIRMED | connection point -1960 kW (plus is import), +429 kvar; volts 0.993 to 1.006; busiest transformer 110%; export 1960 kW is 1910 kW over the 50 kW limit: the solar |
| 1992 | SITE SURVEY | generic site 1865 | CONFIRMED | connection point -2490 kW (plus is import), +1232 kvar; volts 0.987 to 1.013; busiest transformer 356%; export 2490 kW is 1990 kW over the 500 kW limit: the sol |
| 1993 | SITE SURVEY | generic site 1866 | CONFIRMED | connection point -163 kW (plus is import), +399 kvar; volts 0.991 to 1.000; busiest transformer 37%; inside every limit |
| 1994 | SITE SURVEY | generic site 1867 | CONFIRMED | connection point -2466 kW (plus is import), +1116 kvar; volts 0.991 to 1.016; busiest transformer 411%; export 2466 kW is 1966 kW over the 500 kW limit: the sol |
| 1995 | SITE SURVEY | generic site 1868 | REFUTED | connection point -3245 kW (plus is import), +4643 kvar; volts 0.851 to 1.000; busiest transformer 1051%; export 3245 kW is 3245 kW over the 0 kW limit: the sola |
| 1996 | SITE SURVEY | generic site 1869 | CONFIRMED | connection point -4214 kW (plus is import), +2827 kvar; volts 0.976 to 1.000; busiest transformer 608%; export 4214 kW is 3714 kW over the 500 kW limit: the sol |
| 1997 | SITE SURVEY | generic site 1870 | CONFIRMED | connection point -1270 kW (plus is import), +603 kvar; volts 0.990 to 1.012; busiest transformer 237%; export 1270 kW is 1270 kW over the 0 kW limit: the solar  |
| 1998 | SITE SURVEY | generic site 1871 | CONFIRMED | connection point -2084 kW (plus is import), +1103 kvar; volts 0.990 to 1.006; busiest transformer 550%; export 2084 kW is 2034 kW over the 50 kW limit: the sola |
| 1999 | SITE SURVEY | generic site 1872 | CONFIRMED | connection point -1194 kW (plus is import), +392 kvar; volts 0.994 to 1.012; busiest transformer 162%; export 1194 kW is 994 kW over the 200 kW limit: the solar |
| 2000 | SITE SURVEY | generic site 1873 | CONFIRMED | connection point -4908 kW (plus is import), +6788 kvar; volts 0.849 to 1.000; busiest transformer 987%; export 4908 kW is 4908 kW over the 0 kW limit: the solar |
| 2001 | SITE SURVEY | generic site 1874 | CONFIRMED | connection point -2653 kW (plus is import), +809 kvar; volts 0.989 to 1.010; busiest transformer 208%; export 2653 kW is 1653 kW over the 1000 kW limit: the sol |
| 2002 | SITE SURVEY | generic site 1875 | CONFIRMED | connection point -2221 kW (plus is import), +709 kvar; volts 0.993 to 1.019; busiest transformer 279%; export 2221 kW is 2021 kW over the 200 kW limit: the sola |
| 2003 | SITE SURVEY | generic site 1876 | CONFIRMED | connection point +73 kW (plus is import), +687 kvar; volts 0.986 to 1.000; busiest transformer 63%; inside every limit |
| 2004 | SITE SURVEY | generic site 1877 | CONFIRMED | connection point -1206 kW (plus is import), +376 kvar; volts 0.995 to 1.013; busiest transformer 192%; export 1206 kW is 706 kW over the 500 kW limit: the solar |
| 2005 | SITE SURVEY | generic site 1878 | CONFIRMED | connection point -3457 kW (plus is import), +1600 kvar; volts 0.985 to 1.012; busiest transformer 459%; export 3457 kW is 3457 kW over the 0 kW limit: the solar |
| 2006 | SITE SURVEY | generic site 1879 | CONFIRMED | connection point -1797 kW (plus is import), +1060 kvar; volts 0.989 to 1.014; busiest transformer 356%; export 1797 kW is 797 kW over the 1000 kW limit: the sol |
| 2007 | SITE SURVEY | generic site 1880 | CONFIRMED | connection point -2055 kW (plus is import), +1588 kvar; volts 0.986 to 1.013; busiest transformer 453%; export 2055 kW is 2005 kW over the 50 kW limit: the sola |
| 2008 | SITE SURVEY | generic site 1881 | CONFIRMED | connection point -271 kW (plus is import), +599 kvar; volts 0.987 to 1.005; busiest transformer 124%; export 271 kW is 271 kW over the 0 kW limit: the solar mus |
| 2009 | SITE SURVEY | generic site 1882 | CONFIRMED | connection point +77 kW (plus is import), +342 kvar; volts 0.988 to 1.000; busiest transformer 30%; inside every limit |
| 2010 | SITE SURVEY | generic site 1883 | CONFIRMED | connection point -5678 kW (plus is import), +2438 kvar; volts 0.987 to 1.016; busiest transformer 378%; export 5678 kW is 5628 kW over the 50 kW limit: the sola |
| 2011 | SITE SURVEY | generic site 1884 | CONFIRMED | connection point +53 kW (plus is import), +723 kvar; volts 0.985 to 1.004; busiest transformer 119%; a transformer is at 119% of its rating |
| 2012 | SITE SURVEY | generic site 1885 | CONFIRMED | connection point -1259 kW (plus is import), +816 kvar; volts 0.988 to 1.009; busiest transformer 222%; export 1259 kW is 759 kW over the 500 kW limit: the solar |
| 2013 | SITE SURVEY | generic site 1886 | CONFIRMED | connection point -804 kW (plus is import), +279 kvar; volts 0.994 to 1.008; busiest transformer 136%; export 804 kW is 604 kW over the 200 kW limit: the solar m |
| 2014 | SITE SURVEY | generic site 1887 | CONFIRMED | connection point -289 kW (plus is import), +360 kvar; volts 0.990 to 1.001; busiest transformer 51%; export 289 kW is 89 kW over the 200 kW limit: the solar mus |
| 2015 | SITE SURVEY | generic site 1888 | CONFIRMED | connection point -2765 kW (plus is import), +1374 kvar; volts 0.988 to 1.013; busiest transformer 394%; export 2765 kW is 2765 kW over the 0 kW limit: the solar |
| 2016 | SITE SURVEY | generic site 1889 | CONFIRMED | connection point -411 kW (plus is import), +361 kvar; volts 0.990 to 1.006; busiest transformer 97%; inside every limit |
| 2017 | SITE SURVEY | generic site 1890 | CONFIRMED | connection point -2669 kW (plus is import), +751 kvar; volts 0.992 to 1.011; busiest transformer 171%; export 2669 kW is 1669 kW over the 1000 kW limit: the sol |
| 2018 | SITE SURVEY | generic site 1891 | CONFIRMED | connection point -2254 kW (plus is import), +1734 kvar; volts 0.987 to 1.000; busiest transformer 675%; export 2254 kW is 1754 kW over the 500 kW limit: the sol |
| 2019 | SITE SURVEY | generic site 1892 | CONFIRMED | connection point -3487 kW (plus is import), +1985 kvar; volts 0.981 to 1.007; busiest transformer 499%; export 3487 kW is 2487 kW over the 1000 kW limit: the so |
| 2020 | SITE SURVEY | generic site 1893 | CONFIRMED | connection point -488 kW (plus is import), +843 kvar; volts 0.986 to 1.002; busiest transformer 112%; a transformer is at 112% of its rating |
| 2021 | SITE SURVEY | generic site 1894 | CONFIRMED | connection point -422 kW (plus is import), +982 kvar; volts 0.985 to 1.010; busiest transformer 347%; export 422 kW is 372 kW over the 50 kW limit: the solar mu |
| 2022 | SITE SURVEY | generic site 1895 | CONFIRMED | connection point -3743 kW (plus is import), +1503 kvar; volts 0.985 to 1.013; busiest transformer 259%; export 3743 kW is 3243 kW over the 500 kW limit: the sol |
| 2023 | SITE SURVEY | generic site 1896 | CONFIRMED | connection point -1217 kW (plus is import), +1363 kvar; volts 0.983 to 1.003; busiest transformer 514%; export 1217 kW is 1017 kW over the 200 kW limit: the sol |
| 2024 | SITE SURVEY | generic site 1897 | CONFIRMED | connection point -469 kW (plus is import), +489 kvar; volts 0.990 to 1.006; busiest transformer 121%; export 469 kW is 419 kW over the 50 kW limit: the solar mu |
| 2025 | SITE SURVEY | generic site 1898 | CONFIRMED | connection point -1868 kW (plus is import), +1192 kvar; volts 0.986 to 1.006; busiest transformer 546%; export 1868 kW is 1868 kW over the 0 kW limit: the solar |
| 2026 | SITE SURVEY | generic site 1899 | CONFIRMED | connection point -2815 kW (plus is import), +657 kvar; volts 0.996 to 1.012; busiest transformer 162%; export 2815 kW is 2765 kW over the 50 kW limit: the solar |
| 2027 | SITE SURVEY | generic site 1900 | CONFIRMED | connection point -409 kW (plus is import), +114 kvar; volts 0.997 to 1.007; busiest transformer 103%; export 409 kW is 409 kW over the 0 kW limit: the solar mus |
| 2028 | SITE SURVEY | generic site 1901 | CONFIRMED | connection point -1390 kW (plus is import), +580 kvar; volts 0.991 to 1.007; busiest transformer 108%; export 1390 kW is 390 kW over the 1000 kW limit: the sola |
| 2029 | SITE SURVEY | generic site 1902 | CONFIRMED | connection point -488 kW (plus is import), +141 kvar; volts 0.994 to 1.008; busiest transformer 125%; export 488 kW is 488 kW over the 0 kW limit: the solar mus |
| 2030 | SITE SURVEY | generic site 1903 | CONFIRMED | connection point -539 kW (plus is import), +730 kvar; volts 0.987 to 1.001; busiest transformer 81%; export 539 kW is 39 kW over the 500 kW limit: the solar mus |
| 2031 | SITE SURVEY | generic site 1904 | CONFIRMED | connection point -1179 kW (plus is import), +626 kvar; volts 0.991 to 1.015; busiest transformer 242%; export 1179 kW is 979 kW over the 200 kW limit: the solar |
| 2032 | SITE SURVEY | generic site 1905 | CONFIRMED | connection point -39 kW (plus is import), +226 kvar; volts 0.989 to 1.005; busiest transformer 84%; inside every limit |
| 2033 | SITE SURVEY | generic site 1906 | CONFIRMED | connection point +108 kW (plus is import), +416 kvar; volts 0.988 to 1.000; busiest transformer 51%; inside every limit |
| 2034 | SITE SURVEY | generic site 1907 | CONFIRMED | connection point -1189 kW (plus is import), +474 kvar; volts 0.990 to 1.002; busiest transformer 80%; export 1189 kW is 989 kW over the 200 kW limit: the solar  |
| 2035 | SITE SURVEY | generic site 1908 | CONFIRMED | connection point -1892 kW (plus is import), +561 kvar; volts 0.995 to 1.009; busiest transformer 119%; export 1892 kW is 1692 kW over the 200 kW limit: the sola |
| 2036 | SITE SURVEY | generic site 1909 | CONFIRMED | connection point -1097 kW (plus is import), +394 kvar; volts 0.993 to 1.013; busiest transformer 191%; export 1097 kW is 1097 kW over the 0 kW limit: the solar  |
| 2037 | SITE SURVEY | generic site 1910 | CONFIRMED | connection point -1276 kW (plus is import), +306 kvar; volts 0.993 to 1.006; busiest transformer 92%; export 1276 kW is 276 kW over the 1000 kW limit: the solar |
| 2038 | SITE SURVEY | generic site 1911 | CONFIRMED | connection point -2767 kW (plus is import), +730 kvar; volts 0.991 to 1.014; busiest transformer 175%; export 2767 kW is 2717 kW over the 50 kW limit: the solar |
| 2039 | SITE SURVEY | generic site 1912 | CONFIRMED | connection point -2509 kW (plus is import), +559 kvar; volts 0.998 to 1.013; busiest transformer 142%; export 2509 kW is 2009 kW over the 500 kW limit: the sola |
| 2040 | SITE SURVEY | generic site 1913 | CONFIRMED | connection point -3775 kW (plus is import), +2303 kvar; volts 0.979 to 1.003; busiest transformer 539%; export 3775 kW is 3575 kW over the 200 kW limit: the sol |
| 2041 | SITE SURVEY | generic site 1914 | CONFIRMED | connection point -599 kW (plus is import), +207 kvar; volts 0.991 to 1.006; busiest transformer 100%; export 599 kW is 599 kW over the 0 kW limit: the solar mus |
| 2042 | SITE SURVEY | generic site 1915 | CONFIRMED | connection point -1996 kW (plus is import), +1296 kvar; volts 0.987 to 1.014; busiest transformer 409%; export 1996 kW is 1996 kW over the 0 kW limit: the solar |
| 2043 | SITE SURVEY | generic site 1916 | CONFIRMED | connection point -506 kW (plus is import), +116 kvar; volts 0.996 to 1.005; busiest transformer 114%; export 506 kW is 506 kW over the 0 kW limit: the solar mus |
| 2044 | SITE SURVEY | generic site 1917 | CONFIRMED | connection point -1118 kW (plus is import), +289 kvar; volts 0.992 to 1.013; busiest transformer 174%; export 1118 kW is 1118 kW over the 0 kW limit: the solar  |
| 2045 | SITE SURVEY | generic site 1918 | CONFIRMED | connection point -1042 kW (plus is import), +243 kvar; volts 0.996 to 1.010; busiest transformer 128%; export 1042 kW is 842 kW over the 200 kW limit: the solar |
| 2046 | SITE SURVEY | generic site 1919 | CONFIRMED | connection point -1189 kW (plus is import), +491 kvar; volts 0.992 to 1.012; busiest transformer 318%; export 1189 kW is 689 kW over the 500 kW limit: the solar |
| 2047 | SITE SURVEY | generic site 1920 | CONFIRMED | connection point -1960 kW (plus is import), +827 kvar; volts 0.991 to 1.010; busiest transformer 180%; export 1960 kW is 1760 kW over the 200 kW limit: the sola |
| 2048 | SITE SURVEY | generic site 1921 | CONFIRMED | connection point -1017 kW (plus is import), +741 kvar; volts 0.990 to 1.015; busiest transformer 363%; export 1017 kW is 817 kW over the 200 kW limit: the solar |
| 2049 | SITE SURVEY | generic site 1922 | CONFIRMED | connection point -176 kW (plus is import), +58 kvar; volts 0.997 to 1.001; busiest transformer 28%; export 176 kW is 176 kW over the 0 kW limit: the solar must  |
| 2050 | SITE SURVEY | generic site 1923 | CONFIRMED | connection point -4272 kW (plus is import), +1408 kvar; volts 0.990 to 1.013; busiest transformer 270%; export 4272 kW is 4222 kW over the 50 kW limit: the sola |
| 2051 | SITE SURVEY | generic site 1924 | CONFIRMED | connection point -2099 kW (plus is import), +1509 kvar; volts 0.988 to 1.000; busiest transformer 626%; export 2099 kW is 1099 kW over the 1000 kW limit: the so |
| 2052 | SITE SURVEY | generic site 1925 | CONFIRMED | connection point -696 kW (plus is import), +460 kvar; volts 0.989 to 1.012; busiest transformer 167%; export 696 kW is 196 kW over the 500 kW limit: the solar m |
| 2053 | SITE SURVEY | generic site 1926 | CONFIRMED | connection point -1881 kW (plus is import), +1830 kvar; volts 0.983 to 1.008; busiest transformer 466%; export 1881 kW is 1681 kW over the 200 kW limit: the sol |
| 2054 | SITE SURVEY | generic site 1927 | CONFIRMED | connection point -4575 kW (plus is import), +2901 kvar; volts 0.979 to 1.000; busiest transformer 633%; export 4575 kW is 4075 kW over the 500 kW limit: the sol |
| 2055 | SITE SURVEY | generic site 1928 | CONFIRMED | connection point -1284 kW (plus is import), +322 kvar; volts 0.991 to 1.010; busiest transformer 186%; export 1284 kW is 1084 kW over the 200 kW limit: the sola |
| 2056 | SITE SURVEY | generic site 1929 | CONFIRMED | connection point -5433 kW (plus is import), +2287 kvar; volts 0.987 to 1.012; busiest transformer 359%; export 5433 kW is 5233 kW over the 200 kW limit: the sol |
| 2057 | SITE SURVEY | generic site 1930 | CONFIRMED | connection point -2072 kW (plus is import), +2598 kvar; volts 0.966 to 1.000; busiest transformer 790%; export 2072 kW is 1072 kW over the 1000 kW limit: the so |
| 2058 | SITE SURVEY | generic site 1931 | CONFIRMED | connection point -1884 kW (plus is import), +1024 kvar; volts 0.991 to 1.009; busiest transformer 160%; export 1884 kW is 1834 kW over the 50 kW limit: the sola |
| 2059 | SITE SURVEY | generic site 1932 | CONFIRMED | connection point -1230 kW (plus is import), +592 kvar; volts 0.991 to 1.012; busiest transformer 193%; export 1230 kW is 1230 kW over the 0 kW limit: the solar  |
| 2060 | SITE SURVEY | generic site 1933 | CONFIRMED | connection point -867 kW (plus is import), +359 kvar; volts 0.994 to 1.007; busiest transformer 124%; export 867 kW is 367 kW over the 500 kW limit: the solar m |
| 2061 | SITE SURVEY | generic site 1934 | CONFIRMED | connection point -2330 kW (plus is import), +838 kvar; volts 0.993 to 1.017; busiest transformer 302%; export 2330 kW is 2280 kW over the 50 kW limit: the solar |
| 2062 | SITE SURVEY | generic site 1935 | CONFIRMED | connection point -2038 kW (plus is import), +1038 kvar; volts 0.991 to 1.015; busiest transformer 370%; export 2038 kW is 1538 kW over the 500 kW limit: the sol |
| 2063 | SITE SURVEY | generic site 1936 | CONFIRMED | connection point -1193 kW (plus is import), +587 kvar; volts 0.992 to 1.017; busiest transformer 350%; export 1193 kW is 693 kW over the 500 kW limit: the solar |
| 2064 | SITE SURVEY | generic site 1937 | CONFIRMED | connection point -3639 kW (plus is import), +1238 kvar; volts 0.990 to 1.012; busiest transformer 236%; export 3639 kW is 3439 kW over the 200 kW limit: the sol |
| 2065 | SITE SURVEY | generic site 1938 | CONFIRMED | connection point -1999 kW (plus is import), +665 kvar; volts 0.993 to 1.012; busiest transformer 167%; export 1999 kW is 1949 kW over the 50 kW limit: the solar |
| 2066 | SITE SURVEY | generic site 1939 | CONFIRMED | connection point -3664 kW (plus is import), +2259 kvar; volts 0.982 to 1.000; busiest transformer 625%; export 3664 kW is 2664 kW over the 1000 kW limit: the so |
| 2067 | SITE SURVEY | generic site 1940 | CONFIRMED | connection point -2832 kW (plus is import), +1553 kvar; volts 0.991 to 1.016; busiest transformer 499%; export 2832 kW is 2332 kW over the 500 kW limit: the sol |
| 2068 | SITE SURVEY | generic site 1941 | CONFIRMED | connection point -2753 kW (plus is import), +1486 kvar; volts 0.987 to 1.008; busiest transformer 479%; export 2753 kW is 2253 kW over the 500 kW limit: the sol |
| 2069 | SITE SURVEY | generic site 1942 | CONFIRMED | connection point -1662 kW (plus is import), +1037 kvar; volts 0.987 to 1.005; busiest transformer 148%; export 1662 kW is 662 kW over the 1000 kW limit: the sol |
| 2070 | SITE SURVEY | generic site 1943 | CONFIRMED | connection point -1366 kW (plus is import), +979 kvar; volts 0.986 to 1.010; busiest transformer 253%; export 1366 kW is 1316 kW over the 50 kW limit: the solar |
| 2071 | SITE SURVEY | generic site 1944 | CONFIRMED | connection point -55 kW (plus is import), +186 kvar; volts 0.992 to 1.000; busiest transformer 20%; inside every limit |
| 2072 | SITE SURVEY | generic site 1945 | CONFIRMED | connection point -1030 kW (plus is import), +695 kvar; volts 0.990 to 1.011; busiest transformer 350%; export 1030 kW is 980 kW over the 50 kW limit: the solar  |
| 2073 | SITE SURVEY | generic site 1946 | CONFIRMED | connection point -2062 kW (plus is import), +467 kvar; volts 0.995 to 1.010; busiest transformer 120%; export 2062 kW is 1862 kW over the 200 kW limit: the sola |
| 2074 | SITE SURVEY | generic site 1947 | REFUTED | connection point -5035 kW (plus is import), -358 kvar; volts 1.000 to 1.463; busiest transformer 1930%; export 5035 kW is 4985 kW over the 50 kW limit: the sola |
| 2075 | SITE SURVEY | generic site 1948 | CONFIRMED | connection point -1931 kW (plus is import), +645 kvar; volts 0.994 to 1.015; busiest transformer 245%; export 1931 kW is 1931 kW over the 0 kW limit: the solar  |
| 2076 | SITE SURVEY | generic site 1949 | CONFIRMED | connection point -1588 kW (plus is import), +1362 kvar; volts 0.983 to 1.004; busiest transformer 553%; export 1588 kW is 1538 kW over the 50 kW limit: the sola |
| 2077 | SITE SURVEY | generic site 1950 | CONFIRMED | connection point -708 kW (plus is import), +437 kvar; volts 0.990 to 1.006; busiest transformer 130%; export 708 kW is 658 kW over the 50 kW limit: the solar mu |
| 2078 | SITE SURVEY | generic site 1951 | CONFIRMED | connection point -1544 kW (plus is import), +556 kvar; volts 0.992 to 1.012; busiest transformer 205%; export 1544 kW is 1344 kW over the 200 kW limit: the sola |
| 2079 | SITE SURVEY | generic site 1952 | CONFIRMED | connection point -1722 kW (plus is import), +1317 kvar; volts 0.987 to 1.004; busiest transformer 555%; export 1722 kW is 1522 kW over the 200 kW limit: the sol |
| 2080 | SITE SURVEY | generic site 1953 | CONFIRMED | connection point -2656 kW (plus is import), +1317 kvar; volts 0.990 to 1.011; busiest transformer 205%; export 2656 kW is 1656 kW over the 1000 kW limit: the so |
| 2081 | SITE SURVEY | generic site 1954 | CONFIRMED | connection point -314 kW (plus is import), +792 kvar; volts 0.987 to 1.002; busiest transformer 98%; inside every limit |
| 2082 | SITE SURVEY | generic site 1955 | CONFIRMED | connection point -707 kW (plus is import), +825 kvar; volts 0.987 to 1.007; busiest transformer 188%; export 707 kW is 207 kW over the 500 kW limit: the solar m |
| 2083 | SITE SURVEY | generic site 1956 | CONFIRMED | connection point -2849 kW (plus is import), +993 kvar; volts 0.993 to 1.021; busiest transformer 198%; export 2849 kW is 2349 kW over the 500 kW limit: the sola |
| 2084 | SITE SURVEY | generic site 1957 | CONFIRMED | connection point -393 kW (plus is import), +697 kvar; volts 0.988 to 1.011; busiest transformer 274%; a transformer is at 274% of its rating |
| 2085 | SITE SURVEY | generic site 1958 | CONFIRMED | connection point -2430 kW (plus is import), +1158 kvar; volts 0.987 to 1.012; busiest transformer 192%; export 2430 kW is 1930 kW over the 500 kW limit: the sol |
| 2086 | SITE SURVEY | generic site 1959 | CONFIRMED | connection point -5031 kW (plus is import), +2475 kvar; volts 0.986 to 1.011; busiest transformer 429%; export 5031 kW is 4831 kW over the 200 kW limit: the sol |
| 2087 | SITE SURVEY | generic site 1960 | CONFIRMED | connection point -2986 kW (plus is import), +886 kvar; volts 0.991 to 1.012; busiest transformer 230%; export 2986 kW is 2986 kW over the 0 kW limit: the solar  |
| 2088 | SITE SURVEY | generic site 1961 | CONFIRMED | connection point -585 kW (plus is import), +661 kvar; volts 0.988 to 1.002; busiest transformer 77%; inside every limit |
| 2089 | SITE SURVEY | generic site 1962 | CONFIRMED | connection point -1554 kW (plus is import), +1136 kvar; volts 0.987 to 1.007; busiest transformer 157%; export 1554 kW is 554 kW over the 1000 kW limit: the sol |
| 2090 | SITE SURVEY | generic site 1963 | CONFIRMED | connection point -1608 kW (plus is import), +1220 kvar; volts 0.987 to 1.006; busiest transformer 529%; export 1608 kW is 1558 kW over the 50 kW limit: the sola |
| 2091 | SITE SURVEY | generic site 1964 | CONFIRMED | connection point -1465 kW (plus is import), +1393 kvar; volts 0.985 to 1.001; busiest transformer 545%; export 1465 kW is 1415 kW over the 50 kW limit: the sola |
| 2092 | SITE SURVEY | generic site 1965 | CONFIRMED | connection point -5070 kW (plus is import), +3625 kvar; volts 0.976 to 1.000; busiest transformer 707%; export 5070 kW is 4070 kW over the 1000 kW limit: the so |
| 2093 | SITE SURVEY | generic site 1966 | CONFIRMED | connection point -5944 kW (plus is import), +3030 kvar; volts 0.975 to 1.000; busiest transformer 496%; export 5944 kW is 5444 kW over the 500 kW limit: the sol |
| 2094 | SITE SURVEY | generic site 1967 | CONFIRMED | connection point -1242 kW (plus is import), +610 kvar; volts 0.989 to 1.013; busiest transformer 357%; export 1242 kW is 1192 kW over the 50 kW limit: the solar |
| 2095 | SITE SURVEY | generic site 1968 | CONFIRMED | connection point -2034 kW (plus is import), +1413 kvar; volts 0.988 to 1.004; busiest transformer 607%; export 2034 kW is 1984 kW over the 50 kW limit: the sola |
| 2096 | SITE SURVEY | generic site 1969 | CONFIRMED | connection point -1209 kW (plus is import), +514 kvar; volts 0.993 to 1.012; busiest transformer 215%; export 1209 kW is 209 kW over the 1000 kW limit: the sola |
| 2097 | SITE SURVEY | generic site 1970 | CONFIRMED | connection point -337 kW (plus is import), +217 kvar; volts 0.991 to 1.000; busiest transformer 70%; inside every limit |
| 2098 | SITE SURVEY | generic site 1971 | CONFIRMED | connection point -1519 kW (plus is import), +837 kvar; volts 0.989 to 1.013; busiest transformer 436%; export 1519 kW is 519 kW over the 1000 kW limit: the sola |
| 2099 | SITE SURVEY | generic site 1972 | CONFIRMED | connection point -2988 kW (plus is import), +2828 kvar; volts 0.942 to 1.000; busiest transformer 874%; export 2988 kW is 1988 kW over the 1000 kW limit: the so |
| 2100 | SITE SURVEY | generic site 1973 | CONFIRMED | connection point -901 kW (plus is import), +414 kvar; volts 0.994 to 1.012; busiest transformer 145%; export 901 kW is 901 kW over the 0 kW limit: the solar mus |
| 2101 | SITE SURVEY | generic site 1974 | CONFIRMED | connection point -1761 kW (plus is import), +336 kvar; volts 0.999 to 1.006; busiest transformer 94%; export 1761 kW is 1711 kW over the 50 kW limit: the solar  |
| 2102 | SITE SURVEY | generic site 1975 | CONFIRMED | connection point -1907 kW (plus is import), +984 kvar; volts 0.992 to 1.013; busiest transformer 194%; export 1907 kW is 907 kW over the 1000 kW limit: the sola |
| 2103 | SITE SURVEY | generic site 1976 | CONFIRMED | connection point -2508 kW (plus is import), +2156 kvar; volts 0.979 to 1.001; busiest transformer 546%; export 2508 kW is 1508 kW over the 1000 kW limit: the so |
| 2104 | SITE SURVEY | generic site 1977 | CONFIRMED | connection point -1806 kW (plus is import), +808 kvar; volts 0.993 to 1.013; busiest transformer 260%; export 1806 kW is 1756 kW over the 50 kW limit: the solar |
| 2105 | SITE SURVEY | generic site 1978 | CONFIRMED | connection point -409 kW (plus is import), +139 kvar; volts 0.995 to 1.000; busiest transformer 31%; export 409 kW is 409 kW over the 0 kW limit: the solar must |
| 2106 | SITE SURVEY | generic site 1979 | CONFIRMED | connection point -646 kW (plus is import), +289 kvar; volts 0.992 to 1.000; busiest transformer 39%; export 646 kW is 446 kW over the 200 kW limit: the solar mu |
| 2107 | SITE SURVEY | generic site 1980 | CONFIRMED | connection point -758 kW (plus is import), +205 kvar; volts 0.992 to 1.003; busiest transformer 55%; export 758 kW is 758 kW over the 0 kW limit: the solar must |
| 2108 | SITE SURVEY | generic site 1981 | CONFIRMED | connection point -577 kW (plus is import), +337 kvar; volts 0.991 to 1.011; busiest transformer 198%; export 577 kW is 377 kW over the 200 kW limit: the solar m |
| 2109 | SITE SURVEY | generic site 1982 | CONFIRMED | connection point -1896 kW (plus is import), +1412 kvar; volts 0.984 to 1.015; busiest transformer 350%; export 1896 kW is 1846 kW over the 50 kW limit: the sola |
| 2110 | SITE SURVEY | generic site 1983 | CONFIRMED | connection point -1803 kW (plus is import), +910 kvar; volts 0.987 to 1.012; busiest transformer 275%; export 1803 kW is 1603 kW over the 200 kW limit: the sola |
| 2111 | SITE SURVEY | generic site 1984 | CONFIRMED | connection point -2969 kW (plus is import), +1399 kvar; volts 0.990 to 1.020; busiest transformer 412%; export 2969 kW is 2469 kW over the 500 kW limit: the sol |
| 2112 | SITE SURVEY | generic site 1985 | CONFIRMED | connection point -4138 kW (plus is import), +1463 kvar; volts 0.992 to 1.016; busiest transformer 323%; export 4138 kW is 3638 kW over the 500 kW limit: the sol |
| 2113 | SITE SURVEY | generic site 1986 | CONFIRMED | connection point +329 kW (plus is import), +715 kvar; volts 0.986 to 1.003; busiest transformer 118%; a transformer is at 118% of its rating |
| 2114 | SITE SURVEY | generic site 1987 | CONFIRMED | connection point -1615 kW (plus is import), +1320 kvar; volts 0.987 to 1.016; busiest transformer 386%; export 1615 kW is 1115 kW over the 500 kW limit: the sol |
| 2115 | SITE SURVEY | generic site 1988 | CONFIRMED | connection point -456 kW (plus is import), +832 kvar; volts 0.988 to 1.013; busiest transformer 321%; export 456 kW is 406 kW over the 50 kW limit: the solar mu |
| 2116 | SITE SURVEY | generic site 1989 | CONFIRMED | connection point -4652 kW (plus is import), +1557 kvar; volts 0.992 to 1.020; busiest transformer 292%; export 4652 kW is 4152 kW over the 500 kW limit: the sol |
| 2117 | SITE SURVEY | generic site 1990 | CONFIRMED | connection point -410 kW (plus is import), +111 kvar; volts 0.993 to 1.004; busiest transformer 52%; export 410 kW is 360 kW over the 50 kW limit: the solar mus |
| 2118 | SITE SURVEY | generic site 1991 | CONFIRMED | connection point -1962 kW (plus is import), +1201 kvar; volts 0.989 to 1.015; busiest transformer 389%; export 1962 kW is 962 kW over the 1000 kW limit: the sol |
| 2119 | SITE SURVEY | generic site 1992 | CONFIRMED | connection point -3377 kW (plus is import), +1434 kvar; volts 0.986 to 1.009; busiest transformer 294%; export 3377 kW is 3377 kW over the 0 kW limit: the solar |
| 2120 | SITE SURVEY | generic site 1993 | CONFIRMED | connection point -3549 kW (plus is import), +1031 kvar; volts 0.989 to 1.014; busiest transformer 223%; export 3549 kW is 3549 kW over the 0 kW limit: the solar |
| 2121 | SITE SURVEY | generic site 1994 | CONFIRMED | connection point -1323 kW (plus is import), +791 kvar; volts 0.992 to 1.017; busiest transformer 414%; export 1323 kW is 323 kW over the 1000 kW limit: the sola |
| 2122 | SITE SURVEY | generic site 1995 | CONFIRMED | connection point -1116 kW (plus is import), +1246 kvar; volts 0.985 to 1.012; busiest transformer 333%; export 1116 kW is 916 kW over the 200 kW limit: the sola |
| 2123 | SITE SURVEY | generic site 1996 | CONFIRMED | connection point -2415 kW (plus is import), +1200 kvar; volts 0.989 to 1.013; busiest transformer 352%; export 2415 kW is 2415 kW over the 0 kW limit: the solar |
| 2124 | SITE SURVEY | generic site 1997 | CONFIRMED | connection point -3380 kW (plus is import), +1664 kvar; volts 0.987 to 1.011; busiest transformer 461%; export 3380 kW is 2380 kW over the 1000 kW limit: the so |
| 2125 | SITE SURVEY | generic site 1998 | CONFIRMED | connection point -2473 kW (plus is import), +759 kvar; volts 0.995 to 1.015; busiest transformer 164%; export 2473 kW is 1473 kW over the 1000 kW limit: the sol |
| 2126 | SITE SURVEY | generic site 1999 | CONFIRMED | connection point -389 kW (plus is import), +154 kvar; volts 0.993 to 1.004; busiest transformer 57%; export 389 kW is 339 kW over the 50 kW limit: the solar mus |
| 2127 | SITE SURVEY | generic site 2000 | CONFIRMED | connection point -345 kW (plus is import), +466 kvar; volts 0.989 to 1.007; busiest transformer 197%; export 345 kW is 345 kW over the 0 kW limit: the solar mus |
| 2128 | CABLE CHECK | the known answer | CONFIRMED | 17.39 kA |
| 2129 | CABLE CHECK | withstand al 95 0.2s 8kA | CONFIRMED | withstands 19.97 kA; asked for 8.0 kA: survives |
| 2130 | CABLE CHECK | withstand al 95 0.2s 16kA | CONFIRMED | withstands 19.97 kA; asked for 16.0 kA: survives |
| 2131 | CABLE CHECK | withstand al 95 0.2s 25kA | CONFIRMED | withstands 19.97 kA; asked for 25.0 kA: DOES NOT SURVIVE: a larger conductor or faster protection |
| 2132 | CABLE CHECK | withstand al 95 1.0s 8kA | CONFIRMED | withstands 8.93 kA; asked for 8.0 kA: survives |
| 2133 | CABLE CHECK | withstand al 95 1.0s 16kA | CONFIRMED | withstands 8.93 kA; asked for 16.0 kA: DOES NOT SURVIVE: a larger conductor or faster protection |
| 2134 | CABLE CHECK | withstand al 95 1.0s 25kA | CONFIRMED | withstands 8.93 kA; asked for 25.0 kA: DOES NOT SURVIVE: a larger conductor or faster protection |
| 2135 | CABLE CHECK | withstand al 95 3.0s 8kA | CONFIRMED | withstands 5.16 kA; asked for 8.0 kA: DOES NOT SURVIVE: a larger conductor or faster protection |
| 2136 | CABLE CHECK | withstand al 95 3.0s 16kA | CONFIRMED | withstands 5.16 kA; asked for 16.0 kA: DOES NOT SURVIVE: a larger conductor or faster protection |
| 2137 | CABLE CHECK | withstand al 95 3.0s 25kA | CONFIRMED | withstands 5.16 kA; asked for 25.0 kA: DOES NOT SURVIVE: a larger conductor or faster protection |
| 2138 | CABLE CHECK | withstand al 185 0.2s 8kA | CONFIRMED | withstands 38.89 kA; asked for 8.0 kA: survives |
| 2139 | CABLE CHECK | withstand al 185 0.2s 16kA | CONFIRMED | withstands 38.89 kA; asked for 16.0 kA: survives |
| 2140 | CABLE CHECK | withstand al 185 0.2s 25kA | CONFIRMED | withstands 38.89 kA; asked for 25.0 kA: survives |
| 2141 | CABLE CHECK | withstand al 185 1.0s 8kA | CONFIRMED | withstands 17.39 kA; asked for 8.0 kA: survives |
| 2142 | CABLE CHECK | withstand al 185 1.0s 16kA | CONFIRMED | withstands 17.39 kA; asked for 16.0 kA: survives |
| 2143 | CABLE CHECK | withstand al 185 1.0s 25kA | CONFIRMED | withstands 17.39 kA; asked for 25.0 kA: DOES NOT SURVIVE: a larger conductor or faster protection |
| 2144 | CABLE CHECK | withstand al 185 3.0s 8kA | CONFIRMED | withstands 10.04 kA; asked for 8.0 kA: survives |
| 2145 | CABLE CHECK | withstand al 185 3.0s 16kA | CONFIRMED | withstands 10.04 kA; asked for 16.0 kA: DOES NOT SURVIVE: a larger conductor or faster protection |
| 2146 | CABLE CHECK | withstand al 185 3.0s 25kA | CONFIRMED | withstands 10.04 kA; asked for 25.0 kA: DOES NOT SURVIVE: a larger conductor or faster protection |
| 2147 | CABLE CHECK | withstand al 300 0.2s 8kA | CONFIRMED | withstands 63.06 kA; asked for 8.0 kA: survives |
| 2148 | CABLE CHECK | withstand al 300 0.2s 16kA | CONFIRMED | withstands 63.06 kA; asked for 16.0 kA: survives |
| 2149 | CABLE CHECK | withstand al 300 0.2s 25kA | CONFIRMED | withstands 63.06 kA; asked for 25.0 kA: survives |
| 2150 | CABLE CHECK | withstand al 300 1.0s 8kA | CONFIRMED | withstands 28.20 kA; asked for 8.0 kA: survives |
| 2151 | CABLE CHECK | withstand al 300 1.0s 16kA | CONFIRMED | withstands 28.20 kA; asked for 16.0 kA: survives |
| 2152 | CABLE CHECK | withstand al 300 1.0s 25kA | CONFIRMED | withstands 28.20 kA; asked for 25.0 kA: survives |
| 2153 | CABLE CHECK | withstand al 300 3.0s 8kA | CONFIRMED | withstands 16.28 kA; asked for 8.0 kA: survives |
| 2154 | CABLE CHECK | withstand al 300 3.0s 16kA | CONFIRMED | withstands 16.28 kA; asked for 16.0 kA: survives |
| 2155 | CABLE CHECK | withstand al 300 3.0s 25kA | CONFIRMED | withstands 16.28 kA; asked for 25.0 kA: DOES NOT SURVIVE: a larger conductor or faster protection |
| 2156 | CABLE CHECK | withstand al 630 0.2s 8kA | CONFIRMED | withstands 132.42 kA; asked for 8.0 kA: survives |
| 2157 | CABLE CHECK | withstand al 630 0.2s 16kA | CONFIRMED | withstands 132.42 kA; asked for 16.0 kA: survives |
| 2158 | CABLE CHECK | withstand al 630 0.2s 25kA | CONFIRMED | withstands 132.42 kA; asked for 25.0 kA: survives |
| 2159 | CABLE CHECK | withstand al 630 1.0s 8kA | CONFIRMED | withstands 59.22 kA; asked for 8.0 kA: survives |
| 2160 | CABLE CHECK | withstand al 630 1.0s 16kA | CONFIRMED | withstands 59.22 kA; asked for 16.0 kA: survives |
| 2161 | CABLE CHECK | withstand al 630 1.0s 25kA | CONFIRMED | withstands 59.22 kA; asked for 25.0 kA: survives |
| 2162 | CABLE CHECK | withstand al 630 3.0s 8kA | CONFIRMED | withstands 34.19 kA; asked for 8.0 kA: survives |
| 2163 | CABLE CHECK | withstand al 630 3.0s 16kA | CONFIRMED | withstands 34.19 kA; asked for 16.0 kA: survives |
| 2164 | CABLE CHECK | withstand al 630 3.0s 25kA | CONFIRMED | withstands 34.19 kA; asked for 25.0 kA: survives |
| 2165 | CABLE CHECK | withstand cu 95 0.2s 8kA | CONFIRMED | withstands 30.38 kA; asked for 8.0 kA: survives |
| 2166 | CABLE CHECK | withstand cu 95 0.2s 16kA | CONFIRMED | withstands 30.38 kA; asked for 16.0 kA: survives |
| 2167 | CABLE CHECK | withstand cu 95 0.2s 25kA | CONFIRMED | withstands 30.38 kA; asked for 25.0 kA: survives |
| 2168 | CABLE CHECK | withstand cu 95 1.0s 8kA | CONFIRMED | withstands 13.59 kA; asked for 8.0 kA: survives |
| 2169 | CABLE CHECK | withstand cu 95 1.0s 16kA | CONFIRMED | withstands 13.59 kA; asked for 16.0 kA: DOES NOT SURVIVE: a larger conductor or faster protection |
| 2170 | CABLE CHECK | withstand cu 95 1.0s 25kA | CONFIRMED | withstands 13.59 kA; asked for 25.0 kA: DOES NOT SURVIVE: a larger conductor or faster protection |
| 2171 | CABLE CHECK | withstand cu 95 3.0s 8kA | CONFIRMED | withstands 7.84 kA; asked for 8.0 kA: DOES NOT SURVIVE: a larger conductor or faster protection |
| 2172 | CABLE CHECK | withstand cu 95 3.0s 16kA | CONFIRMED | withstands 7.84 kA; asked for 16.0 kA: DOES NOT SURVIVE: a larger conductor or faster protection |
| 2173 | CABLE CHECK | withstand cu 95 3.0s 25kA | CONFIRMED | withstands 7.84 kA; asked for 25.0 kA: DOES NOT SURVIVE: a larger conductor or faster protection |
| 2174 | CABLE CHECK | withstand cu 185 0.2s 8kA | CONFIRMED | withstands 59.16 kA; asked for 8.0 kA: survives |
| 2175 | CABLE CHECK | withstand cu 185 0.2s 16kA | CONFIRMED | withstands 59.16 kA; asked for 16.0 kA: survives |
| 2176 | CABLE CHECK | withstand cu 185 0.2s 25kA | CONFIRMED | withstands 59.16 kA; asked for 25.0 kA: survives |
| 2177 | CABLE CHECK | withstand cu 185 1.0s 8kA | CONFIRMED | withstands 26.45 kA; asked for 8.0 kA: survives |
| 2178 | CABLE CHECK | withstand cu 185 1.0s 16kA | CONFIRMED | withstands 26.45 kA; asked for 16.0 kA: survives |
| 2179 | CABLE CHECK | withstand cu 185 1.0s 25kA | CONFIRMED | withstands 26.45 kA; asked for 25.0 kA: survives |
| 2180 | CABLE CHECK | withstand cu 185 3.0s 8kA | CONFIRMED | withstands 15.27 kA; asked for 8.0 kA: survives |
| 2181 | CABLE CHECK | withstand cu 185 3.0s 16kA | CONFIRMED | withstands 15.27 kA; asked for 16.0 kA: DOES NOT SURVIVE: a larger conductor or faster protection |
| 2182 | CABLE CHECK | withstand cu 185 3.0s 25kA | CONFIRMED | withstands 15.27 kA; asked for 25.0 kA: DOES NOT SURVIVE: a larger conductor or faster protection |
| 2183 | CABLE CHECK | withstand cu 300 0.2s 8kA | CONFIRMED | withstands 95.93 kA; asked for 8.0 kA: survives |
| 2184 | CABLE CHECK | withstand cu 300 0.2s 16kA | CONFIRMED | withstands 95.93 kA; asked for 16.0 kA: survives |
| 2185 | CABLE CHECK | withstand cu 300 0.2s 25kA | CONFIRMED | withstands 95.93 kA; asked for 25.0 kA: survives |
| 2186 | CABLE CHECK | withstand cu 300 1.0s 8kA | CONFIRMED | withstands 42.90 kA; asked for 8.0 kA: survives |
| 2187 | CABLE CHECK | withstand cu 300 1.0s 16kA | CONFIRMED | withstands 42.90 kA; asked for 16.0 kA: survives |
| 2188 | CABLE CHECK | withstand cu 300 1.0s 25kA | CONFIRMED | withstands 42.90 kA; asked for 25.0 kA: survives |
| 2189 | CABLE CHECK | withstand cu 300 3.0s 8kA | CONFIRMED | withstands 24.77 kA; asked for 8.0 kA: survives |
| 2190 | CABLE CHECK | withstand cu 300 3.0s 16kA | CONFIRMED | withstands 24.77 kA; asked for 16.0 kA: survives |
| 2191 | CABLE CHECK | withstand cu 300 3.0s 25kA | CONFIRMED | withstands 24.77 kA; asked for 25.0 kA: DOES NOT SURVIVE: a larger conductor or faster protection |
| 2192 | CABLE CHECK | withstand cu 630 0.2s 8kA | CONFIRMED | withstands 201.45 kA; asked for 8.0 kA: survives |
| 2193 | CABLE CHECK | withstand cu 630 0.2s 16kA | CONFIRMED | withstands 201.45 kA; asked for 16.0 kA: survives |
| 2194 | CABLE CHECK | withstand cu 630 0.2s 25kA | CONFIRMED | withstands 201.45 kA; asked for 25.0 kA: survives |
| 2195 | CABLE CHECK | withstand cu 630 1.0s 8kA | CONFIRMED | withstands 90.09 kA; asked for 8.0 kA: survives |
| 2196 | CABLE CHECK | withstand cu 630 1.0s 16kA | CONFIRMED | withstands 90.09 kA; asked for 16.0 kA: survives |
| 2197 | CABLE CHECK | withstand cu 630 1.0s 25kA | CONFIRMED | withstands 90.09 kA; asked for 25.0 kA: survives |
| 2198 | CABLE CHECK | withstand cu 630 3.0s 8kA | CONFIRMED | withstands 52.01 kA; asked for 8.0 kA: survives |
| 2199 | CABLE CHECK | withstand cu 630 3.0s 16kA | CONFIRMED | withstands 52.01 kA; asked for 16.0 kA: survives |
| 2200 | CABLE CHECK | withstand cu 630 3.0s 25kA | CONFIRMED | withstands 52.01 kA; asked for 25.0 kA: survives |
| 2201 | CABLE CHECK | run al 95 150A 200m 11kV | CONFIRMED | drop 0.20%, loaded to 85% of its derated rating; within 15 per cent of its derated rating: commission a buried cable thermal study |
| 2202 | CABLE CHECK | run al 95 150A 200m 33kV | CONFIRMED | drop 0.07%, loaded to 97% of its derated rating; within 15 per cent of its derated rating: commission a buried cable thermal study |
| 2203 | CABLE CHECK | run al 95 150A 800m 11kV | CONFIRMED | drop 0.78%, loaded to 85% of its derated rating; within 15 per cent of its derated rating: commission a buried cable thermal study |
| 2204 | CABLE CHECK | run al 95 150A 800m 33kV | CONFIRMED | drop 0.26%, loaded to 97% of its derated rating; within 15 per cent of its derated rating: commission a buried cable thermal study |
| 2205 | CABLE CHECK | run al 95 150A 2500m 11kV | CONFIRMED | drop 2.45%, loaded to 85% of its derated rating; within 15 per cent of its derated rating: commission a buried cable thermal study; voltage drop 2.45% is over 1 |
| 2206 | CABLE CHECK | run al 95 150A 2500m 33kV | CONFIRMED | drop 0.82%, loaded to 97% of its derated rating; within 15 per cent of its derated rating: commission a buried cable thermal study |
| 2207 | CABLE CHECK | run al 95 300A 200m 11kV | CONFIRMED | drop 0.39%, loaded to 170% of its derated rating; over its derated rating |
| 2208 | CABLE CHECK | run al 95 300A 200m 33kV | CONFIRMED | drop 0.13%, loaded to 195% of its derated rating; over its derated rating |
| 2209 | CABLE CHECK | run al 95 300A 800m 11kV | CONFIRMED | drop 1.57%, loaded to 170% of its derated rating; over its derated rating; voltage drop 1.57% is over 1.5% |
| 2210 | CABLE CHECK | run al 95 300A 800m 33kV | CONFIRMED | drop 0.52%, loaded to 195% of its derated rating; over its derated rating |
| 2211 | CABLE CHECK | run al 95 300A 2500m 11kV | CONFIRMED | drop 4.90%, loaded to 170% of its derated rating; over its derated rating; voltage drop 4.90% is over 1.5% |
| 2212 | CABLE CHECK | run al 95 300A 2500m 33kV | CONFIRMED | drop 1.63%, loaded to 195% of its derated rating; over its derated rating; voltage drop 1.63% is over 1.5% |
| 2213 | CABLE CHECK | run al 95 450A 200m 11kV | CONFIRMED | drop 0.59%, loaded to 256% of its derated rating; over its derated rating |
| 2214 | CABLE CHECK | run al 95 450A 200m 33kV | CONFIRMED | drop 0.20%, loaded to 292% of its derated rating; over its derated rating |
| 2215 | CABLE CHECK | run al 95 450A 800m 11kV | CONFIRMED | drop 2.35%, loaded to 256% of its derated rating; over its derated rating; voltage drop 2.35% is over 1.5% |
| 2216 | CABLE CHECK | run al 95 450A 800m 33kV | CONFIRMED | drop 0.78%, loaded to 292% of its derated rating; over its derated rating |
| 2217 | CABLE CHECK | run al 95 450A 2500m 11kV | CONFIRMED | drop 7.35%, loaded to 256% of its derated rating; over its derated rating; voltage drop 7.35% is over 1.5% |
| 2218 | CABLE CHECK | run al 95 450A 2500m 33kV | CONFIRMED | drop 2.45%, loaded to 292% of its derated rating; over its derated rating; voltage drop 2.45% is over 1.5% |
| 2219 | CABLE CHECK | run al 185 150A 200m 11kV | CONFIRMED | drop 0.11%, loaded to 59% of its derated rating; inside both limits |
| 2220 | CABLE CHECK | run al 185 150A 200m 33kV | CONFIRMED | drop 0.04%, loaded to 67% of its derated rating; inside both limits |
| 2221 | CABLE CHECK | run al 185 150A 800m 11kV | CONFIRMED | drop 0.42%, loaded to 59% of its derated rating; inside both limits |
| 2222 | CABLE CHECK | run al 185 150A 800m 33kV | CONFIRMED | drop 0.14%, loaded to 67% of its derated rating; inside both limits |
| 2223 | CABLE CHECK | run al 185 150A 2500m 11kV | CONFIRMED | drop 1.33%, loaded to 59% of its derated rating; inside both limits |
| 2224 | CABLE CHECK | run al 185 150A 2500m 33kV | CONFIRMED | drop 0.44%, loaded to 67% of its derated rating; inside both limits |
| 2225 | CABLE CHECK | run al 185 300A 200m 11kV | CONFIRMED | drop 0.21%, loaded to 117% of its derated rating; over its derated rating |
| 2226 | CABLE CHECK | run al 185 300A 200m 33kV | CONFIRMED | drop 0.07%, loaded to 134% of its derated rating; over its derated rating |
| 2227 | CABLE CHECK | run al 185 300A 800m 11kV | CONFIRMED | drop 0.85%, loaded to 117% of its derated rating; over its derated rating |
| 2228 | CABLE CHECK | run al 185 300A 800m 33kV | CONFIRMED | drop 0.28%, loaded to 134% of its derated rating; over its derated rating |
| 2229 | CABLE CHECK | run al 185 300A 2500m 11kV | CONFIRMED | drop 2.65%, loaded to 117% of its derated rating; over its derated rating; voltage drop 2.65% is over 1.5% |
| 2230 | CABLE CHECK | run al 185 300A 2500m 33kV | CONFIRMED | drop 0.88%, loaded to 134% of its derated rating; over its derated rating |
| 2231 | CABLE CHECK | run al 185 450A 200m 11kV | CONFIRMED | drop 0.32%, loaded to 176% of its derated rating; over its derated rating |
| 2232 | CABLE CHECK | run al 185 450A 200m 33kV | CONFIRMED | drop 0.11%, loaded to 201% of its derated rating; over its derated rating |
| 2233 | CABLE CHECK | run al 185 450A 800m 11kV | CONFIRMED | drop 1.27%, loaded to 176% of its derated rating; over its derated rating |
| 2234 | CABLE CHECK | run al 185 450A 800m 33kV | CONFIRMED | drop 0.42%, loaded to 201% of its derated rating; over its derated rating |
| 2235 | CABLE CHECK | run al 185 450A 2500m 11kV | CONFIRMED | drop 3.98%, loaded to 176% of its derated rating; over its derated rating; voltage drop 3.98% is over 1.5% |
| 2236 | CABLE CHECK | run al 185 450A 2500m 33kV | CONFIRMED | drop 1.33%, loaded to 201% of its derated rating; over its derated rating |
| 2237 | CABLE CHECK | run al 300 150A 200m 11kV | CONFIRMED | drop 0.07%, loaded to 45% of its derated rating; inside both limits |
| 2238 | CABLE CHECK | run al 300 150A 200m 33kV | CONFIRMED | drop 0.02%, loaded to 51% of its derated rating; inside both limits |
| 2239 | CABLE CHECK | run al 300 150A 800m 11kV | CONFIRMED | drop 0.28%, loaded to 45% of its derated rating; inside both limits |
| 2240 | CABLE CHECK | run al 300 150A 800m 33kV | CONFIRMED | drop 0.09%, loaded to 51% of its derated rating; inside both limits |
| 2241 | CABLE CHECK | run al 300 150A 2500m 11kV | CONFIRMED | drop 0.87%, loaded to 45% of its derated rating; inside both limits |
| 2242 | CABLE CHECK | run al 300 150A 2500m 33kV | CONFIRMED | drop 0.29%, loaded to 51% of its derated rating; inside both limits |
| 2243 | CABLE CHECK | run al 300 300A 200m 11kV | CONFIRMED | drop 0.14%, loaded to 89% of its derated rating; within 15 per cent of its derated rating: commission a buried cable thermal study |
| 2244 | CABLE CHECK | run al 300 300A 200m 33kV | CONFIRMED | drop 0.05%, loaded to 102% of its derated rating; over its derated rating |
| 2245 | CABLE CHECK | run al 300 300A 800m 11kV | CONFIRMED | drop 0.55%, loaded to 89% of its derated rating; within 15 per cent of its derated rating: commission a buried cable thermal study |
| 2246 | CABLE CHECK | run al 300 300A 800m 33kV | CONFIRMED | drop 0.18%, loaded to 102% of its derated rating; over its derated rating |
| 2247 | CABLE CHECK | run al 300 300A 2500m 11kV | CONFIRMED | drop 1.73%, loaded to 89% of its derated rating; within 15 per cent of its derated rating: commission a buried cable thermal study; voltage drop 1.73% is over 1 |
| 2248 | CABLE CHECK | run al 300 300A 2500m 33kV | CONFIRMED | drop 0.58%, loaded to 102% of its derated rating; over its derated rating |
| 2249 | CABLE CHECK | run al 300 450A 200m 11kV | CONFIRMED | drop 0.21%, loaded to 134% of its derated rating; over its derated rating |
| 2250 | CABLE CHECK | run al 300 450A 200m 33kV | CONFIRMED | drop 0.07%, loaded to 153% of its derated rating; over its derated rating |
| 2251 | CABLE CHECK | run al 300 450A 800m 11kV | CONFIRMED | drop 0.83%, loaded to 134% of its derated rating; over its derated rating |
| 2252 | CABLE CHECK | run al 300 450A 800m 33kV | CONFIRMED | drop 0.28%, loaded to 153% of its derated rating; over its derated rating |
| 2253 | CABLE CHECK | run al 300 450A 2500m 11kV | CONFIRMED | drop 2.60%, loaded to 134% of its derated rating; over its derated rating; voltage drop 2.60% is over 1.5% |
| 2254 | CABLE CHECK | run al 300 450A 2500m 33kV | CONFIRMED | drop 0.87%, loaded to 153% of its derated rating; over its derated rating |
| 2255 | CABLE CHECK | run al 630 150A 200m 11kV | CONFIRMED | drop 0.04%, loaded to 30% of its derated rating; inside both limits |
| 2256 | CABLE CHECK | run al 630 150A 200m 33kV | CONFIRMED | drop 0.01%, loaded to 35% of its derated rating; inside both limits |
| 2257 | CABLE CHECK | run al 630 150A 800m 11kV | CONFIRMED | drop 0.16%, loaded to 30% of its derated rating; inside both limits |
| 2258 | CABLE CHECK | run al 630 150A 800m 33kV | CONFIRMED | drop 0.05%, loaded to 35% of its derated rating; inside both limits |
| 2259 | CABLE CHECK | run al 630 150A 2500m 11kV | CONFIRMED | drop 0.48%, loaded to 30% of its derated rating; inside both limits |
| 2260 | CABLE CHECK | run al 630 150A 2500m 33kV | CONFIRMED | drop 0.16%, loaded to 35% of its derated rating; inside both limits |
| 2261 | CABLE CHECK | run al 630 300A 200m 11kV | CONFIRMED | drop 0.08%, loaded to 61% of its derated rating; inside both limits |
| 2262 | CABLE CHECK | run al 630 300A 200m 33kV | CONFIRMED | drop 0.03%, loaded to 70% of its derated rating; inside both limits |
| 2263 | CABLE CHECK | run al 630 300A 800m 11kV | CONFIRMED | drop 0.31%, loaded to 61% of its derated rating; inside both limits |
| 2264 | CABLE CHECK | run al 630 300A 800m 33kV | CONFIRMED | drop 0.10%, loaded to 70% of its derated rating; inside both limits |
| 2265 | CABLE CHECK | run al 630 300A 2500m 11kV | CONFIRMED | drop 0.97%, loaded to 61% of its derated rating; inside both limits |
| 2266 | CABLE CHECK | run al 630 300A 2500m 33kV | CONFIRMED | drop 0.32%, loaded to 70% of its derated rating; inside both limits |
| 2267 | CABLE CHECK | run al 630 450A 200m 11kV | CONFIRMED | drop 0.12%, loaded to 91% of its derated rating; within 15 per cent of its derated rating: commission a buried cable thermal study |
| 2268 | CABLE CHECK | run al 630 450A 200m 33kV | CONFIRMED | drop 0.04%, loaded to 105% of its derated rating; over its derated rating |
| 2269 | CABLE CHECK | run al 630 450A 800m 11kV | CONFIRMED | drop 0.47%, loaded to 91% of its derated rating; within 15 per cent of its derated rating: commission a buried cable thermal study |
| 2270 | CABLE CHECK | run al 630 450A 800m 33kV | CONFIRMED | drop 0.16%, loaded to 105% of its derated rating; over its derated rating |
| 2271 | CABLE CHECK | run al 630 450A 2500m 11kV | CONFIRMED | drop 1.45%, loaded to 91% of its derated rating; within 15 per cent of its derated rating: commission a buried cable thermal study |
| 2272 | CABLE CHECK | run al 630 450A 2500m 33kV | CONFIRMED | drop 0.48%, loaded to 105% of its derated rating; over its derated rating |
| 2273 | CABLE CHECK | run cu 95 150A 200m 11kV | CONFIRMED | drop 0.12%, loaded to 66% of its derated rating; inside both limits |
| 2274 | CABLE CHECK | run cu 95 150A 200m 33kV | CONFIRMED | drop 0.04%, loaded to 76% of its derated rating; inside both limits |
| 2275 | CABLE CHECK | run cu 95 150A 800m 11kV | CONFIRMED | drop 0.49%, loaded to 66% of its derated rating; inside both limits |
| 2276 | CABLE CHECK | run cu 95 150A 800m 33kV | CONFIRMED | drop 0.16%, loaded to 76% of its derated rating; inside both limits |
| 2277 | CABLE CHECK | run cu 95 150A 2500m 11kV | CONFIRMED | drop 1.53%, loaded to 66% of its derated rating; voltage drop 1.53% is over 1.5% |
| 2278 | CABLE CHECK | run cu 95 150A 2500m 33kV | CONFIRMED | drop 0.51%, loaded to 76% of its derated rating; inside both limits |
| 2279 | CABLE CHECK | run cu 95 300A 200m 11kV | CONFIRMED | drop 0.24%, loaded to 133% of its derated rating; over its derated rating |
| 2280 | CABLE CHECK | run cu 95 300A 200m 33kV | CONFIRMED | drop 0.08%, loaded to 152% of its derated rating; over its derated rating |
| 2281 | CABLE CHECK | run cu 95 300A 800m 11kV | CONFIRMED | drop 0.98%, loaded to 133% of its derated rating; over its derated rating |
| 2282 | CABLE CHECK | run cu 95 300A 800m 33kV | CONFIRMED | drop 0.33%, loaded to 152% of its derated rating; over its derated rating |
| 2283 | CABLE CHECK | run cu 95 300A 2500m 11kV | CONFIRMED | drop 3.06%, loaded to 133% of its derated rating; over its derated rating; voltage drop 3.06% is over 1.5% |
| 2284 | CABLE CHECK | run cu 95 300A 2500m 33kV | CONFIRMED | drop 1.02%, loaded to 152% of its derated rating; over its derated rating |
| 2285 | CABLE CHECK | run cu 95 450A 200m 11kV | CONFIRMED | drop 0.37%, loaded to 199% of its derated rating; over its derated rating |
| 2286 | CABLE CHECK | run cu 95 450A 200m 33kV | CONFIRMED | drop 0.12%, loaded to 228% of its derated rating; over its derated rating |
| 2287 | CABLE CHECK | run cu 95 450A 800m 11kV | CONFIRMED | drop 1.47%, loaded to 199% of its derated rating; over its derated rating |
| 2288 | CABLE CHECK | run cu 95 450A 800m 33kV | CONFIRMED | drop 0.49%, loaded to 228% of its derated rating; over its derated rating |
| 2289 | CABLE CHECK | run cu 95 450A 2500m 11kV | CONFIRMED | drop 4.58%, loaded to 199% of its derated rating; over its derated rating; voltage drop 4.58% is over 1.5% |
| 2290 | CABLE CHECK | run cu 95 450A 2500m 33kV | CONFIRMED | drop 1.53%, loaded to 228% of its derated rating; over its derated rating; voltage drop 1.53% is over 1.5% |
| 2291 | CABLE CHECK | run cu 185 150A 200m 11kV | CONFIRMED | drop 0.07%, loaded to 46% of its derated rating; inside both limits |
| 2292 | CABLE CHECK | run cu 185 150A 200m 33kV | CONFIRMED | drop 0.02%, loaded to 52% of its derated rating; inside both limits |
| 2293 | CABLE CHECK | run cu 185 150A 800m 11kV | CONFIRMED | drop 0.27%, loaded to 46% of its derated rating; inside both limits |
| 2294 | CABLE CHECK | run cu 185 150A 800m 33kV | CONFIRMED | drop 0.09%, loaded to 52% of its derated rating; inside both limits |
| 2295 | CABLE CHECK | run cu 185 150A 2500m 11kV | CONFIRMED | drop 0.86%, loaded to 46% of its derated rating; inside both limits |
| 2296 | CABLE CHECK | run cu 185 150A 2500m 33kV | CONFIRMED | drop 0.29%, loaded to 52% of its derated rating; inside both limits |
| 2297 | CABLE CHECK | run cu 185 300A 200m 11kV | CONFIRMED | drop 0.14%, loaded to 91% of its derated rating; within 15 per cent of its derated rating: commission a buried cable thermal study |
| 2298 | CABLE CHECK | run cu 185 300A 200m 33kV | CONFIRMED | drop 0.05%, loaded to 105% of its derated rating; over its derated rating |
| 2299 | CABLE CHECK | run cu 185 300A 800m 11kV | CONFIRMED | drop 0.55%, loaded to 91% of its derated rating; within 15 per cent of its derated rating: commission a buried cable thermal study |
| 2300 | CABLE CHECK | run cu 185 300A 800m 33kV | CONFIRMED | drop 0.18%, loaded to 105% of its derated rating; over its derated rating |
| 2301 | CABLE CHECK | run cu 185 300A 2500m 11kV | CONFIRMED | drop 1.71%, loaded to 91% of its derated rating; within 15 per cent of its derated rating: commission a buried cable thermal study; voltage drop 1.71% is over 1 |
| 2302 | CABLE CHECK | run cu 185 300A 2500m 33kV | CONFIRMED | drop 0.57%, loaded to 105% of its derated rating; over its derated rating |
| 2303 | CABLE CHECK | run cu 185 450A 200m 11kV | CONFIRMED | drop 0.21%, loaded to 137% of its derated rating; over its derated rating |
| 2304 | CABLE CHECK | run cu 185 450A 200m 33kV | CONFIRMED | drop 0.07%, loaded to 157% of its derated rating; over its derated rating |
| 2305 | CABLE CHECK | run cu 185 450A 800m 11kV | CONFIRMED | drop 0.82%, loaded to 137% of its derated rating; over its derated rating |
| 2306 | CABLE CHECK | run cu 185 450A 800m 33kV | CONFIRMED | drop 0.27%, loaded to 157% of its derated rating; over its derated rating |
| 2307 | CABLE CHECK | run cu 185 450A 2500m 11kV | CONFIRMED | drop 2.57%, loaded to 137% of its derated rating; over its derated rating; voltage drop 2.57% is over 1.5% |
| 2308 | CABLE CHECK | run cu 185 450A 2500m 33kV | CONFIRMED | drop 0.86%, loaded to 157% of its derated rating; over its derated rating |
| 2309 | CABLE CHECK | run cu 300 150A 200m 11kV | CONFIRMED | drop 0.05%, loaded to 35% of its derated rating; inside both limits |
| 2310 | CABLE CHECK | run cu 300 150A 200m 33kV | CONFIRMED | drop 0.02%, loaded to 40% of its derated rating; inside both limits |
| 2311 | CABLE CHECK | run cu 300 150A 800m 11kV | CONFIRMED | drop 0.18%, loaded to 35% of its derated rating; inside both limits |
| 2312 | CABLE CHECK | run cu 300 150A 800m 33kV | CONFIRMED | drop 0.06%, loaded to 40% of its derated rating; inside both limits |
| 2313 | CABLE CHECK | run cu 300 150A 2500m 11kV | CONFIRMED | drop 0.58%, loaded to 35% of its derated rating; inside both limits |
| 2314 | CABLE CHECK | run cu 300 150A 2500m 33kV | CONFIRMED | drop 0.19%, loaded to 40% of its derated rating; inside both limits |
| 2315 | CABLE CHECK | run cu 300 300A 200m 11kV | CONFIRMED | drop 0.09%, loaded to 70% of its derated rating; inside both limits |
| 2316 | CABLE CHECK | run cu 300 300A 200m 33kV | CONFIRMED | drop 0.03%, loaded to 80% of its derated rating; inside both limits |
| 2317 | CABLE CHECK | run cu 300 300A 800m 11kV | CONFIRMED | drop 0.37%, loaded to 70% of its derated rating; inside both limits |
| 2318 | CABLE CHECK | run cu 300 300A 800m 33kV | CONFIRMED | drop 0.12%, loaded to 80% of its derated rating; inside both limits |
| 2319 | CABLE CHECK | run cu 300 300A 2500m 11kV | CONFIRMED | drop 1.15%, loaded to 70% of its derated rating; inside both limits |
| 2320 | CABLE CHECK | run cu 300 300A 2500m 33kV | CONFIRMED | drop 0.38%, loaded to 80% of its derated rating; inside both limits |
| 2321 | CABLE CHECK | run cu 300 450A 200m 11kV | CONFIRMED | drop 0.14%, loaded to 105% of its derated rating; over its derated rating |
| 2322 | CABLE CHECK | run cu 300 450A 200m 33kV | CONFIRMED | drop 0.05%, loaded to 119% of its derated rating; over its derated rating |
| 2323 | CABLE CHECK | run cu 300 450A 800m 11kV | CONFIRMED | drop 0.55%, loaded to 105% of its derated rating; over its derated rating |
| 2324 | CABLE CHECK | run cu 300 450A 800m 33kV | CONFIRMED | drop 0.18%, loaded to 119% of its derated rating; over its derated rating |
| 2325 | CABLE CHECK | run cu 300 450A 2500m 11kV | CONFIRMED | drop 1.73%, loaded to 105% of its derated rating; over its derated rating; voltage drop 1.73% is over 1.5% |
| 2326 | CABLE CHECK | run cu 300 450A 2500m 33kV | CONFIRMED | drop 0.58%, loaded to 119% of its derated rating; over its derated rating |
| 2327 | CABLE CHECK | run cu 630 150A 200m 11kV | CONFIRMED | drop 0.03%, loaded to 24% of its derated rating; inside both limits |
| 2328 | CABLE CHECK | run cu 630 150A 200m 33kV | CONFIRMED | drop 0.01%, loaded to 27% of its derated rating; inside both limits |
| 2329 | CABLE CHECK | run cu 630 150A 800m 11kV | CONFIRMED | drop 0.11%, loaded to 24% of its derated rating; inside both limits |
| 2330 | CABLE CHECK | run cu 630 150A 800m 33kV | CONFIRMED | drop 0.04%, loaded to 27% of its derated rating; inside both limits |
| 2331 | CABLE CHECK | run cu 630 150A 2500m 11kV | CONFIRMED | drop 0.35%, loaded to 24% of its derated rating; inside both limits |
| 2332 | CABLE CHECK | run cu 630 150A 2500m 33kV | CONFIRMED | drop 0.12%, loaded to 27% of its derated rating; inside both limits |
| 2333 | CABLE CHECK | run cu 630 300A 200m 11kV | CONFIRMED | drop 0.06%, loaded to 48% of its derated rating; inside both limits |
| 2334 | CABLE CHECK | run cu 630 300A 200m 33kV | CONFIRMED | drop 0.02%, loaded to 54% of its derated rating; inside both limits |
| 2335 | CABLE CHECK | run cu 630 300A 800m 11kV | CONFIRMED | drop 0.22%, loaded to 48% of its derated rating; inside both limits |
| 2336 | CABLE CHECK | run cu 630 300A 800m 33kV | CONFIRMED | drop 0.07%, loaded to 54% of its derated rating; inside both limits |
| 2337 | CABLE CHECK | run cu 630 300A 2500m 11kV | CONFIRMED | drop 0.70%, loaded to 48% of its derated rating; inside both limits |
| 2338 | CABLE CHECK | run cu 630 300A 2500m 33kV | CONFIRMED | drop 0.23%, loaded to 54% of its derated rating; inside both limits |
| 2339 | CABLE CHECK | run cu 630 450A 200m 11kV | CONFIRMED | drop 0.08%, loaded to 71% of its derated rating; inside both limits |
| 2340 | CABLE CHECK | run cu 630 450A 200m 33kV | CONFIRMED | drop 0.03%, loaded to 82% of its derated rating; inside both limits |
| 2341 | CABLE CHECK | run cu 630 450A 800m 11kV | CONFIRMED | drop 0.34%, loaded to 71% of its derated rating; inside both limits |
| 2342 | CABLE CHECK | run cu 630 450A 800m 33kV | CONFIRMED | drop 0.11%, loaded to 82% of its derated rating; inside both limits |
| 2343 | CABLE CHECK | run cu 630 450A 2500m 11kV | CONFIRMED | drop 1.05%, loaded to 71% of its derated rating; inside both limits |
| 2344 | CABLE CHECK | run cu 630 450A 2500m 33kV | CONFIRMED | drop 0.35%, loaded to 82% of its derated rating; inside both limits |
| 2345 | SITE ENERGY | the known answers | CONFIRMED | both durations hold. 62 MW is the average if the 271 GWh falls in a 12 hour day; spread over all 8,760 hours the average is 30.9 MW. A model must say which it u |
| 2346 | SITE ENERGY | 0 MWp, 0 MWh | CONFIRMED | makes 0% of its own electricity; still pulls up to 44 MW from the grid; throws away 0.0 GWh of solar |
| 2347 | SITE ENERGY | 0 MWp, 150 MWh | CONFIRMED | makes 0% of its own electricity; still pulls up to 44 MW from the grid; throws away 0.0 GWh of solar |
| 2348 | SITE ENERGY | 0 MWp, 300 MWh | CONFIRMED | makes 0% of its own electricity; still pulls up to 44 MW from the grid; throws away 0.0 GWh of solar |
| 2349 | SITE ENERGY | 0 MWp, 600 MWh | CONFIRMED | makes 0% of its own electricity; still pulls up to 44 MW from the grid; throws away 0.0 GWh of solar |
| 2350 | SITE ENERGY | 0 MWp, 1200 MWh | CONFIRMED | makes 0% of its own electricity; still pulls up to 44 MW from the grid; throws away 0.0 GWh of solar |
| 2351 | SITE ENERGY | 50 MWp, 0 MWh | CONFIRMED | makes 17% of its own electricity; still pulls up to 42 MW from the grid; throws away 0.3 GWh of solar |
| 2352 | SITE ENERGY | 50 MWp, 150 MWh | CONFIRMED | makes 17% of its own electricity; still pulls up to 42 MW from the grid; throws away 0.0 GWh of solar |
| 2353 | SITE ENERGY | 50 MWp, 300 MWh | CONFIRMED | makes 17% of its own electricity; still pulls up to 42 MW from the grid; throws away 0.0 GWh of solar |
| 2354 | SITE ENERGY | 50 MWp, 600 MWh | CONFIRMED | makes 17% of its own electricity; still pulls up to 42 MW from the grid; throws away 0.0 GWh of solar |
| 2355 | SITE ENERGY | 50 MWp, 1200 MWh | CONFIRMED | makes 17% of its own electricity; still pulls up to 42 MW from the grid; throws away 0.0 GWh of solar |
| 2356 | SITE ENERGY | 100 MWp, 0 MWh | CONFIRMED | makes 28% of its own electricity; still pulls up to 41 MW from the grid; throws away 13.7 GWh of solar |
| 2357 | SITE ENERGY | 100 MWp, 150 MWh | CONFIRMED | makes 32% of its own electricity; still pulls up to 41 MW from the grid; throws away 2.1 GWh of solar |
| 2358 | SITE ENERGY | 100 MWp, 300 MWh | CONFIRMED | makes 33% of its own electricity; still pulls up to 41 MW from the grid; throws away 0.0 GWh of solar |
| 2359 | SITE ENERGY | 100 MWp, 600 MWh | CONFIRMED | makes 33% of its own electricity; still pulls up to 41 MW from the grid; throws away 0.0 GWh of solar |
| 2360 | SITE ENERGY | 100 MWp, 1200 MWh | CONFIRMED | makes 33% of its own electricity; still pulls up to 41 MW from the grid; throws away 0.0 GWh of solar |
| 2361 | SITE ENERGY | 150 MWp, 0 MWh | CONFIRMED | makes 35% of its own electricity; still pulls up to 40 MW from the grid; throws away 40.8 GWh of solar |
| 2362 | SITE ENERGY | 150 MWp, 150 MWh | CONFIRMED | makes 43% of its own electricity; still pulls up to 40 MW from the grid; throws away 16.6 GWh of solar |
| 2363 | SITE ENERGY | 150 MWp, 300 MWh | CONFIRMED | makes 47% of its own electricity; still pulls up to 40 MW from the grid; throws away 4.7 GWh of solar |
| 2364 | SITE ENERGY | 150 MWp, 600 MWh | CONFIRMED | makes 48% of its own electricity; still pulls up to 40 MW from the grid; throws away 0.0 GWh of solar |
| 2365 | SITE ENERGY | 150 MWp, 1200 MWh | CONFIRMED | makes 48% of its own electricity; still pulls up to 40 MW from the grid; throws away 0.0 GWh of solar |
| 2366 | SITE ENERGY | 200 MWp, 0 MWh | CONFIRMED | makes 39% of its own electricity; still pulls up to 39 MW from the grid; throws away 74.3 GWh of solar |
| 2367 | SITE ENERGY | 200 MWp, 150 MWh | CONFIRMED | makes 49% of its own electricity; still pulls up to 39 MW from the grid; throws away 43.2 GWh of solar |
| 2368 | SITE ENERGY | 200 MWp, 300 MWh | CONFIRMED | makes 57% of its own electricity; still pulls up to 39 MW from the grid; throws away 20.9 GWh of solar |
| 2369 | SITE ENERGY | 200 MWp, 600 MWh | CONFIRMED | makes 60% of its own electricity; still pulls up to 39 MW from the grid; throws away 11.7 GWh of solar |
| 2370 | SITE ENERGY | 200 MWp, 1200 MWh | CONFIRMED | makes 60% of its own electricity; still pulls up to 39 MW from the grid; throws away 11.1 GWh of solar |
| 2371 | SITE ENERGY | 300 MWp, 0 MWh | CONFIRMED | makes 44% of its own electricity; still pulls up to 37 MW from the grid; throws away 150.2 GWh of solar |
| 2372 | SITE ENERGY | 300 MWp, 150 MWh | CONFIRMED | makes 57% of its own electricity; still pulls up to 37 MW from the grid; throws away 112.2 GWh of solar |
| 2373 | SITE ENERGY | 300 MWp, 300 MWh | CONFIRMED | makes 68% of its own electricity; still pulls up to 37 MW from the grid; throws away 79.9 GWh of solar |
| 2374 | SITE ENERGY | 300 MWp, 600 MWh | CONFIRMED | makes 71% of its own electricity; still pulls up to 37 MW from the grid; throws away 70.0 GWh of solar |
| 2375 | SITE ENERGY | 300 MWp, 1200 MWh | CONFIRMED | makes 71% of its own electricity; still pulls up to 37 MW from the grid; throws away 69.3 GWh of solar |
| 2376 | DC TRACTION | the known answers | CONFIRMED | 50 to 100 GWh a year is 5 to 10% of ALL traction energy (1003 GWh): it is the prize if every unit came in on the direct current side. On 80 GWh of solar the sam |
| 2377 | DC TRACTION | routes inv 0.97 rect 0.95 dc 0.97 | CONFIRMED | 91.2% arrives by the usual route, 97.0% by the direct route: 5.8% of the SOLAR is saved |
| 2378 | DC TRACTION | routes inv 0.97 rect 0.95 dc 0.985 | CONFIRMED | 91.2% arrives by the usual route, 98.5% by the direct route: 7.3% of the SOLAR is saved |
| 2379 | DC TRACTION | routes inv 0.97 rect 0.97 dc 0.97 | CONFIRMED | 93.1% arrives by the usual route, 97.0% by the direct route: 3.9% of the SOLAR is saved |
| 2380 | DC TRACTION | routes inv 0.97 rect 0.97 dc 0.985 | CONFIRMED | 93.1% arrives by the usual route, 98.5% by the direct route: 5.4% of the SOLAR is saved |
| 2381 | DC TRACTION | routes inv 0.98 rect 0.95 dc 0.97 | CONFIRMED | 92.2% arrives by the usual route, 97.0% by the direct route: 4.8% of the SOLAR is saved |
| 2382 | DC TRACTION | routes inv 0.98 rect 0.95 dc 0.985 | CONFIRMED | 92.2% arrives by the usual route, 98.5% by the direct route: 6.3% of the SOLAR is saved |
| 2383 | DC TRACTION | routes inv 0.98 rect 0.97 dc 0.97 | CONFIRMED | 94.1% arrives by the usual route, 97.0% by the direct route: 2.9% of the SOLAR is saved |
| 2384 | DC TRACTION | routes inv 0.98 rect 0.97 dc 0.985 | CONFIRMED | 94.1% arrives by the usual route, 98.5% by the direct route: 4.4% of the SOLAR is saved |
| 2385 | DC TRACTION | 80 GWh at 5% | CONFIRMED | saves 4.0 GWh a year; the solar is 8.0% of traction energy; an average traction substation carries about 382 kW |
| 2386 | DC TRACTION | 80 GWh at 7.5% | CONFIRMED | saves 6.0 GWh a year; the solar is 8.0% of traction energy; an average traction substation carries about 382 kW |
| 2387 | DC TRACTION | 80 GWh at 10% | CONFIRMED | saves 8.0 GWh a year; the solar is 8.0% of traction energy; an average traction substation carries about 382 kW |
| 2388 | DC TRACTION | 160 GWh at 5% | CONFIRMED | saves 8.0 GWh a year; the solar is 15.9% of traction energy; an average traction substation carries about 382 kW |
| 2389 | DC TRACTION | 160 GWh at 7.5% | CONFIRMED | saves 12.0 GWh a year; the solar is 15.9% of traction energy; an average traction substation carries about 382 kW |
| 2390 | DC TRACTION | 160 GWh at 10% | CONFIRMED | saves 16.0 GWh a year; the solar is 15.9% of traction energy; an average traction substation carries about 382 kW |
| 2391 | DC TRACTION | 400 GWh at 5% | CONFIRMED | saves 20.0 GWh a year; the solar is 39.9% of traction energy; an average traction substation carries about 382 kW |
| 2392 | DC TRACTION | 400 GWh at 7.5% | CONFIRMED | saves 30.0 GWh a year; the solar is 39.9% of traction energy; an average traction substation carries about 382 kW |
| 2393 | DC TRACTION | 400 GWh at 10% | CONFIRMED | saves 40.0 GWh a year; the solar is 39.9% of traction energy; an average traction substation carries about 382 kW |
