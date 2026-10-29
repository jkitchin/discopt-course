"""Consistency checks across the packaged course tree.

These catch drift between the syllabus, the lesson notebooks, and the
bibliography that ships with the course (``course/references.bib``).
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

from discopt.course import package_root

pytestmark = pytest.mark.smoke

ROOT = package_root()
REPO = Path(__file__).resolve().parents[1]
TRACKS = ("basic", "intermediate", "advanced", "electives")
N_LESSONS = 33  # 30 core lessons + electives 31-33
LESSON_FILES = ("reading.ipynb", "exercises.ipynb", "writing.md", "rubric.md")

_CITE = re.compile(r"\{cite:[pt]\}`([^`]*)`")
_KEY = re.compile(r"^[A-Za-z][\w:.-]*$")
_BIB_KEY = re.compile(r"^@\w+\{([^,\s]+),", re.M)


def _lesson_dirs() -> list[Path]:
    return [d for t in TRACKS for d in sorted((ROOT / t).iterdir()) if d.is_dir()]


def _text(path: Path) -> str:
    if path.suffix == ".ipynb":
        nb = json.loads(path.read_text())
        return "\n".join("".join(c.get("source", [])) for c in nb["cells"])
    return path.read_text()


def _notebook_title(reading: Path) -> tuple[int, str]:
    for line in _text(reading).splitlines():
        m = re.match(r"# Lesson (\d+) — (.+)", line)
        if m:
            return int(m.group(1)), m.group(2).strip()
    raise AssertionError(f"{reading}: no '# Lesson N — Title' heading")


def _bib_keys() -> set[str]:
    return set(_BIB_KEY.findall((ROOT / "references.bib").read_text()))


def test_all_lessons_complete_and_numbered():
    dirs = _lesson_dirs()
    assert len(dirs) == N_LESSONS
    for i, d in enumerate(dirs, start=1):
        assert d.name.startswith(f"{i:02d}_"), d
        for f in LESSON_FILES:
            assert (d / f).is_file(), d / f


def test_syllabus_matches_lesson_directories_and_titles():
    syllabus = (ROOT / "SYLLABUS.md").read_text()
    rows = {
        int(m.group(1)): (m.group(2).strip(), m.group(3))
        for m in re.finditer(r"^\| (\d\d) \| (.+?) \| \[`([\w/]+)`\]", syllabus, re.M)
    }
    assert len(rows) == N_LESSONS
    for d in _lesson_dirs():
        num, title = _notebook_title(d / "reading.ipynb")
        assert d.name.startswith(f"{num:02d}_"), f"{d}: heading says lesson {num}"
        assert rows[num] == (title, f"{d.parent.name}/{d.name}"), (
            f"SYLLABUS row {num} is out of sync with {d.parent.name}/{d.name}/reading.ipynb"
        )


def test_syllabus_references_resolve():
    keys = _bib_keys()
    syllabus = (ROOT / "SYLLABUS.md").read_text()
    for line in syllabus.splitlines():
        m = re.match(r"^\| \d\d \|.*\| ([^|]+) \|$", line)
        if not m:
            continue
        for key in (k.strip() for k in m.group(1).split(",")):
            if _KEY.match(key) and not key.startswith("mixed"):
                assert key in keys, f"SYLLABUS cites {key!r}, not in references.bib"


def test_every_citation_resolves():
    keys = _bib_keys()
    sources = [p for p in ROOT.rglob("*") if p.suffix in (".ipynb", ".md")]
    sources += [p for p in (REPO / "docs").rglob("*") if p.suffix in (".ipynb", ".md")]
    missing: dict[str, set[str]] = {}
    for path in sources:
        # _claude_assets/ documents the citation syntax itself; skip it.
        if {"_build", ".ipynb_checkpoints", "_claude_assets"} & set(path.parts):
            continue
        for group in _CITE.findall(_text(path)):
            for key in (k.strip() for k in group.split(",")):
                # Skip prose that only names the role, e.g. "`{cite:p}` keys ...".
                if _KEY.match(key) and key not in keys:
                    missing.setdefault(key, set()).add(str(path.relative_to(REPO)))
    assert not missing, f"citation keys missing from references.bib: {missing}"


def test_docs_book_uses_shipped_bibliography():
    config = (REPO / "docs" / "_config.yml").read_text()
    assert "../src/discopt/course/references.bib" in config


def test_docs_toc_files_exist():
    toc = (REPO / "docs" / "_toc.yml").read_text()
    entries = re.findall(r"(?:root|file):\s*(\S+)", toc)
    assert entries
    for entry in entries:
        candidates = [REPO / "docs" / f"{entry}{ext}" for ext in ("", ".md", ".ipynb")]
        assert any(c.is_file() for c in candidates), entry
