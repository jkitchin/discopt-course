# Rubric — Lesson 32

**Total: 100**

## Exercises (70)
- E1 (10): Nondominated set $\{A,B,F,H\}$ identified by hand, with a dominating design named for each dominated one; ideal $(9, 0.99)$ and nadir $(14, 0.85)$ correct; `filter_nondominated` check uses the right `senses`.
- E2 (15): $\varepsilon$ is a parameter and the row is named. $z^\star(\varepsilon)$ is swept over $[35, 80]$ and plotted. $\lambda = 30$ and $\lambda = 40$ \$/t are read from `constraint_duals` and agree with `r.gradient`. Each slope is explained as a fuel switch. Carbon prices 10/35/45 map to emissions 80/75/35 and are linked to $\lambda$. The front is confirmed with `epsilon_constraint`.
- E3 (15): Exact front of 7 points from enumeration. The weighted sum misses $(33,37)$ and $(37,35)$, and a plot shows they lie inside the convex hull. AUGMECON2 with step $\le 1$ finds all 7. The coarse grid's miss of $(36,36)$ is explained by grid resolution.
- E4 (15): Four fronts plus the analytic reference front. Hypervolumes use the shared reference $(1.1, 1.1)$ and match the expected values to ±0.005. The closed form $1.21 - \pi/4$ is derived. The discussion explains that spread rewards the 2-point weighted-sum front, which is misleading.
- E5 (15): Exact front of 14 points. The three points missing from the 41-point sweep are identified and explained by the $\varepsilon$ step versus the 0.6 emissions gap; the complete sweep is verified. $L_2$, $L_\infty$ and Tchebycheff compromises are reported with their open sites. The answer notes that the $L_\infty$ choice changes once the front is complete.

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
