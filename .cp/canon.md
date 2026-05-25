# Canon

Locked facts for this project. Ground truth that all reasoning
must respect. Only the human approves additions or removals.

## Framework

- Artifact types: project, plan, canon, checkpoint, memory
- Each artifact has an owning skill that contains its
  template; canon is the exception (human-owned)
- All management artifacts live inside `.cp/`
- Skills are agent-executed, not copy-paste prompts
- Skills use folder structure: `skill-name/SKILL.md`
- YAML frontmatter requires `name` and `description` fields
- Deploy targets: `~/.copilot/skills/` and `~/.codex/skills/`
- `.cp/` directory is analogous to `.git/` — infrastructure,
  not content
- Plans live at `.cp/plans/`, not at project root
- Human triggers skills manually — no auto-execute

## Design Principles

- State over history — preserve decisions, not conversations
- Operational over narrative — no "first we discussed..."
- Markdown-only — every artifact readable without tooling
- Git-native — all artifacts versionable and diffable

## Session Model

- Two bookends: human calls cp-hydrate (start) and
  cp-session-end (close) — nothing else manually
- cp-session-end orchestrates: compact → canon → checkpoint
  → plan → delta
- Agent proposes canon additions; human approves before write
- Mundane workflow steps are never persisted in state
  artifacts

## Execution Model

- Sub-agents (Haiku) handle all `.cp/` file reading; the
  main agent receives only structured output
- `.cp/` file contents never enter the main context window
- Sub-agent output contract: structured summary ≤ 600 words
  plus a list of files read / missing
- Skills never specify a model name — only the intent
  (e.g. "cheapest/fastest available"); the executing agent
  chooses the appropriate model for its environment
