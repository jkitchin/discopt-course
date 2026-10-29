# discopt: An Optimization Course

A self-paced, LLM-assisted course in mathematical optimization, taught
through the `discopt` solver. Three core tracks (basic, intermediate, advanced)
totalling **30 lessons**, plus three optional electives (dynamic optimization,
multi-objective, piecewise-linear and grey-box models), each pairing a reading notebook with an exercise
notebook, a writing prompt, and a rubric. Claude Code acts as your TA: it
delivers material, answers questions, hints when you're stuck, and grades your
work against the rubric.

The course targets **discopt 0.10** or newer with the `jax` extra (check with
`discopt about`) on Python 3.12+. Claude Code is the default TA; other agents
can run the course through the bundled `discopt-course` and `course-assessor`
Agent Skills (`discopt tutor install` puts them in `.claude/skills/`, and
`uvx knowhow add jkitchin/discopt-course --all` installs them for any
supported agent).

## How the course works

Each lesson lives in `course/<track>/<id>/` and contains:

| File             | Purpose                                                       |
| ---------------- | ------------------------------------------------------------- |
| `reading.ipynb`  | The lesson — math, examples, runnable code with `discopt`.    |
| `exercises.ipynb`| 3-6 exercises with `# TODO` cells you fill in.                |
| `writing.md`     | A short essay or analysis prompt (≈ 1 page).                  |
| `rubric.md`      | The criteria Claude uses to assess your work.                 |

You write your essay in `writing_response.md` next to the prompt. Reference
solutions are not distributed with the course: try each exercise yourself, and
ask Claude for graduated hints (`/course:hint`) — it will not hand you the
answer.

## Quick start

```bash
# 1. Install discopt-course (pulls in discopt[jax]>=0.10) and Jupyter
pip install "git+https://github.com/jkitchin/discopt-course.git" jupyterlab

# 2. In a working directory of your choice: materialize a writable course/,
#    install the /course: slash commands + the two skills into ./.claude/,
#    and seed course/progress.yaml
discopt tutor install

# 3. See the dashboard, then launch lesson 1 in Claude Code
discopt tutor
discopt tutor start 1

# 4. When you finish the exercises, ask Claude (inside that session) to assess
/course:assess basic/01_intro_to_optimization
```

Other verbs: `discopt tutor list`, `discopt tutor resume`, `discopt tutor next`,
and `discopt tutor reset [<lesson>]`. See `SYLLABUS.md` for the full lesson
list.

To install the slash commands for every project instead (`~/.claude/`), run
`bash course/install_skills.sh --user`.

## Slash commands

The course ships with these Claude Code commands:

- `/course:lesson <id>` — load a lesson, get a guided tour of the reading.
- `/course:hint <id> <ex#>` — get a graduated hint for a specific exercise.
- `/course:assess <id>` — Claude grades your exercises against the rubric.
- `/course:grade-writing <id>` — Claude grades your `writing_response.md`.
- `/course:progress` — show what you've completed and what's next.
- `/course:cite-check` — verify all `{cite:p}` keys resolve in `references.bib`.

The grading behaviour is implemented by the `course-assessor` skill in
`.claude/skills/course-assessor/`, so it is consistent across sessions.

discopt also ships its own general-purpose Claude Code commands and expert
agents (install them with `discopt install-skills`). `/debug` is useful when a
lesson cell fails because of your installation rather than your model, and
`/diagnose` explains a `SolveResult`. Don't use `/formulate` to write your
exercise answers — that defeats the point of the course.

## Tracks

- **Basic (1–10)**: modeling, LP, duality, IP, B&B, convexity, NLP. Aimed at
  someone who has had calculus and linear algebra and wants a working
  knowledge of optimization plus the `discopt` API.
- **Intermediate (11–20)**: simplex internals, IPM, cuts, branching rules,
  presolve, relaxations, conic optimization, decomposition, stochastic
  programming. Algorithms-first; you'll implement small pieces and benchmark
  against `discopt`'s defaults.
- **Advanced (21–30)**: spatial B&B, global optimization theory, GDP,
  NN-embedded MINLP, robust optimization, ML-for-OR, differentiable
  optimization, bilevel, reformulations. Capstone is a paper-style writeup
  with computational results.
- **Electives (31–33, optional)**: dynamic optimization and optimal control
  with `discopt.dae` (after intermediate); multi-objective optimization with
  `discopt.mo` (after basic); piecewise-linear approximation and grey-box
  models with `m.piecewise`, `dm.nonlinear_to_pwl` and `dm.external` (after
  basic). They never block the core tracks.

## Progress tracking

Your state is recorded in `course/progress.yaml`, seeded from
`progress.template.yaml` by `discopt tutor install` (or by the first
`/course:progress` call). A lesson is passed at ≥ 70 / 100. Lessons unlock in
order within a track, but tracks can be done in parallel.

## Citations

Every reading cites the literature with `{cite:p}` / `{cite:t}` keys that
resolve to entries in `course/references.bib` (lesson files that mention
`docs/references.bib` mean this file). Cite from it in your own essays, and
run `/course:cite-check` to verify.

## Working with the notebooks

The notebooks use the real `discopt` modeling API directly
(`discopt.Model`, `m.continuous / .integer / .binary`, `m.subject_to`,
`m.minimize`, `m.solve()`). If you modify a reading notebook and want the
pristine version back, delete it and re-run `discopt tutor install` (it only
copies files that are missing unless you pass `--force`, which overwrites
every packaged file, including your exercise notebooks).
