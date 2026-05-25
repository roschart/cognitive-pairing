# Plan: Context Efficiency via Sub-agents

## Context

- All cp-* skills currently run fully in the main context window
- Skills like cp-hydrate read 4-5 files; cp-compact reads even more
- cp-compact is the clearest failure: it loads into main context the
  very content it is trying to remove from context
- Sub-agents (Haiku) can read and summarize, then terminate —
  leaving only their output in the main context window
- This pattern applies to every skill that reads files before
  producing a summary

## Decisions

- **Sub-agent model**: reader sub-agents use
  `task(agent_type: "explore")` cheapest/fastest available —
  file-reading task, not reasoning; main agent never reads
  source files directly
- **Output contract**: sub-agent returns a structured summary
  (~300 words max) plus a list of key file paths
- **cp-compact corrected flow**: sub-agent reads `.cp/` files
  → main agent uses output + conversation to write `active.md`
- **Scope**: all skills that read `.cp/` files are candidates
- **cp-compact before /compact**: always run `cp-compact`
  first (domain-aware extraction), then optionally run the
  runtime `/compact` builtin to free context window; running
  `/compact` first risks lossy discard of unpreserved state

## Tasks

- [x] redesign cp-compact (highest impact, clearest flow fix) · ✓ 2026-05-25
    - [x] define corrected flow in SKILL.md: sub-agent reads →
          summarises → main agent writes `active.md`
    - [x] define sub-agent output contract (schema + word limit)
- [x] redesign cp-hydrate · ✓ 2026-05-25
    - [x] define output contract (alignment summary + key paths)
    - [x] add `## Sub-agent execution` section to SKILL.md
- [x] redesign cp-session-end · ✓ 2026-05-25
    - [x] identify which orchestration steps benefit from
          delegation
    - [x] update SKILL.md
- [x] redesign cp-checkpoint · ✓ 2026-05-25
    - [x] update SKILL.md
- [x] redesign cp-plan · ✓ 2026-05-25
- [x] redesign cp-prune · ✓ 2026-05-25
- [x] redesign cp-project · ✓ 2026-05-25
- [x] run `make sync` to deploy updated skills · ✓ 2026-05-25
- [ ] update canon with sub-agent execution rule
- [ ] validate all skills in a real session

## Potential Work

- [ ] shared sub-agent prompt template for reading `.cp/` files
  **Promote when:** 2+ skills implement the pattern and
  duplication is visible
- [ ] token-count benchmark before/after per skill
  **Promote when:** first skill is implemented and deployed

## Next Session

> Active: 2026-05-25

- Propose and approve canon addition for sub-agent rule
- Validate updated skills in a real session (cp-hydrate first)
- Token-count benchmark: measure context savings with updated hydrate
