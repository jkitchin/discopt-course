# discopt-course

**discopt-course** is the optimization-course plugin for the
[discopt](https://github.com/jkitchin/discopt) modeling language. It installs
as the `discopt.course` namespace package and adds the `tutor` subcommand to
the base `discopt` CLI, so `discopt tutor` works exactly as it did when the
course lived in the base package (discopt 0.5 and earlier).

The course is a self-paced, Claude-Code-assisted curriculum in mathematical
optimization, taught through the `discopt` solver. Three tracks — basic,
intermediate, and advanced — total 30 core lessons, plus two optional
electives (dynamic optimization, multi-objective), each pairing a reading notebook
with an exercise notebook, a writing prompt, and a grading rubric. The
foundations lean on the standard references {cite:p}`Boyd2004,Nocedal2006`.
Claude Code acts as the teaching assistant: it delivers material, answers
questions, hints when you are stuck, and grades your work against the rubric
via the `/course:` slash commands bundled with the package.

## Install

discopt-course is installed from GitHub (it is not on PyPI); this pulls in
[discopt](https://pypi.org/project/discopt/) 0.9 or newer from PyPI:

```bash
pip install "git+https://github.com/jkitchin/discopt-course.git"
```

Requires Python 3.12+ and `discopt>=0.9` — the lessons are written against
the discopt 0.9 API. Installing this package registers the `tutor` subcommand
with the base discopt CLI automatically. The interactive verbs also need
[Claude Code](https://claude.com/claude-code) (`claude` on your PATH).

## Quick start

```bash
discopt tutor                              # dashboard: progress + next lesson
discopt tutor install                      # materialize a writable course/ + /course: commands
discopt tutor list                         # every lesson with completion status
discopt tutor start basic/01_intro_to_optimization   # launch a lesson in Claude Code
discopt tutor resume                       # continue the current lesson
discopt tutor next                         # current lesson until passed, then the one after
```

`discopt tutor install` copies the `/course:` slash commands into `./.claude/`,
materializes a writable copy of the course tree into `./course/`, and seeds
`course/progress.yaml`; the packaged copy shipped in the wheel stays
read-only.

## Where to start

- Never used the tutor before? Walk through the
  {doc}`tutor course tour <notebooks/tutor_course>`.
- Then run `discopt tutor install` and `discopt tutor start 1`, which opens
  `/course:lesson basic/01_intro_to_optimization` in Claude Code.
- For discopt itself — the modeling API, solver options, and self-contained
  tutorials — see the [discopt repository](https://github.com/jkitchin/discopt)
  and its `docs/notebooks/`.
