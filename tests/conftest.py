"""Shared test configuration.

The course plugin is pure-stdlib (plus an optional lazy PyYAML import for
progress tracking), so — unlike the base repo's conftest — there is no JAX
or solver setup to perform here. Tests that touch progress.yaml guard their
own PyYAML dependency with ``pytest.importorskip("yaml")``.
"""
