---
name: cp-sync
description: >
  Reconcile one selected Cognitive Pairing work document with verified
  progress and the current conversation. Use when the human asks to
  sync a work before pausing, compacting context, or marking a milestone,
  or when its state has drifted or accumulated obsolete detail.
  Distill resolved history while preserving what is needed to resume.
  Does not commit, compact the conversation, or sync unrelated works.
---

# cp-sync

Keep one existing work safe to resume without preserving a transcript.
Use its helpful structure rather than imposing a new template.

## Select and read

Resolve the nearest `.cp/` using the script bundled with
`cp-workflows`. Ask which work to sync if its identity is unclear;
never infer it from the most recently edited file or another work's
memory. Stop if the selected `.cp/works/<slug>.md` does not exist.
Do not create it, migrate legacy artifacts, or load all active works.

Read the entire latest selected work before editing, even when it was
read earlier; another conversation may have changed it. Review all
sections for current value, not just recent additions. Use the
available conversation and inspect relevant repository
outcomes when they affect the work. Treat human reports about external
systems as reports, not as independently verified results. Do not
invent evidence from missing context or assume that deployed changes
fixed an issue. If essential state is missing or contradictory, ask
for clarification before changing it.

Canon and `cp-workflows` require fresh, scoped reading before edits.
This skill never changes canon; propose additions for human approval
outside the sync.

## Reconcile

Update only meaningful differences in the selected work:

- Make the executive summary a short, accurate orientation to the
  objective, current state, and next concrete action. Aim for one
  short paragraph, usually three to five sentences. Put it near the
  top, followed by tasks so pending work is easy to find. Do not turn
  it into a second task list or a session diary.
- Mark tasks done only when the outcome is supported. Add, revise,
  or remove tasks when scope changes; keep unresolved work visible.
  Do not equate a PR or work-item status with CP task completion.
- Look for consequential content that emerged during the work but
  was not captured: settled decisions, concrete risks, new
  constraints, or open questions needed to resume. Use an existing
  section where it fits; add a named section when the content
  warrants its own place. Do not add empty sections, put open
  alternatives among decisions, mistake hypotheses for facts, or
  record insights the human declined to capture.
- Preserve useful structure, technical context, and references that
  still serve the work. Leave unrelated task state unchanged. Avoid
  rewriting stable prose merely to make the sync look productive.

## Distill by current value

On each sync, reconcile both missing state and surplus history.
Lossy semantic compression means keeping the meaning needed to
continue while deliberately discarding detail that no longer serves
that purpose. It is not a shorter transcript or word-by-word copyedit.
Judge usefulness by unresolved work and continuing obligations, not
age, checkbox status, or document length alone.

- Keep concrete evidence while it supports an open investigation,
  acceptance criterion, dependency, risk, or next action. An old
  finding or a completed task can still matter to unfinished work.
- When a task or phase is resolved, replace its investigation trail
  with the useful outcome: confirmed cause or conclusion, change,
  validation and its scope, remaining limitations, and references
  needed to act on or substantiate it. Keep reported results distinct
  from independently verified ones.
- Remove obsolete measurements, logs, timestamps, superseded
  hypotheses, repeated explanations, and resolved risks once they
  no longer affect continuation. Keep decisions and rationale that
  still constrain the work, not every past choice.
- Collapse completed subtasks into a concise checked outcome when
  their individual detail is no longer useful. Keep pending tasks,
  acceptance criteria, blockers, dependencies, and useful PR or
  work-item links explicit. Do not remove unfinished scope or make
  a mixed-status parent look complete.
- Preserve exact details required for reproduction, audit, rollback,
  or a human retention request, even after resolution. Do not replace
  necessary inline evidence with an unavailable or invented link.
  If a consequential loss is uncertain, keep that content and ask
  a focused question; routine removal of clearly obsolete detail
  needs no separate approval.

For example, keep exact duplicate-series counts while an exporter
investigation is open. Once the cause and fix are verified, a short
cause/change/validation summary may replace the metric tables and
sample timestamps. Deployment alone does not establish resolution.

Use 500-1500 words as an advisory range for an ordinary work, not a
minimum or a hard cap. Tiny and completed works can be much shorter;
complex investigations may need more. Above roughly 1500 words,
actively look for stale detail and duplication. Keep necessary
content even when the work remains longer, and briefly explain why.
Never pad a short work, delete useful evidence to meet a quota, or
create sidecar archives or appendices to hide the same excess.

Keep the executive summary and pending tasks as the reading path;
supporting sections should earn their space. Remove headings and
link definitions made empty or unused by pruning, and repair internal
references. Before writing, check that someone with the work and its
available sources can still resume every open task without this
conversation. If it is already concise and current, leave it alone.

Do not update canon or any legacy memory, plan, or checkpoint. Do
not touch other works, application code, PRs, or external work items.
If another conversation has changed the selected work, reconcile
against its latest contents rather than replacing them with stale
session context; ask when the two cannot be merged confidently.

## Milestone Handoff

After reconciling, consider whether verified progress represents a
meaningful milestone, such as completing a substantial phase or
deliverable. A changed work document or a high task count alone is not
enough. If there is a concrete outcome and a reviewable set of related
changes, briefly offer `cp-milestone` as an optional next step. Never
invoke it automatically or request commit approval as part of a sync.

When `cp-sync` is running as part of `cp-milestone`, do not make a
separate milestone offer; continue the milestone flow instead.

## Report

If no meaningful change is needed, leave the file untouched and say
so. Otherwise write only the selected work file, then report a brief
delta: what changed, what resolved detail was distilled or removed,
what remains open, and any uncertainty that requires human correction.
Do not copy the discarded detail into the report. Include a milestone
offer only when it meets the criteria above. Never commit or invoke `/compact`.
Suggest `/compact` only when the work is ready to resume and freeing
conversation context would help; the human decides when to run it.
