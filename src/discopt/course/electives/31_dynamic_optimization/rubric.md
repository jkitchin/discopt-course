# Rubric — Lesson 31

## Exercises (70)
- E1 (10) FD / Radau / Legendre transcriptions built; observed orders ≈ 1, 3, 5, 4; Legendre end-point trap explained (last node τ < 1) and fixed with `state_at`.
- E2 (15) Time scaling correct; t_f = 2 with bang-bang control at N = 20; t_f > 2 with odd N explained (switch not on the grid); speed-limited t_f ≈ 2.05 derived by hand and matched by the NLP; u(t), v(t) plotted on the true time axis.
- E3 (15) Ramp-rate path constraint added (b ≈ 0.6101) and its effect on the early profile explained; free-batch-time productivity ≈ 0.668 at t_f ≈ 0.16 h; optimum validated by simulation (|Δb| < 1e-6).
- E4 (15) `fit_trajectories` used for single- and two-experiment fits; Gauss–Newton standard errors from trajectory sensitivities; estimates within 3 SE of truth; ≈ 2× smaller SE(k₂) with experiment 2 explained physically; total-versus-partial derivative point discussed.
- E5 (10) (K, N) table with NLP objective, simulated objective, size and time; K = 1 optimism identified; smallest adequate grid chosen with justification; the two error sources separated.
- E6 (5) Relaxed and switch-limited MIQPs solved; monotone J(S) plotted; chattering and the relaxation gap explained.

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
