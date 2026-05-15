# Artifact Specification

Each artifact type has a defined structure, purpose, and lifecycle.

---

## plan.md

**Purpose:** Living declaration of intent.

**Owner:** Human-curated.

**Lifecycle:** Created once at project start. Never replaced.
Sections evolve: active tasks move to completed; ideas move to
parked or pruned.

**When to update:**
- Direction changes
- New goals identified
- Tasks completed or abandoned
- Major decisions affect scope

**Structure:**

```markdown
# Plan: <project name>

## Context
2-5 bullet summary of the current situation.

## Decisions
Decisions already made that constrain the plan.
Format: - **decision**: one-line rationale

## Tasks
Committed scope. Indented checkboxes for hierarchy.
States: [ ] pending  [-] in progress  [x] done · ✓ YYYY-MM-DD

## Potential Work
Ideas not yet committed. Each has a promotion condition.

## Next Session
> Paused: YYYY-MM-DD
1-3 specific pickup points.
```

**Anti-patterns:**

- Using plan.md as a conversation transcript
- Deleting completed sections instead of marking done
- Letting it grow without pruning (becomes noise)

---

## .cp/canon.md

**Purpose:** Permanent ground truth. Locked facts that all
reasoning must respect.

**Owner:** Human-curated only. The agent reads this file but
never modifies it.

**Lifecycle:** Grows slowly. Items are added when a fact becomes
permanently locked. Items are removed only when genuinely
obsolete (rare).

**When to update:**
- A decision is made that should never be re-litigated
- A project invariant is established
- A constraint becomes permanent (not session-specific)

**Structure:**

```markdown
# Canon

Locked facts for this project. Ground truth that all reasoning
must respect. Only the human adds or removes entries.

## Project

- <project-level locked fact>
- <project-level locked fact>

## Technical

- <technical locked fact>

## Boundaries

- <scope boundary or non-negotiable constraint>
```

**What belongs in canon vs memory:**
- Canon: permanent facts that survive across all sessions
- Memory (Active Constraints): session-specific or temporary
  constraints that may change

**What belongs in canon vs checkpoint (Resolved Decisions):**
- Canon: the WHAT — "The database is PostgreSQL"
- Checkpoint: the snapshot — what was true at that moment

---

## .cp/checkpoints/YYYY-MM-DD-label.md

**Purpose:** Stable, recoverable state at a coherent milestone.

**Owner:** AI-generated, human-reviewed.

**Lifecycle:** Immutable once committed. Never edited. Accumulate
over time. Old checkpoints are reference material, not active
state.

**Naming convention:**

- `2026-05-14-v0.1.md` — date + semantic version
- `2026-05-14-pathfinder-act2.md` — date + label

**When to create:**

- Reached a stable milestone
- About to make a major pivot
- Before a long pause (days without work)
- After resolving a blocking issue

**Structure:**

```markdown
# Checkpoint: <label> — YYYY-MM-DD

## Current State
Factual, concise. What is true right now. No narrative.

## Resolved Decisions
Decisions made and locked. Present-tense statements.

## Active Constraints
Hard limits that govern all future work.

## Current Direction
What we are working toward from this point.

## Pending Work
Ordered by priority.

## Open Questions
Things unresolved but not currently blocking.

## Context Tags
#tag1 #tag2
```

**What NOT to include:**

- History of how we got here
- Rejected alternatives (unless they are constraints now)
- Conversational context

---

## .cp/memory/active.md

**Purpose:** Minimal operational context to reason effectively
right now.

**Owner:** AI-generated via `cp-compact`, human-trimmed.

**Lifecycle:** Replaced at each compaction cycle. Previous
version archived to `memory/archive/YYYY-MM-DD.md`.

**Goal:** Should fit in a single AI context injection. 500–1500
words max. If it grows beyond that, it needs pruning.

**Structure:**

```markdown
# Working Memory — YYYY-MM-DD

## Active Goals
What we are trying to achieve RIGHT NOW.

## Active Constraints
Hard limits on current work. Session-specific or temporary.
(Permanent constraints belong in canon.md.)

## Current Focus
The specific problem or task we are working on now.

## Key Relationships
Important dependencies or tensions between elements.

## Unresolved Problems
Open problems affecting current work. Actual blockers.

## Recent Decisions
Decisions from recent sessions that are still active.

## Do Not Revisit
Explicitly abandoned ideas. Brief reason for each.
```

**What NOT to include:**

- Canon facts (they live in `.cp/canon.md`)
- Resolved decisions from past phases (move to checkpoint)
- History of the session
- Completed tasks
