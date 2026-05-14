# cp-snapshot

Create a raw, unfiltered capture of current state before experimental
or risky work.

---

## Purpose

A snapshot is a safety net. Unlike a checkpoint (which requires stable
state), a snapshot captures things as-is — experiments in progress,
broken ideas, uncertain paths. If the experiment fails, the snapshot
enables recovery.

In many projects, git commits serve this purpose adequately. Use
`cp-snapshot` when git is insufficient: when the "state" includes
reasoning, decisions-in-progress, or conceptual work not reflected
in the code.

---

## Trigger

Run `cp-snapshot` when:

- About to try something that might break the current direction
- Exploring a risky alternative with uncertain outcome
- Starting a large refactor or redesign with unclear results
- Working on something experimental that may be discarded
- Before a discussion that might overturn settled decisions

Do NOT use as a substitute for checkpointing. Snapshots are raw and
not authoritative.

---

## Input

Provide the AI with:

1. Current session context (conversation excerpt)
2. The current `memory/active.md`
3. A note on WHY the snapshot is being taken

---

## Output

- Creates `snapshots/YYYY-MM-DDTHHMM-<label>.md`
- Does NOT modify any other artifact
- Disposable — can be pruned once the experiment resolves

---

## Naming Convention

```text
snapshots/
  2026-05-14T1430-before-db-redesign.md
  2026-05-15T0900-alt-auth-experiment.md
```

Always include:
- Timestamp (so multiple snapshots per day work)
- A label describing the trigger or experiment

---

## Prompt

Use this instruction with your AI assistant:

```
cp-snapshot [label]

Capture the current state as a raw snapshot. Include everything
relevant to the current moment, even if incomplete or uncertain.

Use this structure for snapshots/YYYY-MM-DDTHHMM-[label].md:

   # Snapshot: [label] — YYYY-MM-DDTHH:MM

   ## Trigger
   Why this snapshot was taken. One sentence.

   ## Current State (Raw)
   Unfiltered description of where things stand.
   Include: decisions in progress, uncertain areas, competing ideas.
   This section can be messy — that is intentional.

   ## Active Experiments
   What is being tried right now that may or may not work.
   For each: what it is, what success looks like, what failure looks like.

   ## Abandoned Branches (This Session)
   Ideas tried and rejected in THIS session, not yet in memory.
   Brief note on each.

   ## Recovery Notes
   If the experiment fails: what should be restored and how.
   What is the last known good state?

   ## Open Threads
   Anything that was in-flight when this snapshot was taken.

Rules:
- This does NOT need to be clean or complete
- Include ambiguities explicitly — do not resolve them for neatness
- The purpose is recovery and reference, not communication
- Do not use as a checkpoint substitute
```

---

## After the Experiment

Once the experiment resolves:

- **If it worked:** run `cp-compact` to incorporate learnings into
  memory, then `cp-checkpoint` if a milestone was reached. Prune the
  snapshot.
- **If it failed:** recover from the snapshot. Load it alongside
  `memory/active.md`. Decide what to restore, then continue.
- **If inconclusive:** keep the snapshot active. Note its existence
  in memory's Open Questions.

---

## Review Checklist

Before using a snapshot for recovery:

- [ ] Timestamp matches the intended recovery point
- [ ] Recovery Notes section exists and is actionable
- [ ] The experiment label matches what actually happened
