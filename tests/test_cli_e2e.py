"""End-to-end ``discopt tutor`` runs through the real base ``discopt`` CLI.

Each step spawns ``python -m discopt.cli tutor ...`` in a scratch directory,
so the ``discopt.cli`` entry-point discovery, the lazy plugin load, and the
``sys.exit(run(args) or 0)`` hand-off in discopt's own CLI are all exercised.
A fake ``claude`` executable on PATH records the slash command it is launched
with instead of opening a real Claude Code session.
"""

from __future__ import annotations

import os
import subprocess
import sys

import pytest

pytestmark = pytest.mark.integration


@pytest.fixture
def workspace(tmp_path):
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    log = tmp_path / "claude.log"
    fake = bin_dir / "claude"
    fake.write_text(f'#!/bin/sh\nprintf "%s\\n" "$*" >> "{log}"\n')
    fake.chmod(0o755)
    work = tmp_path / "work"
    work.mkdir()
    env = dict(os.environ)
    env.pop("DISCOPT_COURSE_DIR", None)
    env["PATH"] = f"{bin_dir}{os.pathsep}{env.get('PATH', '')}"
    # Keep ~/.claude lookups (slash-command presence hint) inside the sandbox.
    env["HOME"] = str(tmp_path)

    def tutor(*args: str, stdin: str = "") -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, "-m", "discopt.cli", "tutor", *args],
            cwd=work,
            env=env,
            input=stdin,
            capture_output=True,
            text=True,
            timeout=120,
        )

    def launched() -> list[str]:
        return log.read_text().splitlines() if log.exists() else []

    return work, tutor, launched


def test_tutor_listed_in_base_help(workspace):
    work, _, _ = workspace
    r = subprocess.run(
        [sys.executable, "-m", "discopt.cli", "--help"],
        cwd=work,
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert r.returncode == 0
    assert "tutor" in r.stdout


def test_full_student_workflow(workspace):
    work, tutor, launched = workspace

    # Before install: dashboard reads the read-only packaged copy.
    r = tutor()
    assert r.returncode == 0, r.stderr
    assert "read-only packaged copy" in r.stdout
    assert "0 / 10" in r.stdout

    # Install materializes course/ + .claude/ and seeds progress.yaml.
    r = tutor("install")
    assert r.returncode == 0, r.stderr
    assert (work / ".claude" / "commands" / "course" / "lesson.md").is_file()
    assert (work / "course" / "progress.yaml").is_file()

    # Dashboard/list now use the writable copy.
    r = tutor()
    assert r.returncode == 0, r.stderr
    assert str(work / "course") in r.stdout
    assert "read-only" not in r.stdout
    assert "current lesson:  basic/01_intro_to_optimization" in r.stdout
    r = tutor("list")
    assert r.returncode == 0
    assert len([ln for ln in r.stdout.splitlines() if "/" in ln]) == 30

    # start / resume / next launch claude with the right slash command.
    assert tutor("start", "2").returncode == 0
    assert tutor("resume").returncode == 0
    assert tutor("next").returncode == 0
    assert launched() == [
        "/course:lesson basic/02_lp_fundamentals",
        "/course:lesson basic/01_intro_to_optimization",
        "/course:lesson basic/01_intro_to_optimization",
    ]
    # The commands were installed, so no "not installed" warning.
    assert "not installed" not in tutor("start", "1").stderr

    # Record a passing score; `next` advances past the current lesson.
    progress = work / "course" / "progress.yaml"
    progress.write_text(
        progress.read_text().replace(
            "scores: null", "scores:\n  basic/01_intro_to_optimization: {total: 85}"
        )
    )
    assert "1 / 10" in tutor().stdout
    assert tutor("next").returncode == 0
    assert launched()[-1] == "/course:lesson basic/02_lp_fundamentals"

    # Per-lesson reset, then full reset (declined, then forced).
    r = tutor("reset", "01")
    assert r.returncode == 0 and "dropped" in r.stdout
    assert "0 / 10" in tutor().stdout
    assert "aborted" in tutor("reset", stdin="n\n").stdout
    r = tutor("reset", "--yes")
    assert r.returncode == 0 and "reset" in r.stdout

    # Unknown lessons fail cleanly.
    r = tutor("start", "99")
    assert r.returncode == 1 and "unknown lesson" in r.stderr
