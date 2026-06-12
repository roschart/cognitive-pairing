#!/usr/bin/env bash
# find-cp-dir.sh — Resolve the nearest .cp/ directory.
#
# Walk upward from the current directory (or $1 if provided) until:
#   - A .cp/ directory is found  → print its path and exit 0
#   - A .git/ directory is found → .cp/ is absent at this scope; exit 1
#   - $HOME is reached           → .cp/ does not exist; exit 2
#
# Exit codes:
#   0 — found; path printed to stdout
#   1 — not found (hit .git/ boundary before finding .cp/)
#   2 — not found (reached $HOME without finding .cp/ or .git/)

dir="${1:-$PWD}"
dir="$(realpath "$dir")"

while true; do
    if [[ -d "$dir/.cp" ]]; then
        echo "$dir/.cp"
        exit 0
    fi

    if [[ -d "$dir/.git" ]]; then
        echo "No .cp/ found (stopped at git root: $dir)" >&2
        exit 1
    fi

    if [[ "$dir" == "$HOME" || "$dir" == "/" ]]; then
        echo "No .cp/ found (reached $HOME without a git root)" >&2
        exit 2
    fi

    dir="$(dirname "$dir")"
done
