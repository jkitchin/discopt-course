# Rubric — Lesson 7

**Total: 100**

## Exercises (70)
- E1 (15): each function correctly classified with proof.
- E2 (15): convex model built in a form the classifier can prove (e.g. $-\log x$, `dm.softplus`); `m.convexity().is_convex` and `r.convex_fast_path == True`; optimum reported.
- E3 (15): one term changed to create nonconvexity; `m.convexity()` names the broken part; `r.convex_fast_path == False` on the default (global) solve; multiple local optima found with local solves (`skip_convex_check=True` + `initial_solution`), and the global solve's answer identified among them.
- E4 (15): valid DC decomposition; both convex pieces verified.
- E5 (10): max of concave reformulated as min of convex (negation).

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

