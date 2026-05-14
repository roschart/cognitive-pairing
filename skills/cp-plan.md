# cp-plan

Create or update a living plan document for a project or workstream.

---

## Purpose

The plan is the strategic layer: goals, direction, and outstanding
work. It is distinct from state (`.cp/checkpoints/`) and from context
(`.cp/memory/active.md`).

A project can have multiple parallel plans, each with its own slug:
`plan-auth.md`, `plan-db-migration.md`, `plan-pathfinder-arc2.md`.

`cp-plan` maintains these files so they remain useful — preventing
degradation into flat task lists or stale goals.

---

## Trigger

Run `cp-plan` when:

- Starting a new plan (initial creation)
- Major direction change after a pivot
- After several sessions — to mark completed work and add new tasks
- Goals have shifted and the current plan no longer reflects reality
- The plan has grown unwieldy

Do NOT run after every session. Plans change less often than memory
or checkpoints.

---

## File Naming

```text
plan-<slug>.md at project root (not inside .cp/)

Examples:
  plan-auth-system.md
  plan-db-migration.md
  plan-pathfinder-arc2.md
  plan-api-redesign.md
```

Use a slug that describes the workstream, not the date.

---

## Input

Provide the AI with:

1. The current `plan-<slug>.md` (if updating)
2. The latest `.cp/checkpoints/` file (for awareness of current state)
3. Any new goals, constraints, or direction from recent sessions
4. Optional: a note on what changed

---

## Output

- Creates or updates `plan-<slug>.md` at project root
- Does NOT create a new file per session — one plan per workstream
- Human reviews and commits

---

## Task Structure

Plans use two sections:

### Tasks (committed scope)

Work that is decided and will be done. Ordered by priority.
Hierarchy uses indentation — no explicit numbering in the text.

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

Work identified but not yet committed. Each entry needs a promotion
condition — the circumstance that would move it to Tasks.

```markdown
## Potential Work

- [ ] explore passwordless login
  **Promote when:** auth MVP is stable and usage shows friction
- [ ] add SSO support
  **Promote when:** enterprise client surfaces this as a blocker
```

Plan complexity is emergent — not a formal tier:
- Few flat tasks, no Potential Work → naturally simple
- Deep hierarchies + substantial Potential Work → naturally complex

---

## Prompt

Use this instruction with your AI assistant:

```
cp-plan <slug> [optional: brief context on what changed]

Create or update plan-<slug>.md at the project root. Use current
state from the provided checkpoint and .cp/memory/active.md.

Use this exact structure:

   # Plan: [descriptive title]

   ## Context
   [2-5 bullet summary of the current situation and why this
   plan exists. What problem it solves or goal it achieves.]

   ## Decisions
   [Decisions already made that constrain the plan.
   Format: - **decision**: one-line rationale]

   ## Tasks
   [Committed scope. Use indented checkboxes for hierarchy.
   No numbering in the text — indentation expresses structure.
   Format:
     - [ ] top-level task
         - [ ] sub-task
             - [ ] sub-sub-task]

   ## Potential Work
   [Unscoped ideas, each with a promotion condition.
   Format:
     - [ ] idea
       Promote when: [condition]]

   ## Next Session
   > Paused: YYYY-MM-DD
   - [1-3 specific pickup points for the next session]

Rules:
  - Hierarchy via indentation only — never add numbers to task text
  - Committed Tasks = will be done; Potential Work = might be done
  - Decisions section explains WHY constraints exist
  - Next Session is replaced each session, never accumulated
  - Draft only — human has final say
```

---

## Review Checklist

Before committing the plan:

- [ ] Context accurately describes the current situation
- [ ] Decisions section captures all active constraints with rationale
- [ ] Task hierarchy reflects actual dependencies
- [ ] Potential Work items each have a promotion condition
- [ ] Next Session is specific and actionable
- [ ] Nothing in `.cp/checkpoints/` Resolved Decisions contradicts
  the plan
