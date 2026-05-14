# Checkpoint: skill-restructure-complete — 2026-05-14 v1.0

## Current State

The Cognitive Pairing framework has been restructured from flat skill
files to the standard folder structure (`skill-name/SKILL.md`). All 7
skills have YAML frontmatter with `name` and `description` fields. A
self-documenting Makefile enables deployment to both Copilot and Codex
user directories.

The skills are now deployed to `~/.copilot/skills/` and ready for use.
The framework dogfood has begun with real artifacts in `.cp/`.

## Resolved Decisions

- Skills use folder structure `skill-name/SKILL.md` with YAML
  frontmatter
- Deploy destinations are `~/.copilot/skills/` and `~/.codex/skills/`
- Deprecated skills are tracked via `DEPRECATED` variable in Makefile
- Templates (`templates/`) and docs (`docs/`) remain unchanged
- `_template/` directory provides reference for creating new skills

## Active Constraints

- Work is on branch `feature/skill-refinement-and-makefile`
- No commits/pushes until human review
- `agents/openai.yaml` deferred for future work

## Current Direction

Complete the dogfooding phase by creating `.cp/` artifacts, then
document decisions and recommendations for future work.

## Pending Work

- [ ] Test `make deploy-codex`
- [ ] Create plan artifact (`plan-skill-refinement.md`)
- [ ] Write session summary with recommendations
- [ ] Human review of all changes before commit

## Open Questions

- Should `agents/openai.yaml` be added now or deferred?
- Should the main README.md reference the `.cp/` directory structure?

## Context Tags

#cognitive-pairing #skills #restructure #makefile #milestone
