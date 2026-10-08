# Work: Cognitive Pairing Evolution

## Executive Summary

CP is being redesigned using lessons from months of daily use. Its
purpose is to keep a human and an AI agent aligned while work outlasts
one conversation, without forcing documentation on small tasks. This
work now has a mapping of existing skills and artifacts and a candidate
Git milestone flow. Drafts of `cp-sync`, `cp-work`, and `cp-milestone`
are deployed to Copilot and Codex for testing, but remain experimental.
The first milestone is commit `87d7577`. Two field trials of `cp-work`
produced satisfactory results: a manual review of this work and a new
work for an external Alloy investigation. Next: reconcile `cp-sync`
and `cp-workflows` reading rules with canon before further field tests.

## Why This Work Exists

The current framework grew incrementally: visible plans for work longer
than one conversation; canon for shared truths; memory and checkpoints
to counter context loss; project documents for larger initiatives.
Actual usage revealed a different shape. Multiple named conversations
often work on unrelated plans in one repository. A single active memory
and the latest global checkpoint mix their state, while hydration loads
unrelated plans. `cp-compact` is useful during ongoing work, followed
by Copilot's `/compact`; the session-end ritual and checkpoint files
rarely add value. Project documents are uncommon in this user's work.

The problem is not merely AI context size. The human also needs a fast,
trustworthy answer to "what were we doing, and what comes next?"

## Artifacts

### `canon.md`

**Present:** Human-approved facts shared across the nearest `.cp/`
scope. `cp-discover` bootstraps it; `cp-hydrate` and other skills read it.
**Strength:** Prevents settled repository context from being
re-litigated. **Future:** Retain it as the only scope-wide state document.
The human must approve amendments, including changes to framework rules;
work-specific decisions belong in their work. `cp-start` reads canon,
while `cp-sync` may propose, but never silently write, an addition.

### `project.md`

**Present:** `cp-project` creates a stable declaration of intent,
constraints, and priorities above plans; `cp-hydrate` and `cp-plan`
consult it. **Tension:** Most work does not justify a separate project
layer. **Future:** Retire this artifact type. Put relevant intent in a
work document; create a coordinating parent work only when several works
need shared direction. `cp-work` would create or refine that parent.
Migration must preserve distinct strategic context without duplicating
it in every child.

### `plans/plan-*.md`

**Present:** `cp-plan` maintains direction, decisions, tasks, potential
work, and a next-session note. `cp-hydrate` reads every active plan.
**Strength:** Makes work visible and resumable beyond one conversation.
**Tension:** Several plans compete for attention during hydration.
**Future:** Replace each independently resumable plan with one
`.cp/works/<slug>.md`, retaining useful context, decisions, open tasks,
and pending ideas. `cp-work` handles deliberate creation or remodeling;
ordinary work and `cp-sync` keep it current. A paused work stays
selectable; only completed or discarded work moves to the archive.

### `memory/active.md`

**Present:** `cp-compact` replaces one global operational memory and
archives its previous version; `cp-hydrate` loads it. **Strength:** Saves
context that would otherwise vanish between conversations. **Tension:**
Concurrent unrelated works overwrite or contaminate one another, and
the file competes with each plan's next-session note. **Future:** Retire
the global file in favor of a brief executive summary inside each work.
`cp-start` presents the selected summary; `cp-sync` verifies its accuracy.
Only unambiguously attributable focus, blockers, and unresolved matters
move into a work during migration; a human resolves ambiguous ownership.

### `checkpoints/`

**Present:** `cp-checkpoint` creates immutable dated snapshots;
`cp-hydrate` and `cp-compact` read the latest one across the scope.
**Tension:** No demonstrated recovery benefit justifies separate
checkpoint files, and the latest may belong to another work.
**Future:** Retire new checkpoint documents. If a milestone merits
marking, identify the approved Git commit containing that work's state
with a searchable message convention. Preserve historical checkpoint
files; carry forward only facts and decisions still relevant to a work.
Do not manufacture retroactive milestone commits.

### `works/<slug>.md`

