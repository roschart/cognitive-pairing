# Architecture

## System Overview

Cognitive Pairing is a state management framework for long AI-human
sessions. The fundamental unit is not a message or a prompt — it is a
**shared artifact**: a structured, versioned, human-readable document
that captures operational state.

The system does not replace conversation. It manages the residue of
conversation so that future conversations can be effective.

---

## The Degradation Problem

A long AI-human session generates:

- Decisions (valuable, must persist)
- Exploration (valuable at the time, mostly disposable later)
- Contradictions (must be resolved or explicitly parked)
- Abandoned paths (must be marked dead, not left ambiguous)
- Noise (irrelevant small talk, corrections, tangents)

Without active management, all of this accumulates in context. The
result is degraded reasoning: the AI (and the human) spend cognitive
budget processing history instead of generating insight.

---

## Directory Layout

Content and state management are separated at the directory level:

```text
project/
├── plan-<slug>.md          # Living plan (content layer, human-visible)
├── [other project files]
└── .cp/                    # State management layer (infrastructure)
    ├── checkpoints/
    │   └── YYYY-MM-DD-label.md
    ├── memory/
    │   ├── active.md
    │   └── archive/
    ├── decisions/
    │   └── NNN-title.md
    └── snapshots/
        └── YYYY-MM-DDTHHMM-label.md
```

`.cp/` is analogous to `.git/`: it holds infrastructure, not content.
The name stands for Cognitive Pairing.

`.cp/` can be nested: a subdirectory with its own distinct workstream
can carry its own `.cp/`. The nearest `.cp/` wins — the same principle
as `.gitignore`. In practice, one `.cp/` at the project root covers
almost every project.

---

## Artifact Model

Four artifact types, each with a distinct purpose and lifecycle:

### plan-slug.md — Intent

The living declaration of goals, direction, and tasks.

- **Location:** Project root (content layer, not inside `.cp/`)
- **Maintained by:** Human (with AI assistance)
- **Updated:** Continuously as direction changes
- **Never replaced:** One file per workstream; evolves in place
- **Multiple plans:** Parallel workstreams each get their own slug
- **Answers:** Where are we going?

### .cp/checkpoints/ — Stable State

Recoverable snapshots of the project at coherent milestones.

- **Maintained by:** AI-generated, human-reviewed
- **Created at:** End of meaningful work phase, before pivots, before
  long pauses
- **Immutable once created:** A checkpoint is never edited
- **Answers:** Where are we now?

### .cp/memory/active.md — Operational Context

The minimal high-value context needed to reason effectively right now.

- **Maintained by:** AI-generated via `cp-compact`, human-trimmed
- **Replaced:** At each compaction cycle; previous version archived to
  `.cp/memory/archive/YYYY-MM-DD.md`
- **Purpose:** Reduce cognitive load by eliminating resolved and
  irrelevant content
- **Answers:** What do we need right now?

### .cp/snapshots/ — Raw Captures

Unfiltered dumps of state before risky or experimental work.

- **Maintained by:** AI-generated via `cp-snapshot`
- **Used for:** Recovery if an experiment fails; retrospective analysis
- **Disposable:** Can be pruned after work is stable
- **Answers:** What exactly was happening at this moment?

---

## Information Flow

```text
                   ┌─────────────────────────────┐
                   │         Active Session        │
                   │  (conversation + exploration) │
                   └──────────────┬────────────────┘
                                  │
                    ┌─────────────▼──────────────┐
                    │        cp-compact           │
                    │  noise reduction            │
                    │  decision extraction        │
                    │  constraint identification  │
                    └─────────────┬──────────────┘
                                  │
             ┌────────────────────┼────────────────────┐
             │                    │                    │
    ┌────────▼───────┐  ┌────────▼───────┐  ┌────────▼───────┐
    │ .cp/memory/    │  │ .cp/checkpoints│  │ .cp/decisions/ │
    │ active.md      │  │ (stable state) │  │  (ADR log)     │
    └────────┬───────┘  └────────────────┘  └────────────────┘
             │
    ┌────────▼───────┐
    │   cp-hydrate   │
    │  (reconstruct  │
    │   new session) │
    └────────────────┘
```

---

## Lifecycle of a Working Session

```text
1. Start session
   → cp-hydrate from latest checkpoint + .cp/memory/active.md
   → Paste hydration prompt into AI context

2. Work
   → Explore, iterate, decide, build
   → No state management needed during flow

3. Compaction trigger (choose one):
   → Context feels heavy or noisy
   → About to make a major pivot
   → Preparing to stop work
   → Hit a stable milestone

4. cp-compact
   → Compress current session into .cp/memory/active.md
   → Archive previous memory to .cp/memory/archive/

5. cp-checkpoint (if stable milestone)
   → Create .cp/checkpoints/YYYY-MM-DD-label.md
   → Review and trim if needed

6. Optional: update plan-<slug>.md
   → Mark completed tasks
   → Add new tasks discovered
   → Park or remove obsolete ideas

7. Reset conversation (deliberate)
   → Start fresh session
   → cp-hydrate with new checkpoint + memory

8. Continue
```

---

## Separation of Concerns

```text
plan-slug.md          → INTENT    What we are trying to build/achieve
.cp/checkpoints/      → STATE     What actually exists and has been decided
.cp/memory/active.md  → CONTEXT   What we need to know to work right now
.cp/snapshots/        → BACKUP    What was happening before a risky change
.cp/decisions/        → RATIONALE Why we made each important choice
```

These are NOT redundant. Each serves a different cognitive function:

- You can update the plan without creating a checkpoint (direction
  changed, state not yet stable).
- You can create a checkpoint without updating the plan (milestone
  reached, direction unchanged).
- You can compact memory without checkpointing (session cleanup,
  not yet a stable milestone).
- You can snapshot without compacting (just saving a moment, not
  cleaning anything).

---

## Human vs AI Responsibilities

### Human-curated (must not be auto-overwritten)

- `plan-<slug>.md` — human makes final calls on goals and direction
- `.cp/decisions/` — human writes the rationale
- Checkpoint review — human validates before committing
- Prune approvals — human decides what is truly dead

### AI-generated (can be auto-created, human reviews)

- `.cp/checkpoints/` content
- `.cp/memory/active.md` content
- `.cp/snapshots/` content
- Hydration prompts

### Collaborative (AI drafts, human edits)

- Plan updates after sessions
- Decision rationale from complex discussions
- Memory trimming (AI compacts, human prunes further)

---

## Key Design Constraints

1. **Markdown-only** — every artifact must be readable without tooling
2. **Git-native** — all artifacts are versionable and diffable
3. **No narrative summaries** — "first we discussed X, then Y" is noise;
   only state, decisions, and direction survive compaction
4. **Operational, not historical** — artifacts answer "what now", not
   "what happened"
5. **Composable** — hydration prompts reference artifacts, not duplicate
   them
