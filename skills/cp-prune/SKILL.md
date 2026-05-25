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

## Sub-agent execution

File reading is delegated to a cheap sub-agent so that `.cp/`
file contents never enter the main context window.

### Sub-agent prompt

```text
Read the following files from the .cp/ directory and return
a structured analysis. Do not infer or add anything not
present in the files.

Files to read (in order):
1. .cp/memory/active.md
2. .cp/canon.md
3. .cp/checkpoints/ — find and read the most recent file
4. .cp/plans/plan-*.md — all active plans

Return exactly this format:

### Sub-agent output

**Read:** <comma-separated list of files successfully read>
**Missing:** <files not found, or "none">

#### Full active.md content
<Verbatim content of active.md>

#### Latest checkpoint — current state
<Current State and Pending Work sections only, verbatim.>

#### Active plans — task status
<For each plan found: plan name + full task list with current
check states.>

#### Canon facts
<Full list — items in active.md that duplicate canon should
be removed.>

Word budget: 600 words maximum.
```

### How the main agent uses the output

1. **Launch sub-agent** (model: haiku) with the prompt above
2. **Receive structured analysis** — `.cp/` files are now
   out of main context
3. **Apply the relevance test** to each item: "if missing,
   would it affect current or near-future work?"
4. **Produce pruned `active.md` draft + removal list**
5. **Show draft** to human for review before writing

---

## Execution

When `cp-prune` is invoked the agent performs these steps:

1. **Launch sub-agent** to read `.cp/` files (see
   Sub-agent execution above). Wait for the structured
   analysis.

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
