---
name: cp-discover
description: >
  Explore a brownfield project and bootstrap .cp/ artifacts. Scans
  the project for token counts, identifies high-signal files, then
  collaboratively builds canon.md and memory/active.md with the
  human. Use when opening a project that has no .cp/ directory.
metadata:
  author: roschart
  version: "1.0"
---

# cp-discover

Explore a brownfield project and bootstrap `.cp/` artifacts through
iterative human-AI collaboration.

---

## Purpose

When joining an existing project that has no `.cp/` directory, the AI
needs to understand the codebase before it can help effectively.
`cp-discover` provides a structured exploration process: scan the
project, report findings, and collaboratively build the initial canon,
memory, and plan artifacts.

This is the **onboarding skill** — run it once per project to
establish the cognitive pairing foundation.

---

## Trigger

Run `cp-discover` when:

- Opening a project that has no `.cp/` directory
- `cp-hydrate` detects missing `.cp/` and suggests discovery
- The human explicitly wants to bootstrap cognitive pairing in a repo

Do NOT run if `.cp/` already exists — use `cp-hydrate` instead.

---

## Execution

### Phase 1 — Scan (non-interactive)

1. Run `scripts/count_tokens.py` on the project root
2. Identify high-signal files automatically:
    - README, CHANGELOG, CONTRIBUTING
    - Package manifests: package.json, pyproject.toml, Cargo.toml,
      go.mod, *.csproj, pom.xml
    - CI config: .github/workflows/, Makefile, Dockerfile
    - Existing docs: docs/, doc/, wiki/
    - Architecture hints: src/ structure, module boundaries
3. Display a **project scan report** to the human:

```
## Project Scan — <project-name>

Total: ~X tokens across N files

### Top directories by token weight
| Directory     | Tokens | Files | Notes          |
|---------------|--------|-------|----------------|
| src/          | 8,200  | 23    | Core code      |
| docs/         | 3,100  | 5     | Documentation  |
| tests/        | 2,400  | 12    | Test suite     |
| ...           | ...    | ...   | ...            |

### High-signal files detected
- README.md (450 tokens)
- package.json (120 tokens)
- .github/workflows/ci.yml (200 tokens)

### Fits in context?
Total project: ~X tokens
Recommended budget for discovery: ~30k tokens
Status: ✅ Fits entirely / ⚠️ Needs selective loading
```

4. Ask the human: "Which areas should I read first? Any folders
   I should skip?"

### Phase 2 — Explore (iterative)

For each area the human selects:

1. Read the files
2. Summarize what you found (2-3 sentences per area)
3. Propose candidate facts for canon (locked truths about the
   project)
4. Identify open questions to ask the human

After each area, ask:
- "Should I explore another area?"
- "Any of these canon candidates wrong or missing?"

### Phase 3 — Bootstrap

Once the human says "enough exploring":

1. Create `.cp/` directory structure:
    - `.cp/canon.md` — from confirmed canon candidates
    - `.cp/memory/active.md` — working context from exploration
    - `.cp/plans/` — empty (first plan after real work starts)
    - `.cp/checkpoints/` — empty (first checkpoint after real
      work)
    - `.cp/project.md` — optional; create only if the human
      has articulated project-level intent, constraints, or
      style during exploration. Ask before creating.
2. Display what was created
3. Suggest: "Run `cp-compact` after your first working session
   to capture state."

---

## Scripts

### count_tokens.py

Located at `skills/cp-discover/scripts/count_tokens.py`.

Counts tokens per file/directory using tiktoken (cl100k_base).
Falls back to word count × 1.3 if tiktoken is not installed.

Usage:
```bash
python3 scripts/count_tokens.py [path] [--top N] [--exclude dir1,dir2]
```

Default exclusions: .git, node_modules, vendor, dist, build,
__pycache__, .venv, .env, target, bin, obj

---

## Output

- On-screen: project scan report + iterative summaries
- Files created: `.cp/canon.md`, `.cp/memory/active.md`
- Nothing else committed — the human decides when to commit

---

## Anti-patterns

- **Boiling the ocean**: Don't try to read the entire repo. Focus
  on high-signal files first, expand only if the human asks.
- **Inventing canon**: Only propose facts you can verify from the
  code. The human confirms or rejects.
- **Skipping the human**: Every phase ends with a question. This
  is collaborative discovery, not autonomous analysis.
