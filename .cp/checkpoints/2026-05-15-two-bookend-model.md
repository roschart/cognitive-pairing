# Checkpoint: Two-Bookend Model — 2026-05-15

## Current State

Framework v2.2. Seven skills deployed. The session model is
now defined: human calls cp-hydrate at start and cp-session-end
at close. All other skills are embedded in session-end or
proposed by the agent during work. Canon updates flow through
session-end with human approval. Mundane workflow steps are
explicitly filtered from state artifacts.

cp-discover validated in real brownfield project (Pathfinder
campaign). Feedback from that session drove the two-bookend
model and canon update changes.

## Resolved Decisions

- Two-bookend model: hydrate (start) + session-end (close)
- Canon: agent proposes, human approves, agent writes
- cp-hydrate detects bloat and suggests cp-prune
- Mundane steps (commit, push, merge) never persisted
- Stale agent.md reference removed from cp-hydrate

## Active Constraints

- Human triggers skills manually — no auto-execute
- Deployed skills in ~/.copilot/skills/ need `make sync`

## Current Direction

Real-world validation phase. Using skills in brownfield
projects for 2-3 weeks to collect feedback before further
changes.

## Pending Work

- Run `make sync` to deploy updated skills
- Test Codex deployment (make deploy-codex)
- Continue Pathfinder campaign validation
- Skill test suite (deferred — promote when regression risk
  justifies)

## Context Tags

#session-model #canon-flow #bookends #v2.2
