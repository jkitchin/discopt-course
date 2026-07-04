"""Packaging-level tests: entry point, namespace resolution, package data."""

import importlib.metadata
from importlib import resources

import pytest

pytestmark = pytest.mark.smoke


def test_cli_entry_point_resolves():
    eps = {ep.name: ep for ep in importlib.metadata.entry_points(group="discopt.cli")}
    assert "tutor" in eps, "discopt-course must register the 'tutor' subcommand"
    mod = eps["tutor"].load()
    assert callable(mod.add_subparser)
    assert callable(mod.run)


def test_namespace_import():
    import discopt
    import discopt.course

    # The plugin merges into the discopt namespace; both must be importable
    # side by side, and the packaged course-root resolver must be present.
    assert callable(discopt.course.package_root)


def test_course_root_ships_as_package_data():
    root = resources.files("discopt.course")
    assert root.joinpath("SYLLABUS.md").is_file()
    assert root.joinpath("progress.template.yaml").is_file()


def test_lesson_notebook_ships_as_package_data():
    reading = resources.files("discopt.course").joinpath(
        "basic", "01_intro_to_optimization", "reading.ipynb"
    )
    assert reading.is_file()


def test_slash_commands_ship_as_package_data():
    lesson = resources.files("discopt.course").joinpath(
        "_claude_assets", "commands", "course", "lesson.md"
    )
    assert lesson.is_file()
