# Work: Cognitive Pairing Evolution

## Executive Summary

CP is evolving toward one resumable work per conversation, with legacy
flows retained during migration. Experimental work-based skills exist;
archive/reopen behavior and migration still need field testing. The
current change adds semantic cleanup to `cp-sync`, prioritizing the
executive summary and pending tasks with an advisory 500-1500-word range.
Next: review its old/new comparison and this distilled work before
deploying the revision and continuing lifecycle tests.

## Tasks

- [ ] Define a usable work-document contract.
    - [ ] Field-test archive, reopen, and the final-archive offer after
          sync; confirm the move appears in the approved commit.
    - [ ] Test a tiny work, a paused long-running work, and a parent with
          children; test the adaptive task format and identify the
          minimum and optional sections for each.
    - [ ] Define how the executive summary stays concise and accurate
          when tasks or decisions change.
    - [ ] Define work selection, pause, follow-up, completion, rejection,
          and archive behavior without forcing exclusive modes.
- [ ] Draft and exercise `cp-sync` on this work.
    - [x] Add current-value compression, retention safeguards, and
          advisory size guidance to the checked-in contract.
    - [ ] Review the three-case old/new comparison and this work's
          cleanup; deploy the approved revision through the Makefile.
    - [ ] Review the resulting delta and refine the sync contract
          before testing another work.
- [ ] Align framework reading and migration guidance.
      Source guidance and migration notices are drafted; deployment
      and migration review remain separate.
- [ ] Draft and field-test `cp-start` alongside `cp-hydrate`.
    - [ ] Review selection for a named work, ambiguous resumption, and
          a small task without a work; refine from real use.
    - [ ] Deploy the approved draft through the repository Makefile
          without retiring `cp-hydrate`.
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
- [ ] Implement the agreed skills and migration path; update remaining
      docs and seek human approval for any further canon changes.
- [ ] Validate human orientation and isolated sync with two concurrent
      works, a weeks-old paused work, a tiny task, and a multi-repo case.
