# Working Memory — 2026-05-15

## Active Goals

- Real-world validation: use skills in personal repos
- First test: Pathfinder campaign (non-code, Codex)
- Collect feedback over 2-3 weeks

## Active Constraints

- Human triggers skills manually — no auto-execute
- Session model: two bookends (hydrate + session-end),
  everything else is embedded or agent-proposed

## Current Focus

Validation phase. Skills are being used in brownfield
projects. Feedback from Pathfinder session informed the
two-bookend model and canon update flow.

## Key Relationships

- cp-hydrate (start) ↔ cp-session-end (close) = bookends
- cp-session-end embeds: compact → canon → checkpoint → plan
- cp-hydrate detects bloat → suggests cp-prune
- cp-discover → one-time brownfield onboarding

## Unresolved Problems

- Codex deployment not tested (make deploy-codex)
- No automated test suite for skills
- Deployed skills in ~/.copilot/skills/ are stale after
  today's changes — need `make sync`

## Recent Decisions

- Two-bookend session model: human calls only hydrate and
  session-end; everything else is embedded or agent-proposed
- Canon updates: agent proposes, human approves, agent writes
- cp-hydrate suggests cp-prune when artifacts are bloated
- Mundane workflow steps (commit, push, merge, deploy) are
  never persisted in memory or delta

## Do Not Revisit

- Auto-execute via agent.md or copilot-instructions.md —
  security risk, not viable
- Flat file structure for skills — rejected in v1.0
- Snapshots, templates, decisions as separate artifacts —
  removed in v2.0
