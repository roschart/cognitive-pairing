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

## Sub-agent execution

File reading is delegated to a cheap sub-agent so that `.cp/`
file contents never enter the main context window.

### Sub-agent prompt

```text
Read the following files from the .cp/ directory and return
a structured context summary. Do not infer or add anything
not present in the files.

Files to read (in order):
1. .cp/plans/plan-<slug>.md — the plan being updated
   (if updating an existing plan)
2. .cp/project.md — if it exists
3. .cp/memory/active.md
4. .cp/canon.md
5. .cp/checkpoints/ — find and read the most recent file

Return exactly this format:

### Sub-agent output

**Read:** <comma-separated list of files successfully read>
**Missing:** <files not found, or "none">

#### Current plan state
<If plan file found: full task list with current check states
and the Next Session section. Verbatim.>

#### Active goals and focus
<From active.md: Active Goals and Current Focus only.>

#### Project constraints
<From project.md: Constraints and Priority Hierarchy only.
Omit if project.md not found.>

#### Canon facts
<Full list of canon facts — do not contradict them in the
updated plan.>

Word budget: 400 words maximum.
```

### How the main agent uses the output

1. **Launch sub-agent** (use the cheapest/fastest model available — this is a file-reading task, not a reasoning task) with the prompt above
2. **Receive structured context** — `.cp/` files are now
   out of main context
3. **Use context + session direction** to produce or update
   the plan file
4. **Show draft** to human for review before writing

---

## Execution

When `cp-plan` is invoked the agent performs these steps:

1. **Launch sub-agent** to read `.cp/` files (see
   Sub-agent execution above). Wait for the structured
   context.

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
