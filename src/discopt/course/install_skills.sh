#!/usr/bin/env bash
# Install the discopt course's slash commands and assessor skill into a
# .claude/ directory.
#
# Prefer `discopt tutor install`, which also materializes a writable course/
# tree and seeds progress.yaml. This script only installs the Claude Code
# assets, and is mainly useful for a user-global install:
#
#   bash course/install_skills.sh           # install into ./.claude (project)
#   bash course/install_skills.sh --user    # install into ~/.claude (global)
#   bash course/install_skills.sh --force   # overwrite existing files
#
# Idempotent: safely re-runnable. Existing files are overwritten only with
# --force. discopt's own commands/agents (/formulate, /debug, /diagnose, ...)
# are installed separately with `discopt install-skills`.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$SCRIPT_DIR/_claude_assets"
if [[ ! -d "$SRC" ]]; then
  # A course/ copy materialized by `discopt tutor install` has no
  # _claude_assets/; fall back to the installed discopt-course package.
  PY="${PYTHON:-python3}"
  PKG="$("$PY" -c 'from discopt.course import package_root; print(package_root())' 2>/dev/null || true)"
  SRC="$PKG/_claude_assets"
  if [[ -z "$PKG" || ! -d "$SRC" ]]; then
    echo "error: can't find _claude_assets/ next to this script or in an installed" >&2
    echo "discopt-course package (set PYTHON to the interpreter that has it)." >&2
    exit 1
  fi
fi

DEST=".claude"
FORCE=0
for arg in "$@"; do
  case "$arg" in
    --user)  DEST="$HOME/.claude" ;;
    --force) FORCE=1 ;;
    *)       echo "unknown flag: $arg"; exit 1 ;;
  esac
done

mkdir -p "$DEST/commands/course" "$DEST/skills/course-assessor"

copy() {
  local src="$1" dst="$2"
  if [[ -e "$dst" && $FORCE -eq 0 ]]; then
    echo "  skip (exists): $dst"
  else
    cp "$src" "$dst"
    echo "  ok           : $dst"
  fi
}

echo "Installing course commands -> $DEST/commands/course/"
for f in "$SRC"/commands/course/*.md; do
  copy "$f" "$DEST/commands/course/$(basename "$f")"
done

echo "Installing course-assessor skill -> $DEST/skills/course-assessor/"
copy "$SRC/skills/course-assessor/SKILL.md" "$DEST/skills/course-assessor/SKILL.md"

echo "Done. Slash commands available: /course:lesson, /course:assess, /course:hint, /course:progress, /course:grade-writing, /course:cite-check"
