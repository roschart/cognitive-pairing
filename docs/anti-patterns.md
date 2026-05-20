# Anti-Patterns and Failure Modes

Common ways the Cognitive Pairing workflow breaks down, with
diagnosis and correction for each.

---

## Anti-Pattern 1: Narrative Summaries

**Symptom:** Checkpoints or memory files start with "First we
discussed X, then we decided Y, and after exploring Z..."

**Why it fails:** Narrative history consumes context budget
without providing operational value. It documents the journey,
not the destination.

**Correct behavior:** State only what is TRUE now. Decisions,
constraints, direction, pending work. No "how we got here".

**Detection:** If any sentence starts with "we" or contains
past-tense verbs describing process rather than outcome, it is
probably narrative noise.

---

## Anti-Pattern 2: Memory Bloat

**Symptom:** `memory/active.md` grows session by session and is
never pruned. Starts to look like a meeting log.

**Why it fails:** Working memory is useful only when minimal.
A 5000-word active memory file defeats its own purpose.

**Correct behavior:** Each `cp-compact` cycle should replace,
not append. Resolved items are removed. Completed decisions
move to checkpoints. Permanent facts move to canon.md.
Target: 500–1500 words.

**Detection:** Active memory longer than 1500 words, or
containing references to things resolved more than two
sessions ago.

---

## Anti-Pattern 3: Checkpoint Proliferation

**Symptom:** A checkpoint is created after every session
regardless of whether a stable milestone was reached.

**Why it fails:** Checkpoints accumulate as noise. Their value
depends on representing meaningful milestones.

**Correct behavior:** Create checkpoints at genuine stability
points: decisions locked, features complete, phase boundaries,
before pivots.

**Detection:** Multiple checkpoints in a single day with
minimal differences between them.

---

## Anti-Pattern 4: Skipping the Reset

**Symptom:** Sessions run indefinitely without resetting. The
AI context window fills slowly and reasoning quality degrades.

**Why it fails:** The system is designed around deliberate
resets. A session that runs forever accumulates all the
problems the framework tries to solve.

**Correct behavior:** Treat resets as healthy maintenance.
`cp-compact` → `cp-checkpoint` → end session → new session
→ `cp-hydrate`.

**Detection:** Sessions exceeding ~30 exchanges without
compaction; noticeable AI confusion about earlier decisions.

---

## Anti-Pattern 5: Over-Compacting

**Symptom:** `cp-compact` is run after every few messages.
Memory is constantly being rewritten.

**Why it fails:** Compaction has overhead. Run it too often
and it becomes the work.

**Correct behavior:** Compact at natural breakpoints — end of
a working block, after a set of decisions, before a milestone.
Not constantly.

**Detection:** Running `cp-compact` more than once per session
in most sessions.

---

## Anti-Pattern 6: Duplicating Information Across Artifacts

**Symptom:** The same fact appears in `plan.md`,
`memory/active.md`, the latest checkpoint, AND `canon.md`.
With slight variations.

**Why it fails:** Divergence is inevitable. Which version is
correct? The artifacts lose trust.

**Correct behavior:** Each piece of information lives in one
canonical artifact. Others reference it.

- Permanent locked facts → `canon.md`
- Current state → latest checkpoint
- Session-specific constraints → `memory/active.md`
- Goals and tasks → `plans/plan-<slug>.md`
- Project intent and constraints → `project.md`

**Detection:** Copy-pasting content between artifact files.

---

## Anti-Pattern 7: Canon Pollution

**Symptom:** `canon.md` grows with every session. Items are
added that are really session-specific constraints, not
permanent facts.

**Why it fails:** Canon should be a short, stable document.
If it grows to 50+ items, it loses its function as a quick
reference for ground truth.

**Correct behavior:** Only add to canon when a fact is
genuinely permanent and non-negotiable. Temporary constraints
belong in `memory/active.md`.

**Detection:** Canon has more items than can be read in
30 seconds; items reference specific sessions or dates.

---

## Anti-Pattern 8: Human Never Reviews AI-Generated Artifacts

**Symptom:** `cp-compact` output is accepted without human
review. Checkpoints are created and immediately used.

**Why it fails:** AI compaction makes errors. It may omit
critical constraints, soften hard decisions, or misclassify
active problems as resolved.

**Correct behavior:** Human reviews all AI-generated state
artifacts before they are used as authoritative input for
future sessions.

**Detection:** The project direction drifts in ways not
explained by decisions; constraints are silently violated.

---

## Anti-Pattern 9: The Plan Becomes a Todo List

**Symptom:** `plan-<slug>.md` degrades into a flat list of
tasks. The Goals and Direction sections are never updated.

**Why it fails:** The plan loses its strategic function. It
becomes a task tracker, which is not its job.

**Correct behavior:** `plan-<slug>.md` should always answer
"why are we doing any of this?" alongside the tasks. If the
goals section hasn't been touched in months, the plan is
degraded.

**Detection:** Plan has more than 20 tasks; Goals section
says something generic like "build the thing".

---

## Anti-Pattern 10: Ignoring Do Not Revisit

**Symptom:** Ideas explicitly parked in memory's "Do Not
Revisit" section are brought up again because context was
not loaded properly.

**Why it fails:** The same discussion happens repeatedly.
Cognitive budget is spent re-deciding closed questions.

**Correct behavior:** cp-hydrate must load the "Do Not
Revisit" section. It should be treated as a hard constraint.

**Detection:** Spending more than 10 minutes discussing
something marked Do Not Revisit.

---

## Failure Mode: Artifact Drift

When checkpoints, memory, and plan describe different realities
due to inconsistent updates.

**Recovery:** Run `cp-compact` with all artifacts as input.
Produce a reconciled `memory/active.md` that acknowledges the
inconsistency, then have a human arbitrate which version is
authoritative before creating a fresh checkpoint.

---

## Failure Mode: Context Poisoning

When a session loads a stale or corrupted checkpoint and
generates work based on invalid state.

**Recovery:** Identify the last trusted checkpoint by reviewing
the `checkpoints/` directory. Run `cp-hydrate` from that
version. Accept that work since that checkpoint may need
re-evaluation.

---

## Failure Mode: Total Loss of Context

When no checkpoint or memory files exist.

**Prevention:** `.cp/` should be committed to git after every
working session.

**Recovery:** Reconstruct from whatever artifacts remain.
If `project.md`, active plans, and `canon.md` survived, they
provide intent, goals, and ground truth. Commit messages and
code comments can reconstruct a rough checkpoint manually.
