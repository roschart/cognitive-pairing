---
name: cp-workflows
description: >
  Foundation rules for Cognitive Pairing during migration. Load with
  any cp-* skill to resolve scope and distinguish legacy artifacts and
  skills from the experimental work-based flow.
---

# cp-workflows

Foundation rules for Cognitive Pairing during its migration. Load this
skill with any `cp-*` skill to resolve the nearest `.cp/` scope and
understand which contracts are current and which are experimental.

## Migration

Legacy artifacts and skills remain available while the work-based
model is tested. Do not delete or silently convert existing material.

- `cp-hydrate` and `cp-session-end` are candidates for replacement by
  `cp-start` and `cp-sync`.
- `cp-plan` and `cp-project` are candidates for replacement by
  `cp-work`; `cp-compact` by `cp-sync`; `cp-checkpoint` by
  `cp-milestone`. `cp-prune` may be retired after migration.
- `cp-start`, `cp-work`, `cp-sync`, and `cp-milestone` exist but are
  experimental. Their use does not automatically retire legacy skills.
- `project.md`, `plans/`, `memory/active.md`, and `checkpoints/`
  coexist with `works/`. Keep their existing content until a reviewed
  migration establishes what belongs in each work.

The legacy session flow is `cp-hydrate` at the start and optionally
`cp-session-end` at the close. The proposed flow selects one work with
`cp-start`, reconciles it with `cp-sync`, and marks significant states
with `cp-milestone`. A sync is useful before a context compaction or
pause; a milestone is optional and requires human approval to commit.
Do not require a session-end ritual or a milestone for routine work.
Follow the selected skill's existing contract during migration; when
invoking a legacy skill, warn that it follows the older artifact flow
rather than silently redirecting its writes to a work. Neither flow
authorizes running the other automatically.

## Reading and coherence

Read only the relevant `.cp/` artifacts directly in the main context.
Do not load every work or delegate small file reads to a sub-agent.
At orientation, use the selected skill's required context. Treat that
context as a starting point, not an immutable snapshot: before
reconciling or editing a work, read its latest version, even if it was
read earlier. At minimum, check its executive summary and tasks;
consult decisions, risks, and other sections when relevant, and
preserve unaffected content. Ask if the conversation and the current
file cannot be reconciled reliably.

Canon still requires sub-agent reading of `.cp/` files and describes
legacy artifact types and session bookends. Those rules conflict with
the checked-in reading instructions and the proposed migration. Do
not claim this skill overrides canon: surface the conflict and seek
explicit human approval before amending canon.

## Maintaining a selected work

When the human has opted into a work document, keep that selected work
useful during ordinary collaboration, not only when `cp-work` or
`cp-sync` runs. Record consequential settled choices, concrete risks,
new constraints, and other information needed to resume the work as
they emerge. Prefer an existing section; add a named section when
the content warrants its own place. Do not add empty sections or
turn open alternatives into decisions or vague concerns into risks.
Respect a human choice not to capture an insight. `cp-sync` reviews
the work for meaningful omissions or drift; it is not the only time
the work can change.

## Artifact precedence

Canon is human-approved and scope-wide. While legacy artifacts exist,
their previous precedence remains `Canon > Project > Plan > Memory >
Checkpoint`. The proposed work model keeps canon shared and makes one
selected work the operational state; do not merge unrelated works or
silently resolve contradictory artifacts during migration.

## `.cp/` Resolution

**Always use the `scripts/find-cp-dir.sh` script** bundled with this
skill to resolve the nearest `.cp/` directory. Never search downward
from the repository root; that can select the wrong monorepo scope.

Run it from the current working directory with the skill base path
supplied by the skill context:

```bash
bash /path/to/cp-workflows/scripts/find-cp-dir.sh
```

The script walks **upward** from `$PWD` (or a given path) and
returns the first `.cp/` it finds. Exit codes:

| Code | Meaning |
|------|---------|
| `0` | Found — path printed to stdout |
| `1` | Not found — stopped at `.git/` boundary |
| `2` | Not found — reached `$HOME` with no git root |

Exit code `1` → `.cp/` absent at this scope; suggest `cp-discover`.
Exit code `2` → not inside a git repo; inform the human.

**Monorepo scoping:** The first `.cp/` found wins. A `.cp/` inside
a subdirectory (e.g. `docs/pci/vikingcloud-templates/.cp/`) scopes
context to that area. The root-level `.cp/` is only reached if no
scoped one exists above the cwd.

---

## Rules

- Human triggers entry-point skills manually (no auto-execute)
- Agent must not commit without explicit human permission
- Skills never specify model names — only intent
- Canon additions require human approval
