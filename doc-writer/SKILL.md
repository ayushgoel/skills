---
name: doc-writer
description: >-
  Use when writing, rewriting, or reviewing concise documentation, including
  technical docs, high-level design docs, DACI decision docs, runbooks, project
  updates, Confluence pages, and docs that need tighter structure, fewer
  sections, a table of contents, cleaner links, useful image prompts, or less
  AI-sounding prose.
---

# Doc Writer

Write concise docs with a clear table of contents, only the sections the doc type needs, and no repeated content.

## First Question

If the target format is not explicit, ask: "Is this a Confluence page?"

If yes, use Confluence-friendly formatting and macros judiciously. Prefer macros only when they improve scanning:
- `table` for comparisons, decision matrices, ownership, timelines, or status grids
- `expand` for details most readers can skip
- `status` for state, risk, priority, or decision markers
- `info`, `note`, or `warning` only when the callout changes reader behavior

## Workflow

1. Identify the doc type before drafting.
2. Put a linked table of contents directly after the title or one-sentence summary.
3. Use the smallest useful section set for the doc type.
4. Merge duplicate ideas instead of restating them in later sections.
5. Add image prompts where a visual would shorten or clarify the doc.
6. Make every paragraph earn its place. Prefer short paragraphs and concrete bullets.
7. Put references last.

## Doc Topics

Use these as topic budgets, not rigid headings. Merge related topics to keep the doc small.

- High-level design: objective, goals and non-goals, context, requirements, design, alternatives, performance, observability, rollout, rollback strategy, security, privacy, risks, work log, open questions, references
- DACI decision doc: decision, status, impact, driver, approver, contributors, informed, due date, relevant data, background, options, decision factors, recommendation, outcome, action items, references
- How-to or runbook: summary, alert or trigger, severity, impact, diagnostics, mitigation, verification, troubleshooting, follow-up, references
- ADR or design decision: context, decision, options, trade-offs, consequences, rollout, rollback, references
- Technical explainer: summary, concepts, architecture or flow, dependencies, edge cases, failure modes, references
- Project update: summary, status, progress, risks, decisions needed, next steps, references
- Proposal: summary, problem, proposal, impact, risks, open questions, references
- Meeting notes: summary, decisions, actions, open questions, references

## DACI Guidance

Use DACI for important decisions, especially when ownership or approval is unclear. Do not bury DACI inside a general design doc; create a separate DACI when the decision needs explicit accountability.

Prefer a compact decision header with status, impact, driver, approver, contributors, informed, due date, and resources. Use a table for the header in Confluence.

## Image Prompts

Bias toward adding image prompts when a diagram would reduce text. Do not generate the image unless explicitly asked.

Use this pattern:
```markdown
Image prompt: Create a clean architecture diagram showing [components], [data flow], [external dependencies], and [failure or rollback path]. Use labels that match the section text.
```

Good candidates:
- Architecture, component, data flow, and sequence diagrams
- Decision trees for DACI options
- Rollout, rollback, and incident flow diagrams
- Before and after diagrams for migrations or refactors

## Style Rules

- Do not use em dashes, two adjacent hyphens, or semicolons in prose. Rewrite with commas, periods, or separate sentences so it sounds human.
- Avoid stock AI phrasing such as "delve", "comprehensive", "robust", "seamless", "game-changing", "leverage", and "unlock".
- Do not add a section just because a template usually has one.
- Do not repeat the same idea in summary, context, and conclusion.
- Do not end with a generic conclusion unless it adds a concrete decision or next step.
- Use direct wording: "Do X because Y" instead of throat clearing.

## Links

Do not paste bare URLs into the body. Link relevant words inside sentences.

Good:
```markdown
Follow the [deployment runbook](https://example.com/runbook) before promoting to production.
```

Bad:
```markdown
Deployment runbook: <bare URL>
```

## References

End with `## References` when any source document was used.

Only include document links in this section. Do not explain or summarize them there.
