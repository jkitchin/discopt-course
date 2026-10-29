# Rubric — Lesson 23

## Exercises (70)
- E1 (15): big-M and hull written by hand and checked against `gdp_method="big-m"`, `"mbigm"` and `"hull"`; all solves agree; root bounds, nodes and times reported, with a justified choice of reformulation.
- E2 (15): reactor network solved with the hull; cheapest configuration reported from both `do.selected_disjuncts` and the indicators, and any disagreement explained (overlapping disjuncts; select-one semantics).
- E3 (10): implication encoded by hand on selectors and with `m.logical` on the indicators; both give the same optimum; a data set where the implication is active is shown.
- E4 (10): nested disjunction flattened by hand (binaries counted); inline nesting solved with big-M and hull, block form with hull and `loa`; answers agree; the hull's root bound is at least big-M's; the student explains that logic-based methods need an indicator for every inner disjunct.
- E5 (15): enumeration gives $z^\star = 137.638$ at units $(2,2,2,2)$ (0-based); table of `big-m`, `hull`, `loa`, `gloa`, `enumerate`, `ldsda`; big-M root bound $\approx 0$ against the hull's $\approx 107.06$, explained; `ldsda` from the default start stops at 139.288 with `status="feasible"`, `bound=None`, and other starting points are compared; the scaling recommendation (10 units per stage) is supported by the measurements.
- E6 (5): an example where big-M is naturally tight, justified and checked with `r.root_bound`.

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

