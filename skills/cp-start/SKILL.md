---
name: cp-start
description: >
  Start or resume a Cognitive Pairing conversation in one selected work.
  Use at the start of a conversation or after a context reset to find
  the nearest .cp/ scope, choose a work, and orient the human and agent
  without loading unrelated works or legacy global state. A small task
  may proceed without a work document.
---

# cp-start

Orient one conversation around one work. This is an experimental
alternative to `cp-hydrate`, not a rename or an implicit migration.
Leave legacy artifacts and the existing skill available.

## Find the scope

Load `cp-workflows` and resolve the nearest `.cp/` with its bundled
script, starting from the current working directory. If none exists,
explain the missing scope and suggest `cp-discover`; do not create
files as a side effect of starting a conversation.

## Select one work

List the names of available `.cp/works/*.md` files in this scope,
excluding `works/archive/`. Do not read every work, infer the chosen
one from modification time, or load global memory, plans, projects,
or checkpoints to make the choice. A paused work remains selectable.

If the human named an existing work, confirm the match and select it.
Otherwise ask which work to open, including the option of a small
task without a document. If the scope has no works, say so and ask
whether to proceed without one or create one explicitly with
`cp-work`. If a requested work does not exist, do not invent it or
silently select a different one.

An already-running conversation may have a selected work. Keep it
when the association is clear and the human is resuming that work;
ask before switching to another work or when the association is
uncertain. Do not treat the most recent file or another conversation
as proof of selection.

## Orient

After selection, obtain this scope's `canon.md` when present and read
only the selected work. Canon is shared across works; do not use a
different scope's canon. Follow its reading rules; if they conflict
with `cp-workflows`, surface the discrepancy. Do not load unrelated
works or legacy global state.

Use the work's executive summary for the objective, current state,
and next action; consult tasks, decisions, risks, and other relevant
sections to check that orientation. If the summary disagrees with the
work, report the discrepancy rather than silently editing it. The
selected work is the operational state, not the conversation
transcript.

Display a short alignment summary to the human: the `.cp/` scope,
the selected work (or "no work document"), its objective, current
state, next action, and any relevant canon constraints or unresolved
conflicts. Do not print every canon fact or reproduce the full work
document. When there is no work document, state the task as the
human described it rather than inventing progress or a next action.
Ask for correction if the orientation is uncertain.

## Boundaries

This skill is read-only. It does not create or sync a work, migrate
legacy artifacts, update canon, invoke `cp-session-end`, commit, or
run `/compact`. Another conversation may edit the selected work
later; `cp-sync` must read its latest state before writing rather
than relying on this initial orientation.
