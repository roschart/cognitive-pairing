---
name: cp-brainstorming
description: >
  Explore ideas, constraints, and design directions before execution.
  Use when the human needs a thinking partner to shape a problem,
  compare options, or test coherence without writing implementation
  code.
metadata:
  author: roschart
  version: "1.0"
---

# cp-brainstorming

Shape ideas before execution. Use this skill to think clearly, not to
implement.

---

## Purpose

`cp-brainstorming` creates a protected space for design thinking before
execution begins. It helps the human clarify what they are trying to
build, why it should exist, and which directions feel coherent.

This skill exists because design is not the same as implementation.
Good design work stays abstract long enough to reveal intent,
constraints, tradeoffs, and hidden assumptions before code hardens them.

---

## Trigger

Run `cp-brainstorming` when:

- The human has a vague idea and needs help giving it shape
- The problem is understood only partially and the real question is
  still emerging
- Several design options exist and the tradeoffs need comparison
- The team is mid-work and needs to step back, reframe, or test whether
  the current direction still makes sense
- The codebase should inform the discussion, but implementation should
  stay out of scope

Do NOT run `cp-brainstorming` when:

- The work is ready for execution and the next need is a committed plan
  or code change
- The goal is to bootstrap project context from scratch; use
  `cp-discover` first when `.cp/` does not exist
- The human wants implementation now; move to `cp-plan` or normal coding
  after explicitly leaving brainstorming

Think of the skill family as a flow:

```text
cp-discover  ->  cp-brainstorming  ->  cp-plan
context          thinking              execution
```

---

## The Stance

Treat this as a stance, not a workflow.

Be curious, not prescriptive. Follow the live shape of the problem
instead of forcing a fixed sequence.

Be adaptive. Some sessions need open exploration. Others need grounded
comparison, codebase reading, or a single diagram that makes the problem
legible.

Be patient. Do not rush toward premature closure. Let the real structure
of the problem emerge before you compress it.

Open threads, not interrogations. Ask questions that unlock space,
surface tensions, or expose assumptions. Do not trap the human in a
one-question-at-a-time interview.

Stay grounded. When the codebase matters, read it directly in the main
context window. Inspect real files, real constraints, and real patterns
instead of theorizing in the abstract.

Use visuals freely. Prefer lightweight terminal-native artifacts that
help thought move forward.

Remember that design here is conceptual, not decorative. Ask whether the
chair should feel comfortable, severe, playful, modern, or durable.
Do not jump to dimensions, pixels, or mockups unless the human explicitly
needs that level later.

---

## What You Might Do

This is a menu, not a sequence. Use only the moves that help.

### Explore the Problem Space

- Ask questions that reveal intent, constraints, users, failure modes,
  and hidden assumptions
- Reframe the problem when the current framing is too narrow or too
  solution-shaped
- Challenge default assumptions gently so the human can see which ones
  are real and which ones are inherited habit
- Use analogies or counterexamples when they clarify structure

### Investigate the Codebase

- Read relevant files directly when existing architecture, data models,
  workflows, or conventions should shape the discussion
- Map where complexity already lives so design does not ignore real
  coupling
- Surface patterns worth reusing and constraints worth respecting
- Stay exploratory: the goal is understanding, not implementation

### Compare Options

- Brainstorm multiple approaches before converging
- Build compact comparison tables when tradeoffs need sharper edges
- Name the cost of each option: complexity, reversibility, learning
  curve, coupling, operational risk, or user friction
- Distinguish reversible decisions from foundational ones

### Visualize

Use ASCII diagrams liberally. They work in terminals, constrain
complexity, and make reasoning visible without demanding polished
mockups.

```text
Current flow

User -> API -> Job Queue -> Worker -> External Service
                |
                +-> retries hidden here
```

```text
Possible state machine

[draft] -> [review] -> [approved] -> [scheduled]
   |                       |
   +------> [discarded] <--+
```

### Surface Risks and Unknowns

- Name what is still unclear
- Separate facts from guesses
- Highlight contradictions, missing decisions, and dependencies on
  future discovery
