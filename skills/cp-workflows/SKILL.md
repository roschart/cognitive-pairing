---
name: cp-workflows
description: Foundation rules for cognitive-pairing framework. Load this skill when using any cp-* skill (cp-hydrate, cp-brainstorming, cp-session-end, etc.) to understand the session model and artifact coherence principles.
---

# cp-workflows

Foundation rules for the cognitive-pairing framework.

**Load this skill when using any cp-* skill** (cp-hydrate,
cp-brainstorming, cp-session-end, etc.) to ensure you understand
the session model, artifact hierarchy, and context coherence
principles.

---

## Session Model

```
cp-hydrate (start) → work → cp-session-end (close)
```

- **cp-hydrate** loads context from `.cp/` at session start
- **cp-session-end** persists state at session close
- These are the two **human entry points** — most other skills
  are orchestrated internally

---

## Context Coherence

**cp-hydrate loads context ONCE at session start.**

When working during a session:
- ✅ Use the context loaded by cp-hydrate (canon, project,
  active memory, plans)
- ❌ Do not reread `.cp/` files directly
- ❓ If you need information not in session context, ask the
  human instead of reading files

---

## Sub-Agent Pattern

All `.cp/` file reading happens via sub-agents:
- `.cp/` files never enter main context
- Main agent receives structured output only (≤600 words)
- Skills specify intent ("cheapest/fastest available"), not
  model names

---

## Artifact Hierarchy

```
Canon > Project > Plan > Memory > Checkpoint
```

- **Canon**: immutable ground truth (human-owned)
- **Project**: identity, intent, constraints, scope
- **Plan**: current workstream goals and tasks
- **Memory**: session-to-session operational state
- **Checkpoint**: milestone snapshot

---

## `.cp/` Resolution

**Always use the `scripts/find-cp-dir.sh` script** (bundled with
this skill) to resolve the nearest `.cp/` directory. Never use
`find` searching downward from the repo root — that bypasses
monorepo scoping and picks the wrong context.

Run it from the skill's base directory (provided in skill context):

```bash
CP_DIR=$(bash scripts/find-cp-dir.sh)
```

The script walks **upward** from `$PWD` (or a given path) and
returns the first `.cp/` it finds. Exit codes:

| Code | Meaning |
|------|---------|
| `0` | Found — path printed to stdout |
| `1` | Not found — stopped at `.git/` boundary |
| `2` | Not found — reached `$HOME` with no git root |

Exit code `1` → `.cp/` absent at this scope; suggest `cp-discover`.
Exit code `2` → not inside a git repo; inform the human.

**Monorepo scoping:** The first `.cp/` found wins. A `.cp/` inside
a subdirectory (e.g. `docs/pci/vikingcloud-templates/.cp/`) scopes
context to that area. The root-level `.cp/` is only reached if no
scoped one exists above the cwd.

---

## Rules

- Human triggers entry-point skills manually (no auto-execute)
- Agent must not commit without explicit human permission
- Skills never specify model names — only intent
- Canon additions require human approval
