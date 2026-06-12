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

When any cp-* skill needs to locate `.cp/`, walk upward from cwd:

1. Check the current working directory for `.cp/`
2. If not found, move up one directory level and repeat
3. Stop at the git root (directory containing `.git/`) —
   never search above it
4. If `.cp/` is not found before the git root, report it as absent

This mirrors how `git` locates `.git/`.

**Monorepo scoping:** The first `.cp/` found wins. Placing `.cp/`
inside a subdirectory (e.g. `terraform/.cp/`) scopes the context
to that area only — walking up will find a root-level `.cp/` as
a fallback only when no scoped one exists.

---

## Rules

- Human triggers entry-point skills manually (no auto-execute)
- Agent must not commit without explicit human permission
- Skills never specify model names — only intent
- Canon additions require human approval
