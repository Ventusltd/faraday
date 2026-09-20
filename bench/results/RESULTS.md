# The hundred: results so far

600 of 2127 run. Every line below is one test; rerun any of them with `python bench/one.py N`.

| family | CONFIRMED | NO EFFECT | REFUTED |
|---|---|---|---|
| ARRANGEMENTS | 3 | 0 | 7 |
| GATES | 10 | 0 | 0 |
| PULSES | 10 | 0 | 0 |
| LOGIC | 10 | 0 | 0 |
| FEEDER PULSE | 60 | 0 | 0 |
| SITE PULSE | 24 | 0 | 0 |
| SITE THRESHOLDS | 2 | 1 | 0 |
| SITE SURVEY | 469 | 0 | 4 |

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
