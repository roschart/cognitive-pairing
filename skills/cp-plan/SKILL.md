---
name: cp-plan
description: >
  Create or update a living plan document for a project or
  workstream. Use when starting a new plan, after major direction
  changes, after several sessions to mark completed work, or when
  goals have shifted. Plans are distinct from state (checkpoints)
  and context (memory).
metadata:
  author: roschart
  version: "2.0"
---

# cp-plan

Create or update a living plan document for a project or
workstream.

---

## Purpose

The plan is the strategic layer: goals, direction, and
outstanding work. It is distinct from state
(`.cp/checkpoints/`) and from context
(`.cp/memory/active.md`).

A project can have multiple parallel plans, each with its own
slug: `plan-auth.md`, `plan-db-migration.md`,
`plan-pathfinder-arc2.md`.

`cp-plan` maintains these files so they remain useful —
preventing degradation into flat task lists or stale goals.

---

## Trigger

Run `cp-plan` when:

- Starting a new plan (initial creation)
- Major direction change after a pivot
- After several sessions — to mark completed work and add
  new tasks
- Goals have shifted and the current plan no longer reflects
  reality
- The plan has grown unwieldy and needs restructuring

Do NOT run after every session. Plans change less often than
memory or checkpoints.

---

## File Naming

```text
.cp/plans/plan-<slug>.md

Examples:
  .cp/plans/plan-auth-system.md
  .cp/plans/plan-db-migration.md
  .cp/plans/plan-pathfinder-arc2.md
```

Completed plans move to `.cp/plans/archive/`.

Use a slug that describes the workstream, not the date.

---

## Output

- Creates or updates `.cp/plans/plan-<slug>.md`
- Does NOT create a new file per session — one plan per
  workstream
- Human reviews and commits

---

## Task Structure

Plans use two sections:

### Tasks (committed scope)

Work that is decided and will be done. Ordered by priority.
Hierarchy uses indentation — no explicit numbering.

```markdown
## Tasks

- [ ] set up authentication module
    - [ ] design token schema
        - [ ] decide JWT vs opaque tokens
        - [ ] define expiry policy
    - [ ] implement login endpoint
    - [ ] implement token refresh
- [ ] migrate legacy users
    - [ ] audit current user table
    - [ ] write migration script
```

Task states:
- `- [ ]` pending
- `- [-]` in progress
- `- [x]` done — append `· ✓ YYYY-MM-DD`

A parent task is not done until all its children are done.

### Potential Work (unscoped ideas)

Work identified but not yet committed. Each entry needs a
promotion condition.

```markdown
## Potential Work

- [ ] explore passwordless login
  **Promote when:** auth MVP is stable and usage shows
  friction
- [ ] add SSO support
  **Promote when:** enterprise client surfaces this as a
  blocker
```

---

## Execution

When `cp-plan` is invoked the agent performs these steps:

1. **Read inputs**
    - The current `.cp/plans/plan-<slug>.md` (if updating)
    - `.cp/project.md` (if it exists, for project-level
      intent and constraints)
    - The latest checkpoint in `.cp/checkpoints/`
    - `.cp/memory/active.md`
    - `.cp/canon.md` (for awareness of locked facts)
    - Any new goals or direction from the current session

2. **Produce or update** `.cp/plans/plan-<slug>.md` using
   this structure:

   ```markdown
   # Plan: <descriptive title>

   ## Context
   2-5 bullet summary of the current situation and why
   this plan exists.

   ## Decisions
   Decisions already made that constrain the plan.
   Format: - **decision**: one-line rationale

   ## Tasks
   Committed scope. Indented checkboxes for hierarchy.
   No numbering in text — indentation expresses structure.

   ## Potential Work
   Unscoped ideas, each with a promotion condition.

   ## Next Session
   > Paused: YYYY-MM-DD
   1-3 specific pickup points for the next session.
   ```

3. **Show the plan** to the human for review before writing.

### Rules

- Hierarchy via indentation only — never add numbers
- Committed Tasks = will be done; Potential Work = might
- Decisions section explains WHY constraints exist
- Next Session is replaced each session, never accumulated
- Draft only — human has final say

---

## Review Checklist

Before committing the plan:

- [ ] Context accurately describes the current situation
- [ ] Decisions captures all active constraints with rationale
- [ ] Task hierarchy reflects actual dependencies
- [ ] Potential Work items each have a promotion condition
- [ ] Next Session is specific and actionable
- [ ] Nothing in canon.md or checkpoint contradicts the plan
