# Working Memory — 2026-05-14

## Active Goals

- Human review of changes on `feature/skill-refinement-and-makefile`
- Decide on commit strategy and merge timing
- Test Codex deployment when environment available

## Canon

- Skills use folder structure: `skill-name/SKILL.md`
- YAML frontmatter requires `name` and `description` fields
- Deploy targets: `~/.copilot/skills/` and `~/.codex/skills/`
- Deprecated skills listed in `DEPRECATED` Makefile variable
- All 7 skills restructured and deployed to Copilot

## Active Constraints

- No commits or pushes — human reviews all changes first
- Work is on branch `feature/skill-refinement-and-makefile`
- `agents/openai.yaml` deferred for future work

## Current Focus

Session ended. Next session: human review of all changes, then decide
whether to commit/merge or iterate further.

## Key Relationships

- `cp-compact` → produces `active.md` (this file)
- `cp-checkpoint` → produces immutable milestone records
- `cp-plan` → produces living plan at project root
- `cp-session-end` → sequences compact + checkpoint + plan
- Makefile → deploys skills to user directories

## Unresolved Problems

- Codex deployment not tested (only Copilot tested so far)
- Main README.md not updated to reference `.cp/` usage

## Recent Decisions

- Skill folder structure: `skill-name/SKILL.md` (not flat files)
- Template stored in `_template/` directory
- Makefile uses regex-based help pattern for self-documentation
- DEPRECATED variable for explicit skill removal list
- ADR created for folder structure decision

## Do Not Revisit

- Flat file structure (`cp-*.md` at skills root) — rejected; doesn't
  match standard skill structure used by Copilot/Codex
- Adding `agents/openai.yaml` now — deferred until Codex integration
  becomes primary use case
