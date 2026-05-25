# Working Memory — 2026-05-25

## Active Goals

- Validate sub-agent pattern in a real session (cp-hydrate
  first — most visible)
- Real-world validation: use skills in personal repos
  (Pathfinder campaign still pending)

## Active Constraints

- Human triggers skills manually — no auto-execute
- Agent must not commit without explicit human permission
- Skills must never specify model names — only intent
  (e.g. "cheapest/fastest available")

## Current Focus

Sub-agent delegation pattern implemented across all 7
cp-* skills (feat/context-efficiency-subagents, PR #1).
Next: validate in a real session, then merge to main.

## Key Relationships

- Sub-agent pattern: main agent never reads `.cp/` files
  directly — delegates to cheap sub-agent, receives
  structured output only
- cp-compact corrected flow: sub-agent reads existing state
  → main agent uses output + conversation to write active.md
- cp-session-end step 0: initial sub-agent snapshot drives
  which optional steps run

## Unresolved Problems

- Real-session validation of updated skills not yet done
- plan-v3-artifact-model has 0 open tasks → candidate
  for archiving to `.cp/plans/archive/`

## Do Not Revisit

- Auto-execute via agent.md or copilot-instructions.md —
  security risk, not viable
- Flat file structure for skills — rejected in v1.0
- Snapshots, templates, decisions as separate artifacts —
  removed in v2.0
- agents/openai.yaml for each skill — discarded
- Skill test suite — discarded (YAGNI)
- Hardcoded model names in skills (e.g. "haiku") —
  rejected; use intent, not model ID
