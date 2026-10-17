# Syllabus

Thirty core lessons in three tracks, plus two optional electives. Each row gives the lesson's title (as in its
`reading.ipynb`), its directory under `course/`, and the primary literature
backing it. Full BibTeX entries are in `course/references.bib` (in a
discopt-course checkout: `src/discopt/course/references.bib`).

Any lesson can be started by number, e.g. `discopt tutor start 7`.

## Basic track — modeling and solving

| #  | Title | Directory | Primary references |
| -- | ----- | --------- | ------------------ |
| 01 | Introduction to Optimization | [`basic/01_intro_to_optimization`](basic/01_intro_to_optimization/) | Bertsimas1997, Williams2013, Wolsey1998 |
| 02 | Linear Programming Fundamentals | [`basic/02_lp_fundamentals`](basic/02_lp_fundamentals/) | Bertsimas1997, Dantzig1963 |
| 03 | Modeling in `discopt` | [`basic/03_modeling_in_discopt`](basic/03_modeling_in_discopt/) | Williams2013 |
| 04 | Sensitivity, Duality, Shadow Prices | [`basic/04_sensitivity_and_duality`](basic/04_sensitivity_and_duality/) | Bertsimas1997, Boyd2004 |
| 05 | Integer Programming Basics | [`basic/05_integer_programming_basics`](basic/05_integer_programming_basics/) | Wolsey1998, Williams2013, Conforti2014 |
| 06 | Branch and Bound, Conceptually | [`basic/06_branch_and_bound`](basic/06_branch_and_bound/) | Land1960, Dakin1965, Wolsey1998 |
| 07 | Convexity | [`basic/07_convexity`](basic/07_convexity/) | Boyd2004, Rockafellar1970 |
| 08 | Unconstrained NLP | [`basic/08_unconstrained_nlp`](basic/08_unconstrained_nlp/) | Nocedal2006 |
| 09 | Constrained NLP, KKT, Interior-Point Methods | [`basic/09_constrained_nlp`](basic/09_constrained_nlp/) | Nocedal2006, Wachter2006 |
| 10 | Capstone (Basic) | [`basic/10_capstone_basic`](basic/10_capstone_basic/) | Williams2013 |

## Intermediate track — algorithms and structure

| #  | Title | Directory | Primary references |
| -- | ----- | --------- | ------------------ |
| 11 | Simplex Revealed | [`intermediate/11_simplex_revealed`](intermediate/11_simplex_revealed/) | Dantzig1963, Bland1977, Bertsimas1997 |
| 12 | Interior-Point Methods | [`intermediate/12_interior_point_methods`](intermediate/12_interior_point_methods/) | Karmarkar1984, Mehrotra1992, Wright1997 |
| 13 | Cutting Planes | [`intermediate/13_cutting_planes`](intermediate/13_cutting_planes/) | Gomory1958, Balas1993, Cornuejols2008 |
| 14 | Branching Rules | [`intermediate/14_branching_rules`](intermediate/14_branching_rules/) | Achterberg2005, Achterberg2007 |
| 15 | Presolve and FBBT | [`intermediate/15_presolve_and_fbbt`](intermediate/15_presolve_and_fbbt/) | Belotti2009, Savelsbergh1994 |
| 16 | Convex Relaxations | [`intermediate/16_convex_relaxations`](intermediate/16_convex_relaxations/) | McCormick1976, Adjiman1998, Tawarmalani2005 |
| 17 | Conic Optimization | [`intermediate/17_conic_optimization`](intermediate/17_conic_optimization/) | BenTal2001, Boyd2004 |
| 18 | Decomposition Methods | [`intermediate/18_decomposition`](intermediate/18_decomposition/) | Benders1962, DantzigWolfe1960 |
| 19 | Stochastic Programming | [`intermediate/19_stochastic_programming`](intermediate/19_stochastic_programming/) | Birge2011, Shapiro2009 |
| 20 | Capstone (Intermediate) | [`intermediate/20_capstone_intermediate`](intermediate/20_capstone_intermediate/) | mixed (your choice, ≥ 5) |

## Advanced track — frontiers

| #  | Title | Directory | Primary references |
| -- | ----- | --------- | ------------------ |
| 21 | Spatial Branch-and-Bound | [`advanced/21_spatial_branch_and_bound`](advanced/21_spatial_branch_and_bound/) | Tawarmalani2005, Smith1999, Belotti2009 |
| 22 | Global Optimization Theory | [`advanced/22_global_optimization_theory`](advanced/22_global_optimization_theory/) | Floudas1999, HorstTuy1996 |
| 23 | Generalized Disjunctive Programming | [`advanced/23_generalized_disjunctive_programming`](advanced/23_generalized_disjunctive_programming/) | Raman1994, Grossmann2013, Trespalacios2015 |
| 24 | Neural-Network-Embedded MINLP | [`advanced/24_nn_embedded_minlp`](advanced/24_nn_embedded_minlp/) | Fischetti2018, Anderson2020, Ceccon2022 |
| 25 | Robust Optimization | [`advanced/25_robust_optimization`](advanced/25_robust_optimization/) | BenTal2009, BertsimasSim2004 |
| 26 | Differentiable Optimization | [`advanced/26_differentiable_optimization`](advanced/26_differentiable_optimization/) | Amos2017, Agrawal2019 |
| 27 | Machine Learning for Optimization | [`advanced/27_ml_for_optimization`](advanced/27_ml_for_optimization/) | Bengio2021, Gasse2019 |
| 28 | Bilevel and Complementarity Programs | [`advanced/28_bilevel_and_complementarity`](advanced/28_bilevel_and_complementarity/) | Dempe2002, LuoPangRalph1996 |
| 29 | Reformulations and Symmetry | [`advanced/29_reformulations_and_symmetry`](advanced/29_reformulations_and_symmetry/) | Liberti2009, Margot2010 |
| 30 | Capstone (Advanced) | [`advanced/30_capstone_advanced`](advanced/30_capstone_advanced/) | mixed (your choice, ≥ 12) |
## Electives — optional

Electives never block the core tracks. Lesson 31 assumes the intermediate
track (NLP, KKT, interior point); lesson 32 assumes the basic track.

| #  | Title | Directory | Primary references |
| -- | ----- | --------- | ------------------ |
| 31 | Dynamic Optimization and Optimal Control | [`electives/31_dynamic_optimization`](electives/31_dynamic_optimization/) | Biegler2010, Betts2010, Cuthrell1987 |
| 32 | Multi-Objective Optimization | [`electives/32_multi_objective`](electives/32_multi_objective/) | ehrgott-2005, miettinen-1999, mavrotas-2009 |

## Pacing

The course is self-paced. A reasonable target is **one lesson per week** for
basic, **one every 1-2 weeks** for intermediate, and **one every 2-3 weeks**
for advanced. The total course is roughly equivalent to a one-year graduate
sequence in optimization.

## Prerequisites

- **Basic**: calculus, linear algebra, comfort with Python.
- **Intermediate**: completion of basic track or equivalent (an undergraduate
  OR or convex optimization course).
- **Electives**: lesson 31 after the intermediate track; lesson 32 after
  the basic track.
- **Advanced**: completion of intermediate track and at least one of: a
  graduate optimization course, research experience, or significant industrial
  experience formulating MINLPs.

## Assessment

Each lesson awards up to 100 points distributed across exercise correctness,
writing quality, and (on capstones) experimental rigor. The `course-assessor`
skill normalizes grading across sessions. Track completion requires ≥ 70 / 100
on every lesson.
