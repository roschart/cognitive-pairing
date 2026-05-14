# Artifact Specification

Each artifact type has a defined structure, purpose, and lifecycle.
Templates for all types are in [`../templates/`](../templates/).

---

## plan.md

**Purpose:** Living declaration of intent.

**Owner:** Human-curated.

**Lifecycle:** Created once at project start. Never replaced. Sections
evolve: active tasks move to completed; ideas move to parked or pruned.

**When to update:**
- Direction changes
- New goals identified
- Tasks completed or abandoned
- Major decisions affect scope

**Structure:**

```markdown
# Plan: <project name>

## Status
Current phase. Last meaningful update date.

## Goals
What we are trying to achieve. Ordered by priority.

## Constraints
Hard limits. Non-negotiables. Things we cannot change.

## Current Direction
Where we are headed right now. One clear paragraph.

## Active Tasks
- [ ] task — brief description

## Completed Tasks
- [x] task — date completed

## Parked Ideas
Ideas not abandoned, just deferred. Must include a trigger condition:
"Revisit when X".

## Explicitly Pruned
Ideas we tried and rejected. Brief reason. Prevents re-opening.
```

**Anti-patterns:**

- Using plan.md as a conversation transcript
- Deleting completed sections instead of marking done
- Letting it grow without pruning (becomes noise)

---

## checkpoints/YYYY-MM-DD-vN.md

**Purpose:** Stable, recoverable state at a coherent milestone.

**Owner:** AI-generated, human-reviewed.

**Lifecycle:** Immutable once committed. Never edited. Accumulate over
time. Old checkpoints are reference material, not active state.

**Naming convention:**

- `2026-05-14-v0.1.md` — date + semantic version
- `2026-05-14-pathfinder-act2.md` — date + label when version is
  ambiguous

**When to create:**

- Reached a stable milestone
- About to make a major pivot
- Before a long pause (days without work)
- After resolving a blocking issue
- Before an experiment that might break things

**Structure:**

```markdown
# Checkpoint: <label> — YYYY-MM-DD vN

## Current State
Factual, concise description of where the project stands.
No narrative. No "first we did X". Just: what is true right now.

## Resolved Decisions
Decisions that are made and locked. Not for reconsideration.

## Active Constraints
Hard limits that govern all current and future work.

## Current Direction
What we are working toward from this point.

## Pending Work
What remains to be done. Ordered by priority.

## Open Questions
Things unresolved but not currently blocking.

## Blocking Issues
If any: what is preventing progress and why.

## Context Tags
#tag1 #tag2 (for search and retrieval)
```

**What NOT to include:**

- History of how we got here
- Rejected alternatives (unless they are constraints now)
- Conversational context
- Emotional notes ("this was hard")

---

## memory/active.md

**Purpose:** Minimal operational context to reason effectively right now.

**Owner:** AI-generated via `/compact`, human-trimmed.

**Lifecycle:** Replaced at each compaction cycle. Previous version
archived to `memory/archive/YYYY-MM-DD.md`.

**Goal:** Should fit in a single AI context injection. 500–1500 words max.
If it grows beyond that, it needs pruning.

**Structure:**

```markdown
# Working Memory — YYYY-MM-DD

## Active Goals
What we are trying to achieve RIGHT NOW. Not long-term vision.

## Canon
Facts that are established, locked, and cannot change.
This is the ground truth that all reasoning must respect.

## Active Constraints
Hard limits on current work. Technical, creative, logistical.

## Current Focus
The specific problem or task we are actively working on.

## Key Relationships
Important dependencies, connections, tensions between elements.

## Unresolved Problems
Open problems that affect current work. Not wishes — actual blockers
or known risks.

## Recent Decisions
Decisions made in recent sessions that are still active.
(Not historical archive — just "still matters now".)

## Do Not Revisit
Ideas explicitly abandoned. Brief reason for each.
This section prevents re-opening closed questions.
```

**What NOT to include:**

- Resolved decisions (move to checkpoint)
- History of the session
- Long explanations of why (link to decisions/ instead)
- Completed tasks

---

## decisions/NNN-title.md

**Purpose:** Permanent rationale log for significant choices (ADR-style).

**Owner:** Human-written (or AI-drafted, human reviewed).

**Lifecycle:** Immutable once written. Status can change to "superseded"
but content stays.

**Naming:** `001-use-markdown-artifacts.md`, `002-no-relational-db.md`

**Structure:**

```markdown
# NNN: <decision title>

## Status
Accepted | Superseded by NNN | Proposed

## Context
What situation forced this decision. What options existed.

## Decision
What we chose and why.

## Consequences
What this enables. What this forecloses. What debt it creates.

## Alternatives Considered
Brief note on rejected alternatives and why.
```

---

## snapshots/YYYY-MM-DDTHHMM.md

**Purpose:** Raw, unfiltered capture before a risky or experimental change.

**Owner:** AI-generated via `/snapshot`.

**Lifecycle:** Disposable. Can be pruned once the experiment resolves.
In many projects, git commits serve this purpose instead.

**Structure:**

```markdown
# Snapshot: <label> — YYYY-MM-DDTHH:MM

## Trigger
Why this snapshot was taken.

## Current State (Raw)
Unfiltered description of where things stand.
Include experiments, broken ideas, uncertain paths.

## Active Experiments
What is being tried right now that may or may not work.

## Abandoned Branches (This Session)
Ideas tried and rejected in this session, not yet in memory.

## Notes
Anything that might matter for recovery.
```

---

## Hydration Prompt

Not a stored artifact but a generated artifact used at session start.

**Purpose:** Reconstruct operational context in a new AI session with
minimal noise.

**Owner:** AI-generated via `/hydrate`.

**Structure:**

```markdown
# Session Context — YYYY-MM-DD

## Project
<project name and one-sentence description>

## Current State
<from latest checkpoint: current state + direction>

## Active Goals
<from memory/active.md>

## Canon
<from memory/active.md>

## Constraints
<merged from checkpoint + memory>

## Current Focus
<from memory/active.md — the specific task>

## Do Not Revisit
<from memory/active.md — closed questions>

## Relevant Files
<links to plan.md, latest checkpoint, memory/active.md>
```

The hydration prompt is pasted at the start of a new AI session to
replace the entire previous conversation history.
