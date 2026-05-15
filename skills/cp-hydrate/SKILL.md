---
name: cp-hydrate
description: >
  Load operational context at the start of a new session. The agent
  reads .cp/ artifacts (canon.md, latest checkpoint, memory/active.md)
  and the active plan, then shows an alignment summary on screen.
  Use at the beginning of every session or after a conversation reset.
metadata:
  author: roschart
  version: "2.0"
---

# cp-hydrate

Load operational context at the start of a new session.

---

## Purpose

After a conversation reset, the new session has no memory of
previous work. `cp-hydrate` restores the minimum necessary context
by reading the `.cp/` artifacts directly and showing the human an
alignment summary so both parties start from the same state.

This is the inverse of `cp-compact`. Compact reduces state;
hydrate reconstructs it.

---

## Trigger

Run `cp-hydrate` when:

- Starting a new session (first skill to run)
- After a deliberate conversation reset
- Opening the project after a pause (hours, days, or weeks)

This should be the FIRST thing that happens in a new session.
Consider configuring it to run automatically via `agent.md` or
equivalent project-level instructions.

---

## Execution

The agent performs these steps:

1. **Locate `.cp/` directory** in the project root (or nearest
   parent)
2. **Read artifacts** in this order:
    1. `.cp/canon.md` — ground truth (if it exists)
    2. `.cp/checkpoints/` — find and read the latest checkpoint
       (by filename date)
    3. `.cp/memory/active.md` — current operational context
    4. `plan-*.md` at project root — active plan(s)
3. **Show alignment summary** on screen using this structure:

```text
## Session Context — YYYY-MM-DD
[project name + one-sentence description]

### Current State
[From checkpoint: where the project stands. 2-3 sentences.]

### Active Goals
[From memory: what we are trying to achieve right now]

### Canon
[From canon.md: locked facts. Full list.]

### Constraints
[From memory: active session-specific constraints]

### Current Focus
[From memory: the specific task or problem]

### Do Not Revisit
[From memory: closed topics — hard constraints]
```

4. **Ask the human** what they want to work on this session
   (unless the plan's "Next Session" section makes it obvious)

---

## Output

- No files created or modified — hydrate is read-only
- The alignment summary is displayed on screen
- The agent's context is now loaded and ready for work

---

## Rules

- No narrative. No "in the previous session...". No history.
- Every section must be immediately useful for reasoning.
- Do not duplicate content between sections.
- If total exceeds ~400 words, trim the least-critical sections.
- Canon is shown in full — it is the non-negotiable ground truth.
- If `.cp/` does not exist, tell the human and offer to create
  the initial structure.

---

## Review Checklist

After the agent shows the alignment summary, the human verifies:

- [ ] Current State matches reality
- [ ] Canon is complete and accurate
- [ ] Do Not Revisit includes all closed questions
- [ ] No stale or incorrect information is present
