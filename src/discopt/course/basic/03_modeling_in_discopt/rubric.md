# Rubric — Lesson 3

**Total: 100**

## Exercises (70)
- E1 (15): Surplus penalty term added correctly; (a) notes total supply = total demand (330) so nothing changes; (b) with supply 200 the \$2 penalty shifts which node serves demand node 4, and the \$5 penalty causes over-shipping on lanes with unit cost < 5 (objectives 1550 and 1650 for the reference data).
- E2 (15): L1 formulation correct; outlier shown to pull L2 fit but not L1.
- E3 (15): A∧B→C linearized correctly via $C \ge A + B - 1$; cheapest config found.
- E4 (10): (a) and (b) solved, node counts/times compared; discussion explains that (a) is easy at any box while (b)'s tree grows with $U$, and mentions implied vs declared bounds (presolve/FBBT).
- E5 (15): Vectorized formulation correct; row/nonzero counts from `to_lp()` reported (loop has $n(n-1)$ rows, vectorized $n(n-1)/2$ — each pair once); same optimum; bonus: clique row gives a tighter LP relaxation.

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

