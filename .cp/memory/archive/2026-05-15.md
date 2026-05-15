# Working Memory — 2026-05-15

## Active Goals

- Real-world validation: use skills in personal repos
- First test: Pathfinder campaign (non-code, Codex)
- Collect feedback over 2-3 weeks

## Active Constraints

- agent.md and copilot-instructions.md do not auto-execute
  skills — this is a security feature, not a bug
- Human triggers skills manually (/cp-hydrate, /cp-discover)

## Current Focus

Session ended. Next session: hydrate, receive feedback from
real-world usage of skills in brownfield projects.

## Key Relationships

- cp-discover → bootstraps .cp/ in brownfield projects
- cp-hydrate → loads context at session start (requires .cp/)
- cp-compact → produces active.md (this file)
- cp-checkpoint → produces immutable milestone records
- count_tokens.py → lives inside cp-discover/scripts/

## Unresolved Problems

- Codex deployment not tested (make deploy-codex)
- No automated test suite for skills

## Recent Decisions

- agent.md removed: auto-execute is a security risk in any
  agent (Copilot, Codex, Cursor) — human triggers skills
- cp-discover created for brownfield onboarding with
  token-aware project scanning
- count_tokens.py moved from repo root to
  skills/cp-discover/scripts/ with fallback for missing
  tiktoken

## Do Not Revisit

- Auto-execute via agent.md or copilot-instructions.md —
  security risk, not viable
- Flat file structure for skills — rejected in v1.0
- Snapshots, templates, decisions as separate artifacts —
  removed in v2.0
