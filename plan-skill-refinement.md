# Plan: Cognitive Pairing Skill Refinement

## Context

- Framework of 7 skills (`cp-*`) for AI-human session state management
- Skills were restructured from flat files to folder structure
- Makefile created for deploying to Copilot and Codex
- All skills now have YAML frontmatter for proper triggering

## Decisions

- **Folder structure**: `skill-name/SKILL.md` — matches standard
  Copilot/Codex skill format
- **YAML frontmatter**: `name` and `description` fields required for
  skill triggering
- **Deployment targets**: `~/.copilot/skills/` and `~/.codex/skills/`
- **Deprecated handling**: Explicit `DEPRECATED` variable in Makefile

## Tasks

- [x] create work branch · ✓ 2026-05-14
- [x] define canonical skill template · ✓ 2026-05-14
- [x] restructure existing skills · ✓ 2026-05-14
    - [x] cp-checkpoint
    - [x] cp-compact
    - [x] cp-hydrate
    - [x] cp-plan
    - [x] cp-prune
    - [x] cp-session-end
    - [x] cp-snapshot
- [x] homogenize skill content · ✓ 2026-05-14
- [x] update skills/README.md · ✓ 2026-05-14
- [x] create Makefile · ✓ 2026-05-14
- [x] validate deployment · ✓ 2026-05-14
- [-] dogfood the skills during this session
    - [x] use cp-compact to create .cp/memory/active.md · ✓ 2026-05-14
    - [x] use cp-checkpoint to create milestone · ✓ 2026-05-14
    - [x] use cp-plan to create this plan · ✓ 2026-05-14
    - [x] test cp-hydrate with fresh agent · ✓ 2026-05-14
- [x] document decisions and next steps · ✓ 2026-05-14
    - [x] ADR for folder structure decision
    - [x] session delta created
- [x] run cp-session-end · ✓ 2026-05-14

## Potential Work

- [ ] add `agents/openai.yaml` to each skill
  **Promote when:** Codex integration becomes primary use case
- [ ] create skill test suite
  **Promote when:** regression risk justifies investment
- [ ] add pre-commit hooks for skill validation
  **Promote when:** multiple contributors edit skills

## Next Session

> Paused: 2026-05-14

- Run `git diff` to review all changes
- Decide: keep `.cp/` artifacts or add to `.gitignore`
- Commit and merge when satisfied
- Test `make deploy-codex` when Codex available