**Present:** This document is the first prototype; no existing skill
owns the new format. **Future:** One document per independently
resumable work, with sections added only as complexity demands. A brief
task need not create one. `cp-work` can create it explicitly;
`cp-brainstorming` can offer to create one after the human agrees.
`cp-start` selects and reads it. The agent maintains it during ordinary
work, while `cp-sync` reconciles its state and reports a short delta.
Related works link to each other; a parent is another work, not a
mandatory project layer. Tasks remain simple checks unless a block
needs its own context or subordinate checks.

### Executive Summary

**Present:** The prototype has this section, but no existing skill
guarantees that it reflects current work. **Future:** Treat it as the
work's entry-point interface, not a separate file or a conversation
history. It answers what matters now, where the work stands, and what
comes next. `cp-start` uses it to orient both participants; `cp-sync`
checks it against tasks, decisions, and actual outcomes and corrects
stale or conflicting claims. Other sections, such as decisions, remain
ordinary parts of the document unless they need their own skill contract.

### Git Milestone Marker

**Present:** Git versions documents, but CP has no agreed convention for
finding significant states in commit history. **Future:** A searchable
marker in a human-approved commit identifies a declared milestone for
one work. It is not another Markdown artifact or a routine `cp-sync`
output; a sync alone never authorizes a commit.
The first milestone used a descriptive commit subject with
`CP-Work: <slug>` and `CP-Milestone: <slug>` in the message body. A
working lookup is:

```bash
git log --oneline --all-match \
  --grep='^CP-Work: <slug>$' --grep='^CP-Milestone:'
```

Include the work document when syncing changes it; do not manufacture
an edit just to make the commit appear in its path history. Review the
exact file set before including related code. A milestone always syncs
and commits, but it does not imply that the work is complete, a PR
exists, or an external work item changes state.

## Skills

Names marked as candidates describe responsibilities, not final names.
The current descriptions below reflect skill definitions, not a claim
that every skill is used regularly.

### `cp-workflows`

**Present:** Loaded with other `cp-*` skills; resolves the nearest
`.cp/` and defines the artifact hierarchy and session bookends.
**Strength:** One scope-resolution mechanism. **Future:** Retain and
revise it for one selected work per conversation, without mandatory
session closure or global active state. Its canon rules require human
approval before changing.

### `cp-discover`

**Present:** Scans a new working scope and bootstraps canon, global
memory, empty plan and checkpoint directories, and sometimes a project.
**Strength:** Keeps initial context discovery collaborative.
**Future:** Retain scope discovery and human-approved canon creation;
do not require memory, a work document, or a project at bootstrap.
Starting a new work in an established scope is not `cp-discover`.

### `cp-brainstorming`

**Present:** Explores unclear directions using relevant canon and
context; it does not automatically write artifacts. **Strength:**
Protects thinking before execution. **Future:** Retain. It may propose
capturing an idea through `cp-work`, but neither a new work nor
brainstorming is mandatory for a small task.

### `cp-hydrate`

**Present:** At session start, loads canon, project, global memory,
latest checkpoint, and every active plan, then shows an alignment
summary. **Tension:** Unrelated works appear together. **Future:**
Replace with `cp-start` (candidate), which offers a lightweight choice
before reading one work and orienting the human and agent.

### `cp-plan`

**Present:** Reads the plan, project, memory, canon, and latest
checkpoint to create or update a living plan. **Strength:** Tracks
direction and progress. **Future:** Retire after migration; `cp-work`
handles deliberate document creation and restructuring. Planning
sections remain available within a work, not as a separate artifact.

### `cp-project`

**Present:** Reads canon and an optional existing project declaration
to create or refine `project.md`. **Strength:** Captures strategic
intent when multiple plans share it. **Tension:** Adds a separate
distinction between scales that often adds no value. **Future:** Retire
after migration; `cp-work` can create a coordinating parent when needed.

### `cp-compact`

