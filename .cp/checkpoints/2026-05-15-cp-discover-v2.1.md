# Checkpoint: cp-discover and v2.1

**Date**: 2026-05-15
**Branch**: main (after squash merge)

## What happened

- Created cp-discover skill for brownfield project onboarding
- Skill scans project with count_tokens.py, reports token
  weight per directory, identifies high-signal files, then
  enters iterative exploration with the human
- Moved count_tokens.py from repo root into
  skills/cp-discover/scripts/ with tiktoken fallback
- Updated cp-hydrate to suggest cp-discover when .cp/ is
  missing
- Updated skills/README.md with new skill in index and
  execution order
- Tested agent.md auto-execute approach — rejected as
  security risk (agent.md and copilot-instructions.md do
  not auto-execute in any tested agent)
- agent.md removed from project

## Test results

| Model | cp-hydrate | cp-discover | agent.md trigger |
|---|---|---|---|
| Haiku 4.5 | ✅ | ✅ | Only with explicit "read agent.md" |
| Sonnet 4.5 | ✅ | ✅ | Only with explicit "read agent.md" |
| GPT-5 mini | ✅ | ✅ | Only with explicit "read agent.md" |

## Artifact state

- 7 skills deployed (added cp-discover)
- 4 artifact types: plan, canon, checkpoint, memory
- canon.md: 22 lines, stable
- Total repo: ~18,890 tokens

## Key decision

agent.md auto-execute is not viable in any agent due to
security constraints. The human triggers skills manually.
This is acceptable because cognitive pairing is a
human-AI collaboration framework, not an automation tool.
