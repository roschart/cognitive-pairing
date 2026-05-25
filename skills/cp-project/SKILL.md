---
name: cp-project
description: >
  Create or refine the project declaration (.cp/project.md)
  that defines intent, constraints, style, and scope. Use when
  starting a project with non-trivial complexity, when multiple
  plans are anticipated, or when the project's identity needs
  to be articulated. Not needed for simple tasks where a single
  plan suffices.
metadata:
  author: roschart
  version: "1.0"
---

# cp-project

Create or refine the project declaration that frames all work
in the project.

---

## Purpose

The project document is the strategic frame that sits above
plans. It declares WHAT the project is and WHY it exists, with
enough constraints and style guidance to steer all downstream
work.

Without a project declaration, plans lack context. The agent
cannot distinguish between "build a family house" and "build
a hospital" — it only sees tasks.

`cp-project` helps the human articulate this declaration and
produces `.cp/project.md`.

---

## Trigger

Run `cp-project` when:

- Starting a new project with non-trivial complexity
- Multiple plans exist or are anticipated under the same
  project
- The project has constraints, style, or identity that must
  govern all work
- A brief, prompt, or conversation has defined intent but no
  persistent artifact captures it yet
- The existing project.md no longer reflects reality after a
  major pivot

Do NOT run when:

- The task is simple enough that a single plan suffices
- The project document already exists and is accurate

---

## Output

- Creates or updates `.cp/project.md`
- Does NOT create plans, checkpoints, or memory
- Does NOT modify `.cp/canon.md`
- Human reviews and commits

---

## Sub-agent execution

File reading is delegated to a cheap sub-agent so that `.cp/`
file contents never enter the main context window.

### Sub-agent prompt

```text
Read the following files from the .cp/ directory and return
their content verbatim. Do not infer or add anything.

Files to read:
1. .cp/project.md — if it exists
2. .cp/canon.md — if it exists

Return exactly this format:

### Sub-agent output

**Read:** <comma-separated list of files successfully read>
**Missing:** <files not found, or "none">

#### project.md content
<Verbatim content, or "not found">

#### canon.md content
<Verbatim content, or "not found">

Word budget: 300 words maximum.
```

### How the main agent uses the output

1. **Launch sub-agent** (use the cheapest/fastest model available — this is a file-reading task, not a reasoning task) with the prompt above
2. **Receive content** — `.cp/` files are now out of main
   context
3. **Gather intent from the human** (for new declarations)
   or **identify what changed** (for refinements)
4. **Draft `.cp/project.md`** and show to human before writing

---

## Execution

When `cp-project` is invoked the agent performs these steps:

### Creating a new project declaration

1. **Launch sub-agent** to read `.cp/` files (see
   Sub-agent execution above). Wait for the content.

2. **Gather intent** from the human. Ask focused questions:
    - What is this project? (identity — not features)
    - Why does it exist? (intent — what outcome matters)
    - What constraints bound the work? (time, budget,
      skills, energy, technology)
    - What style or philosophy should guide decisions?
    - What matters most vs least? (priority hierarchy)
    - What is this project NOT? (anti-patterns)
    - How do we know it is on track or done? (success
      criteria)

2. **Draft `.cp/project.md`** using this structure:

   ```markdown
   # Project: <name>

   ## Identity
   What this project IS. One to three sentences.
   Not what it does — what it is.

   ## Intent
   Why this project exists. What outcome it targets.
   The reason all the work matters.

   ## Constraints
   Real limits: time, budget, skills, technology, people,
   energy. Things that bound the solution space.

   ## Style
   How the work should feel. Design philosophy, aesthetic,
   approach. The qualitative criteria that guide decisions
   when multiple valid options exist.

   ## Priority Hierarchy
   What matters most, what matters less. Ordered by
   importance. When two goals conflict, the higher one
   wins.

   ## Anti-patterns
   What this project is NOT. What to avoid. Explicit
   negative space that prevents scope drift and
   misinterpretation.

   ## Success Criteria
   How to know the project is done or on track.
   Observable, not aspirational.
   ```

3. **Show the draft** to the human for review before writing.

4. **Write the file** only after human approval.

### Refining an existing project declaration

1. **Launch sub-agent** to read `.cp/` files (see
   Sub-agent execution above). The sub-agent returns the
   current project.md and canon.md content.
2. **Identify** what has changed — ask the human what
   triggered the refinement
3. **Propose specific edits** — show before/after for each
   section that changes
4. **Apply changes** only after human approval

### Rules

- Sections can be omitted if genuinely not applicable. Not
  every project needs a Style section or Anti-patterns.
  The minimum viable project document has Identity and
  Intent.
- Do NOT invent constraints or anti-patterns the human has
  not stated. Ask, do not assume.
- Do NOT include tasks or work items — that is the plan's
  job.
- Do NOT duplicate facts already in `.cp/canon.md`.
- The document should be concise. If any section exceeds
  ~100 words, it probably contains implementation detail
  that belongs in a plan.
- Project documents are stable — they capture foundational
  intent, not session-specific decisions.

---

## Review Checklist

Before committing the project declaration:

- [ ] Identity answers "what is this?" without listing
      features
- [ ] Intent answers "why does this matter?" clearly
- [ ] Constraints are real limits, not aspirations
- [ ] Priority Hierarchy resolves conflicts (if X vs Y,
      which wins?)
- [ ] Anti-patterns prevent the most likely misinterpretation
- [ ] Success Criteria are observable, not vague
- [ ] No tasks or work items are present (those go in plans)
- [ ] No duplication with `.cp/canon.md`
- [ ] Total length is under 500 words