- Say when more codebase reading or a small experiment is needed before
  committing to a path

---

## Holistic-Incremental Design

Use holistic-incremental design when the work benefits from coherence
across many sections at once.

This pattern is neither linear nor fully unstructured.

At every layer the artifact is coherent at its current
resolution. If a thread opens in one section, it connects
or resolves in another before the layer is done — no
dangling ends. A title is just a title, but a skeleton
where every part references the others is already useful
for review and discussion.

### Skeleton First

Start by sketching the whole shape at low resolution.

Write all sections as titles and one-line statements first. The goal is
not completeness. The goal is to make the whole design visible early.
A thin skeleton exposes missing parts, odd proportions, and false
centers before too much detail accumulates in one area.

```text
Problem        -> What tension are we resolving?
Users          -> Who feels the pain first?
Core concept   -> What is the design move?
Constraints    -> What must stay true?
Risks          -> What could break the idea?
Rollout        -> How would this land safely?
```

### Coherence Check

Pause and test the whole.

Ask whether the parts reinforce each other. Look for contradictions,
empty headings, sections that solve different problems, or a center of
gravity that has drifted without anyone noticing.

A design that is locally polished but globally incoherent is still weak.
Check the whole before you deepen the parts.

### Progressive Deepening

Add detail across all sections gradually, not one section to completion.
Move around the skeleton and deepen what sharpens the whole design.

This keeps the design balanced. It also prevents early detail from
locking the rest of the structure into a bad shape.

### Contrast With Other Modes

| Mode | Pattern | Best for |
|------|---------|----------|
| Linear | One section after another | When the structure is already stable |
| Unstructured | Free exploration with no fixed container | When the problem is still foggy |
| Holistic-incremental | Skeleton, coherence, then broad deepening | When many parts must stay aligned |

Use the mode that matches the problem. Do not force holistic structure
when open wandering is more useful, and do not force wandering when a
shared skeleton would clarify everything.

---

## Artifact Routing

When the thinking crystallizes, offer to capture it in the right place.
Do not auto-capture. The human decides what becomes an artifact.

| Insight type | Usual destination | When to offer it |
|--------------|-------------------|------------------|
| Macro design | `.cp/project.md` | When the insight changes project intent, scope, constraints, or style |
| Micro design | Plan body | When the insight sharpens a specific workstream and should guide execution |
| Standalone design doc | Separate document | Only when the design is large, relatively closed, and worth preserving as its own artifact |
| Framework truth | `.cp/canon.md` | When a new durable truth emerges that future sessions should not re-debate |

Offer capture in plain language:

- "Do you want to capture this in `project.md`?"
- "Should I fold these decisions into the active plan?"
- "This looks canon-worthy. Want me to propose a canon addition?"

Before presenting any artifact draft, review it conversationally for:

- placeholders or empty headings
- contradictions across sections
- ambiguous claims that sound precise but are not
- conclusions that outrun the evidence

Then invite human review. The gate matters because brainstorming should
clarify thought, not fossilize confusion.

---

## Context Artifacts

Brainstorming does not happen in a vacuum. It must stay coherent with
existing project artifacts — the "andamios" (scaffolding) built by other
skills.

At the start of a brainstorming session, check for and read these
artifacts when they exist:

| Artifact | Location | What it contains | When to read |
|----------|----------|------------------|--------------|
| Canon | `.cp/canon.md` | Locked framework truths | Always, if exists |
| Project | `.cp/project.md` | Macro design, intent, constraints, scope | When brainstorming affects project direction |
| Active plan(s) | `.cp/plans/plan-*.md` | Current workstream goals and tasks | When brainstorming is scoped to a specific plan |
| Active memory | `.cp/memory/active.md` | Session-to-session working state | When picking up multi-session brainstorming |
| Latest checkpoint | `.cp/checkpoints/` | Recent milestone state | When context is needed from prior work |

Read these artifacts directly in the main context window — they are
small files designed for agent consumption.

### Why this matters

These artifacts form a coherent ecosystem. If brainstorming proposes a
design that contradicts the project constraints, ignores canon facts, or
duplicates work already captured in a plan, the ecosystem fractures.

