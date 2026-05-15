# Pathfinder Campaign — Example

This directory demonstrates the Cognitive Pairing workflow applied
to a tabletop RPG campaign preparation project.

## Structure

```text
pathfinder/
├── plan-campaign-arc1.md   # Living plan (content layer)
└── .cp/                    # State management layer
    ├── canon.md            # Locked world/character facts
    ├── checkpoints/        # Stable state captures
    └── memory/
        ├── active.md       # Current working memory
        └── archive/        # Previous compacted memories
```

The `.cp/` folder is analogous to `.git/`: it holds
infrastructure, not content.

## Reading Order

1. `plan-campaign-arc1.md` — the living plan
2. `.cp/canon.md` — permanent ground truth
3. `.cp/memory/active.md` — current operational context
4. `.cp/checkpoints/` — stable state captures
