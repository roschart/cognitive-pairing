# Architecture

## System Overview

Cognitive Pairing is a state management framework for long AI-human
sessions. The fundamental unit is not a message or a prompt — it is
a **shared artifact**: a structured, versioned, human-readable
document that captures operational state.

The system does not replace conversation. It manages the residue of
conversation so that future conversations can be effective.

Skills are designed for AI agents — the agent reads and executes
them directly. Both the human and the agent benefit from the
shared artifacts.

---

## The Degradation Problem

A long AI-human session generates:

- Decisions (valuable, must persist)
- Exploration (valuable at the time, mostly disposable later)
- Contradictions (must be resolved or explicitly parked)
- Abandoned paths (must be marked dead, not left ambiguous)
- Noise (irrelevant small talk, corrections, tangents)

Without active management, all of this accumulates in context.
The result is degraded reasoning: the AI (and the human) spend
cognitive budget processing history instead of generating insight.

---

## Directory Layout

Content and state management are separated at the directory level:

```text
project/
├── plan-<slug>.md          # Living plan (human-visible)
├── [other project files]
└── .cp/                    # State management layer
    ├── canon.md            # Locked facts (human-curated)
    ├── checkpoints/
    │   └── YYYY-MM-DD-label.md
    └── memory/
        ├── active.md
        └── archive/
```

`.cp/` is analogous to `.git/`: it holds infrastructure, not
content. The name stands for Cognitive Pairing.

`.cp/` can be nested: a subdirectory with its own distinct
workstream can carry its own `.cp/`. The nearest `.cp/` wins —
the same principle as `.gitignore`. In practice, one `.cp/` at
the project root covers almost every project.

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

### .cp/canon.md — Ground Truth

Locked facts that all reasoning must respect. The permanent
record of what is true and non-negotiable.

- **Location:** `.cp/canon.md`
- **Maintained by:** Human only — the agent never modifies it
- **Updated:** When a new fact becomes permanently locked
- **Purpose:** Prevent re-litigation of settled questions;
  provide stable ground truth across sessions
- **Answers:** What is permanently true?

### .cp/checkpoints/ — Stable State

Recoverable snapshots of the project at coherent milestones.

- **Maintained by:** AI-generated, human-reviewed
- **Created at:** End of meaningful work phase, before pivots,
  before long pauses
- **Immutable once created:** A checkpoint is never edited
- **Answers:** Where are we now?

### .cp/memory/active.md — Operational Context

The minimal high-value context needed to reason effectively
right now.

- **Maintained by:** AI-generated via `cp-compact`, human-trimmed
- **Replaced:** At each compaction cycle; previous version
  archived to `.cp/memory/archive/YYYY-MM-DD.md`
- **Purpose:** Reduce cognitive load by eliminating resolved and
  irrelevant content
- **Answers:** What do we need right now?

---

## Information Flow

```text
              ┌─────────────────────────────┐
              │       cp-hydrate            │
              │  reads .cp/ artifacts       │
              │  shows alignment summary    │
              └──────────────┬──────────────┘
                             │
              ┌──────────────▼──────────────┐
              │       Active Session         │
              │  (conversation + work)       │
              └──────────────┬──────────────┘
                             │
               ┌─────────────▼─────────────┐
               │       cp-compact          │
               │  noise reduction          │
               │  constraint extraction    │
               └─────────────┬─────────────┘
                             │
          ┌──────────────────┼──────────────┐
          │                  │              │
 ┌────────▼───────┐ ┌───────▼──────┐ ┌─────▼──────┐
 │ .cp/memory/    │ │ .cp/         │ │ .cp/       │
 │ active.md      │ │ checkpoints/ │ │ canon.md   │
 │ (replaced)     │ │ (appended)   │ │ (stable)   │
 └────────────────┘ └──────────────┘ └────────────┘
```

---

## Lifecycle of a Working Session

```text
1. Start session
   → agent runs cp-hydrate automatically
   → reads canon.md + latest checkpoint + memory/active.md
   → shows alignment summary on screen

2. Work
   → Explore, iterate, decide, build
   → No state management needed during flow

3. Compaction trigger (when any of these are true):
   → More than ~30 exchanges without compaction
   → memory/active.md exceeds ~1500 words
   → About to make a major direction change
   → Preparing to stop work for the day
   → Reached a stable milestone

4. cp-compact
   → Compress current session into .cp/memory/active.md
   → Archive previous memory to .cp/memory/archive/

5. cp-checkpoint (only if a genuine milestone was reached)
   → Create .cp/checkpoints/YYYY-MM-DD-label.md

6. Optional: update plan-<slug>.md
   → Mark completed tasks
   → Add new tasks discovered
   → Park or remove obsolete ideas

7. cp-session-end
   → Structured wrap-up: compact + optional checkpoint + delta

8. Conversation reset (deliberate)
   → Start fresh session
   → cp-hydrate loads context automatically
```

---

## Separation of Concerns

```text
plan-slug.md          → INTENT  Where we are going
.cp/canon.md          → TRUTH   What is permanently locked
.cp/checkpoints/      → STATE   Where we are now
.cp/memory/active.md  → CONTEXT What we need to reason now
```

These are NOT redundant. Each serves a different cognitive
function:

- Canon is permanent; memory is ephemeral
- Plan is aspirational; checkpoints are factual
- You can update the plan without checkpointing
- You can compact memory without checkpointing
- Canon survives every compact and hydrate cycle unchanged

---

## Human vs AI Responsibilities

### Human-curated (agent never modifies)

- `plan-<slug>.md` — human makes final calls on direction
- `.cp/canon.md` — human decides what is permanently true
- Checkpoint review — human validates before committing
- Prune approvals — human decides what is truly dead

### AI-generated (human reviews)

- `.cp/checkpoints/` content
- `.cp/memory/active.md` content
- Alignment summaries (shown on screen during hydrate)

### Collaborative (AI drafts, human edits)

- Plan updates after sessions
- Canon additions (AI suggests, human approves)
- Memory trimming (AI compacts, human prunes further)

---

## Key Design Constraints

1. **Markdown-only** — every artifact is readable without tooling
2. **Git-native** — all artifacts are versionable and diffable
3. **No narrative** — "first we discussed X, then Y" is noise;
   only state, decisions, and direction survive compaction
4. **Operational, not historical** — artifacts answer "what now",
   not "what happened"
5. **Skills serve both parties** — the agent executes the skill,
   the human reviews the output, both benefit from the artifacts
