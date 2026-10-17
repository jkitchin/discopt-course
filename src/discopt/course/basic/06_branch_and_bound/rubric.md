# Rubric — Lesson 6

**Total: 100**

## Exercises (70)
- E1 (15): `bnb_trace` dict supplied (7 nodes for the reference instance $v = (9,14,13,11)$, root LP 28, optimum 27); every LP value verified against a `discopt` LP-relaxation solve within 1e-6; prune reasons correct.
- E2 (15): hard instance shown to be vastly harder (with `DISCOPT_LP_MILP_BACKEND=rust` node counts); LP gap explanation; notes that HiGHS hides the difference at this size.
- E3 (10): three strategies compared; trade-offs articulated.
- E4 (15): symmetric instance built; lex constraint reduces nodes in `discopt`'s own tree (HiGHS node counts stay ≈1, explained).
- E5 (15): TUM (or other) example with integer LP at root.

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

