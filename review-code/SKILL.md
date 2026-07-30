---
name: review-code
description: >-
  Use for code, branch, diff, and pull-request reviews in any language. Performs
  analysis-only review by default, prioritizes correctness and production risk,
  adds Kotlin-specific analysis through kotlin-code-reviewer, and uses PRFlow or
  TWG when remote PR state or company context is needed.
---

# Review Code

Review for actionable defects and material engineering risk. Default to
analysis-only.

## Mutation Boundary

- Do not edit files, push commits, post comments, approve, merge, or update a PR
  unless the user explicitly requests that action.
- A request to "review", "audit", "inspect", or "give feedback" is read-only.
- When fixes are requested, switch to `write-code` after completing enough
  analysis to define the change.

## Gather The Right Evidence

1. Read repository guidance and identify the exact diff or files in scope.
2. Inspect nearby code, tests, callers, contracts, and configuration needed to
   validate suspected findings.
3. Use `prflow` for direct Bitbucket PR metadata, diff context, comments, checks,
   pipelines, and failed logs.
4. Use `twg` for linked Jira requirements, Confluence designs, historical
   decisions, ownership, and cross-repository context.
5. For Kotlin or Kotlin-script changes, apply `kotlin-code-reviewer` as a
   language-specific extension to this review.

Use live CLI help through the owning skill when command syntax is uncertain.
Remote reads are allowed when needed for the review. Remote mutations still
require an explicit user request.

## Review Priorities

Review in this order:

1. Correctness and behavioral regressions
2. Security, authorization, privacy, and data integrity
3. Concurrency, resource lifecycle, failure handling, and reliability
4. Public contracts, compatibility, architecture, and cross-module impact
5. Missing or misleading tests for changed behavior
6. Performance issues supported by a realistic execution path
7. Maintainability and style only when they create material risk

Check whether each issue is introduced by the reviewed change. Verify the
execution path and surrounding code before reporting it.

## Finding Threshold

Report an issue when all of these are true:

- The changed code introduces or exposes it.
- It has a concrete impact.
- The evidence is visible in the diff or supporting code.
- A reasonable correction exists.

Avoid speculative edge cases, generic best practices, unrelated legacy issues,
and preferences already enforced by repository tooling. Match existing style
unless that style causes a material defect.

Keep changes surgical when suggesting corrections. Do not turn a local defect
into an unrelated redesign. Prefer existing utilities and dependencies over new
abstractions.

## Feedback Format

Lead with findings ordered by severity:

- **Blocker**: unsafe to merge or deploy
- **High**: likely correctness, security, data, or reliability failure
- **Medium**: real defect with narrower impact or conditions
- **Low**: material maintainability or test weakness

Each finding must include:

- severity and a precise title
- file and line reference
- concrete impact and triggering conditions
- evidence or reasoning that establishes the issue
- the smallest credible correction

Use code snippets only when they make the correction clearer. After findings,
list open questions or assumptions, then give a short summary. When no findings
meet the threshold, say so clearly and note any test gaps or residual risk.
