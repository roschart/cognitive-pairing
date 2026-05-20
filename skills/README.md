# Skills

Each folder in this directory defines one workflow skill. Skills are
prefixed with `cp-` (Cognitive Pairing) to avoid naming conflicts
with built-in AI assistant commands.

Skills are designed for AI agents — the agent reads the skill
definition and executes it directly. Both the human and the agent
benefit from the shared artifacts.

## Folder Structure

```text
skills/
├── _template/              # Reference template for new skills
│   └── SKILL.md
├── cp-checkpoint/
│   └── SKILL.md
├── cp-compact/
│   └── SKILL.md
├── cp-discover/
│   ├── SKILL.md
│   └── scripts/
│       └── count_tokens.py
├── cp-hydrate/
│   └── SKILL.md
├── cp-plan/
│   └── SKILL.md
├── cp-project/
│   └── SKILL.md
├── cp-prune/
│   └── SKILL.md
└── cp-session-end/
    └── SKILL.md
```

Each `SKILL.md` contains:

- **YAML frontmatter** — `name` and `description` for triggering
- **Purpose** — what it does and why
- **Trigger** — when to invoke it (with measurable heuristics)
- **Execution** — what the agent does step by step
- **Output** — what files are created or modified
- **Review checklist** — what the human verifies

## Artifact Layout

All management artifacts live inside `.cp/`:

```text
.cp/
├── project.md          # Project declaration (intent)
├── canon.md            # Locked facts (human-curated)
├── plans/
│   ├── plan-<slug>.md  # Living plans
│   └── archive/        # Completed plans
├── checkpoints/
│   └── YYYY-MM-DD-label.md
└── memory/
    ├── active.md
    └── archive/
```

## Skills Index

| Skill | Purpose |
|-------|---------|
| [cp-discover](cp-discover/SKILL.md) | Explore brownfield project and bootstrap `.cp/` |
| [cp-project](cp-project/SKILL.md) | Create or refine the project declaration |
| [cp-hydrate](cp-hydrate/SKILL.md) | Load context at session start |
| [cp-compact](cp-compact/SKILL.md) | Compress session into memory |
| [cp-checkpoint](cp-checkpoint/SKILL.md) | Create stable state at milestones |
| [cp-plan](cp-plan/SKILL.md) | Create/update living plans |
| [cp-prune](cp-prune/SKILL.md) | Remove stale content |
| [cp-session-end](cp-session-end/SKILL.md) | End-of-session wrap-up |

## Recommended Execution Order

The human interacts with two bookends. Everything else is either
embedded in those skills or proposed by the agent during work.

```text
First time:        cp-discover (brownfield onboarding)
Project start:     cp-project (when complexity warrants it)
Session start:     cp-hydrate (human triggers explicitly)
During session:    agent proposes checkpoint/plan when needed
Session end:       cp-session-end (human triggers explicitly)
                   → sequences: compact → canon → checkpoint → plan
Maintenance:       cp-prune (suggested by hydrate when bloated)
```

## Prefix Rationale

`cp-` stands for Cognitive Pairing. The prefix:

- Avoids conflicts with built-in commands (`/plan`, `/compact`)
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

These skills work with any AI assistant that can read
instructional context:

- **GitHub Copilot CLI** — deploy to `~/.copilot/skills/`
- **OpenAI Codex** — deploy to `~/.codex/skills/`
- **Any AI agent with file access** — point it at the
  `skills/` directory
