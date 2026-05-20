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

The solution is not better prompts. It is disciplined state
management.

## The Core Insight

Humans already solve this problem naturally: notes, plans, ADRs,
outlines, summaries, documentation. This framework formalizes
those patterns into a set of composable, versionable,
AI-readable artifacts.

## Artifact Hierarchy

| Artifact         | Question it answers             | Owner         | Lifecycle     |
|------------------|---------------------------------|---------------|---------------|
| `project.md`     | What are we building and why?   | Human-curated | Stable        |
| `plans/`         | How and how much is left?       | Human-curated | Living doc    |
| `canon.md`       | What is permanently true?       | Human-curated | Permanent     |
| `checkpoint/`    | Where are we now?               | AI-generated  | Per-milestone |
| `memory/active`  | What do we need right now?      | AI-generated  | Per-session   |

## Skills

| Skill            | Purpose                                  |
|------------------|------------------------------------------|
| `cp-project`     | Create or refine the project declaration  |
| `cp-hydrate`     | Load context at session start             |
| `cp-compact`     | Compress working memory                   |
| `cp-checkpoint`  | Create stable state at milestones         |
| `cp-plan`        | Create or update the living plan          |
| `cp-prune`       | Remove stale content from memory          |
| `cp-session-end` | End-of-session structured wrap-up         |

Skills are designed for AI agents — the agent reads the skill
definition and executes it directly. Both the human and the
agent benefit from the shared artifacts.

## Recommended Workflow

```text
New session
    ↓
cp-hydrate  →  agent loads .cp/ artifacts, shows alignment summary
    ↓
Work (exploration, iteration, decision-making)
    ↓
cp-compact  →  compress noisy history into memory/active.md
    ↓
cp-checkpoint → lock stable state into checkpoints/ (if milestone)
    ↓
cp-session-end → structured wrap-up
    ↓
Conversation reset (deliberate, not failure)
    ↓
New session → cp-hydrate again
```

The reset is **good practice**, not failure. Clean context
improves reasoning quality.

## Project Structure

```text
project/
├── [project content files]
└── .cp/                    # State management layer
    ├── project.md          # Project declaration (intent)
    ├── canon.md            # Locked facts (human-curated)
    ├── plans/
    │   ├── plan-<slug>.md  # Living plans
    │   └── archive/        # Completed plans
    ├── checkpoints/        # Stable state captures
    │   └── YYYY-MM-DD-label.md
    └── memory/
        ├── active.md       # Current operational context
        └── archive/        # Previous compacted states
```

## Contents of This Repo

- [`docs/`](docs/) — Architecture, artifact spec, anti-patterns
- [`skills/`](skills/) — Skill definitions for AI agents
- [`examples/pathfinder/`](examples/pathfinder/) — Working example

## Design Principles

1. **State over history** — preserve decisions, not conversations
2. **Operational over narrative** — active constraints, not arcs
3. **Resumable over complete** — optimize for continuation
4. **Human-readable AND AI-readable** — markdown, always
5. **Versionable** — every artifact belongs in git
6. **Composable** — artifacts reference each other, not duplicate
7. **Skills serve both parties** — the agent executes, the human
   reviews and steers

## Applicability

This framework is domain-agnostic. It has been validated with:

- Software projects
- Creative writing
- Research and analysis
- Worldbuilding and game preparation
- Long-form documentation
- Design and architecture work
