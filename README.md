# faraday

A numbered, dated log of what was actually done and what was actually observed.

Faraday numbered every paragraph of *Experimental Researches in Electricity* continuously, 1 to
3430, across thirty years, so that any later paragraph could cite any earlier one by number alone.
He dated them, wrote them in plain first person without mathematics, and recorded the failures.
This is that instrument.

Open `index.html`. Everything is collapsed. Open what you want.

- Numbers run continuously and are **never reused or renumbered**.
- Every entry states the question, the apparatus, what was done, what was observed (verbatim where
  possible), what it shows, which law it tests, and the result.
- **REFUTED** and **NO EFFECT** are recorded as readily as **CONFIRMED**. A refuted entry is a
  record of an error made here and then corrected, kept deliberately.
- `tools/build.py` refuses to publish an entry that is missing any part, a reused number, or a gap.

The laws these experiments test are at [Ventusltd/law](https://github.com/Ventusltd/law). The
engine most of them were run on is [Ventusltd/cosmic](https://github.com/Ventusltd/cosmic).

Code under Apache-2.0. Documentation under CC BY 4.0. No warranty is given.
