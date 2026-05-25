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
  `task(agent_type: "explore", model: "haiku")` — cheap and fast
  for file reading; main agent never reads source files directly
- **Output contract**: sub-agent returns a structured summary
  (~300 words max) plus a list of key file paths
- **cp-compact corrected flow**: sub-agent reads all `.cp/` files
  → produces compact summary → terminates → main agent writes
  `active.md` using only the sub-agent output
- **Scope**: all skills that read `.cp/` files are candidates

## Tasks

- [ ] redesign cp-compact (highest impact, clearest flow fix)
    - [ ] define corrected flow in SKILL.md: sub-agent reads →
          summarises → main agent writes `active.md`
    - [ ] define sub-agent output contract (schema + word limit)
    - [ ] test end-to-end in this branch
- [ ] redesign cp-hydrate
    - [ ] define output contract (alignment summary + key paths)
    - [ ] add `## Sub-agent execution` section to SKILL.md
    - [ ] test with Haiku sub-agent
- [ ] redesign cp-session-end
    - [ ] identify which orchestration steps benefit from
          delegation
    - [ ] update SKILL.md
- [ ] redesign cp-checkpoint
    - [ ] update SKILL.md
- [ ] update canon with sub-agent execution rule
- [ ] run `make sync` to deploy updated skills
- [ ] validate all four skills in a real session

## Potential Work

- [ ] shared sub-agent prompt template for reading `.cp/` files
  **Promote when:** 2+ skills implement the pattern and
  duplication is visible
- [ ] token-count benchmark before/after per skill
  **Promote when:** first skill is implemented and deployed

## Next Session

> Active: 2026-05-25

- Start with cp-compact: define corrected flow + output contract
- Edit `skills/cp-compact/SKILL.md`
- Smoke-test in this branch before touching other skills
