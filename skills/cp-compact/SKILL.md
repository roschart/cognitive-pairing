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

## Context window vs. persistent state

`cp-compact` writes state to disk. It does NOT free the current
session's context window — the conversation history is
append-only and cannot be removed in-session.

To free the context window, use the runtime's built-in `/compact`
command **after** running `cp-compact`:

```
1. cp-compact (this skill)
   → Full conversation still available
   → Extracts what matters with domain knowledge
   → Writes active.md — important state now persisted

2. /compact (runtime built-in, optional)
   → Compresses conversation context, freeing memory
   → Lossy is acceptable — everything important is
     already in active.md
   → Only needed if continuing the current session
```

Running `/compact` first is wrong: it may discard decisions
or context that `cp-compact` would have captured. Always run
`cp-compact` first.

If ending the session (via `cp-session-end`), `/compact` is
not needed — the session closes anyway.

---



File reading is delegated to a cheap sub-agent so that `.cp/`
file contents never enter the main context window. Only the
structured output lands in main context.

### Sub-agent prompt

```text
Read the following files from the .cp/ directory and return
a structured snapshot. Do not infer or add anything not
present in the files.

Files to read (in order):
1. .cp/memory/active.md
2. .cp/canon.md
3. .cp/checkpoints/ — find and read the most recent file
   (highest date in filename)

Return exactly this format:

### Sub-agent output

**Read:** <comma-separated list of files successfully read>
**Missing:** <files not found, or "none">

#### Existing memory (active.md)
<full content of active.md, verbatim>

#### Latest checkpoint summary
<2–3 sentences: current state and pending work from the
checkpoint. No narrative.>

#### Canon facts
<bullet list of every canon fact — these must NOT be
duplicated in the new active.md>

Word budget: 500 words maximum.
```

### How the main agent uses the output

1. **Launch sub-agent** (use the cheapest/fastest model available — this is a file-reading task, not a reasoning task) with the prompt above
2. **Receive structured snapshot** — `.cp/` files are now
   out of main context
3. **Use snapshot + current session conversation** to
   produce the new `active.md` (see Execution below)
4. **Archive** the previous `active.md` and write the new one

---

## Execution

When `cp-compact` is invoked the agent performs these steps:

1. **Launch sub-agent** to read `.cp/` files (see
   Sub-agent execution above). Wait for the structured
   snapshot.

2. **Produce a new `.cp/memory/active.md`** using the
   snapshot and the current session conversation. The new
   file must:
    - Preserve ONLY what is needed to continue working
      effectively
    - Remove: resolved questions, completed tasks, corrected
      mistakes, abandoned ideas, conversational noise
    - Use this exact structure:

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

5. **Show the new `active.md`** to the human for review
   before writing (or state that it has been written if
   invoked non-interactively).

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
