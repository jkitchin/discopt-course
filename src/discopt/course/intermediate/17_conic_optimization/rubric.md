# Rubric — Lesson 17

## Exercises (70)
- E1 (15) Lasso → SOCP correctly.
- E2 (10) MISOCP/MIQP solved; cardinality respected; compared with 5-asset unconstrained optimum.
- E3 (20) GW SDP (external solver or Burer–Monteiro) set up + rounded; compared to brute-force optimum.
- E4 (10) LMI feasibility interval found (SDP solver or eigenvalue bisection); convexity argument given.
- E5 (5) Robust LP → SOCP.
- E6 (10) Box GP in standard form; `classify_gp` recognizes it; `solve_gp` vs `m.solve()` compared; why the nonconvex-looking model is certified (log-convexity) and what breaks it explained.

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

