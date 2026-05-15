---
name: cp-session-end
description: >
  Structured end-of-session wrap-up that ensures state is
  captured before closing. Sequences cp-compact, optionally
  cp-checkpoint and cp-plan updates, then produces a session
  delta. Use when ending a working session, about to be
  interrupted, or reaching a natural pause point.
metadata:
  author: roschart
  version: "2.0"
---

# cp-session-end

Structured end-of-session wrap-up that ensures state is
captured before closing.

---

## Purpose

Without a deliberate end-of-session ritual, valuable decisions
and context are lost between sessions. `cp-session-end`
provides a fast, structured sequence to close a session cleanly.

This is NOT a summary of what happened. It is a state capture
that makes the next session effective.

---

## Trigger

Run `cp-session-end` when:

- Ending a working session (planned)
- About to be interrupted for more than a few hours
- Reached a natural pause point
- Context window is getting large and you want a clean break
- More than ~30 exchanges have passed and work is at a
  stopping point

Do NOT run mid-work — wait for a natural stopping point.

---

## Execution Sequence

`cp-session-end` is a meta-skill that sequences other skills:

```text
1. cp-compact    →  compress session into .cp/memory/active.md
2. canon review  →  propose additions to .cp/canon.md (optional)
3. cp-checkpoint →  create if milestone was reached (optional)
4. cp-plan       →  update plan if tasks changed (optional)
5. session delta →  show structured delta on screen
```

Steps 2–4 are optional depending on what happened in the
session. The agent asks the human before modifying canon,
creating checkpoints, or updating plans.

---

## Execution

When `cp-session-end` is invoked the agent performs these
steps:

1. **STEP 1 — Always required:**
   Run `cp-compact`. Produce an updated
   `.cp/memory/active.md`. Read `.cp/canon.md` to ensure
   canon facts are not duplicated into memory.

2. **STEP 2 — If permanent facts were established:**
   Review decisions made during the session. Identify any
   that qualify as permanent ground truth (stable facts
   unlikely to change, not project-specific preferences).
   Propose specific additions to `.cp/canon.md`. Show
   the proposed lines and ask the human for approval.
   Write to canon only after explicit confirmation.
   If nothing qualifies, skip this step silently.

3. **STEP 3 — If a milestone was reached:**
   Run `cp-checkpoint` with an appropriate label.
   Ask the human to confirm before creating the file.

4. **STEP 4 — If tasks were completed, added, or direction
   changed:**
   Propose specific changes to `plan-<slug>.md`.
   Ask the human to confirm before applying.

5. **STEP 5 — Session delta:**
   Show a brief (5-10 bullet) structured delta on screen:

   ```text
   ## Session Delta — YYYY-MM-DD

   ### Decided
   - <decision>

   ### Completed
   - <task>

   ### Opened
   - <new question or task>

   ### Blocked
   - <blocker, if any>

   ### Next Session Focus
   - <recommended starting point>
   ```

### Rules

- The session delta is NOT a narrative. No "we discussed" or
  "then we..."
- Only facts, decisions, and state changes
- If nothing significant happened, say so explicitly
- Confirm with the human before writing any checkpoint,
  plan changes, or canon additions
- Canon additions require explicit human approval — the
  agent proposes, the human decides
- Never record mundane workflow steps as pending work.
  Things like "merge PR", "push changes", "human review",
  "deploy", or "commit" are obvious mechanics — they add
  noise and mislead the next hydration into surfacing
  trivial actions as the session focus. Only record items
  that require genuine thought or decision.

---

## Session Delta Format

The session delta is a lightweight artifact — it can be kept
as a section in `.cp/memory/active.md` (rotating last 2-3
sessions) or discarded after review. It is NOT a permanent
artifact.

Its purpose is to give the human a quick review before
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
- [ ] Canon additions proposed and approved (if any)
- [ ] Plan tasks are marked complete if work was done
- [ ] New tasks discovered are added to plan
- [ ] Checkpoint created if a genuine milestone was reached
- [ ] Git commit includes all artifact changes
- [ ] "Do Not Revisit" includes anything closed this session
- [ ] Next Session Focus is clear and specific