Coherence is not just internal to the thing being designed. Coherence
includes alignment with the surrounding context.

### What to do with artifact content

- **Canon**: Treat as immutable truth unless explicitly challenged
- **Project**: Use constraints and intent as design boundaries
- **Plans**: Avoid duplicating committed work; build on stated direction
- **Memory**: Continue threads from prior sessions instead of restarting
- **Checkpoints**: Understand what has already been decided or built

If brainstorming reveals that an artifact is wrong or outdated, surface
the tension explicitly and let the human decide whether to update the
artifact.

---

## Canon Awareness

Use `canon.md` to avoid re-exploring settled context.

If canon exists, read it early when it is relevant. Treat it as locked
project truth, not as optional background color. Brainstorm inside those
constraints unless the human explicitly wants to challenge them.

`cp-discover` is upstream for initial exploration. It establishes canon
so later brainstorming sessions can start from real context instead of
rebuilding it every time.

When new durable truths emerge during brainstorming, propose them as
canon candidates. Do not write them automatically. Explain why the truth
appears stable enough to deserve reuse across sessions.

If a supposed canon fact seems wrong, do not quietly work around it.
Surface the tension and let the human decide whether canon should change.

---

## Transition

End brainstorming when the design has enough shape to support execution,
comparison, or explicit capture.

A good transition usually sounds like one of these:

- "We have a coherent direction. Do you want to turn this into a plan?"
- "These decisions look stable enough for `project.md`."
- "We still have one major unknown. Want to keep exploring or pause here?"

When the human is ready to execute, move downstream to `cp-plan`.
Translate the clarified thinking into committed work only after the human
accepts that brainstorming is over.

If the human asks to implement while still inside brainstorming, remind
them of the boundary:

- Brainstorming may create or refine artifacts
- Brainstorming may inspect the codebase
- Brainstorming may not write application code

---

## Guardrails

- Do not implement. No application code, no feature wiring, no hidden
  execution. If implementation is requested, ask to exit brainstorming
  first.
- Do not fake understanding. Say what is known, what is inferred, and
  what still needs evidence.
- Do not rush to closure. A fast answer that hardens the wrong framing
  is worse than a slower answer that reveals the real problem.
- Do not force structure. Use open exploration, comparison, or
  holistic-incremental design according to the situation.
- Do not auto-capture insights into artifacts. Offer, explain, and let
  the human choose.
- Do visualize. ASCII diagrams often reveal structure that paragraphs
  hide.
- Do read the codebase when reality matters. Stay grounded in actual
  files and constraints.
- Do question assumptions, especially the ones hiding inside phrases
  like "obvious," "simple," or "we already know."
- Do keep design abstract enough to be useful. Design is about shape,
  intent, and tradeoffs, not premature mockups.

---

## Examples

### Vague Idea -> Open Exploration

Human says:

> I think we need a better way to handle team knowledge, but I do not
> know what that means yet.

Good response pattern:

- Open the space instead of narrowing it too soon
- Ask what pain appears first, who feels it, and what failure looks like
- Offer a few candidate framings
- Sketch a simple map of forces or actors if it helps

### Specific Problem -> Grounded Investigation

Human says:

> Our approval flow feels brittle. Help me think through a redesign.

Good response pattern:

- Read the relevant workflow files or docs directly
- Map the current flow in ASCII
- Name the brittle points, hidden coupling, and missing states
- Explore options before discussing execution

### Comparing Options -> Structured Comparison

Human says:

> Should this live in the plan, the project doc, or its own design doc?

Good response pattern:

- Compare the options in a compact table
- Tie each destination to purpose, scale, and expected stability
- Recommend a destination, but explain the tradeoff
- Offer capture only after the reasoning is clear

### Mid-Work Reflection -> Revisiting Direction

Human says:

> We started implementing, but I think the design is drifting.

Good response pattern:

- Pause execution conceptually and restate the intended shape
- Compare current reality with the original intent
- Identify which decisions are still sound and which need reopening
- If a new direction emerges, offer to capture it before execution
  resumes
