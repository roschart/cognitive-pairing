# Skills

Each folder in this directory defines one workflow skill. Skills are
prefixed with `cp-` (Cognitive Pairing) to avoid naming conflicts with
built-in AI assistant commands.

## Folder Structure

```text
skills/
├── _template/              # Reference template for new skills
│   └── SKILL.md
├── cp-checkpoint/
│   └── SKILL.md
├── cp-compact/
│   └── SKILL.md
├── cp-hydrate/
│   └── SKILL.md
├── cp-plan/
│   └── SKILL.md
├── cp-prune/
│   └── SKILL.md
├── cp-session-end/
│   └── SKILL.md
└── cp-snapshot/
    └── SKILL.md
```

Each `SKILL.md` contains:

- **YAML frontmatter** — `name` and `description` for skill triggering
- **Purpose** — what it does and why
- **Trigger** — when to invoke it
- **Input** — what artifacts or context it reads
- **Output** — what it produces and where
- **Prompt** — the instruction to give the AI
- **Review checklist** — what the human should verify before accepting

## Skills Index

| Skill | Command | Purpose |
|-------|---------|---------|
| [cp-checkpoint](cp-checkpoint/SKILL.md) | `cp-checkpoint` | Create stable state at milestones |
| [cp-compact](cp-compact/SKILL.md) | `cp-compact` | Compress session into memory |
| [cp-hydrate](cp-hydrate/SKILL.md) | `cp-hydrate` | Reconstruct context in new session |
| [cp-plan](cp-plan/SKILL.md) | `cp-plan` | Create/update living plans |
| [cp-prune](cp-prune/SKILL.md) | `cp-prune` | Remove stale content |
| [cp-session-end](cp-session-end/SKILL.md) | `cp-session-end` | End-of-session wrap-up |
| [cp-snapshot](cp-snapshot/SKILL.md) | `cp-snapshot` | Raw capture before experiments |

## Recommended Execution Order

```text
Start of session:  cp-hydrate
During session:    work freely — no skills needed in flow state
End of work block: cp-compact → cp-checkpoint → cp-session-end
Before experiment: cp-snapshot
Maintenance:       cp-prune (when memory exceeds ~1500 words)
Plan changes:      cp-plan
```

## Prefix Rationale

`cp-` stands for Cognitive Pairing. The prefix:

- Avoids conflicts with built-in slash commands (`/plan`, `/compact`)
- Avoids ambiguity when multiple skill sets are loaded
- Makes the skill's origin recognizable at a glance

## Deployment

Skills are deployed to user directories via the Makefile at the
project root:

```bash
make deploy-copilot   # Deploy to ~/.copilot/skills/
make deploy-codex     # Deploy to ~/.codex/skills/
make sync             # Deploy + remove deprecated skills
```

See `make help` for all available targets.

## Integration

These skills work with any AI assistant that accepts instructional
context:

- **GitHub Copilot CLI** — deploy to `~/.copilot/skills/`
- **OpenAI Codex** — deploy to `~/.codex/skills/`
- **Claude / ChatGPT** — paste the `## Prompt` section at the start
  of a session
- **Any AI with long context** — include prompt as system context
