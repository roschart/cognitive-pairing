# Canon

Locked facts for this project. Ground truth that all reasoning
must respect. Only the human adds or removes entries.

## Framework

- Artifact types: plan, canon, checkpoint, memory
- Skills are agent-executed, not copy-paste prompts
- Skills use folder structure: `skill-name/SKILL.md`
- YAML frontmatter requires `name` and `description` fields
- Deploy targets: `~/.copilot/skills/` and `~/.codex/skills/`
- `.cp/` directory is analogous to `.git/` — infrastructure,
  not content
- Plans live at project root, not inside `.cp/`

## Design Principles

- State over history — preserve decisions, not conversations
- Operational over narrative — no "first we discussed..."
- Markdown-only — every artifact readable without tooling
- Git-native — all artifacts versionable and diffable
