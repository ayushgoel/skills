---
name: review-code
description: >-
  Reviews code for design alignment, clean code quality, functional style, and
  comment discipline, following the same principles used when writing code.
  Use when reviewing pull requests, examining code changes, or when asked to
  "review", "code review", "look at this PR", "give feedback on", or audit any
  source file or diff.
---

# Review Code

## Order of review

1. **Design alignment** — does the new code fit the shape of the codebase?
2. **Clean code quality** — are functions, names, and structure sound?
3. **Style** — is functional style used where it should be?
4. **Comments** — are comments earning their place?

---

## 1. Design alignment (start here)

Before reading individual lines, check that the change fits the surrounding codebase:

- Naming conventions match existing vocabulary
- Layering and module boundaries are respected
- Data flow patterns are consistent with neighboring components
- No new abstractions that duplicate existing ones

If the design doesn't fit, say so at the top — line-level feedback is secondary.

## 2. Clean code quality

Flag any of these code smells:
- **Rigidity**: a small change cascades into many other changes
- **Fragility**: unrelated things break together
- **Needless complexity**: abstractions or indirection with no payoff
- **Opacity**: hard to understand without running it mentally

Functions must be:
- Small and focused on one thing
- Free of side effects
- Free of flag arguments (split into separate functions instead)
- Named descriptively — the name should make the body readable

Names must be:
- Descriptive, unambiguous, and consistent with the rest of the codebase
- Not encoded or prefixed with type information

## 3. Functional style

- Flag classes used as bags of static methods — prefer module-level functions
- Flag mutable shared state and hidden side effects
- Flag inheritance used where composition or plain functions would be clearer
- Flag over-engineered patterns: factory hierarchies, unnecessary generics, premature abstraction

Prefer: pure functions, explicit data flow, immutability, simple composition.

## 4. Comments

- **Flag**: comments that restate what the code already says
- **Flag**: commented-out code (it belongs in version history, not the file)
- **Flag**: closing-brace labels and noise comments
- **Commend**: comments that explain non-obvious intent, tricky constraints, or warn of consequences

---

## Feedback format

Group feedback by severity:

- **Must fix**: correctness issues, broken design boundaries, hidden side effects
- **Should fix**: code smells, naming, style violations
- **Consider**: optional improvements, alternative approaches worth discussing

Each item: state the problem, explain why it matters, suggest a concrete fix.
