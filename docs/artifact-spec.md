# Artifact Specification

Each artifact type has a defined structure, purpose, and
lifecycle. Every artifact with an owning skill stores its
template in that skill's SKILL.md — this spec is the
high-level reference.

## Summary

| Artifact   | Purpose             | Skill         | Location             | On end  |
|------------|---------------------|---------------|----------------------|---------|
| project    | Intent and scope    | cp-project    | `.cp/project.md`     | Archive |
| plan       | Work and progress   | cp-plan       | `.cp/plans/`         | Archive |
| canon      | Locked ground truth | (human-owned) | `.cp/canon.md`       | N/A     |
| checkpoint | Stable state        | cp-checkpoint | `.cp/checkpoints/`   | Archive |
| memory     | Operational context | cp-compact    | `.cp/memory/active`  | Replace |

---

## .cp/project.md — Project Declaration

| Field       | Value                                    |
|-------------|------------------------------------------|
| Purpose     | Master declaration of intent and scope   |
| Skill       | cp-project                               |
| Location    | `.cp/project.md`                         |
| Owner       | Human-curated                            |
| Create when | Multiple plans anticipated, non-obvious  |
|             | constraints, or project identity needed  |
| Not needed  | Simple tasks where one plan suffices     |
| On end      | Archive (rarely — projects outlive plans)|

**Lifecycle:** Created once at project inception. Rarely
modified — refined, not rewritten. Survives across all
sessions and plans.

**Template:** See `cp-project` skill for structure.

**What belongs in project.md vs canon.md:**

- Project: declarations made BEFORE or AT THE START
  (initial intent, constraints, style)
- Canon: decisions made DURING the project (emergent
  truth that must be locked)

**What belongs in project.md vs plan.md:**

- Project: WHAT and WHY (direction, identity, constraints)
- Plan: HOW and HOW MUCH (tasks, progress, next steps)

**Anti-patterns:**

- Turning the project document into a task list (that is
  the plan's job)
- Updating it after every session (it should be stable)
- Including implementation details (those belong in plans
  or canon)
- Duplicating constraints already in canon.md

---

## .cp/plans/plan-slug.md — Work Plan

| Field       | Value                                    |
|-------------|------------------------------------------|
| Purpose     | Living declaration of work and progress  |
| Skill       | cp-plan                                  |
| Location    | `.cp/plans/plan-<slug>.md`               |
| Owner       | Human-curated                            |
| Create when | Work needs tracking across sessions      |
| Not needed  | One-shot tasks solvable in a prompt      |
| On end      | Archive to `.cp/plans/archive/`          |

**Lifecycle:** Created once per workstream. Never replaced.
Sections evolve: active tasks move to completed; ideas move
to parked or pruned.

**Template:** See `cp-plan` skill for structure.

**Anti-patterns:**

- Using the plan as a conversation transcript
- Deleting completed sections instead of marking done
- Letting it grow without pruning (becomes noise)

---

## .cp/canon.md — Ground Truth

| Field       | Value                                    |
|-------------|------------------------------------------|
| Purpose     | Permanent ground truth. Locked facts     |
| Skill       | (human-owned — no dedicated skill)       |
| Location    | `.cp/canon.md`                           |
| Owner       | Human-curated only                       |
| Create when | A decision must never be re-litigated    |
| Not needed  | Session-specific constraints (use memory)|
| On end      | N/A — canon is permanent                 |

**Lifecycle:** Grows slowly. Items are added when a fact
becomes permanently locked. Items are removed only when
genuinely obsolete (rare).

Canon has no owning skill. The agent reads it but never
modifies it directly. `cp-session-end` proposes additions;
the human approves before anything is written.

**Structure:**

```markdown
# Canon

Locked facts for this project. Ground truth that all
reasoning must respect. Only the human adds or removes
entries.

## Project

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

**What belongs in canon vs checkpoint:**

- Canon: the WHAT — "The database is PostgreSQL"
- Checkpoint: the snapshot — what was true at that moment

---

## .cp/checkpoints/YYYY-MM-DD-label.md — Stable State

| Field       | Value                                    |
|-------------|------------------------------------------|
| Purpose     | Recoverable state at a coherent milestone|
| Skill       | cp-checkpoint                            |
| Location    | `.cp/checkpoints/YYYY-MM-DD-label.md`    |
| Owner       | AI-generated, human-reviewed             |
| Create when | Milestone reached, before pivots or      |
|             | long pauses                              |
| Not needed  | After every session (only at milestones) |
| On end      | Archive to `.cp/checkpoints/archive/`    |

**Lifecycle:** Immutable once committed. Never edited.
Accumulate over time. Old checkpoints are reference
material, not active state.

**Template:** See `cp-checkpoint` skill for structure.

**Naming convention:**

- `2026-05-14-v0.1.md` — date + semantic version
- `2026-05-14-pathfinder-act2.md` — date + label

**What NOT to include:**

- History of how we got here
- Rejected alternatives (unless they are constraints now)
- Conversational context

---

## .cp/memory/active.md — Operational Context

| Field       | Value                                    |
|-------------|------------------------------------------|
| Purpose     | Minimal context to reason effectively    |
| Skill       | cp-compact                               |
| Location    | `.cp/memory/active.md`                   |
| Owner       | AI-generated via cp-compact              |
| Create when | At each compaction cycle (session end)   |
| Not needed  | N/A — always maintained                  |
| On end      | Replace (previous archived to            |
|             | `memory/archive/YYYY-MM-DD.md`)          |

**Lifecycle:** Replaced at each compaction cycle. Previous
version archived. 500–1500 words max.

**Template:** See `cp-compact` skill for structure.

**What NOT to include:**

- Canon facts (they live in `.cp/canon.md`)
- Resolved decisions from past phases (move to checkpoint)
- History of the session
- Completed tasks
