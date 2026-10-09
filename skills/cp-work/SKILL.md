---
name: cp-work
description: >
  Create or deliberately reshape one Cognitive Pairing work document
  for independently resumable human-AI work. Use when the human asks
  to start, capture, split, or restructure a work, including a paused
  investigation or a coordinating parent work. Leave routine progress
  reconciliation to cp-sync; trivial tasks need no work unless requested.
---

# cp-work

Create a lightweight coordination document for a selected work. This
is an opt-in draft of the proposed model; it does not replace
`cp-plan`, `cp-project`, or the current canon for existing artifacts.

## Scope

Resolve the nearest `.cp/` by walking upward with the script bundled
with `cp-workflows`. Work in that scope, not a different repository or
the nearest `.cp/` found by searching downward. If there is no `.cp/`
at this scope, stop and suggest `cp-discover` before creating a work.

Use the canon already loaded in this conversation; otherwise obtain
only this scope's `canon.md` when present. Follow its reading rules;
if they conflict with `cp-workflows`, surface the discrepancy rather
than silently choosing one. Do not infer content from another scope.
Do not load every plan, global memory, or the latest checkpoint to
create a new work. If the proposed work conflicts with canon, make
the discrepancy visible; never edit canon as part of this skill.

Use `.cp/works/<descriptive-slug>.md` for one independently resumable
work. Check existing work titles before creating another. If one may
cover the same objective, ask whether to reshape it, create a distinct
work, or do neither. Read the selected work before reshaping it and
preserve useful context, links, and task state. Never overwrite an
existing work or migrate legacy files implicitly. A brief task that
will not need resuming requires no work file unless the human asks.

## Draft

Ground the document in the human's description and any evidence
actually inspected. Distinguish observed outcomes from hypotheses
and planned checks. Do not infer that a fix worked merely because it
was deployed, or that a work item changed state because a CP task did.

For a new document, start with `# Work: <descriptive title>` and
these sections. When reshaping an existing document, preserve its
title and helpful headings rather than imposing new names:

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

Keep even an explicitly requested tiny work short: a title, brief
orientation, and a few checks may be enough. Let sections emerge
from the work's actual complexity. Use an existing section when it
fits; add `## Decisions` for consequential settled choices, `## Risks`
for concrete risks, or another section when distinct content would
help someone resume the work. Record useful rationale and impact
without inventing certainty. Do not add empty sections or treat
open alternatives, hypotheses, and vague concerns as settled facts.
Respect the human's choice not to capture an insight.
Keep open questions distinct from committed tasks.
For a paused work, state what it is waiting for and what evidence will
allow it to resume; do not label it completed or invent a status field.
For a coordinating parent, record shared direction and dependencies;
link children only when they exist, without duplicating their tasks.

PRs and external work items are optional links. Place each link near
the task it clearly relates to, or at work level if it spans tasks.
Do not add placeholder fields such as `PR: no`. One task may span
several PRs, and a PR may span tasks.

Write the document in English with one H1, ordered heading levels,
lines of at most 80 characters outside headings and code blocks, and
LF line endings. Use fenced code blocks with a language if needed.
Leave legacy artifacts untouched.

## Finish

Create or edit only the selected work file. If reviewing an existing
work reveals no meaningful improvement, leave it untouched; do not
edit merely to record that this skill was exercised. Report its path,
current state, next action, and any unresolved attribution or canon
conflicts. Let the human review it. This skill manages the work
document; do not investigate the underlying engineering issue, modify
application code or external work items, commit, open a PR, or claim a
milestone as an implicit side effect.
