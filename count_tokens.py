#!/usr/bin/env python3
"""Count tokens for every text file in the project (excludes .git)."""

import os
import sys
from pathlib import Path

import tiktoken

EXCLUDED_DIRS = {".git"}
ENCODING = "cl100k_base"  # GPT-4 / Claude-compatible BPE
BINARY_CHECK_BYTES = 1024

enc = tiktoken.get_encoding(ENCODING)


def is_text_file(path: Path) -> bool:
    try:
        with path.open("rb") as f:
            chunk = f.read(BINARY_CHECK_BYTES)
        return b"\x00" not in chunk
    except OSError:
        return False


def count_tokens(path: Path) -> int:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        return len(enc.encode(text))
    except OSError:
        return 0


def walk(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS]
        for name in filenames:
            yield Path(dirpath) / name


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    root = root.resolve()

    results: list[tuple[int, Path]] = []
    total = 0

    for path in sorted(walk(root)):
        if not is_text_file(path):
            continue
        tokens = count_tokens(path)
        total += tokens
        results.append((tokens, path))

    col_w = max((len(str(p.relative_to(root))) for _, p in results), default=4)
    col_w = min(col_w, 80)

    print(f"\n{'File':<{col_w}}  {'Tokens':>8}")
    print("-" * (col_w + 10))
    for tokens, path in sorted(results, key=lambda x: -x[0]):
        rel = str(path.relative_to(root))
        print(f"{rel:<{col_w}}  {tokens:>8,}")

    print("-" * (col_w + 10))
    print(f"{'TOTAL':<{col_w}}  {total:>8,}")
    print(f"\nEncoding : {ENCODING}")
    print(f"Files    : {len(results)}")


if __name__ == "__main__":
    main()
