---
name: cp-checkpoint
description: >
  Create a stable, recoverable state artifact at a coherent
  milestone. Use when a meaningful phase completes, before major
  pivots, before long pauses, or after resolving significant
  blocking issues. Checkpoints are immutable once created and
  accumulate over time.
metadata:
  author: roschart
  version: "2.0"
---

# cp-checkpoint

Create a stable, recoverable state artifact at a coherent
milestone.

---

## Purpose

A checkpoint is a point-in-time record of where the project
stands. It is the recovery anchor for future sessions and the
baseline for measuring progress.

Unlike `.cp/memory/active.md` (which is replaced), checkpoints
accumulate. They are immutable once created.

---

## Trigger

Run `cp-checkpoint` when:

- A meaningful phase of work is complete
- A blocking issue has been resolved
- About to make a major pivot (create one before AND after)
- About to pause work for more than a few days
- After resolving a significant conflict or redesign

Do NOT checkpoint after every session. Reserve it for genuine
milestones.

---

## Output

- Creates `.cp/checkpoints/YYYY-MM-DD-<label>.md`
- Does NOT modify `.cp/memory/active.md`
- Does NOT modify `.cp/canon.md`
- Does NOT modify `.cp/plans/plan-<slug>.md`

---

## Naming Convention

```text
.cp/checkpoints/
  2026-05-14-v0.1.md             # semantic version
  2026-05-14-db-schema.md        # milestone label
  2026-05-15-v0.2-post-pivot.md  # version + label
```

Use labels when the version number is ambiguous or when the
checkpoint marks a recognizable event.

---

## Execution

When `cp-checkpoint` is invoked the agent performs these steps:

1. **Read inputs**
    - `.cp/memory/active.md` (run `cp-compact` first if needed)
    - `.cp/canon.md` (for awareness of locked facts — never
      modify)
    - The latest existing checkpoint in `.cp/checkpoints/`
      (for comparison and to avoid duplication)
    - A label or version tag provided by the human

2. **Produce a new checkpoint file** at
   `.cp/checkpoints/YYYY-MM-DD-<label>.md` using this structure:

   ```markdown
   # Checkpoint: <label> — YYYY-MM-DD

   ## Current State
   One to three paragraphs. Factual. What is true about the
   project right now. No narrative of how we got here.

   ## Resolved Decisions
   Decisions made and locked. Present-tense statements.
   Example: "The database uses PostgreSQL."

   ## Active Constraints
   Hard limits that govern all future work.

   ## Current Direction
   What we are actively working toward from this point.

   ## Pending Work
   Ordered list of what remains to be done.

   ## Open Questions
   Things unresolved but not currently blocking.

   ## Context Tags
   #tag1 #tag2
   ```

3. **Show the checkpoint** to the human for review before
   writing the file.

### Rules

- No narrative. No "we decided" or "after exploring".
- State facts: "X is Y". "Z uses W".
- Do not duplicate canon.md content — the checkpoint describes
  state at this moment; canon holds permanent truth.
- A checkpoint should be fully understandable without reading
  any previous artifact.
- Omit Blocking Issues section if there are none.

---

## Review Checklist

Before committing the checkpoint:

- [ ] Current State describes the project without narrative
- [ ] All major decisions from this phase are in Resolved
      Decisions
- [ ] No constraint from memory was silently dropped
- [ ] Pending work is ordered by priority
- [ ] Open Questions contains only things truly open
- [ ] The file is self-contained
- [ ] Committed to git
