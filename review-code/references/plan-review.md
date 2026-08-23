# Technical Plan And Design Review

Review a proposal for executable decisions, overlooked production risk, and
unnecessary complexity. Do not rewrite it into a standard template or block it
on details that can safely be decided during implementation.

## Evidence

- Read the proposal, linked requirements, relevant repository guidance, and the
  existing implementation boundaries it intends to change.
- Treat repository domain language, `CONTEXT.md`, `CONTEXT-MAP.md`, and
  architecture decision records as evidence when present, not as automatically
  correct constraints.
- Use TWG for material company requirements or decisions that the proposal
  references but does not contain.
- State when a conclusion depends on missing or stale evidence.

## Review Questions

Apply only the questions relevant to the proposal:

- **Outcome:** Is observable success clear? Are goals, non-goals, and scope
  consistent with the requested result?
- **Assumptions:** Which facts must be true? Does current code or evidence
  support them?
- **Domain model:** Are important terms, ownership boundaries, invariants, and
  state transitions explicit and consistent with the system?
- **Interfaces:** Are affected callers, APIs, schemas, events, persistence, and
  compatibility obligations understood?
- **Failure behavior:** Are partial failure, retries, idempotency, concurrency,
  security, privacy, and data integrity addressed where material?
- **Delivery:** Can the change be split into thin, complete increments? Are
  migration, rollout, rollback, and reversibility credible?
- **Operations:** Will operators be able to observe success, diagnose failure,
  and contain impact?
- **Verification:** Are acceptance criteria and checks tied to observable
  behavior and the actual risk?
- **Simplicity:** Does the proposal reuse existing code, platform facilities, or
  dependencies before adding abstractions or infrastructure?

## Feedback

Lead with blocking or material findings, ordered by impact. For each finding,
identify the affected decision, the triggering condition, the consequence, the
supporting evidence, and the smallest correction or decision needed.

Separate these from:

- open questions that genuinely block execution
- assumptions that should be confirmed but need not block the plan
- optional simplifications or follow-up improvements

Calibrate challenge to evidence. Do not manufacture opposition, demand every
edge case be specified up front, or replace a sound local change with a broad
redesign.
