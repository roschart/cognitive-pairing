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

All management artifacts live inside `.cp/`. Project content
lives outside it:

```text
project/
├── [project content files]
└── .cp/                    # State management layer
    ├── project.md          # Project declaration (intent)
    ├── canon.md            # Locked facts (human-curated)
    ├── plans/
    │   ├── plan-<slug>.md  # Living plans
    │   └── archive/        # Completed plans
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

Five artifact types, each with a distinct purpose and lifecycle:

### .cp/project.md — Intent

The master declaration of what the project is, why it exists,
and what constraints govern all work.

- **Location:** `.cp/project.md`
- **Maintained by:** Human (created once, rarely refined)
- **Updated:** Only when intent, constraints, or style change
- **Answers:** What are we building and why?

### .cp/plans/plan-slug.md — Work

The living declaration of goals, direction, and tasks.

- **Location:** `.cp/plans/` (completed plans archived to
  `.cp/plans/archive/`)
- **Maintained by:** Human (with AI assistance)
- **Updated:** Continuously as direction changes
- **Never replaced:** One file per workstream; evolves in place
- **Multiple plans:** Parallel workstreams each get their own
  slug
- **Answers:** How are we doing it and how much is left?

### .cp/canon.md — Ground Truth

Locked facts that all reasoning must respect. The permanent
record of what is true and non-negotiable.

- **Location:** `.cp/canon.md`
- **Maintained by:** Human approves — the agent proposes,
  the human confirms before any change is written
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
              │  (project, canon, plans,    │
              │   checkpoint, memory)       │
              │  shows alignment summary    │
              └──────────────┬──────────────┘
                             │
              ┌──────────────▼──────────────┐
              │       Active Session        │
              │  (conversation + work)      │
              └──────────────┬──────────────┘
                             │
              ┌──────────────▼──────────────┐
              │     cp-session-end          │
              │  compact → canon review     │
              │  → checkpoint → plan        │
              └──────────────┬──────────────┘
                             │
          ┌──────────────────┼──────────────┐
          │                  │              │
 ┌────────▼───────┐ ┌───────▼──────┐ ┌─────▼──────┐
 │ .cp/memory/    │ │ .cp/         │ │ .cp/       │
 │ active.md      │ │ checkpoints/ │ │ canon.md   │
 │ (replaced)     │ │ (appended)   │ │ (approved) │
 └────────────────┘ └──────────────┘ └────────────┘
```

---

## Lifecycle of a Working Session

The human interacts with two bookends: `cp-hydrate` at session
start and `cp-session-end` at session close. Everything else is
either embedded in those two skills or proposed by the agent
during work.

```text
1. Start session
   → human runs cp-hydrate
   → reads project.md + canon.md + latest checkpoint
     + memory/active.md + active plans
   → shows alignment summary on screen
   → checks artifact health (suggests cp-prune if bloated)

2. Work
   → Explore, iterate, decide, build
   → Agent may propose cp-checkpoint at milestones
   → Agent may propose plan updates when tasks change
   → No skills need to be called manually during work

3. End session
   → human runs cp-session-end, which sequences:
     a. cp-compact → compress session into memory/active.md
     b. canon review → propose additions (human approves)
     c. cp-checkpoint → create if milestone reached (optional)
     d. cp-plan → update plan if tasks changed (optional)
     e. session delta → show structured summary on screen
```

### Skill Trigger Summary

| Skill | Triggered by | Frequency |
|---|---|---|
| cp-hydrate | Human (session start) | Every session |
| cp-session-end | Human (session close) | Every session |
| cp-compact | Embedded in session-end | Automatic |
| cp-checkpoint | Agent proposes, human confirms | At milestones |
| cp-plan | Agent proposes, human confirms | When tasks change |
| cp-project | Human (project inception) | Once per project |
| cp-prune | Hydrate suggests when needed | Rare |
| cp-discover | Human (once per project) | One-time |

---

## Separation of Concerns

```text
.cp/project.md        → INTENT    What we are building and why
.cp/plans/            → WORK      How we do it and how much is left
.cp/canon.md          → TRUTH     What is permanently locked
.cp/checkpoints/      → STATE     Where we are now
.cp/memory/active.md  → CONTEXT   What we need to reason now
```

These are NOT redundant. Each serves a different cognitive
function:

- Project is stable; plans evolve constantly
- Canon is permanent; memory is ephemeral
- Plans are aspirational; checkpoints are factual
- You can update a plan without checkpointing
- You can compact memory without checkpointing
- Canon survives every compact and hydrate cycle unchanged
- Project frames all work; plans decompose it

---

## Human vs AI Responsibilities

### Human-curated (agent proposes, human approves)

- `.cp/project.md` — human declares project intent and
  constraints
- `.cp/plans/plan-<slug>.md` — human makes final calls on
  direction
- `.cp/canon.md` — agent proposes additions at session end,
  human approves before anything is written
- Checkpoint review — human validates before committing
- Prune approvals — human decides what is truly dead

### AI-generated (human reviews)

- `.cp/checkpoints/` content
- `.cp/memory/active.md` content
- Alignment summaries (shown on screen during hydrate)

### Collaborative (AI drafts, human edits)

- Plan updates after sessions
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
