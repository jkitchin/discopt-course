# Rubric — Lesson 19

## Exercises (70)
- E1 (15) SAA convergence plot; converges to $x^\star = 125$ (critical fractile $3/4$); hand-built and `build_extensive_form` agree.
- E2 (15) Chance-constrained portfolio via SOCP ($r^\top w$, not $\mu^\top w$, inside the probability); SAA check with `chance_constraint`.
- E3 (15) CVaR$_{0.95}$ LP works and matches `CVaR(alpha=0.95)`; comparison with mean-variance done.
- E4 (15) 3-period tree (125 leaves) with non-anticipativity solved; EVPI computed.
- E5 (10) VSS, EVPI defined and computed correctly.

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

