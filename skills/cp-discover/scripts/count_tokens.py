#!/usr/bin/env python3
"""Scan a project and report token counts per directory and file.

Used by the cp-discover skill to assess what fits in context.
Falls back to word-based estimation if tiktoken is not installed.
"""

import argparse
import os
import sys
from pathlib import Path

DEFAULT_EXCLUSIONS = {
    ".git",
    "node_modules",
    "vendor",
    "dist",
    "build",
    "__pycache__",
    ".venv",
    ".env",
    "target",
    "bin",
    "obj",
    ".next",
    ".nuxt",
    "coverage",
    ".tox",
}

BINARY_CHECK_BYTES = 1024

# Try to use tiktoken for accurate counts, fall back to word estimation
try:
    import tiktoken

    _enc = tiktoken.get_encoding("cl100k_base")

    def _count_tokens(text: str) -> int:
        return len(_enc.encode(text))

    TOKEN_METHOD = "tiktoken (cl100k_base)"
except ImportError:
    def _count_tokens(text: str) -> int:
        # Rough approximation: 1 token ≈ 0.75 words
        return int(len(text.split()) * 1.3)

    TOKEN_METHOD = "word estimate (×1.3)"


def is_text_file(path: Path) -> bool:
    """Check if a file is likely text (not binary)."""
    try:
        with path.open("rb") as f:
            chunk = f.read(BINARY_CHECK_BYTES)
        return b"\x00" not in chunk
    except OSError:
        return False


def count_file_tokens(path: Path) -> int:
    """Count tokens in a single file."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        return _count_tokens(text)
    except OSError:
        return 0


def walk_project(root: Path, exclusions: set[str]):
    """Walk project tree, skipping excluded directories."""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in exclusions]
        for name in filenames:
            yield Path(dirpath) / name


def scan(root: Path, exclusions: set[str]) -> dict:
    """Scan the project and return structured results."""
    file_results: list[tuple[int, Path]] = []
    dir_totals: dict[str, dict] = {}

    for path in sorted(walk_project(root, exclusions)):
        if not is_text_file(path):
            continue
        tokens = count_file_tokens(path)
        file_results.append((tokens, path))

        # Aggregate by top-level directory
        rel = path.relative_to(root)
        top_dir = rel.parts[0] if len(rel.parts) > 1 else "."
        if top_dir not in dir_totals:
            dir_totals[top_dir] = {"tokens": 0, "files": 0}
        dir_totals[top_dir]["tokens"] += tokens
        dir_totals[top_dir]["files"] += 1

    total_tokens = sum(t for t, _ in file_results)

    return {
        "files": file_results,
        "directories": dir_totals,
        "total_tokens": total_tokens,
        "total_files": len(file_results),
        "method": TOKEN_METHOD,
    }


def print_report(results: dict, root: Path, top_n: int):
    """Print a formatted scan report."""
    print(f"\n## Project Scan — {root.name}")
    print(f"\nTotal: ~{results['total_tokens']:,} tokens across "
          f"{results['total_files']} files")
    print(f"Method: {results['method']}")

    # Top directories
    print("\n### Top directories by token weight")
    print(f"{'Directory':<30} {'Tokens':>8} {'Files':>6}")
    print("-" * 48)

    sorted_dirs = sorted(
        results["directories"].items(),
        key=lambda x: x[1]["tokens"],
        reverse=True,
    )
    for dirname, info in sorted_dirs[:top_n]:
        print(f"{dirname:<30} {info['tokens']:>8,} {info['files']:>6}")

    # Top files
    print(f"\n### Top {top_n} files by token count")
    print(f"{'File':<50} {'Tokens':>8}")
    print("-" * 60)

    sorted_files = sorted(results["files"], key=lambda x: -x[0])
    for tokens, path in sorted_files[:top_n]:
        rel = str(path.relative_to(root))
        if len(rel) > 49:
            rel = "..." + rel[-46:]
        print(f"{rel:<50} {tokens:>8,}")

    # Context fit assessment
    total = results["total_tokens"]
    print(f"\n### Fits in context?")
    print(f"Total project: ~{total:,} tokens")
    print(f"Recommended budget for discovery: ~30,000 tokens")
    if total <= 30_000:
        print("Status: ✅ Fits entirely — can load full project")
    elif total <= 100_000:
        print("Status: ⚠️  Needs selective loading — pick key areas")
    else:
        print("Status: ❌ Too large — must focus on specific modules")

    print()


def main():
    parser = argparse.ArgumentParser(
        description="Count tokens per file/directory in a project"
    )
    parser.add_argument(
        "path", nargs="?", default=".",
        help="Project root to scan (default: current directory)"
    )
    parser.add_argument(
        "--top", type=int, default=15,
        help="Number of top items to show (default: 15)"
    )
    parser.add_argument(
        "--exclude", type=str, default="",
        help="Comma-separated additional directories to exclude"
    )

    args = parser.parse_args()
    root = Path(args.path).resolve()

    exclusions = DEFAULT_EXCLUSIONS.copy()
    if args.exclude:
        exclusions.update(d.strip() for d in args.exclude.split(","))

    if not root.is_dir():
        print(f"Error: {root} is not a directory", file=sys.stderr)
        sys.exit(1)

    results = scan(root, exclusions)
    print_report(results, root, args.top)


if __name__ == "__main__":
    main()
