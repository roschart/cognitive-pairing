# Pathfinder Campaign — Example

This directory demonstrates the Cognitive Pairing workflow applied to
a tabletop RPG campaign preparation project.

## Structure

```text
pathfinder/
├── plan-campaign-arc1.md   # Living plan (content layer)
└── .cp/                    # State management layer
    ├── checkpoints/        # Stable state captures
    ├── memory/
    │   ├── active.md       # Current working memory
    │   └── archive/        # Previous compacted memories
    ├── decisions/          # World-building decisions (ADR-style)
    └── snapshots/          # Pre-experiment state captures
```

The `.cp/` folder is analogous to `.git/`: it holds infrastructure,
not content. The project directory stays clean and focused on actual
work artifacts.

`.cp/` can also be nested — a subdirectory with its own workstream
can have its own `.cp/`. This mirrors how `.gitignore` works: the
nearest `.cp/` wins. In practice, one `.cp/` at the project root
covers almost every use case.

## Reading Order

1. `plan-campaign-arc1.md` — the living plan
2. `.cp/memory/active.md` — current operational context
3. `.cp/checkpoints/` — stable state captures
