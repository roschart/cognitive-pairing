# Canon

Locked facts for this project. Ground truth that all reasoning
must respect. Only the human approves additions or removals.

## Purpose and Transition

- This repository authors Cognitive Pairing skills for keeping a
  human and an AI agent aligned across conversations and concurrent
  work. The framework is being revised using lessons from real use.
- Legacy and work-based skills coexist during this transition.
  `cp-hydrate`, `cp-session-end`, `cp-plan`, `cp-project`,
  `cp-compact`, and `cp-checkpoint` are candidates for retirement;
  the future of `cp-prune` remains under review.
- `cp-start`, `cp-work`, `cp-sync`, and `cp-milestone` are experimental
  work-based skills. `cp-discover`, `cp-brainstorming`, and
  `cp-workflows` remain relevant; the last provides shared scope
  and coordination rules.
- Do not retire a legacy skill or remove its artifacts until the
  replacement has been tested and a reviewed migration preserves
  useful content. Legacy skills still operate on legacy artifacts;
  work-based skills focus on one selected work, or a small task
  without a work document.

## Framework

- `canon.md` holds human-approved truths shared by the nearest
  `.cp/` scope. `.cp/works/<slug>.md` holds the operational state
  of one independently resumable work; small tasks need no work file.
- Legacy project, plan, checkpoint, and memory artifacts remain
  available during migration. Do not silently move or discard them.
- `cp-work` creates or deliberately reshapes a work, the agent
  maintains its meaningful state during ordinary collaboration,
  and `cp-sync` reconciles it. Sections emerge when content warrants
  them; no empty sections are required.
- All management artifacts live inside `.cp/`
- Skills are agent-executed, not copy-paste prompts
- Skills use folder structure: `skill-name/SKILL.md`
- YAML frontmatter requires `name` and `description` fields
- Skills are authored and reviewed in this repository's `skills/`
- Deploy skills through this repository's Makefile; never edit deployed
  copies in user directories directly
- Deploy targets: `~/.copilot/skills/` and `~/.codex/skills/`
- `.cp/` directory is analogous to `.git/` — infrastructure,
  not content
- Legacy plans live at `.cp/plans/`, not at project root
- Human triggers skills manually — no auto-execute

## Design Principles

- State over history — preserve decisions, not conversations
- Operational over narrative — no "first we discussed..."
- Markdown-only — every artifact readable without tooling
- Git-native — all artifacts versionable and diffable

## Session Model

- The legacy session flow uses `cp-hydrate` and `cp-session-end`;
  it remains available but is not required for work-based sessions.
- `cp-start` offers work selection and orients the conversation;
  `cp-sync` reconciles that work when needed. `cp-milestone`
  syncs and requests explicit approval before a searchable Git
  commit. A routine sync does not imply a commit or session closure.
- A conversation normally focuses on one explicitly selected work.
  Switching works is explicit; do not infer selection from the
  most recently changed file. A small task may have no work file.
- Agent proposes canon additions; human approves before write
- Mundane workflow steps are never persisted in state
  artifacts

## Execution Model

- The main agent reads only relevant `.cp/` files directly.
  Do not load every active work or delegate small file reads.
- Orientation is not a permanent cache. Before editing a selected
  work, read its latest state; check the executive summary and tasks
  at minimum, and other sections when relevant. Ask when current
  file contents and conversation cannot be reconciled safely.
- Skills never specify a model name — only the intent
  (e.g. "cheapest/fastest available"); the executing agent
  chooses the appropriate model for its environment
- In work-based sessions, use `cp-sync` to make the selected work
  safe to resume before the separate, optional runtime `/compact`
  when context should be freed. Legacy `cp-compact` may still
  maintain global memory for sessions using that flow.
- cp-workflows is a meta-skill providing foundation rules;
  loaded when using any cp-* skill (not in every session)
- `.cp/` resolution: start from cwd, walk up to git root
  (`.git/`); use the first `.cp/` found. Subdirectory `.cp/`
  scopes context to that area; root `.cp/` is the fallback
- Skills resolving `.cp/` load `cp-workflows` to use its shared
  scope-resolution script rather than duplicating traversal logic
