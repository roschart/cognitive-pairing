# cp-checkpoint

Create a stable, recoverable state artifact at a coherent milestone.

---

## Purpose

A checkpoint is a point-in-time record of where the project stands.
It is the recovery anchor for future sessions and the baseline for
measuring progress.

Unlike `memory/active.md` (which is replaced), checkpoints accumulate.
They are immutable once created.

---

## Trigger

Run `cp-checkpoint` when:

- A meaningful phase of work is complete
- A blocking issue has been resolved
- About to make a major pivot (create one before AND after)
- About to pause work for more than a few days
- After resolving a significant conflict or redesign
- Before a risky experiment (use `cp-snapshot` for quick pre-experiment
  captures)

Do NOT checkpoint after every session. Reserve it for genuine
milestones.

---

## Input

Provide the AI with:

1. The current `memory/active.md` (run `cp-compact` first if needed)
2. The latest existing checkpoint (for comparison)
3. A label or version tag (e.g., `v0.3`, `act-2-complete`, `db-schema-locked`)

---

## Output

- Creates `checkpoints/YYYY-MM-DD-<label>.md`
- Does NOT modify `memory/active.md`
- Does NOT modify `plan.md`

---

## Naming Convention

```text
checkpoints/
  2026-05-14-v0.1.md           # semantic version
  2026-05-14-db-schema.md      # milestone label
  2026-05-15-v0.2-post-pivot.md  # version + label
```

Use labels when the version number is ambiguous or when the checkpoint
marks a recognizable event.

---

## Prompt

Use this instruction with your AI assistant:

```
cp-checkpoint [label]

Using the current memory/active.md and the latest checkpoint (if
provided), produce a new checkpoint file for checkpoints/YYYY-MM-DD-[label].md.

Use this exact structure:

   # Checkpoint: [label] — YYYY-MM-DD

   ## Current State
   One to three paragraphs. Factual. What is true about the project
   right now. No narrative of how we got here.

   ## Resolved Decisions
   Decisions that are made and locked. Present-tense statements.
   Example: "The database uses PostgreSQL. This is not up for revision."

   ## Active Constraints
   Hard limits that govern all future work.

   ## Current Direction
   What we are actively working toward from this point.

   ## Pending Work
   Ordered list of what remains to be done.

   ## Open Questions
   Things unresolved but not currently blocking.

   ## Blocking Issues
   If none: omit this section.

   ## Context Tags
   #tag1 #tag2 (for search and retrieval)

Rules:
- No narrative. No "we decided" or "after exploring".
- State facts: "X is Y". "Z uses W". "The constraint is C."
- Do not duplicate content from memory/active.md verbatim.
  The checkpoint describes state; memory describes active context.
- A checkpoint should be fully understandable without reading
  any previous artifact.
```

---

## Review Checklist

Before committing the checkpoint:

- [ ] Current State accurately describes the project without narrative
- [ ] All major decisions from this phase are in Resolved Decisions
- [ ] No constraint from memory was silently dropped
- [ ] Pending work is ordered by priority
- [ ] Open Questions contains only things truly open (not re-opened
  closed questions)
- [ ] The file is self-contained — readable without prior context
- [ ] Committed to git
