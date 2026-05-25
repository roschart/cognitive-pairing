# Checkpoint: Sub-agent Pattern — 2026-05-25

## Current State

Framework at v3.1. All 7 cp-* skills updated to delegate
`.cp/` file reading to cheap sub-agents. Source files never
enter the main context window — only structured output reaches
the main agent. Skills deployed to `~/.copilot/skills/` and
`~/.codex/skills/` via `make sync`. PR #1 open on
`feat/context-efficiency-subagents`.

cp-session-end validated live this session: Step 0 sub-agent
snapshot worked correctly, cp-compact sub-agent read produced
clean output, session-end orchestration completed without
loading `.cp/` files into main context.

## Resolved Decisions

- Sub-agents handle all `.cp/` file reading; main agent
  receives structured output only
- Skills never specify model names — only intent
  (e.g. "cheapest/fastest available")
- cp-compact corrected flow: sub-agent reads existing state
  first, main agent uses output + conversation to write
  new active.md
- Shared output contract: `### Sub-agent output` block with
  `**Read:**` / `**Missing:**` plus structured summary
  ≤ 600 words

## Active Constraints

- Human triggers skills manually — no auto-execute
- Agent must not commit without explicit human permission
- Skills never specify model names — only intent

## Current Direction

Validation phase: run updated skills in real sessions across
different projects before merging PR #1 to main.

## Pending Work

- Validate updated skills in a real session (cp-hydrate first)
- Archive `plan-v3-artifact-model.md` (0 open tasks)
- Merge PR #1 after successful validation
- Pathfinder campaign validation (cp-project + non-code repo)

## Context Tags

#subagent-pattern #context-efficiency #v3.1 #pr-1
