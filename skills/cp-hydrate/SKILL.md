---
name: cp-hydrate
description: >
  Load operational context at the start of a new session. The agent
  reads .cp/ artifacts (project.md, canon.md, latest checkpoint,
  memory/active.md) and the active plans, then shows an alignment
  summary on screen. Use at the beginning of every session or after
  a conversation reset.
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
The human triggers it explicitly at the start of each session.

---

## File reading

Read `.cp/` files directly — do not delegate this to a
sub-agent. Read each file listed below yourself and build the
alignment summary from their contents.

Files to read (in order):
1. .cp/project.md — if it exists
2. .cp/canon.md — if it exists
3. .cp/checkpoints/ — find and read the most recent file
   (highest date in filename)
4. .cp/memory/active.md — if it exists
5. .cp/plans/plan-*.md — all active plans

Build the internal summary in this shape (do not print this
intermediate form — go straight to the final display format
in step 2 below):

**Read:** <comma-separated list of files successfully read>
**Missing:** <files not found, or "none">

#### Project
<From project.md: identity and intent in 1–2 sentences.
Omit if project.md not found.>

#### Current State
<From checkpoint: where the project stands. 2–3 sentences.
Omit if no checkpoint found.>

#### Active Goals
<From active.md: bullet list of current goals.>

#### Canon
<From canon.md: full list of locked facts, verbatim.>

#### Constraints
<From active.md: hard limits on current work.>

#### Current Focus
<From active.md: the specific task or problem right now.>

#### Do Not Revisit
<From active.md: closed topics, one line each.>

#### Active Plans
<For each plan-*.md found: plan name + 2–3 bullet next steps.>

Word budget: 400 words maximum.

### How the main agent uses this

1. **Read the files directly** and build the alignment
   summary above.
2. **Display the summary** to the human (reformatted as
   `## Session Context — YYYY-MM-DD`)
3. **Proceed** to ask what the human wants to work on

---

## Execution

The agent performs these steps:

**Step 0 — Load foundation rules and resolve `.cp/`:**
Invoke `cp-workflows`. Follow its `.cp/` Resolution rules
to locate the working `.cp/` directory (walk up from cwd to
git root). Use the resolved path for all steps below.

1. **Read `.cp/` files directly** (see File reading above)
   and build the alignment summary.

2. **Display the alignment summary** to the human using
   this structure:

```text
## Session Context — YYYY-MM-DD
[project name + one-sentence description]

### Project
[From project.md: identity, intent, and priority hierarchy.
Omit if project.md does not exist.]

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
5. **Check artifact health** before starting work:
    - If `.cp/memory/active.md` exceeds ~1500 words, suggest
      running `cp-prune` before starting
    - If `.cp/checkpoints/` contains more than 5 files,
      mention that old checkpoints could be archived
    - These are suggestions, not blockers — the human decides

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
- If `.cp/` does not exist, inform the human and suggest running
  `cp-discover` to explore the project and bootstrap the initial
  `.cp/` artifacts collaboratively.

---

## Review Checklist

After the agent shows the alignment summary, the human verifies:

- [ ] Current State matches reality
- [ ] Canon is complete and accurate
- [ ] Do Not Revisit includes all closed questions
- [ ] No stale or incorrect information is present
