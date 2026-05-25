# Working Memory — 2026-05-25

## Active Goals

- Validate sub-agent pattern in a real session across projects
- Real-world validation: Pathfinder campaign (cp-project,
  non-code repo) still pending

## Active Constraints

- Human triggers skills manually — no auto-execute
- Agent must not commit without explicit human permission
- Skills must never specify model names — only intent

## Current Focus

Sub-agent pattern validated in-session: cp-session-end step 0
and cp-compact both executed correctly — `.cp/` files never
entered main context. PR #1 open. Next: merge after one more
real-session validation in a different project.

## Key Relationships

- cp-compact before /compact builtin: cp-compact extracts
  state with domain knowledge while conversation is full;
  /compact (builtin) can then safely free context
- Sub-agent pattern: main agent never reads `.cp/` files
  directly — delegates, receives structured output only
- cp-session-end step 0: initial sub-agent snapshot drives
  which optional steps run

## Recent Decisions

- cp-compact always runs before /compact builtin — order
  matters; reverse risks lossy discard of unpreserved state

## Do Not Revisit

- Auto-execute via agent.md/copilot-instructions.md —
  security risk, not viable
- Flat file structure for skills — rejected v1.0
- Snapshots, templates, decisions as separate artifacts —
  removed v2.0
- agents/openai.yaml per skill — discarded
- Skill test suite — discarded (YAGNI)
- Hardcoded model names in skills — rejected; use intent
- Running /compact before cp-compact — lossy, wrong order
