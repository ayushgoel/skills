---
name: kotlin-code-reviewer
description: >-
  Kotlin-specific extension for review-code. Use alongside the general reviewer
  when a pull request, branch, diff, or source set contains Kotlin or Kotlin
  script files. Adds coroutine, null-safety, Kotlin idiom, library-first,
  architecture, and JVM compatibility checks.
---

# Kotlin Code Reviewer

Apply this skill as an extension to `review-code`, which owns the read-only
default, evidence standard, severity order, and final response structure.

## Select The Diff

For a Bitbucket pull request, use `prflow` to identify the repository, source and
destination branches, diff, comments, checks, and pipeline state. Use
`atlas prflow <command> --help` when current flags are uncertain.

For a local branch review:

1. Inspect the current branch, working tree, and configured remotes.
2. Resolve the remote default branch from `refs/remotes/<remote>/HEAD` or remote
   metadata. Do not assume it is `main`.
3. Compare the merge-base range with three-dot syntax:
   `git diff <default-ref>...<review-head>`.
4. Fetch only when current remote state is required and the user has asked for a
   current branch or PR review. Do not alter the working tree.

If the intended base cannot be established reliably, state the ambiguity instead
of silently selecting a branch.

## Kotlin Review Workflow

1. Identify touched modules, layers, public APIs, serialized models, build files,
   and Java interoperability boundaries.
2. Use `rg` to inspect callers and consumers of changed public symbols.
3. Apply the material checks in
   [`references/review-framework.md`](references/review-framework.md).
4. Use [`references/kotlin-idioms.md`](references/kotlin-idioms.md) for
   null-safety, collections, coroutines, sealed types, value classes,
   immutability, extensions, and delegated properties.
5. Format Kotlin-specific findings using
   [`references/output-format.md`](references/output-format.md).

Prioritize production behavior over idiomatic preference. In particular, check:

- blocking calls, unstructured concurrency, cancellation, dispatcher choice,
  shared mutable state, and lifecycle leaks
- nullability contracts, unchecked assertions, exceptions, and result handling
- API and binary compatibility, serialization changes, Java callers, and
  event-schema compatibility
- resource closure, transaction boundaries, retries, timeouts, and idempotency
- existing stdlib or project-library alternatives before accepting new helpers
- tests for coroutine timing, cancellation, failure, and changed contracts

Follow the general review finding threshold. Every reported issue needs a
concrete correction. Provide a copy-pasteable patch only when it is small and
safe. Explain architecture trade-offs only for material design findings.
