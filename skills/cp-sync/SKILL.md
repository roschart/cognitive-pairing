---
name: cp-sync
description: >
  Reconcile one selected Cognitive Pairing work document with verified
  progress and the current conversation. Use when the human asks to
  sync a work before pausing, compacting context, or marking a milestone,
  or when its executive summary, tasks, or decisions may have drifted.
  Does not commit, compact the conversation, or sync unrelated works.
---

# cp-sync

Keep one existing work safe to resume without preserving a transcript.
This opt-in draft can run before `cp-work` exists: use the selected
document's current structure rather than imposing a new template.

## Select and read

Resolve the nearest `.cp/` using the script bundled with
`cp-workflows`. Ask which work to sync if its identity is unclear;
never infer it from the most recently edited file or another work's
memory. Stop if the selected `.cp/works/<slug>.md` does not exist.
Do not create it, migrate legacy artifacts, or load all active works.

Read the latest selected work before editing, even when it was read
earlier in the conversation; another conversation may have changed
it. Use the available conversation and inspect relevant repository
outcomes when they affect the work. Treat human reports about external
systems as reports, not as independently verified results. Do not
invent evidence from missing context or assume that deployed changes
fixed an issue. If essential state is missing or contradictory, ask
for clarification before changing it.

The current canon and `cp-workflows` disagree about who reads `.cp/`
files and whether they can be reread during a session. Surface this
conflict when exercising the draft; do not claim this skill silently
changes those rules or rewrites canon.

## Reconcile

Update only meaningful differences in the selected work:

- Make the executive summary a short, accurate orientation to the
  objective, current state, and next concrete action. Do not turn it
  into a second task list or a session diary.
- Mark tasks done only when the outcome is supported. Add, revise,
  or remove tasks when scope changes; keep unresolved work visible.
  Do not equate a PR or work-item status with CP task completion.
- Record consequential decisions and newly relevant constraints
  where the document already keeps them, or add a section when it
  would genuinely help. Distinguish decisions from open questions
  and hypotheses from observed facts.
- Preserve useful structure, technical context, existing links,
  and the state of unrelated tasks. Avoid rewriting stable prose
  merely to make the sync look productive.

Do not update canon or any legacy memory, plan, or checkpoint. Do
not touch other works, application code, PRs, or external work items.
If another conversation has changed the selected work, reconcile
against its latest contents rather than replacing them with stale
session context; ask when the two cannot be merged confidently.

## Report

If no meaningful change is needed, leave the file untouched and say
so. Otherwise write only the selected work file, then report a brief
delta: what changed, what remains open, and any uncertainty that
requires human correction. Never commit or invoke `/compact`.
Suggest `/compact` only when the work is ready to resume and freeing
conversation context would help; the human decides when to run it.
