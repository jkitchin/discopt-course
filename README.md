# discopt-course

[![ci](https://github.com/jkitchin/discopt-course/actions/workflows/ci.yml/badge.svg)](https://github.com/jkitchin/discopt-course/actions/workflows/ci.yml)

Optimization course + `tutor` CLI plugin for the
[discopt](https://github.com/jkitchin/discopt) modeling language. Installs as
the `discopt.course` namespace package and adds the `tutor` subcommand to the
base discopt CLI — `discopt tutor ...` works unchanged from when the course
lived in the base package.

A self-paced, LLM-assisted course in mathematical optimization, taught
through the `discopt` solver. Three core tracks (basic, intermediate, advanced)
totalling **30 lessons**, plus three optional electives (dynamic optimization,
multi-objective, piecewise-linear and grey-box models), each pairing a reading notebook with an exercise
notebook, a writing prompt, and a rubric. Claude Code acts as your TA: it
delivers material, answers questions, hints when you're stuck, and grades your
work against the rubric. Claude Code gets dedicated `/course:` slash
commands; any agent that reads [Agent Skills](https://agentskills.io) (Codex,
Cursor, OpenCode, Gemini CLI, ...) can run the course through the bundled
skills (see [Running the course from an LLM](#running-the-course-from-an-llm)).

## Install

discopt-course is not on PyPI; install it from GitHub. It pulls in
`discopt[jax]>=0.10` from PyPI (prebuilt wheels, no Rust toolchain needed):

```bash
pip install "git+https://github.com/jkitchin/discopt-course.git"
discopt about        # should report discopt 0.10.0 or newer
discopt tutor        # the tutor subcommand is now registered
```

Requires Python 3.12+. The lessons target discopt 0.10 (`Model.piecewise`,
`dm.external`, `SolveResult.termination`, the native GDP algorithms, ...).
JAX became an optional discopt extra in 0.10; the course depends on
`discopt[jax]` because several lessons use the JAX-only features
(`dm.custom`, `discopt.sensitivity`, `discopt.estimate`, the differentiable
layer). Installing this package registers the `tutor` subcommand with the base discopt
CLI automatically. You also need [Claude Code](https://claude.com/claude-code)
(the `claude` binary on your PATH) for the interactive verbs, and Jupyter if
you want to open the notebooks yourself (`pip install jupyterlab`).

## Quick start

```bash
discopt tutor                              # dashboard: counts + next lesson
discopt tutor install                      # materialize a writable course/ + /course: commands
discopt tutor list                         # every lesson with completion status
discopt tutor start basic/01_intro_to_optimization   # launch a lesson in Claude Code
discopt tutor start 1                      # ...or by number
discopt tutor resume                       # continue the current lesson
discopt tutor next                         # current lesson until passed, then the one after
discopt tutor reset [<lesson>] [--yes]     # drop one progress entry (or all)
```

`discopt tutor install` copies the `/course:` slash commands and the
`course-assessor` skill into `./.claude/`, materializes a writable copy of the
course tree into `./course/`, and seeds `course/progress.yaml` from the
template. Re-running it is safe; `--force` overwrites packaged files
(including notebooks you have edited) but never `progress.yaml`. The packaged
copy shipped in the wheel stays read-only; a walk-up search from the current
directory means a materialized `course/` in your project always wins over the
packaged copy. Point `DISCOPT_COURSE_DIR` at a course tree to override.

## How the course works

Each lesson lives in `course/<track>/<id>/` and contains:

| File              | Purpose                                                    |
| ----------------- | ---------------------------------------------------------- |
| `reading.ipynb`   | The lesson — math, examples, runnable code with `discopt`. |
| `exercises.ipynb` | 3–6 exercises with `# TODO` cells you fill in.             |
| `writing.md`      | A short essay or analysis prompt.                          |
| `rubric.md`       | The criteria Claude uses to assess your work.              |

The syllabus is [`src/discopt/course/SYLLABUS.md`](src/discopt/course/SYLLABUS.md);
the course bibliography, cited by the readings and by your essays, is
[`src/discopt/course/references.bib`](src/discopt/course/references.bib)
(materialized as `course/references.bib`).

Progress is tracked in a per-student `progress.yaml` (from
`progress.template.yaml`); the tutor's dashboard, `list`, `resume`, `next`, and
`reset` verbs read and write it. PyYAML is a runtime dependency for that.

## Development

The project is uv-managed:

```bash
uv sync --python 3.12  # create .venv (discopt[jax]>=0.10 from PyPI + dev tools)
uv run pytest          # fast test set (unit, packaging, end-to-end CLI)
uv run ruff check .
uv run ruff format --check .
```

To develop against a local discopt checkout instead of the PyPI release, add
a `[tool.uv.sources]` override (don't commit it) pointing `discopt` at your
editable clone:

```toml
[tool.uv.sources]
discopt = { path = "../discopt", editable = true }
```

CI (`.github/workflows/ci.yml`) runs the same commands against the released
discopt. `.github/workflows/discopt-integration.yml` re-runs the tests against
discopt `main` whenever discopt publishes a release (discopt lists this repo
in its `.github/dependents.yml`), weekly, and on demand.

Docs are a Jupyter Book:

```bash
uv run jupyter-book build docs/
```

## Running the course from an LLM

The course ships two [Agent Skills](https://agentskills.io) under
`src/discopt/course/_claude_assets/skills/`:

| Skill | What it does |
| ----- | ------------ |
| `discopt-course` | The tutor: setup, progress, choosing the next lesson, walking through a reading, graduated hints, citation checks. |
| `course-assessor` | Grading against a lesson's rubric (exercises, writing, capstone milestones) and `progress.yaml` updates. |

They are written for any agent that can run shell commands and read files,
not only Claude Code. Install them with
[knowhow](https://github.com/jkitchin/knowhow) (v0.3+), which finds them
through the root `skills/` symlink:

```bash
uvx knowhow add jkitchin/discopt-course --list   # 2 skills
uvx knowhow add jkitchin/discopt-course --all    # install them for your agent(s)
```

Then ask your agent to "start the discopt course" in an empty working
directory: the tutor skill installs the course (`discopt tutor install`) and
takes it from there. `discopt tutor install` also installs both skills into
`./.claude/skills/`. On Windows, clone with `git config core.symlinks true` or
install from the subpath `jkitchin/discopt-course/src/discopt/course/_claude_assets/skills`.

## Claude Code slash commands

The package bundles the `/course:` slash commands (lesson, hint, assess,
progress, cite-check, grade-writing) and the two skills under
`src/discopt/course/_claude_assets/`. The commands are deliberately not in the
knowhow layout: knowhow installs commands without their folder, which would
turn `/course:assess` into a bare `/assess`. `discopt tutor install` drops them into
`./.claude/` where Claude Code picks them up (or run
`bash course/install_skills.sh --user` to install them into `~/.claude/`).

discopt itself ships separate, general-purpose Claude Code commands and expert
agents (`/formulate`, `/debug`, `/diagnose`, `/reformulate`, ...), installed
with `discopt install-skills`. They don't conflict with the `/course:`
namespace; `/debug` is handy when a lesson cell fails because of your
installation. (Using `/formulate` to write your exercise answers defeats the
point of the course.)
