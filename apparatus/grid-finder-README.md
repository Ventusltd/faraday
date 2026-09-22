# Grid finder apparatus

Experiment 20 in Faraday's continuous ledger. This is an offline computation over published network records, with a Python standard-library implementation and repeatable fixtures.

```sh
python apparatus/test_grid_finder.py
python apparatus/grid_finder.py --lat 53.3 --lon -0.8 --mw 100 --voltage-kv 132
```

From Python, import `GridFinder` from `apparatus.grid_finder` and call `query(latitude, longitude, mw, voltage_kv=None, target_kv=400, headroom_mw_by_site=None, limit=12, max_hops=12, radius_km=None)`.

Candidates retain geographic distance order. Pareto tiers compare distance and the fewest validated published edges to the target voltage; unknown paths remain ungraded. A missing connection voltage does not acquire an assumed value. Entered headroom is an optional scenario keyed by published site code, kept separate from the source's ratings.

`compare_published_path_ratings(path, mw, power_factor, season='winter')` compares entered apparent demand with each published edge nameplate. It does not distribute flows or subtract existing demand. The West Burton example tests 100 MW and 300 MW at 0.95 against a published 274 MVA transformer; neither answer provides available headroom.

## Evidence and coverage

The compact data contains 886 candidate sites, 489 with mapped coordinates and 397 without, plus 2679 graph nodes and 2864 existing circuit/transformer edges. Of the nodes, 726 have no validated voltage and cannot be traversed by this strict search. Planned changes are excluded. No same-site bus connections are invented. Results report whether a path was found, the search limit was reached, or no validated published path was found.

Public source files were checked byte-for-byte against [data-grid-gb commit 5181de3423e4fe50c77c568b9f3066c61a1d9e41](https://github.com/Ventusltd/data-grid-gb/tree/5181de3423e4fe50c77c568b9f3066c61a1d9e41/derived): `connection-points.v3.json` and `gb-transmission-network.v1.json`. Full source SHA256 hashes and row identities travel with the compact data and results.

The network is derived from NESO Electricity Ten Year Statement 2025, Appendix B; the source product also describes Appendix D fault levels, which this apparatus does not copy or calculate. Coordinates are joined from OpenStreetMap contributors via the GridAtlas release. Geographic separation uses the existing Atlas spherical radius of 6378.137 km and is not a surveyed cable route. The geodesy fixture file identifies its public source and source hash.

Code follows this repository's Apache-2.0 licence; original explanatory text follows CC BY 4.0. Third-party records retain their own terms. Attribute NESO ETYS 2025 and [OpenStreetMap contributors](https://www.openstreetmap.org/copyright); the repository's code licence does not relicense their data.

This is candidate screening, not solved power flow, spare capacity, fault analysis, a connection offer or engineering approval. The apparatus uses a dated snapshot, not a live operational network.
