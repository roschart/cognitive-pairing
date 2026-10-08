---
name: cp-milestone
description: >
  Mark a meaningful milestone in one selected Cognitive Pairing work.
  Use when the human says a milestone has been reached and wants the
  work synced and a searchable Git commit. Review the exact files and
  message and obtain approval before committing. PRs, work-item changes,
  and Copilot's /compact are separate, optional actions.
---

# cp-milestone

Mark a significant state of one work with a reviewed Git commit,
not a new checkpoint document. A routine `cp-sync` is not a milestone.

## Prepare

Resolve the nearest `.cp/` with `cp-workflows` and identify the one
work the human wants to mark. Ask if its identity is ambiguous. Run
`cp-sync` for that work first, then present its delta or no-change
result. If `cp-sync` is unavailable, stop rather than claiming it ran.
For an explicitly authorized trial of repository source skills, the
agent may follow the checked-in `cp-sync` instructions manually and
must disclose that it was not an installed skill invocation.

Inspect the worktree and staged changes before selecting files.
Include the selected work if the sync changed it, along with only
related deliverables the human intends to mark. Do not change the
work document merely to force it into the commit's path history.
Never infer that every dirty file belongs to this milestone.

Propose a concise, descriptive subject and a message body with:

```text
CP-Work: <work-slug>
CP-Milestone: <milestone-slug>
```

The work slug comes from `.cp/works/<work-slug>.md`. Use a distinct,
meaningful milestone slug. A milestone does not imply the work is
finished, a PR exists, or an external work item changed state.

## Approve and commit

Show the human the exact files and commit message, including any
pre-staged files. Ask for explicit approval of that scope before
staging or committing. If unrelated files are already staged, stop
and ask how to handle them; do not reset another person's index.
If there are no meaningful changes to commit, do not make an empty
or marker-only commit; surface the situation for a human decision.

After approval, stage only the approved paths. Confirm the staged
diff matches the approved set, then create a normal commit with the
approved message. Do not amend an earlier commit, push, open a PR,
or modify work items as an implicit side effect. If staging or the
commit fails, report the error; do not claim a milestone was made.

Confirm the new commit can be found with both message markers, for
example:

```bash
git log --oneline --all-match \
  --grep='^CP-Work: <work-slug>$' --grep='^CP-Milestone:'
```

Report the commit ID, included files, and any changes left uncommitted.
Suggest that the human run `/compact` if freeing conversation context
would help; never run it automatically. PR and work-item follow-up
remain separate choices.
