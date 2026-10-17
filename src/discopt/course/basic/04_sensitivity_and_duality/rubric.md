# Rubric — Lesson 4

**Total: 100**

## Exercises (70)
- E1 (15): Dual stated correctly; primal/dual objectives match.
- E2 (15): Model built once with $b_1$ as a parameter and re-solved via `.value`; plot piecewise linear; basis-change corners identified.
- E3 (10): direct (`constraint_duals`), finite-difference and `r.gradient` shadow prices computed and agree; dual feasibility and equal-objective conditions verified within 1e-4.
- E4 (15): Genuinely degenerate 2D LP; non-smooth perturbation behaviour exhibited.
- E5 (15): Dual certificate constructed and verified.

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

