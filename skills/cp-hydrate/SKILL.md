---
name: cp-hydrate
description: >
  Reconstruct operational context in a new, clean AI session. Use when
  starting a new session after a deliberate reset, opening the project
  after a long pause, handing off to a different AI assistant, or
  starting a focused sub-session. Generates a hydration prompt that
  replaces conversation history.
metadata:
  author: roschart
  version: "1.0"
---

# cp-hydrate

Reconstruct operational context in a new, clean AI session.

---

## Purpose

After a conversation reset, the new session has no memory of previous
work. `cp-hydrate` generates a structured context injection — the
"hydration prompt" — that restores the minimum necessary context for
effective work without loading the entire history.

This is the inverse of `cp-compact`. Compact reduces state; hydrate
reconstructs it.

The hydration prompt replaces the conversation history. It should be
the FIRST thing the AI receives in a new session.

---

## Trigger

Run `cp-hydrate` when:

- Starting a new session after a deliberate reset
- Opening the project after a long pause (days or weeks)
- Handing off to a different AI assistant
- Starting a sub-session focused on a specific subtask

Do NOT run mid-session — it is designed for session starts.

---

## Input

Provide the AI with:

1. The latest `.cp/checkpoints/YYYY-MM-DD-label.md`
2. The current `.cp/memory/active.md`
3. The relevant `plan-<slug>.md` (Goals and Tasks at minimum)
4. Optional: a note on what you want to work on this session

---

## Output

- Generates a hydration prompt (structured context block)
- The human pastes this prompt at the start of the new session
- Not stored as a file by default (it is ephemeral)
- Optional: save to `.cp/memory/hydration-YYYY-MM-DD.md` for reuse

---

## Prompt

Use this instruction with your AI assistant:

```
cp-hydrate [optional: what I want to work on this session]

Using the provided checkpoint, .cp/memory/active.md, and
plan-<slug>.md, generate a hydration prompt I can paste at the
start of a new AI session.

The hydration prompt must:
1. Restore operational context — not history
2. Fit in a single message (target 500–800 words)
3. Use this structure:

   # Session Context — YYYY-MM-DD
   [project name + one-sentence description]

   ## Current State
   [From checkpoint: where the project stands. 2-3 sentences.]

   ## Active Goals
   [From memory: what we are trying to achieve right now]

   ## Canon
   [From memory: locked facts that cannot change]

   ## Constraints
   [Merged from checkpoint + memory: hard limits]

   ## Current Focus
   [From memory: the specific task for this session.
    If the human provided a session focus, use that instead.]

   ## Recent Decisions
   [From memory: decisions still active and relevant]

   ## Do Not Revisit
   [From memory: closed topics — treat as hard constraints.
    Do not re-open without explicit human instruction.]

   ## Session Orientation
   [1-2 sentences: what the human wants to accomplish today.
    Leave blank if no focus was provided — the human will fill it.]

Rules:
  - No narrative. No "in the previous session...". No history.
  - Every section must be immediately useful for reasoning.
  - Do not duplicate content between sections.
  - If total exceeds 800 words, trim the least-critical sections.
```

---

## Using the Hydration Prompt

1. Generate using the prompt above
2. Review: verify Current Focus matches today's intent
3. Fill in Session Orientation if it is blank
4. Open a new AI session (or reset the current one)
5. Paste the hydration prompt as the first message
6. Begin working — the AI now has the operational context

---

## Review Checklist

Before pasting the hydration prompt:

- [ ] Current State is accurate as of the latest checkpoint
- [ ] Do Not Revisit includes all closed questions
- [ ] Session Orientation is clear and specific
- [ ] Total length is under 800 words
- [ ] No narrative or history is present