**Present:** Uses global memory, canon, latest checkpoint, and the
conversation to replace `memory/active.md`; the built-in `/compact`
must be run separately to free conversation context. **Strength:**
Captures operational state during ongoing work. **Future:** Replace
with `cp-sync` (candidate), which reconciles only the selected work.
Copilot's `/compact` remains a separate operation, useful after any
sync that has made the work safe to resume.

### `cp-checkpoint`

**Present:** Reads memory, canon, and the latest checkpoint and creates
a dated immutable file at a milestone. **Tension:** These files have
not proved useful for resuming work. **Future:** Retire; an approved
Git milestone commit replaces new checkpoint files when a milestone is
declared.

### `cp-session-end`

**Present:** Reads global state, invokes compact, optionally proposes
canon, checkpoint and plan changes, and shows a session delta.
**Tension:** Work often continues in a named conversation across
days; closure is not a necessary state transition. **Future:** Retire
the required ritual. `cp-sync` can reconcile work and show a delta
mid-session or before stopping, without creating a milestone.

### `cp-prune`

**Present:** Reviews oversized global memory and accumulated
checkpoints; drafts a shorter memory and recommends archiving.
**Strength:** Challenges stale context. **Future:** Incorporate
routine pruning in work maintenance and archival. Retain a separate
maintenance skill only if real usage warrants it; never delete
historical source material automatically during migration.

### `cp-start` (candidate)

**Present:** Does not exist. **Future:** Resolve the nearest `.cp/`,
list available works without loading them all, ask which work to open,
then read canon and that work to orient both participants. Associate
the conversation with that work; allow work without a document for a
small task. If a resumed conversation's association is uncertain, ask.

### `cp-work` (candidate)

**Present:** An experimental draft exists in `skills/cp-work/` and is
deployed to Copilot and Codex. A first review used the checked-in
instructions before deployment; a second agent produced a work for
the paused Alloy investigation after deployment. The agent's use of
the installed skill was not independently verified here.
**Future:** Explicitly create or reshape a work document, including
an optional coordinating parent. Use a small structure by default
and add sections when they solve a real problem.
This skill is not the sole editor: the agent may maintain the selected
work during ordinary collaboration.

### `cp-sync` (candidate)

**Present:** An experimental draft exists in `skills/cp-sync/` and is
deployed to Copilot and Codex. Its first trial on this document was
manual; it has now been invoked to reconcile this work. **Future:**
Reconcile the selected work with the conversation and actual outcomes;
verify tasks, decisions, and especially the executive summary. Write
only meaningful changes, then show a brief delta for human correction.
Ask rather than guess the work if its identity is uncertain; never
silently amend canon or create a commit. It does not free Copilot's
context window.

### `cp-milestone` (candidate)

**Present:** An experimental draft exists in `skills/cp-milestone/`
and is deployed to Copilot and Codex. This work is its first
installed trial. The earlier milestone commit (`87d7577`) followed
its proposed convention.
**Future:** Invoke `cp-sync` for the selected work, show its delta and
the exact proposed file set, and request explicit approval before
committing only the reviewed changes with searchable work and milestone
markers. Suggest `/compact` after the commit if the conversation
continues; do not run it automatically.
Opening a PR and updating or closing an external work item are optional
follow-up steps, not prerequisites or automatic consequences of a CP
milestone. Their links may be added to the work when available; a PR
created after the commit cannot be linked in that same commit. Personal
work needs no work item.

### `cp-migrate` (candidate)

**Present:** Does not exist. **Future:** Support a reviewed conversion
of projects and plans to works, attributing global memory and old
checkpoint content only where ownership is clear. Keep historical
plan and memory archives and all other sources intact until the new
works are verified. A dedicated skill is justified only if the
migration cannot be handled safely as a one-time guided process.

## Cross-Cutting Tensions

- `cp-compact` does not read the selected plan, while it and
  `cp-hydrate` use the latest checkpoint across unrelated works.
- Plan `Next Session`, global memory, and checkpoint `Pending Work`
  can disagree. The executive summary must reflect current tasks
  without becoming another competing task list.
