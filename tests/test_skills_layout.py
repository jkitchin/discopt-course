"""knowhow / Agent Skills compatibility of the packaged skills.

``knowhow add jkitchin/discopt-course`` discovers skills at
``skills/<name>/SKILL.md`` in the repository root. The root ``skills`` entry is a
symlink into the package data (``_claude_assets/skills``), so ``discopt tutor
install`` and knowhow install the same files. The slash commands stay out of
the knowhow layout on purpose: knowhow installs commands flat, which would turn
the namespaced ``/course:assess`` into a generic ``/assess``.
"""

import re
from pathlib import Path

import pytest

pytestmark = pytest.mark.smoke

_REPO_ROOT = Path(__file__).resolve().parents[1]
_SKILLS = _REPO_ROOT / "src" / "discopt" / "course" / "_claude_assets" / "skills"
_COMMANDS = _REPO_ROOT / "src" / "discopt" / "course" / "_claude_assets" / "commands"
# Agent Skills spec: lowercase letters, digits and single hyphens, <= 64 chars.
_SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def _frontmatter(path: Path) -> dict:
    yaml = pytest.importorskip("yaml")
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"{path} has no YAML frontmatter"
    return yaml.safe_load(text.split("---\n", 2)[1]) or {}


def _skill_dirs():
    return sorted(d for d in _SKILLS.iterdir() if (d / "SKILL.md").is_file())


def test_root_skills_link_resolves_to_package_data():
    link = _REPO_ROOT / "skills"
    if not link.exists():
        pytest.skip("not running from a source checkout")
    assert link.is_symlink(), "skills/ must be a symlink to the package data, not a copy"
    assert link.resolve() == _SKILLS.resolve()


def test_expected_skills_ship():
    assert {d.name for d in _skill_dirs()} >= {"course-assessor", "discopt-course"}


@pytest.mark.parametrize("skill_dir", _skill_dirs(), ids=lambda d: d.name)
def test_skill_frontmatter_meets_agent_skills_spec(skill_dir):
    fm = _frontmatter(skill_dir / "SKILL.md")
    assert fm.get("name") == skill_dir.name, "skill name must equal its directory"
    assert _SKILL_NAME_RE.match(skill_dir.name) and len(skill_dir.name) <= 64
    desc = fm.get("description", "")
    assert isinstance(desc, str) and 0 < len(desc) <= 1024
    assert re.search(r"\b(use|when|trigger)", desc, re.I), "description must say when to use it"
    compat = fm.get("compatibility")
    assert compat is None or (isinstance(compat, str) and len(compat) <= 500)


def test_no_skill_name_collides_with_a_command():
    # A skill and a command of the same name shadow each other in Claude Code.
    commands = {p.stem for p in _COMMANDS.rglob("*.md")}
    assert not commands & {d.name for d in _skill_dirs()}


def test_skills_have_no_nested_skill_or_symlinks():
    # knowhow skips directory symlinks inside a skill and lets a higher SKILL.md
    # hide nested ones, so each skill must be a plain, self-contained directory.
    for d in _skill_dirs():
        for p in d.rglob("*"):
            assert not p.is_symlink(), p
            if p.name == "SKILL.md":
                assert p.parent == d, p
