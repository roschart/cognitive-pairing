# Plan: v3 Artifact Model

## Context

- v2.1 established 4 artifact types (plan, canon, checkpoint,
  memory) with 7 skills
- Analysis of a real-world project prompt revealed a gap: no
  artifact for project-level intent, constraints, and style
- `project.md` introduced as 5th artifact type; plans moved
  inside `.cp/plans/` (done, committed on this branch)
- Next step: align the skill and spec structure with the new
  model — each artifact owns its template in its skill,
  `artifact-spec.md` becomes a high-level reference only

## Decisions

- **project.md is a cp artifact**: not external content, it is
  management infrastructure like the rest of `.cp/`
- **plans live inside .cp/**: all management artifacts together,
  project root stays clean
- **each artifact has a skill owner**: the owning skill contains
  the template; canon is the exception (human-owned)
- **artifact-spec.md is reference, not template source**: avoids
  duplication with skill files

## Tasks

- [x] add project.md artifact type · ✓ 2026-05-20
- [x] move plans inside .cp/plans/ · ✓ 2026-05-20
- [x] create cp-project skill · ✓ 2026-05-20
    - [x] define SKILL.md with project.md template inside
    - [x] add trigger conditions and execution steps
    - [x] register in skills/README.md index
    - [x] verify with `make verify`
- [x] refactor artifact-spec.md · ✓ 2026-05-20
    - [x] add summary table (artifact, purpose, skill,
          location, on-end)
    - [x] convert each artifact section to consistent header
          (purpose, skill, location, owner, create-when,
          not-needed, on-end)
    - [x] remove inline templates (reference skill instead)
    - [x] keep canon template in spec (no owning skill)
- [x] update canon with ownership rule · ✓ 2026-05-20
    - [x] add: "Each artifact has an owning skill that
          contains its template; canon is the exception
          (human-owned)"

## Potential Work

- [ ] archive plan-skill-refinement.md (all tasks done)
  **Promote when:** v3 changes are merged to main
- [ ] validate cp-project with a real project (pathfinder)
  **Promote when:** skill is implemented and deployed

## Next Session

> Active: 2026-05-20

- Create cp-project skill
- Refactor artifact-spec.md
- Update canon
