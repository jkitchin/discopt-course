# discopt-course

Optimization course + `tutor` CLI plugin for the
[discopt](https://github.com/jkitchin/discopt) modeling language. Installs as
the `discopt.course` namespace package and adds the `tutor` subcommand to the
base discopt CLI — `discopt tutor ...` works unchanged from when the course
lived in the base package.

A self-paced, Claude-Code-assisted course in mathematical optimization, taught
through the `discopt` solver. Three tracks (basic, intermediate, advanced)
totalling **30 lessons**, each pairing a reading notebook with an exercise
notebook, a writing prompt, and a rubric. Claude Code acts as your TA: it
delivers material, answers questions, hints when you're stuck, and grades your
work against the rubric.

## Install

```bash
pip install discopt-course
```

Requires `discopt>=0.6` (the first release with the `discopt.cli` plugin hook).
Installing this package registers the `tutor` subcommand with the base discopt
CLI automatically.

## Quick start

```bash
discopt tutor                              # dashboard: counts + next lesson
discopt tutor install                      # materialize a writable course/ + /course: commands
discopt tutor list                         # every lesson with completion status
discopt tutor start basic/01_intro_to_optimization   # launch a lesson in Claude Code
discopt tutor resume                       # continue the current lesson
discopt tutor next                         # start the next-numbered lesson
discopt tutor reset [<lesson>]             # drop one progress entry (or all)
```

`discopt tutor install` copies the `/course:` slash commands into `./.claude/`
and materializes a writable copy of the course tree into `./course/`. The
packaged copy shipped in the wheel stays read-only; a walk-up search from the
current directory means a materialized `course/` in your project always wins
over the packaged copy. Point `DISCOPT_COURSE_DIR` at a course tree to override.

## How the course works

Each lesson lives in `course/<track>/<id>/` and contains:

| File              | Purpose                                                    |
| ----------------- | ---------------------------------------------------------- |
| `reading.ipynb`   | The lesson — math, examples, runnable code with `discopt`. |
| `exercises.ipynb` | 3–6 exercises with `# TODO` cells you fill in.             |
| `writing.md`      | A short essay or analysis prompt.                          |
| `rubric.md`       | The criteria Claude uses to assess your work.              |

Progress is tracked in a per-student `progress.yaml` (from
`progress.template.yaml`); the tutor's dashboard, `list`, `resume`, `next`, and
`reset` verbs read and write it. PyYAML is a runtime dependency for that.

## Development

The project is uv-managed:

```bash
uv sync                # create .venv (installs discopt from the pinned branch)
uv run pytest          # fast test set
uv run ruff check .
uv run ruff format --check .
```

To develop against a local discopt checkout instead of the pinned branch, add
a `[tool.uv.sources]` override pointing `discopt` at your editable clone:

```toml
[tool.uv.sources]
discopt = { path = "../../projects/discopt", editable = true }
```

Docs are a Jupyter Book:

```bash
uv run jupyter-book build docs/
```

## Claude Code slash commands

The package bundles the `/course:` slash commands (lesson, hint, assess,
progress, cite-check, grade-writing) and the `course-assessor` skill under
`discopt.course/_claude_assets/`. `discopt tutor install` drops them into
`./.claude/` where Claude Code picks them up.
