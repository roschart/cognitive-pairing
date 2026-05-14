# 001: Skill Folder Structure

## Status

Accepted

## Context

The Cognitive Pairing framework had 7 skills defined as flat `.md`
files in `skills/` (e.g., `skills/cp-checkpoint.md`). This structure
did not match the standard skill folder format used by GitHub Copilot
CLI and OpenAI Codex, which expect:

```text
skill-name/
├── SKILL.md          # YAML frontmatter + instructions
├── agents/           # Optional: UI metadata
└── references/       # Optional: auxiliary docs
```

Options considered:
1. Keep flat files, generate folder structure on deploy
2. Restructure to folder format, deploy directly via rsync
3. Keep flat files, require manual copy-paste for deployment

## Decision

Restructure all skills to folder format with YAML frontmatter. Each
skill becomes `skills/cp-<name>/SKILL.md` with `name` and `description`
fields in the frontmatter. Deploy via rsync (Makefile targets).

We chose this because:
- Matches the expected format for both Copilot and Codex
- Enables direct rsync deployment without transformation
- Allows future addition of `agents/` and `references/` subdirectories
- Skills are immediately usable after deployment

## Consequences

- All 7 skills were restructured (breaking change for anyone using
  old file paths)
- Old flat files were deleted
- `_template/` directory added as reference for creating new skills
- Makefile added for deployment automation
- Future skills must follow the folder structure

## Alternatives Considered

- **Generate on deploy**: Rejected — adds complexity, requires build
  step, harder to debug
- **Manual copy-paste**: Rejected — error-prone, doesn't scale, no
  sync capability
