---
name: cp-migrate
description: >
  Prepare and review a one-time migration of legacy Cognitive Pairing
  plans, project declarations, and active memory into independently
  resumable works. Use only when the human explicitly asks to migrate
  an existing .cp/ scope. Archive historical checkpoints after review;
  never infer ownership, delete sources, or migrate automatically.
---

# cp-migrate

Convert legacy state to work-based state through a human-reviewed
transition. This is a temporary, experimental migration skill, not
a routine session step. Do not run it merely because legacy artifacts
exist or a legacy skill was invoked.

## Inventory and mapping

Load `cp-workflows` and resolve the nearest `.cp/` with its script.
Read this scope's canon, active plans, project declaration, active
memory, and checkpoint inventory when present. Read relevant
checkpoints to identify durable facts and decisions that still matter;
do not treat a historical snapshot as current state. List existing
works and read any that a proposed conversion would affect.

Propose one work for each independently resumable active plan,
matching existing works rather than creating duplicates. Place
project-level intent in a coordinating parent work only when several
works need shared direction; otherwise put it in the relevant work.
Attribute active memory to a work only when ownership is clear.
Flag ambiguous ownership, conflicting claims, stale tasks, and
unassigned information for human review. Do not copy global memory
into every work or turn unverified reports into facts.

Show the proposed source-to-destination mapping, material to retain
or omit, uncertain items, and exact files to create or change. Ask
the human to resolve ambiguity and approve the mapping before
writing. If scope or ownership is unclear, stop rather than guessing.

## Convert and review

After approval, reread each affected source and destination to avoid
overwriting newer work. Create or update only the approved works,
following `cp-work`'s adaptive structure: a concise executive
summary and actionable tasks, with decisions, risks, and other
sections only when warranted. Preserve useful links and settled
context. Do not silently change canon or unrelated works.

Present the resulting works for human review against the source
material. Keep every legacy source in place until the human accepts
the conversion. Correct omissions and conflicts before treating a
work as migrated. Do not commit, deploy, or change legacy skill
behavior as part of this conversion.

## Archive checkpoints

After the converted works are reviewed, propose archiving historical
checkpoints under `.cp/checkpoints/archive/` without rewriting
their contents. Carry forward only still-relevant, attributable
facts or decisions; flag unresolved content for human review first.
Show the exact checkpoint paths and obtain separate approval before
moving them. Never delete the source history or manufacture
retroactive Git milestones.

Discuss the fate of active legacy plans, `project.md`, and
`memory/active.md` separately after their replacements are verified.
Do not archive or remove those sources implicitly. Report what
was converted, what remains unresolved, and which legacy artifacts
still need a reviewed retirement decision.
