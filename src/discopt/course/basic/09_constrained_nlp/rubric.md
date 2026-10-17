# Rubric — Lesson 9

**Total: 100**

## Exercises (70)
- E1 (15): KKT system written; solution computed; matches solver.
- E2 (15): LICQ failure exhibited via Jacobian rank deficiency *and* unbounded-multiplier observation *and* a reproducible `discopt` report (global solve's status/point explained via feasibility tolerance; local solve's huge `constraint_duals` and non-vanishing `kkt` dual infeasibility).
- E3 (15): barrier subproblems solved (e.g. SciPy); central path traced; iterates converge to $(1, 2)/\sqrt 5$.
- E4 (15): closed-form KKT linear system; matches numerical.
- E5 (10): Slater violation; sufficiency vs necessity articulated.

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

