---
name: cp-compact
description: >
  Compress the current session's working state into a minimal
  operational context file (.cp/memory/active.md). Use when more
  than ~30 exchanges have passed without compaction, before major
  direction changes, preparing to end a session, or when
  memory exceeds ~1500 words. This is operational compression,
  not summarization.
metadata:
  author: roschart
  version: "2.0"
---

# cp-compact

Compress the current session's working state into a minimal
operational context file (`.cp/memory/active.md`).

---

## Purpose

Long sessions accumulate noise: exploratory tangents, resolved
questions, corrected mistakes, discarded ideas. `cp-compact`
removes that noise and preserves only what is needed to continue
working.

This is NOT summarization. It is operational compression.

The output is a replacement for `.cp/memory/active.md`, not an
addition to it.

---

## Trigger

Run `cp-compact` when any of these conditions is met:

- More than ~30 exchanges have passed without compaction
- `.cp/memory/active.md` exceeds ~1500 words
- About to make a major direction change
- Preparing to end the session
- Reached a stable milestone before checkpointing

Do NOT run after every few messages — compaction has overhead.

---

## Execution

When `cp-compact` is invoked the agent performs these steps:

1. **Read inputs**
    - The current session conversation
    - The existing `.cp/memory/active.md` (if present)
    - The latest checkpoint in `.cp/checkpoints/` (optional
      but helpful for deduplication)
    - `.cp/canon.md` (permanent, human-curated facts — never
      modified by this skill)

2. **Produce a new `.cp/memory/active.md`** that:
    - Preserves ONLY what is needed to continue working
      effectively
    - Removes: resolved questions, completed tasks, corrected
      mistakes, abandoned ideas, conversational noise
    - Uses this exact structure:

      ## Active Goals
      What we are trying to achieve RIGHT NOW. Not long-term
      vision.

      ## Active Constraints
      Hard limits on current work.

      ## Current Focus
      The specific problem or task we are working on now.

      ## Key Relationships
      Important dependencies or tensions between
      concepts/entities.

      ## Unresolved Problems
      Open problems affecting current work. Actual blockers,
      not wishes.

      ## Recent Decisions
      Decisions from recent sessions that are still active.

      ## Do Not Revisit
      Explicitly abandoned ideas. One line each with reason.

3. **Archive the previous version** of
   `.cp/memory/active.md` to
   `.cp/memory/archive/YYYY-MM-DD.md`

4. **Write the new file** in place of the old one.

### Rules

- No narrative. No "we discussed" or "first we tried".
- No history. Only current state.
- No duplicates with checkpoint (reference it, don't repeat).
- Canon facts live in `.cp/canon.md` — do not copy them into
  `active.md`.
- No mundane operational steps. Never persist things like
  "pending merge", "pending push", "pending human review",
  "commit changes", or "deploy". These are obvious workflow
  mechanics that add noise and distract on rehydration.
  Only persist items that require genuine thought or decision.
- Target length: 500–1000 words. Flag if more is genuinely
  needed.
- If a section has nothing to add, omit it.
- Does NOT create a checkpoint (that is `cp-checkpoint`).

---

## Review Checklist

Before accepting the compacted memory:

- [ ] Active goals are accurate and current (not stale)
- [ ] No active constraints were silently dropped
- [ ] "Do Not Revisit" includes everything closed this session
- [ ] Total length is under 1500 words
- [ ] No narrative or history is present
- [ ] Nothing resolved in this session still appears as open
- [ ] Canon facts are not duplicated from `.cp/canon.md`
