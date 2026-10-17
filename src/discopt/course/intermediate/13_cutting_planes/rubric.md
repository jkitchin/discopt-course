# Rubric — Lesson 13

## Exercises (70)
- E1 (15): Cut verified — (a) $x_1 + x_2 \le 4$ holds at every integer point of $[0,5]^2$ that satisfies the original constraints (in particular at $(3,1)$ where $3+1=4$ ✓); (b) violated by LP optimum (LHS $\approx 4.6 > 4$); (c) re-solved LP with cut returns objective $= 4$.
- E2 (15) Plot shows separation visually.
- E3 (15) MIR applied; LP-bound movement and node counts (`milp_backend="native", milp_cuts=False`) reported.
- E4 (10) `milp_cuts=True` vs `milp_cuts=False` on the native tree compared (nodes, time, cuts added, root bound) on ≥ 3 instances; LP gap and root gap closed reported; honest verdict on whether cuts paid off (they need not on every seed).
- E5 (15) Cover-cut callback works (invoked via `cut_callback`); node counts compared against a no-cut callback baseline on the same spatial B&B route.

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