- The checked-in skills direct the main agent to read `.cp/` files,
  while the canon mandates sub-agent reading. Decide which rule to
  keep; do not silently reconcile the contradiction.
- `cp-workflows` discourages rereading `.cp/` files after hydration,
  while `cp-sync` must reconcile the latest selected work. The human
  authorized direct rereading for this trial; canon remains unchanged.
- The current canon requires five artifact types and two bookends.
  Replacing them needs explicit human-approved canon changes.

## Target Model

- The nearest `.cp/` defines a working scope, usually one repository.
  A multi-repository effort may use a lead repository and explicit links.
- `canon.md` holds truths shared across that scope; additions require
  human approval. Scope discovery remains distinct from starting work.
- `.cp/works/<slug>.md` is one selectable document per independently
  resumable work. Finished or discarded works move to `works/archive/`;
  paused work remains selectable without loading it by default.
- A work can range from a complex user story to a small set of epics.
  Tiny tasks need no work file. The file gains sections when they serve
  a real need, rather than when it crosses a numerical threshold.
- A concise executive summary gives both participants their entry point.
  Stable context, tasks, decisions, risks, design, and other sections
  appear only where useful. The document manages coordination; code,
  presentations, and other deliverables remain outside it.
- Related works link to each other. Create a parent work only if shared
  goals, priorities, dependencies, or risks need active coordination.
- A conversation normally belongs to one selected work. Changing work
  is possible but explicit and uncommon. If the association is lost,
  the agent asks rather than updating an inferred destination.
- Starting a conversation lists available works before reading one.
  Syncing writes the selected document and reports a short delta for
  human correction. Copilot's `/compact` separately frees context and
  can follow a routine sync without a milestone commit.
- The current document is the live state. Milestones, if worth marking,
  require a sync and an approved Git commit with a searchable message
  convention rather than appended checkpoint files. No skill commits
  without human approval.

## Task Representation

Default to checklist items for bounded tasks and nested checks for
straightforward breakdowns. Use a `###` heading under `## Tasks` only
when a substantial block needs its own context, criteria, or subordinate
checks; its heading groups the checks rather than introducing a second
status field. Do not turn every checkbox into a structured record.

PRs and external work items are optional links, not properties every
task must carry. Place a link beneath a task when the relationship is
useful and unambiguous; place it at work or milestone level when it
spans several tasks. Omit absent links rather than writing `PR: no` or
`Work item: no`. A task may span multiple PRs, and a PR may cover
multiple tasks. Add links when known, without rewriting an earlier
milestone commit solely to record a PR created afterward.

## Work Modes

Discovery, implementation, and follow-up describe the **dominant kind
of attention**, not mutually exclusive states. Different parts of one
work may occupy different modes at the same time. Discovery resolves
unknowns; implementation delivers bounded changes; follow-up monitors
external dependencies, outcomes, or maintenance without pretending the
work is finished. Archive is a separate decision that the work is done
or abandoned, not a fourth mode.
An external work item's review status is not a CP mode: review and
follow-up can coexist with ongoing implementation.

A task is implementation-ready when someone with this document and the
repository can state its bounded objective, inputs, expected output,
and acceptance criteria without relying on this conversation. If they
cannot, the next task is discovery, not a vague implementation checkbox.

## Decisions To Preserve

- Keep `canon.md` shared per `.cp/` scope and human-approved.
- Use `work` as the scale-neutral name and one document per independent
  work; do not require a separate project or memory artifact.
- Select one work explicitly when starting a conversation; sync only
  that work and show a brief, factual delta after writing.
- Keep Git commits under human control. A milestone marker is metadata
  on an approved commit, not a new checkpoint document.
- For `cp-sync`, reread the selected work's executive summary and tasks
  at minimum; consult decisions, risks, and other sections when the
  conversation or possible external edits make them relevant. This
  trial uses direct reading; update the conflicting framework rules
  only after explicit canon approval.
- Preserve existing artifacts during migration until their replacement
  has been reviewed. Revise canon only with explicit approval.

## Tasks

