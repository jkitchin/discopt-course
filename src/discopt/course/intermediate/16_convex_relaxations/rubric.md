# Rubric — Lesson 16

## Exercises (70)
- E1 (10) Four inequalities; tightness analysis.
- E2 (15) 3D plots show envelope and refined envelope.
- E3 (15) αBB computation; plot.
- E4 (20) Pooling solved locally from several starts (local optima found, e.g. 100 vs 400), globally with the default, with `rlt=True`, and with `solver="amp"`; objectives, bounds, nodes, `termination` and times reported; a reasoned explanation of AMP's weak bound (e.g. the rows its outer approximation skips because they are not proved convex; on the reference install AMP stops at 400 with a bound near 675 while spatial B&B certifies 400).
- E5 (10) Quadratic gap scaling.

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