- [x] Map legacy skills and artifacts to the work-based target.
- [x] Establish the milestone convention; first approved commit `87d7577`.
- [x] Review two `cp-work` trials: this redesign and the external Alloy
      investigation (AB#13452); both were satisfactory. The first trial
      was manual; installed invocation in the second was not verified.

## Why This Work Exists

Global memory and the latest checkpoint mix unrelated conversations;
hydrating every plan loads irrelevant state. A work must answer what
matters now and what comes next for both the human and the agent.
Field feedback also shows that investigation trails accumulate after
their useful life. The human mainly consults the executive summary
and pending tasks, not resolved risks or completed subtasks.

## Target and Continuing Constraints

- Retain shared, human-approved canon in the nearest `.cp/` scope.
  Use one explicitly selected `.cp/works/<slug>.md` per independently
  resumable work; tiny tasks need no file. Multi-repository work can
  use a lead repository and links.
- Replace separate projects, plans, global memory, and new checkpoints
  only after reviewed migration. Preserve useful strategic context,
  pending ideas, and attributable state. Parent works coordinate shared
  direction and dependencies without copying children's tasks.
- `cp-discover` remains scope discovery and canon bootstrap, not work
  creation. `cp-start` is read-only selection and orientation;
  `cp-work` creates or reshapes; ordinary collaboration maintains
  meaningful state; `cp-sync` reconciles one work and reports a delta.
  No mandatory session-end ritual or global active work is required.
- Sections emerge from real content. Prefer checklist tasks and simple
  nesting; use task headings only for substantial blocks with context
  or criteria. An implementation-ready task needs a bounded objective,
  inputs, expected output, and acceptance criteria; otherwise discover
  those first. PR and work-item links are optional, not status fields.
- Discovery, implementation, and follow-up describe attention, not
  exclusive states. Paused work remains selectable and states what
  will unblock it. External work-item status does not determine CP mode.
- Implementation tasks end at the intended final PR becoming ready for
  review. Post-PR validation is guidance, not a completion checkbox.
  Archive only when all tasks are done and the human confirms readiness;
  reopen or create follow-up work if review or validation reveals more.
- Archive/reopen rules remain in `cp-work`: move to or from
  `.cp/works/archive/`, preserve the basename, and never overwrite a
  collision. `cp-start` routes archived work through `cp-work`.
- A milestone includes sync and explicit approval of exact files and
  message. Its optional archive move must be in that approval.
  Routine sync never commits, changes external items, or runs `/compact`.
  Milestones use `CP-Work` and `CP-Milestone` message markers; later
  PR links do not justify amending a commit.

## Semantic Compression Contract

Each sync reads the whole current work and removes detail only after
its operational value expires. Retain evidence for open investigations,
dependencies, reproduction, audit, rollback, or explicit human requests.
Distill resolved trails into cause, change, validation scope, limitations,
and useful references; collapse completed subtasks without hiding
unfinished scope. Keep still-active decisions and rationale. Preserve
uncertain consequential content and ask rather than guessing.

Put a short executive summary and findable pending tasks first. Use
500-1500 words as guidance, never a minimum or cap. Larger necessary
evidence is valid; do not create sidecar history to evade the target.
Report the cleanup without repeating discarded detail. Canon and
legacy artifacts remain outside this operation.

## Migration Map and Source Contracts

| Legacy responsibility | Intended replacement |
| --- | --- |
| Project declaration and plans | One work, or a coordinating parent |
| Global active memory | Work state and executive summary |
| New checkpoint documents | Approved Git milestone commits |
| `cp-hydrate` | `cp-start` |
| `cp-plan`, `cp-project` | `cp-work` |
| `cp-compact`, `cp-session-end` | `cp-sync`, without mandatory closure |
| `cp-checkpoint` | `cp-milestone` |
| `cp-prune` | Routine sync cleanup; separate maintenance remains undecided |

Keep `cp-discover`, `cp-brainstorming`, and shared `cp-workflows`.
Preserve historical sources until reviewed migration; do not manufacture
retroactive milestone commits.

Detailed source contracts: [cp-workflows](../../skills/cp-workflows/SKILL.md),
[cp-work](../../skills/cp-work/SKILL.md),
[cp-sync](../../skills/cp-sync/SKILL.md), and
[cp-milestone](../../skills/cp-milestone/SKILL.md).
The [sync cases](../../skills/cp-sync/evals/evals.json) cover open evidence,
resolved history, and mandatory retention above the advisory size.
One old/new trial per case passed 12/12 checks for the revision versus
8/12 for the baseline: resolved detail shrank from 617 to 297 words;
the open and mandatory-retention cases stayed unchanged in both.
These trials do not replace human review or field testing.

Earlier `cp-work`, `cp-sync`, and `cp-milestone` drafts were deployed to
Copilot and Codex. The current compression revision is source-only
pending review; its comparisons are manual source-instruction trials,
not installed skill invocations. `cp-start` deployment remains pending
in this work. Legacy warnings and the temporary `cp-migrate` draft
remain undeployed; migration has not been run. Deploy through the
repository Makefile, never by editing installed copies.

## Open Questions

- Which proposed skill names and divisions of responsibility survive
  comparison with actual usage?
- What concrete progress qualifies for a milestone offer, and which
  related changes belong in its approved Git commit?
- What should mark a declared milestone if all relevant changes were
  already committed and a sync produces no meaningful edits?
- How should an active conversation discover that its selected work
  changed elsewhere before it syncs?
- Does the new semantic compression preserve enough context in field use,
  and is the advisory 500-1500-word range useful across work sizes?
- Does this iteration need a release number, and how does that relate
  to the older skill metadata and framework checkpoint versions?
- Would a `cp-archive` wrapper that checks readiness, moves the work,
  and hands off to `cp-milestone` reduce coupling or add needless
  complexity compared with the integrated final-archive offer?

## Next Action

Review the compression comparison and this distilled work, then deploy
the approved revision. Continue archive/reopen and final-archive field
tests, `cp-start` routing, and the sync-to-milestone handoff before
migrating legacy artifacts.