- [x] Map the existing framework to this target.
    - [x] Record each skill's trigger, inputs, writes, and dependencies;
          flag overlap and contradictions with canon and deployed skills.
    - [x] Specify the fate of each of the five existing artifact types,
          including content that must survive migration.
- [ ] Define a usable work-document contract.
    - [ ] Test a tiny work, a paused long-running work, and a parent with
          children; test the adaptive task format and identify the
          minimum and optional sections for each.
    - [ ] Define how the executive summary stays concise and accurate
          when tasks or decisions change.
    - [ ] Define work selection, pause, follow-up, completion, rejection,
          and archive behavior without forcing exclusive modes.
- [ ] Draft and exercise `cp-sync` on this work.
    - [x] Draft an opt-in sync for one explicitly selected,
          existing work without requiring `cp-work` or migrating
          legacy artifacts.
    - [x] Reconcile this document with verified outcomes and the
          current conversation; check tasks, decisions, and executive
          summary without inventing progress or committing changes.
    - [ ] Review the resulting delta and refine the sync contract
          before testing another work.
- [x] Mark the first milestone before testing `cp-work`.
    - [x] Draft `cp-milestone` to sync the selected work, present
          the exact commit scope and message for approval, and
          suggest `/compact` afterward.
    - [x] Review the synced work and selected repository changes,
          then make an approved, searchable milestone commit (`87d7577`).
    - [x] Suggest the built-in `/compact` after committing; the human
          decides when to run it.
- [x] Field-test the first `cp-work` draft on two real works.
    - [x] Draft `cp-work` in this repository as an opt-in trial.
    - [x] Refine the draft and agree on test prompts and review criteria.
    - [x] Deploy it to Copilot and Codex through the repository
          Makefile; never edit installed copies directly.
    - [x] Have a separate agent use the checked-in draft to review
          this redesign work, preserving its useful content; the
          draft was not invoked as an installed skill.
    - [x] Have a separate agent create a work for the idle Alloy
          log-replay investigation (AB#13452), without investigating
          or changing Alloy or the external work item.
    - [x] Review both documents for factual accuracy, useful task
          granularity, concise orientation, and optional links. The
          outputs are sufficient for this test; Alloy follow-up
          belongs to its own work in another repository.
- [ ] Turn the interaction model into actionable skill contracts.
    - [ ] Settle skill names and start/sync responsibilities, including
          a new task with no document and a resumed named conversation.
    - [ ] Specify sync's write target, short delta, no-change behavior,
          ambiguity handling, and canon-approval boundary.
    - [ ] Decide the milestone commit convention and a matching Git log
          query, which files belong in the commit, and how later PR or
          work-item links are recorded; require no commit for routine
          syncs.
- [ ] Design a safe migration using this repository as a first case.
    - [ ] Map each existing plan to a work; identify whether any project
          merits a coordinating parent work.
    - [ ] Attribute global memory and checkpoints only when ownership is
          clear; present ambiguous content for human review.
    - [ ] Retain source files until new works have been checked, and
          define an archive/rollback path.
- [ ] Revisit the draft `cp-work`, `cp-sync`, and `cp-milestone` skills
      after field tests and migration decisions; adjust their contracts
      together before treating them as stable.
- [ ] Implement the agreed skills and migration path; update docs and
      propose canon changes for explicit human approval.
- [ ] Validate human orientation and isolated sync with two concurrent
      works, a weeks-old paused work, a tiny task, and a multi-repo case.

## Open Questions

- Which proposed skill names and divisions of responsibility survive
  comparison with actual usage?
- What qualifies as a milestone, and which related changes belong in
  its approved Git commit?
- What should mark a declared milestone if all relevant changes were
  already committed and a sync produces no meaningful edits?
- How should an active conversation discover that its selected work
  changed elsewhere before it syncs?
- Does this iteration need a release number, and how does that relate
  to the older skill metadata and framework checkpoint versions?

## Next Action

Decide how `cp-sync` rereads the selected work and align that behavior
with `cp-workflows` and the human-approved canon before the next field
tests.
