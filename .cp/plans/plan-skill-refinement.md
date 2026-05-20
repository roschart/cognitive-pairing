# Plan: Cognitive Pairing Skill Refinement

## Context

- Framework of 7 skills (`cp-*`) for AI-human session state
  management
- v1.0: Skills restructured to folder format with Makefile
- v2.0: All skills rewritten to agent-driven voice, simplified
  from 7 to 6 skills (removed cp-snapshot), 6 to 4 artifact
  types (removed decisions/, snapshots/, templates/)
- v2.1: Added cp-discover skill for brownfield onboarding,
  removed agent.md (auto-execute not viable due to security)

## Decisions

- **Folder structure**: `skill-name/SKILL.md` — matches standard
  Copilot/Codex skill format
- **YAML frontmatter**: `name` and `description` fields required
  for skill triggering
- **Deployment targets**: `~/.copilot/skills/` and
  `~/.codex/skills/`
- **4 artifact types**: plan, canon, checkpoint, memory
- **canon.md**: agent proposes additions, human approves
  before write
- **agent.md removed**: auto-execute is a security risk; human
  triggers skills manually
- **cp-discover**: new skill for brownfield project onboarding
  with token-aware scanning

## Tasks

- [x] create work branch · ✓ 2026-05-14
- [x] define canonical skill template · ✓ 2026-05-14
- [x] restructure existing skills · ✓ 2026-05-14
- [x] homogenize skill content · ✓ 2026-05-14
- [x] create Makefile · ✓ 2026-05-14
- [x] validate deployment · ✓ 2026-05-14
- [x] dogfood the skills during sessions · ✓ 2026-05-14
- [x] rewrite all skills to agent-driven v2.0 · ✓ 2026-05-15
- [x] remove templates/, cp-snapshot, decisions/ · ✓ 2026-05-15
- [x] create canon.md artifact · ✓ 2026-05-15
- [x] update docs (architecture, artifact-spec,
  anti-patterns) · ✓ 2026-05-15
- [x] test cp-hydrate with Haiku + Sonnet via CLI · ✓ 2026-05-15
- [x] create cp-discover skill · ✓ 2026-05-15
- [x] move count_tokens.py into cp-discover/scripts · ✓ 2026-05-15
- [x] test cp-discover with Haiku, Sonnet,
  GPT-5 mini · ✓ 2026-05-15
- [x] evaluate agent.md auto-execute — rejected · ✓ 2026-05-15
- [x] implement two-bookend session model · ✓ 2026-05-15
- [x] add canon update flow to cp-session-end · ✓ 2026-05-15
- [x] filter mundane noise from state artifacts · ✓ 2026-05-15

## Potential Work

- [ ] real-world validation: use skills in pathfinder (non-code)
  and other personal repos for 2-3 weeks
  **Promote when:** ready to start using framework seriously
- ~~add `agents/openai.yaml` to each skill~~ — discarded
- ~~create skill test suite~~ — discarded

## Next Session

> Paused: 2026-05-15

- Continue real-world validation in brownfield projects
- Run `make sync` to deploy updated skills
- Test Codex deployment (make deploy-codex)
