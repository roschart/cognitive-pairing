# cp-compact

Compress the current session's working state into a minimal operational
context file (`memory/active.md`).

---

## Purpose

Long sessions accumulate noise: exploratory tangents, resolved
questions, corrected mistakes, discarded ideas. `/compact` removes
that noise and preserves only what is needed to continue working.

This is NOT summarization. It is operational compression.

The output is a replacement for `memory/active.md`, not an addition
to it.

---

## Trigger

Run `cp-compact` when:

- Context feels heavy or you are losing track of the current focus
- About to make a major pivot
- Preparing to end a working session
- Approaching a stable milestone before checkpointing
- Memory/active.md exceeds ~1500 words

---

## Input

Provide the AI with:

1. The current session conversation (or a relevant excerpt)
2. The current `memory/active.md` (if it exists)
3. The latest `checkpoints/YYYY-MM-DD-vN.md` (optional but helpful)

---

## Output

- Replaces `memory/active.md` with the compacted version
- Archives the previous `memory/active.md` to
  `memory/archive/YYYY-MM-DD.md`
- Does NOT create a checkpoint (that is `cp-checkpoint`)

---

## Prompt

Use this instruction with your AI assistant:

```
cp-compact

Read the current session context and the existing memory/active.md
(if provided). Produce a new memory/active.md that:

1. Preserves ONLY what is needed to continue working effectively
2. Removes: resolved questions, completed tasks, corrected mistakes,
   abandoned ideas, conversational noise
3. Uses this exact structure:

   ## Active Goals
   What we are trying to achieve RIGHT NOW. Not long-term vision.

   ## Canon
   Facts that are established, locked, and cannot change.

   ## Active Constraints
   Hard limits on current work.

   ## Current Focus
   The specific problem or task we are working on now.

   ## Key Relationships
   Important dependencies or tensions between concepts/entities.

   ## Unresolved Problems
   Open problems affecting current work. Actual blockers, not wishes.

   ## Recent Decisions
   Decisions from recent sessions that are still active.

   ## Do Not Revisit
   Explicitly abandoned ideas. One line each with reason.

Rules:
- No narrative. No "we discussed" or "first we tried".
- No history. Only current state.
- No duplicates with checkpoint (reference it, don't repeat it).
- Target length: 500–1000 words. Flag if more is genuinely needed.
- If a section has nothing to add, omit it.
```

---

## Review Checklist

Before accepting the compacted memory:

- [ ] Active goals are accurate and current (not stale)
- [ ] Canon includes all locked facts from the session
- [ ] No active constraints were silently dropped
- [ ] "Do Not Revisit" includes everything closed this session
- [ ] Total length is under 1500 words
- [ ] No narrative or history is present
- [ ] Nothing was resolved in this session that still appears as open
