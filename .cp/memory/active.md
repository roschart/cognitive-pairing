# Working Memory — 2026-05-20

## Active Goals

- Real-world validation: use skills in personal repos
- Test cp-project with the Pathfinder campaign using the
  GM assistant super-prompt
- Validate new artifact model (5 types, plans inside .cp/)

## Active Constraints

- Human triggers skills manually — no auto-execute
- Agent must not commit without explicit human permission

## Current Focus

Validation phase. v3 artifact model implemented (project.md
as 5th artifact, plans inside .cp/, artifact-spec refactored
to reference-only). Next: deploy updated skills and test
cp-project in pathfinder with the GM assistant prompt.

## Key Relationships

- cp-project → creates .cp/project.md (intent layer)
- cp-plan → creates .cp/plans/plan-<slug>.md (work layer)
- artifact-spec.md → reference only, templates live in
  owning skills
- cp-hydrate reads project.md first in artifact load order

## Unresolved Problems

- Deployed skills in ~/.copilot/skills/ are stale — need
  `make sync`
- Codex deployment not tested (make deploy-codex)

## Do Not Revisit

- Auto-execute via agent.md or copilot-instructions.md —
  security risk, not viable
- Flat file structure for skills — rejected in v1.0
- Snapshots, templates, decisions as separate artifacts —
  removed in v2.0
- agents/openai.yaml for each skill — discarded
- Skill test suite — discarded (YAGNI)
