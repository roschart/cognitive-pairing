# Plan: Create cp-brainstorming Skill

## Context

- The cognitive-pairing framework (v3.1) lacks a structured
  thinking/exploration phase before implementation begins.
- Two external skills were analyzed as prior art:
  superpowers `brainstorming` (linear, 9-step checklist,
  spec-driven) and openspec `openspec-explore` (conversational
  stance, no fixed workflow, ASCII-heavy).
- Neither skill supports holistic-incremental design — the
  practitioner's preferred pattern of sketching all sections
  as titles first, validating coherence, then deepening
  iteratively.
- cp-discovery already handles project context exploration
  (analogous to step 1 of brainstorming) — cp-brainstorming
  must not duplicate that.
- Canon provides persistent project context, eliminating
  the need to re-explore on every session (a token cost
  problem in brainstorming's approach).

## Decisions

- **Name: cp-brainstorming** (not cp-exploration): avoids
  confusion with cp-discover which explores existing context
- **Philosophy: openspec-explore stance**: curious, adaptive,
  patient — not a checklist. "Stance, not workflow."
- **Design depth is emergent**: no mandatory spec document.
  Macro design → project.md, micro design → plan body,
  standalone design doc only when design is large and closed
- **Holistic-incremental pattern**: skeleton first (titles +
  one-liners), coherence check, progressive deepening across
  all sections simultaneously — not linear section-by-section
- **ASCII diagrams over web companion**: keeps things simple,
  constrains complexity naturally, works everywhere
- **Hard gate from brainstorming**: no implementation until
  design is validated — but the gate is conversational, not
  a checklist step
- **Artifact proposals from brainstorming**: after thinking
  crystallizes, offer to capture in the right place (plan,
  project, canon) — but never auto-capture
- **Self-review and user-review gates**: adopt from
  brainstorming — check for placeholders, contradictions,
  ambiguity before presenting to human
- **Canon-aware**: leverage canon to avoid re-exploring
  settled context; propose canon additions when new truths
  emerge

## Tasks

- [ ] write SKILL.md for cp-brainstorming
    - [ ] define the stance (adapted from openspec-explore)
    - [ ] define "what you might do" menu (not a sequence)
    - [ ] document holistic-incremental design pattern
    - [ ] document artifact routing table (where insights go)
    - [ ] define the hard gate (no implementation in explore)
    - [ ] define transition: how brainstorming ends
    - [ ] add guardrails section
    - [ ] add examples for different entry points
- [ ] integrate with existing cp-* skill family
    - [ ] ensure cp-discover is upstream (context already
      loaded via canon)
    - [ ] ensure cp-plan is downstream (brainstorming flows
      into plan creation)
    - [ ] update cp-session-end if brainstorming state needs
      persisting
- [ ] deploy and validate
    - [ ] make sync to deploy
    - [ ] test in a real brainstorming session

## Potential Work

- [ ] explore whether brainstorming insights should persist
  in a lightweight artifact between sessions
  **Promote when:** real usage shows sessions losing
  brainstorming context across resets
- [ ] consider a "resume brainstorming" flow for multi-session
  explorations
  **Promote when:** first complex brainstorming spans 2+
  sessions

## Next Session

> Paused: 2026-05-26

- Start with SKILL.md: write the stance and "what you might
  do" sections first (skeleton)
- Key design reference: openspec-explore for tone,
  brainstorming for artifact gates
- Review the artifact routing table (plan vs project vs
  canon vs standalone doc)
