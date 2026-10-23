---
name: git-workflow
description: >-
  Prepare commits, branches, and stacked pull requests. Use when planning or
  carrying out Git change delivery, rather than for code edits or read-only
  Git inspection.
---

# Git Workflow

Deliver the smallest coherent, reviewable changes while preserving existing
work and commit history. Explicit user instructions take precedence over this
skill's guidelines.

## Authority And Tools

- A plan or review request is read-only. Commit, push, create or retarget pull
  requests, or merge only when requested. Authorization already given carries
  forward without repeated confirmation.
- Use local Git for branch and commit operations. Use `write-code` for
  implementation and, when available, `prflow` for Bitbucket operations. This
  skill owns delivery structure, not provider-specific commands.

## Change Boundaries

- Prefer one logical, independently reviewable outcome per commit and pull
  request. Keep the files and resources needed for that outcome together.
- Separate independent outcomes. Use a stack when later changes depend on
  earlier ones, and independent branches when they do not.
- Choose boundaries by behavior and dependencies. A file, chart, or resource
  count alone does not determine how many pull requests are needed.

## Branches And Stacks

- Inspect the working tree, branch, upstream, and relevant remote or PR metadata
  to establish the intended base and destination. Do not assume the default
  branch is `main`, or guess a target that remains ambiguous.
- For each branch in a stack, state its base, PR destination, dependencies, and
  merge order. A dependent PR targets its predecessor until that predecessor
  merges; include any needed retargeting in the delivery plan.
- Inspect each branch's diff against its intended base so parent changes are
  not attributed to the child PR.
- Add follow-up commits and use additive merges to update branches. Do not
  amend, rebase, squash, otherwise rewrite commits, or force-push.
- On a push rejection, inspect remote state and preserve both histories. Ask
  when reconciliation needs an unresolved decision or additional authority.

## Commits

- Preserve unrelated work. Stage only the requested paths or hunks and inspect
  the staged diff before committing.
- Follow repository commit conventions. Otherwise, use an imperative,
  capitalized subject of at most 50 characters with no trailing period.
- Add a body when needed, separated by a blank line and wrapped near 72
  characters. Explain the meaningful change and its reason.
- Before publishing, inspect the outgoing diff for credentials, personal or
  company information, private URLs, and machine-specific paths.

## Verification And Handoff

- Use the affected project's verification requirements and relevant skill.
  Reuse checks already completed for the current change; rerun or broaden them
  when subsequent changes or unresolved risk justify it.
- After an authorized mutation, verify the resulting commit, branch, or remote
  PR state. Do not infer publication or merge success from a local command's
  intent.
- Report created commits and PRs, remaining work, and verification gaps. For
  stacks, include branch destinations, dependencies, and merge order.
