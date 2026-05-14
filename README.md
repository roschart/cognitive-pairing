# Cognitive Pairing

A framework of reusable AI-human workflow skills for long iterative
projects. Focuses on shared state management rather than prompt
engineering.

## The Core Problem

Long AI-human sessions degrade over time:

- Context windows fill up
- Irrelevant history accumulates
- Contradictions linger
- Abandoned ideas pollute reasoning
- Both parties lose clarity

The solution is not better prompts. It is disciplined state management.

## The Core Insight

Humans already solve this problem naturally: notes, plans, ADRs,
outlines, summaries, documentation. This framework formalizes those
patterns into a set of composable, versionable, AI-readable artifacts.

## Artifact Hierarchy

| Artifact         | Question it answers       | Owner            | Lifecycle   |
|------------------|---------------------------|------------------|-------------|
| `plan.md`        | Where are we going?       | Human-curated    | Living doc  |
| `checkpoint/`    | Where are we now?         | AI-generated     | Per-milestone |
| `memory/active`  | What do we need right now? | AI-generated    | Per-session |
| `decisions/`     | Why did we choose this?   | Human-reviewed   | Permanent   |
| `snapshots/`     | What exactly was happening? | AI-generated  | Disposable  |

## Skills (Commands)

| Skill               | Purpose                                        |
|---------------------|------------------------------------------------|
| `/checkpoint`       | Create a stable, recoverable state             |
| `/compact`          | Compress working memory                        |
| `/hydrate`          | Reconstruct context in a new session           |
| `/plan`             | Create or update the living plan               |
| `/snapshot`         | Raw state dump before risky experiments        |
| `/prune`            | Remove stale content from memory               |
| `/summarize-session`| End-of-session structured wrap-up              |

## Recommended Workflow

```text
Long session (exploration, iteration, decision-making)
    ↓
/compact   →  compress noisy history into memory/active.md
    ↓
/checkpoint →  lock stable state into checkpoints/
    ↓
Conversation reset  (deliberate, not failure)
    ↓
/hydrate   →  reload context into clean session
    ↓
Continue work
```

The reset is **good practice**, not failure. Clean context improves
reasoning quality.

## Project Structure

```text
project/
├── plan.md                 # Living plan — intent, goals, tasks
├── checkpoints/            # Stable state captures
│   └── YYYY-MM-DD-vN.md
├── memory/
│   ├── active.md           # Current operational context
│   └── archive/            # Previous compacted states
├── decisions/              # Decision log (ADR-style)
│   └── NNN-title.md
└── snapshots/              # Raw experimental captures
    └── YYYY-MM-DDTHHM.md
```

## Contents of This Repo

- [`docs/`](docs/) — Architecture, workflow, artifact spec, anti-patterns
- [`skills/`](skills/) — Skill definitions with prompts and usage guides
- [`templates/`](templates/) — Artifact templates ready to copy
- [`examples/pathfinder/`](examples/pathfinder/) — Working example

## Design Principles

1. **State over history** — preserve decisions, not conversations
2. **Operational over narrative** — active constraints, not story arcs
3. **Resumable over complete** — optimize for continuation
4. **Human-readable AND AI-readable** — markdown, always
5. **Versionable** — every artifact belongs in git
6. **Composable** — artifacts reference each other, not duplicate

## Applicability

This framework is domain-agnostic. It has been validated with:

- Software projects
- Creative writing
- Research and analysis
- Worldbuilding and game preparation
- Long-form documentation
- Design and architecture work
