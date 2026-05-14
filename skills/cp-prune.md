# cp-prune

Remove stale, obsolete, or low-value content from working memory and
checkpoints.

---

## Purpose

Artifacts accumulate noise over time even with disciplined compaction.
Resolved decisions that are no longer relevant, constraints that no
longer apply, completed work that is not needed for orientation —
all of these consume cognitive budget without contributing value.

`cp-prune` is a maintenance skill. It should not be needed frequently
if `cp-compact` is run properly. Use it when memory feels bloated or
when a major phase boundary has been crossed.

---

## Trigger

Run `cp-prune` when:

- `memory/active.md` exceeds 1500 words despite recent compaction
- A major phase of the project has completed and early decisions
  are no longer relevant
- The project has pivoted and old constraints or goals are stale
- Checkpoints have accumulated and most are no longer needed as
  recovery anchors
- The "Recent Decisions" section of memory refers to things from
  months ago

Do NOT prune reactively during active work. Prune at phase boundaries
or during maintenance sessions.

---

## Input

Provide the AI with:

1. The current `memory/active.md`
2. The `plan.md` (to verify what is still active)
3. The latest checkpoint (to verify what is stable)
4. Optional: a note on what phase just ended or what changed

---

## Output

- Produces a pruned `memory/active.md` (human reviews before replacing)
- Optional: identifies checkpoints in `checkpoints/` that can be
  archived or deleted
- Does NOT automatically delete anything — outputs recommendations,
  human decides

---

## Prompt

Use this instruction with your AI assistant:

```
cp-prune

Review memory/active.md against the current plan.md and latest
checkpoint. Identify and remove content that no longer serves active
work.

For each item in memory, apply this test:
  "If this were missing from context, would it affect current or
   near-future work?"
  - YES → keep
  - NO → remove or archive

Specifically prune:
  - Decisions that are stable and no longer in flux (move to checkpoint;
    they do not need to stay in active memory)
  - Goals that have been achieved
  - Constraints that no longer apply (note WHY they no longer apply)
  - "Recent Decisions" older than 2-3 sessions that are now background
    facts, not active decisions
  - Open questions that were implicitly resolved
  - Do Not Revisit entries that are so old they are no longer a risk

Output:
  1. A pruned memory/active.md
  2. A short list of what was removed and why (so the human can verify)
  3. A list of checkpoints that could be archived (if any), with reason

Rules:
  - Do NOT remove something just because it is old — remove it because
    it is no longer operationally relevant
  - If uncertain, keep it and flag it: "[FLAGGED: may be obsolete]"
  - The human has final say on all deletions
```

---

## Review Checklist

Before accepting pruned memory:

- [ ] Nothing currently active was removed
- [ ] "Do Not Revisit" still covers all genuinely closed questions
- [ ] Canon (locked facts) is intact and complete
- [ ] The removal list makes sense — no surprises
- [ ] Resulting memory is under 1000 words (if not, more pruning needed)
- [ ] Flagged items are reviewed and decided (keep or remove)

---

## Archiving Checkpoints

Old checkpoints do not need to be deleted. If they are no longer useful
as recovery anchors but you want to preserve them:

```text
checkpoints/archive/
  2026-01-15-v0.1.md   # archived — superseded by v0.3
```

Keep at minimum:
- The latest checkpoint (always)
- The checkpoint before any major pivot
- Any checkpoint that resolved a significant blocking issue
