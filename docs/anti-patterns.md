# Anti-Patterns and Failure Modes

Common ways the Cognitive Pairing workflow breaks down, with diagnosis
and correction for each.

---

## Anti-Pattern 1: Narrative Summaries

**Symptom:** Checkpoints or memory files start with "First we discussed
X, then we decided Y, and after exploring Z we landed on..."

**Why it fails:** Narrative history consumes context budget without
providing operational value. It documents the journey, not the
destination.

**Correct behavior:** State only what is TRUE now. Decisions,
constraints, direction, pending work. No "how we got here".

**Detection:** If any sentence in a checkpoint starts with "we" or
contains past-tense verbs describing process rather than outcome, it is
probably narrative noise.

---

## Anti-Pattern 2: Memory Bloat

**Symptom:** `memory/active.md` grows session by session and is never
pruned. Starts to look like a meeting log.

**Why it fails:** Working memory is useful only when minimal. A 5000-word
active memory file defeats its own purpose — the AI still has to process
all of it.

**Correct behavior:** Each `/compact` cycle should replace, not append.
Resolved items are removed. Completed decisions move to checkpoints.
Target: 500–1500 words.

**Detection:** Active memory longer than 1500 words, or containing
references to things that were resolved more than two sessions ago.

---

## Anti-Pattern 3: Checkpoint Proliferation

**Symptom:** A checkpoint is created after every session regardless of
whether a stable milestone was reached.

**Why it fails:** Checkpoints accumulate as noise. Their value depends on
representing meaningful milestones. Checkpointing every day creates a
log, not a recovery system.

**Correct behavior:** Create checkpoints at genuine stability points:
decisions locked, features complete, phase boundaries, before pivots.

**Detection:** Multiple checkpoints in a single day with minimal
differences between them.

---

## Anti-Pattern 4: Skipping the Reset

**Symptom:** Sessions run indefinitely without resetting. The AI context
window fills slowly and reasoning quality degrades gradually.

**Why it fails:** The system is designed around deliberate resets. A
session that runs forever accumulates all the problems the framework
tries to solve.

**Correct behavior:** Treat resets as healthy maintenance. `/compact` →
`/checkpoint` → end session → `/hydrate` → new session.

**Detection:** Sessions exceeding 50+ exchanges; noticeable AI confusion
about earlier decisions; contradictory advice within the same session.

---

## Anti-Pattern 5: Over-Compacting

**Symptom:** `/compact` is run after every few messages. Memory is
constantly being rewritten. The human spends more time managing state
than doing work.

**Why it fails:** Compaction has overhead. Run it too often and it
becomes the work.

**Correct behavior:** Compact at natural breakpoints — end of a working
block, after a set of decisions, before a milestone. Not constantly.

**Detection:** Running `/compact` more than once per session in most
sessions.

---

## Anti-Pattern 6: Duplicating Information Across Artifacts

**Symptom:** The same decision is in `plan.md`, `memory/active.md`, the
latest checkpoint, AND a decision log. With slight variations.

**Why it fails:** Divergence is inevitable. Which version is correct?
The artifacts lose trust.

**Correct behavior:** Each piece of information lives in one canonical
artifact. Others reference it.

- Decision rationale → `decisions/`
- Current state → latest checkpoint
- Active constraints → `memory/active.md`
- Goals and tasks → `plan.md`

**Detection:** Copy-pasting content between artifact files.

---

## Anti-Pattern 7: Treating Snapshots as Checkpoints

**Symptom:** Snapshots are treated as authoritative state references.
Hydration loads from a snapshot instead of a checkpoint.

**Why it fails:** Snapshots are raw and potentially unstable. They
include experiments and broken ideas. Loading them as authoritative
context injects noise.

**Correct behavior:** Use checkpoints for hydration. Use snapshots only
for recovery from failed experiments.

**Detection:** Snapshots are referenced in hydration prompts; old
snapshots accumulate without being pruned.

---

## Anti-Pattern 8: Human Never Reviews AI-Generated Artifacts

**Symptom:** `/compact` output is committed without human review.
Checkpoints are created and immediately used without checking.

**Why it fails:** AI compaction makes errors. It may omit critical
constraints, soften hard decisions, or misclassify active problems as
resolved.

**Correct behavior:** Human reviews all AI-generated state artifacts
before they are used as authoritative input for future sessions.

**Detection:** The project direction drifts in ways not explained by
decisions; constraints are silently violated.

---

## Anti-Pattern 9: The Plan Becomes a Todo List

**Symptom:** `plan.md` degrades into a flat list of tasks. The Goals
and Direction sections are never updated.

**Why it fails:** The plan loses its strategic function. It becomes
a task tracker, which is not its job. Tools like GitHub Issues or ADO
are better task trackers.

**Correct behavior:** `plan.md` should always answer "why are we doing
any of this?" alongside the tasks. If the goals section hasn't been
touched in months, the plan is degraded.

**Detection:** Plan has more than 20 tasks; Goals section says something
generic like "build the thing"; Direction section is empty or stale.

---

## Anti-Pattern 10: Ignoring the Do Not Revisit Section

**Symptom:** Ideas explicitly parked in memory's "Do Not Revisit"
section are brought up again in new sessions because the hydration
prompt was not loaded, or was loaded but ignored.

**Why it fails:** The same discussion happens repeatedly. Cognitive
budget is spent re-deciding already-closed questions.

**Correct behavior:** The "Do Not Revisit" section must be visible in
every hydration prompt. It should be treated as a hard constraint: if a
topic appears there, do not re-open it without explicit human decision to
do so.

**Detection:** Spending more than 10 minutes discussing something marked
Do Not Revisit in memory.

---

## Failure Mode: Artifact Drift

When checkpoints, memory, and plan describe different realities due to
inconsistent updates.

**Recovery:** Run `/compact` with all three artifacts as input. Produce
a reconciled `memory/active.md` that acknowledges the inconsistency,
then have a human arbitrate which version is authoritative before
creating a fresh checkpoint.

---

## Failure Mode: Context Poisoning

When a session loads a stale or corrupted checkpoint and generates work
based on invalid state.

**Recovery:** Identify the last trusted checkpoint by reviewing the
`checkpoints/` directory. `/hydrate` from that version. Accept that
work since that checkpoint may need to be re-evaluated.

---

## Failure Mode: Total Loss of Context

When the working directory is lost, git history is inaccessible, and
no checkpoint files exist.

**Prevention:** `checkpoints/` and `memory/` should be committed to git
after every working session. Enable automated backup if the project is
critical.

**Recovery:** Reconstruct from whatever artifacts remain. If plan.md
survived, it provides goals. Decisions in code comments, commit messages,
or external documents can reconstruct a rough checkpoint manually.
