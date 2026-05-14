---
name: cp-session-end
description: >
  Structured end-of-session wrap-up that ensures state is captured
  before closing. Sequences cp-compact, optionally cp-checkpoint and
  cp-plan updates, then produces a session delta. Use when ending a
  working session, about to be interrupted, or reaching a natural
  pause point.
metadata:
  author: roschart
  version: "1.0"
---

# cp-session-end

Structured end-of-session wrap-up that ensures state is captured
before closing.

---

## Purpose

Without a deliberate end-of-session ritual, valuable decisions and
context are lost between sessions. `cp-session-end` provides a
fast, structured sequence to close a session cleanly.

This is NOT a summary of what happened. It is a state capture that
makes the next session effective.

---

## Trigger

Run `cp-session-end` when:

- Ending a working session (planned)
- About to be interrupted for more than a few hours
- Reached a natural pause point
- Context window is getting large and you want a clean break

Do NOT run mid-work — wait for a natural stopping point.

---

## Execution Sequence

`cp-session-end` is a meta-skill that sequences other skills:

```text
1. cp-compact    →  compress session into .cp/memory/active.md
2. cp-checkpoint →  create if milestone was reached (optional)
3. cp-plan       →  update plan-<slug>.md if tasks changed (optional)
4. git add + commit → commit all artifacts
```

Steps 2 and 3 are optional depending on what happened in the session.

---

## Input

- Current session conversation
- All existing artifacts (memory, checkpoint, plan)

---

## Output

- Updated `.cp/memory/active.md`
- New checkpoint (if milestone reached)
- Updated `plan-<slug>.md` (if direction or tasks changed)
- Git commit with all changes

---

## Prompt

Use this instruction with your AI assistant:

```
cp-session-end

Review the current session. Execute the following sequence:

STEP 1 — Always required:
  Run cp-compact. Produce an updated .cp/memory/active.md.

STEP 2 — If a milestone was reached:
  Run cp-checkpoint with an appropriate label.
  Ask me to confirm before creating the checkpoint file.

STEP 3 — If tasks were completed, added, or direction changed:
  Propose specific changes to plan-<slug>.md.
  Ask me to confirm before applying.

STEP 4 — Session delta:
  Produce a brief (5-10 bullet) structured delta of this session:

  ## Session Delta — YYYY-MM-DD
  ### Decided
  - [decision 1]
  ### Completed
  - [task 1]
  ### Opened
  - [new question or task]
  ### Blocked
  - [anything that surfaced as a blocker]
  ### Next Session Focus
  - [recommended starting point]

Rules:
  - The session delta is NOT a narrative. No "we discussed" or
    "then we..."
  - Only facts, decisions, and state changes
  - If nothing significant happened, say so explicitly
  - Confirm with me before writing any checkpoint or plan changes
```

---

## Session Delta Format

The session delta is a lightweight artifact — it can be kept as a
section in `.cp/memory/active.md` (rotating last 3 sessions) or
discarded after review. It is NOT a permanent artifact.

Its purpose is to give the human a quick review mechanism before
committing state.

---

## Git Commit Convention

Use this commit message pattern for end-of-session commits:

```text
chore(state): session wrap-up YYYY-MM-DD

- Update .cp/memory/active.md
- [Add checkpoint: label] (if applicable)
- [Update plan: what changed] (if applicable)
```

---

## Review Checklist

Before closing the session:

- [ ] `.cp/memory/active.md` is updated and accurate
- [ ] Plan tasks are marked complete if work was done
- [ ] New tasks discovered this session are added to plan
- [ ] Checkpoint created if a genuine milestone was reached
- [ ] Git commit includes all artifact changes
- [ ] "Do Not Revisit" includes anything closed this session
- [ ] Next Session Focus is clear and specific
