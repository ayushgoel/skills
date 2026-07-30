---
name: write-code
description: >-
  Use when implementing features, fixing bugs, refactoring, or making any
  requested code change. Guides scoped implementation, explicit side-effect
  boundaries, focused tests, risk-based verification, company-context discovery
  through TWG, and Bitbucket PR or CI work through PRFlow.
---

# Write Code

Implement the requested behavior with the smallest coherent change that fits the
existing codebase.

## Working Contract

- Inspect the relevant code, tests, repository guidance, and working-tree state
  before editing.
- State assumptions that affect behavior. Ask only when a missing decision cannot
  be recovered from the codebase or available context.
- Prefer established project patterns, dependencies, and domain language.
- Do not add features, configurability, abstractions, or broad cleanup beyond the
  request.
- Preserve unrelated user changes. Every changed line should trace to the
  requested behavior or to cleanup caused by that change.

## Implementation Loop

1. Define observable success criteria.
2. For a bug, reproduce the failure or identify a deterministic failing path.
3. Find the narrowest ownership boundary for the change.
4. Implement the smallest complete solution.
5. Run the most focused relevant test, lint, type, or build check.
6. Broaden verification according to blast radius and shared-contract risk.
7. Inspect the final diff for accidental churn and report remaining risk.

If reproduction is impractical, explain the substitute evidence used. Do not
claim verification that was not performed.

## Tool Routing

- Use `twg` for Jira requirements, Confluence designs, historical decisions,
  ownership, and cross-repository or company context.
- Use `prflow` for direct Bitbucket PR state, review comments, checks, pipelines,
  failed logs, and merge readiness.
- Use local `git`, `rg`, and repository-native build tools for source inspection
  and local verification.
- Read remote context needed to complete the task. Perform PR, Jira, Confluence,
  or pipeline mutations only when the user requested that action.
- Use live CLI help through the owning skill when TWG or PRFlow syntax is
  uncertain.

## Design

- Prefer the simplest design that satisfies current requirements.
- Add an abstraction only when it removes real duplication or represents an
  existing domain boundary.
- Keep functions and modules focused. Avoid flag arguments when separate
  operations make behavior clearer.
- Prefer explicit data flow and immutable values where they improve reasoning.
- Isolate side effects at clear boundaries such as adapters, repositories, or
  command handlers. Make state changes, I/O, retries, and transactions explicit
  and testable.
- Use classes when lifecycle, state, polymorphism, or framework integration makes
  them clearer than functions.
- Remove imports, variables, helpers, or tests made obsolete by this change.
  Mention unrelated dead code instead of deleting it.

## Verification

- Test externally observable behavior and failure modes, not implementation
  trivia.
- For shared APIs, schemas, persistence, concurrency, security, or cross-module
  changes, check affected callers and run broader tests.
- For narrow internal changes, focused tests are sufficient when the blast
  radius is demonstrably small.
- When a check fails, determine whether the change caused it. Do not rewrite
  unrelated code merely to make the suite green.

## Names And Comments

- Use descriptive, consistent, searchable names without type encodings.
- Replace unexplained magic values with domain names or constants.
- Prefer code that explains itself.
- Comment non-obvious intent, constraints, invariants, or consequences. Remove
  restatements and commented-out code introduced by the change.

## Commits

Commit only when the user asks. Keep each requested commit logical,
self-contained, and working.

- Use an imperative, capitalized subject of at most 50 characters with no period.
- The subject should complete: "If applied, this commit will ..."
- Add a body when needed, separated by a blank line and wrapped near 72
  characters.
- Explain what changed and why. The diff already shows how.
- Split unrelated changes instead of forcing them under one subject.
