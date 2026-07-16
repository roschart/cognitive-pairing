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

## File reading

Read `.cp/` files directly — do not delegate this to a
sub-agent.

Files to read (in order):
1. .cp/memory/active.md
2. .cp/canon.md
3. .cp/checkpoints/ — find and read the most recent file
   (highest date in filename)

From these, build an internal snapshot:

- Current state (from active.md): Active Goals, Current
  Focus, Pending Work — verbatim from active.md.
- Resolved decisions (from latest checkpoint): bullet list
  of decisions listed in the checkpoint.
- Canon facts: full list — these must NOT be duplicated in
  the checkpoint.

### How the main agent uses this

1. **Read the files directly** and build the snapshot above.
2. **Use snapshot + human-provided label** to produce the
   checkpoint file
3. **Show draft** to human for review before writing

---

## Execution

When `cp-checkpoint` is invoked the agent performs these
steps:

1. **Read `.cp/` files directly** (see File reading above)
   and build the internal snapshot.

2. **Ask the human** for a label or version tag if not
   already provided.

3. **Produce a new checkpoint file** at
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

3. **Show the checkpoint draft** to the human for review
   before writing the file.

4. **Write the file** only after human confirmation.

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
