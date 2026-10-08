---
name: cp-work
description: >
  Create or deliberately reshape one Cognitive Pairing work document
  for independently resumable human-AI work. Use when the human asks
  to start, draft, or restructure a work, including a paused
  investigation or a coordinating parent work. Do not invoke for
  routine state syncs or trivial tasks that need no persistent document.
---

# cp-work

Create a lightweight coordination document for a selected work. This
is an opt-in draft of the proposed work model; it does not replace
`cp-plan`, `cp-project`, or the current canon for existing artifacts.

## Scope

Resolve the nearest `.cp/` by walking upward with the script bundled
with `cp-workflows`. Work in that scope, not a different repository or
the nearest `.cp/` found by searching downward. If there is no `.cp/`
at this scope, stop and suggest `cp-discover` before creating a work.

Use the canon already loaded in this conversation; otherwise obtain
only this scope's `canon.md` when present. Respect the scope's rules
for reading it; if those conflict with the installed `cp-workflows`
instructions, surface the conflict instead of silently choosing one.
Do not load every plan, global memory, or the latest checkpoint to
create a new work. If the proposed work conflicts with canon, make
the discrepancy visible; never edit canon as part of this skill.

Create `.cp/works/<descriptive-slug>.md` for one independently
resumable work. If an existing work might cover the same objective,
ask whether to update it, create a distinct work, or do neither.
Never overwrite an existing work or migrate legacy files implicitly.
Do not create a work for a brief task that can be finished without
resuming it in a later conversation unless the human explicitly asks.

## Draft

Ground the document in the human's description and any evidence
actually inspected. Distinguish observed outcomes from hypotheses
and planned checks. Do not infer that a fix worked merely because it
was deployed, or that a work item changed state because a CP task did.

Start with `# Work: <descriptive title>` and these sections:

- `## Executive Summary`: a few short sentences stating what the work
  is about, its current state, and the next concrete action. Orient a
  reader who has not seen the conversation; do not retell its history
  or duplicate the entire task list.
- `## Why This Work Exists`: the objective, relevant evidence and
  constraints needed to resume without the conversation. Identify
  uncertain claims as such. Link an external source when known.
- `## Tasks`: actionable checks reflecting the current state. Use
  `- [ ]` for pending work and `- [x]` only for verified outcomes.
  Nest checks for simple breakdowns. Add a `###` heading beneath
  `## Tasks` only when a substantial block needs its own context,
  acceptance criteria, or subordinate checks. A heading groups
  checks; it is not a second task status.

Add other sections only when they help this work: for example,
`## Decisions`, `## Risks`, `## Potential Work`, or a more specific
technical heading. Keep open questions distinct from committed tasks.
For a paused work, state what it is waiting for and what evidence will
allow it to resume; do not label it completed or invent a status field.
For a coordinating parent, link children only when they exist.

PRs and external work items are optional links. Place each link near
the task it clearly relates to, or at work level if it spans tasks.
Do not add placeholder fields such as `PR: no`. One task may span
several PRs, and a PR may span tasks.

Write the document in English with one H1, ordered heading levels,
lines of at most 80 characters outside headings and code blocks, and
LF line endings. Use fenced code blocks with a language if needed.
Leave legacy artifacts untouched.

## Finish

Create or edit only the selected work file. Report its path, the
current state and next action, and any unresolved attribution or
canon conflicts. Let the human review it. Do not investigate the
underlying engineering issue, modify application code or external
work items, commit, open a PR, or claim a milestone unless separately
requested and authorized.
