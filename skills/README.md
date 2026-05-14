# Skills

Each file in this directory defines one workflow skill.

Skills are prefixed with `cp-` (Cognitive Pairing) to avoid naming
conflicts with built-in AI assistant commands.

A skill definition includes:

- **Purpose** — what it does and why
- **Trigger** — when to invoke it
- **Input** — what artifacts or context it reads
- **Output** — what it produces and where
- **Prompt** — the instruction to give the AI
- **Review checklist** — what the human should verify before accepting

## Skills Index

| Skill                                           | Command             |
|-------------------------------------------------|---------------------|
| [cp-compact](cp-compact.md)                     | `cp-compact`        |
| [cp-checkpoint](cp-checkpoint.md)               | `cp-checkpoint`     |
| [cp-hydrate](cp-hydrate.md)                     | `cp-hydrate`        |
| [cp-plan](cp-plan.md)                           | `cp-plan`           |
| [cp-snapshot](cp-snapshot.md)                   | `cp-snapshot`       |
| [cp-prune](cp-prune.md)                         | `cp-prune`          |
| [cp-session-end](cp-session-end.md)             | `cp-session-end`    |

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

## Integration

These skills are written as plain-language AI prompts. They work with
any AI assistant that accepts instructional context:

- **GitHub Copilot CLI** — place `.md` files in `.github/skills/` or
  the user skills folder
- **Claude / ChatGPT** — paste the `## Prompt` section at the start of
  a session
- **Any AI with long context** — include prompt as system context
