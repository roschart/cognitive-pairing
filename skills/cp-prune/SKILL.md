---
name: cp-prune
description: >
  Remove stale, obsolete, or low-value content from working
  memory and checkpoints. Use when memory exceeds 1500 words
  despite compaction, a major phase has completed, the project
  has pivoted, or old checkpoints clutter the directory. This
  is maintenance, not routine.
metadata:
  author: roschart
  version: "2.0"
---

# cp-prune

Remove stale, obsolete, or low-value content from working
memory and checkpoints.

---

## Purpose

Artifacts accumulate noise over time even with disciplined
compaction. Resolved decisions that are no longer relevant,
constraints that no longer apply, completed work not needed
for orientation — all consume cognitive budget without value.

`cp-prune` is a maintenance skill. It should not be needed
frequently if `cp-compact` is run properly. Use it when memory
feels bloated or when a major phase boundary has been crossed.

---

## Trigger

Run `cp-prune` when:

- `.cp/memory/active.md` exceeds 1500 words despite recent
  compaction
- A major phase has completed and early decisions are no
  longer relevant
- The project has pivoted and old constraints or goals are
  stale
- Checkpoints have accumulated beyond 5-6 files and most are
  no longer needed as recovery anchors
- "Recent Decisions" in memory refers to things from months
  ago

Do NOT prune reactively during active work. Prune at phase
boundaries or during maintenance sessions.

---

## Output

- Produces a pruned `.cp/memory/active.md` (human reviews
  before replacing)
- Identifies checkpoints that can be archived or deleted
- Does NOT automatically delete anything — outputs
  recommendations, human decides
- Does NOT modify `.cp/canon.md` (but may suggest removals)

---

## Execution

When `cp-prune` is invoked the agent performs these steps:

1. **Read inputs**
    - `.cp/memory/active.md`
    - `.cp/canon.md` (to verify locked facts are intact)
    - The latest checkpoint in `.cp/checkpoints/`
    - `plan-<slug>.md` (to verify what is still active)

2. **Apply the relevance test** to each item in memory:
   "If this were missing from context, would it affect
   current or near-future work?"
    - YES → keep
    - NO → remove or archive

3. **Specifically prune:**
    - Decisions that are stable and no longer in flux
    - Goals that have been achieved
    - Constraints that no longer apply (note WHY)
    - "Recent Decisions" older than 2-3 sessions that are now
      background facts
    - Open questions that were implicitly resolved
    - "Do Not Revisit" entries so old they are no longer a
      risk of resurfacing

4. **Suggest canon promotions:** if any fact in memory should
   be permanent, suggest moving it to `.cp/canon.md` (human
   decides).

5. **Produce output:**
    - A pruned `.cp/memory/active.md`
    - A short list of what was removed and why
    - A list of checkpoints that could be archived (if any)

### Rules

- Do NOT remove something just because it is old — remove it
  because it is no longer operationally relevant
- If uncertain, keep it and flag it: "[FLAGGED: may be
  obsolete]"
- The human has final say on all deletions
- Canon facts in `.cp/canon.md` are never pruned by this
  skill — suggest removals to the human if needed

---

## Archiving Checkpoints

Old checkpoints do not need to be deleted. If they are no
longer useful as recovery anchors:

```text
.cp/checkpoints/archive/
  2026-01-15-v0.1.md   # archived — superseded by v0.3
```

Keep at minimum:
- The latest checkpoint (always)
- The checkpoint before any major pivot
- Any checkpoint that resolved a significant blocking issue

---

## Review Checklist

Before accepting pruned memory:

- [ ] Nothing currently active was removed
- [ ] "Do Not Revisit" still covers all closed questions
- [ ] Canon facts in `.cp/canon.md` are intact
- [ ] The removal list makes sense — no surprises
- [ ] Resulting memory is under 1000 words
- [ ] Flagged items are reviewed and decided
