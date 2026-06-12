# Working Memory — 2026-06-12

## Active Goals

- Test cp-brainstorming in a real brainstorming session
- Explore additional context compression / cost reduction
  (Copilot cost increase flagged this session)
- Test Codex deployment (`make deploy-codex`)

## Active Constraints

- Human triggers entry-point skills manually (cp-hydrate,
  cp-session-end) — no auto-execute
- Agent must not commit without explicit human permission
- Skills must never specify model names — only intent

## Current Focus

`.cp/` upward traversal implemented and committed (ee672bc).
cp-workflows is now the single source of resolution logic;
entry-point skills (cp-hydrate, cp-session-end, cp-discover)
load it at Step 0. Real-world validation of sub-agent pattern
confirmed this session.

## Key Relationships

- cp-workflows loaded by cp-hydrate, cp-session-end, and
  cp-discover at Step 0 — single source for resolution logic
  and foundation rules
- `.cp/` resolution: walk up from cwd to git root; first
  `.cp/` found wins (monorepo scoping enabled)
- Sub-agent pattern: all .cp/ reading delegated; main agent
  receives structured output only

## Recent Decisions

- `.cp/` resolution lives in cp-workflows only (DRY) —
  entry-point skills reference it, never duplicate it
- Monorepo scoping via subdirectory `.cp/` is an explicit
  supported pattern (e.g. `terraform/.cp/`)
- "Skills You'll Call" section removed from cp-workflows —
  noise when loaded as foundation reference

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
- Adding framework structure doc for cp-workflows — not
  needed (grows organically)
- Duplicating `.cp/` resolution logic per-skill — rejected
  this session; DRY via cp-workflows
