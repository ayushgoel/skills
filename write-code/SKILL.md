---
name: write-code
description: >-
  Guides code implementation following clean code principles, functional style,
  and disciplined commit practices. Use when implementing features, writing new
  code, making code changes, or when asked to "implement", "write code",
  "build this", "add feature", or any explicit coding task.
---

# Write Code

## Commits

Make one logical change per commit. A commit should be a complete, self-contained unit that leaves the codebase in a working state.

**Subject line rules** (from [cbea.ms/git-commit](https://cbea.ms/git-commit/)):
- Imperative mood: "Add feature" not "Added feature" or "Adding feature"
- ≤50 characters, capitalized, no trailing period
- Test: "If applied, this commit will ___" must complete naturally

**Body** (when the subject isn't enough):
- Separate from subject with a blank line
- Wrap at 72 characters
- Explain _what_ and _why_, not _how_ — the diff shows how

**Scope discipline:**
- Commit early and often; don't batch unrelated changes
- If you can't write a concise subject, the commit is too large — split it

## Design

- **KISS**: simpler is always better; reduce complexity as much as possible
- **Boy scout rule**: leave code cleaner than you found it
- Use the simplest abstraction that solves the problem; avoid design pattern overhead
- Avoid premature generalization and needless repetition
- Small functions that do one thing; few arguments; no side effects; no flag arguments

## Style: functional over OOP

- Prefer pure functions and functional composition over classes
- Favor immutability and explicit data flow over mutable shared state
- Reach for a class only when encapsulating long-lived state with behavior is genuinely clearer

## Names

- Descriptive, unambiguous, pronounceable, and searchable
- No type prefixes, no encodings, no abbreviations that need decoding
- Replace magic numbers with named constants
- Be consistent: if you name something a certain way, name all similar things the same way

## Comments

Explain yourself in code first. A comment is a last resort.

- **Write**: non-obvious intent, tricky constraints, warnings of consequences
- **Never write**: restatements of what the code does, closing-brace labels, noise
- **Delete**: commented-out code — version control remembers it
