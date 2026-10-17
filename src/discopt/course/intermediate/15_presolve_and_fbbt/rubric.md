# Rubric — Lesson 15

## Exercises (70)
- E1 (15) FBBT trace correct; fixpoint $x_1 \in [0.5, 5]$, $x_2 \in [0, 4.5]$ (matches `fbbt_box`).
- E2 (20) FBBT implemented; bounds improve on test problem; cross-checked against `fbbt_box`.
- E3 (15) Probing fixings + cliques reported; compared with `probe_box`.
- E4 (10) OBBT bounds tighter than FBBT; trade-off discussed.
- E5 (10) Presolve on/off measured on a MILP (HiGHS via `scipy.optimize.milp`) and on a spatial-B&B model; route-dependence of `presolve=False` and redundancy with root/in-tree tightening discussed.

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

