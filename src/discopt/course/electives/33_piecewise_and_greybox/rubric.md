# Rubric — Lesson 33

**Total: 100**

## Exercises (70)
- E1 (10): Predictions made before counting and stated as formulas in $n$. Counts $(11,12)$, $(4,13)$, $(12,24)$ confirmed with `num_integer`/`num_continuous` (subtracting $x$ and $y$). The two-breakpoint case is explained (one segment means $y$ is an affine function of $x$, so there is no choice to encode) and confirmed. A non-SOS2 method is recommended for export, with `"log"` or `"incremental"` justified by binary count or speed.
- E2 (15): The `PiecewiseDomainError` is explained as a refusal to silently clamp the load to 100. $z^\star = 1320$ with `ub=100` (loads a permutation of $(10, 100, 100)$). $z^\star = 1260$ with the extended table (a permutation of $(50, 40, 120)$), explained by the 3 k\$/MWh band beyond 100 and the 9 k\$/MWh band that the first solution was buying. The widened-bound case is refused at `solve()` through `validate()`. Both optima are confirmed by enumeration.
- E3 (15): Native solve gives $-0.758628$ at $x \approx 1.5366$, $y = 1$, certified. Both outer runs certify the same value. Rounds and breakpoint counts are reported for $s = 4$ and $s = 8$ (more starting segments save a few rounds). `T.skipped` is empty and both terms are listed. The approximate mode gives `bound=None` and `gap_certified=False`, explained as "the chord interpolant is not a relaxation". The timing comparison notes that the spatial B&B is faster, and the outer route is justified only when a MILP is the goal.
- E4 (15): Newton solver and IFT derivatives are correct, and the FD relative errors are below $10^{-6}$ at all three points. The external block is built on a scalar `D` with output shapes `(1,)`. The grey box gives $D^\star \approx 0.14865$ m and cost $\approx 42066.33$ as `feasible` with `bound=None`. The twin certifies the same cost (`optimal`, `gap_certified=True`), and the answer says that only the twin is a certificate.
- E5 (15): The refusal is explained (binaries from the table plus an opaque block give no valid node relaxation). Route A certifies $\approx 43.749$ at $(\tau, T) \approx (3.8685, 400)$. Route B enumerates the 4 segments with linear costs, finds the third segment $[3, 6]$ best with the same value, and reports every segment's value. The comparison says that route B proves nothing globally (each segment is a local solve), and suggests multistart per segment, or a twin or surrogate check, to make it convincing.

## Writing (30)

- **Concept coverage (10):** the response names ≥ 3 specific concepts from
  this lesson with a one-line definition or formula each, AND references at
  least one numerical result the student produced in the exercise notebook
  (objective value, runtime, gap, plot point).
- **Technical correctness (10):** every claim about complexity, an algorithm,
  or a solver's behaviour is either a citation or a derivation; nothing
  factually wrong per the assessor's checklist for this lesson.
- **Citations (5):** ≥ 2 `{cite:p}` keys resolve in `course/references.bib`,
  at least one of which is a recommended reference for this lesson; no
  invented or unverifiable keys.
- **Engagement (5):** the response cites a specific surprise, equation,
  measurement, or solver-log line the student personally observed — not a
  generic platitude.
