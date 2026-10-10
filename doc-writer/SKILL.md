---
name: doc-writer
description: >-
  Use when writing, rewriting, or reviewing concise documentation, including
  technical and design docs, PRDs, DACI decisions, runbooks, project updates,
  meeting notes, Confluence pages, and Word or PDF deliverables. Also use when
  documentation needs diagrams or images, tighter structure, source-backed
  claims, preserved links, or less AI-sounding prose.
---

# Doc Writer

Write concise, evidence-based docs with only the sections the reader needs.

## Destination And Evidence

- Infer the destination from the request, page URL, referenced page, open file, or
  active workspace. Ask only when the destination materially changes the result.
- Treat a Confluence URL, page ID, existing page, or explicit publish/update
  request as Confluence context.
- Use the `twg` skill for company evidence from Confluence, Jira, Drive, Slack,
  ownership records, decisions, and related work.
- Read the smallest useful evidence set. Preserve source links during rewrites
  and place citations next to the claims they support.
- Distinguish facts from assumptions, recommendations, and unresolved questions.

## Workflow

1. Identify the audience, decision or task, document type, and destination.
2. Read existing content and source material before changing its structure.
3. Resolve material evidence gaps with local sources or `twg`.
4. Draft the smallest useful section set for the document type.
5. Remove repetition, unsupported claims, empty sections, and generic prose.
6. Verify links, claims, visuals, ownership, decisions, and requested output
   format.
7. Write or publish only under the mutation rules below.

For long documents, put a linked table of contents after the title or
one-sentence summary. Skip it when the document is already easy to scan.

## File Deliverables

Write ordinary Markdown and plain-text documents directly. When the requested
deliverable is a Word document, read
[references/docx-output.md](references/docx-output.md). When it is a PDF, or a
document must be exported to PDF, read
[references/pdf-output.md](references/pdf-output.md).

Treat authoring and final-format validation as separate concerns. Preserve an
existing document's useful styles, links, comments, and revision intent. For a
new document, use restrained formatting appropriate to its destination. Render
the final artifact and inspect representative pages when layout is part of the
request; a successful conversion alone does not establish visual correctness.

## Confluence Reads And Writes

For Confluence reads, use `twg` to resolve the page and fetch its current
content, metadata, and relevant comments or children. A read, review, summary,
or draft request is analysis-only and must not mutate the page.

For Confluence writes:

- When the user explicitly asks to create, update, publish, move, or comment,
  read the current page state first and execute the requested mutation.
- Without an explicit write request, produce a draft and identify the intended
  destination without changing Confluence.
- Preserve existing links, page hierarchy, ownership, and useful formatting.
- Avoid overwriting concurrent edits. Re-read current state when the write follows
  a long analysis or the page may have changed.
- Use `twg help` or `twg help describe` when the current command grammar or write
  contract is uncertain.

Use Confluence tables for comparisons, ownership, timelines, decisions, or
status. Use expand, status, info, note, and warning macros only when they improve
scanning or change reader behavior.

## Document Suites And Review Comments

- Give each page one job. Pillar pages lead with the target state, summarize the
  current state briefly, name the gaps, and link to the work log for execution.
  Do not turn a direction-setting page into an exhaustive inventory.
- Keep action items, owners, targets, and status in one work log. Link to it from
  narrative pages instead of duplicating action tables across the suite.
- If the user marks that work log or another page as manually owned, treat it as
  read-only. Collect exact follow-up items in the handoff for the owner to add.
- Treat an answered review comment as a decision. Update every affected page,
  remove the item from open questions, and add any implementation work to the
  work log.
- Move content to the page where readers need it under pressure. For example,
  operational kill switches belong with incident response, while the service
  overview should link to them.
- Resolve comments only after re-reading the published pages and checking that
  cross-links, terminology, decisions, and work-log actions agree.

## PRD Mode

Use PRD mode for product or feature requirements. Gather known context from the
conversation and linked company evidence before asking questions. Ask only for
missing information that blocks a useful draft, and mark unresolved details as
`TBD` rather than inventing them.

Select from these topics rather than treating them as a fixed template:

- problem, users, proposed outcome, goals, and non-goals
- user journeys, stories, and testable acceptance criteria
- functional and non-functional requirements
- measurable success metrics and guardrail metrics
- dependencies, constraints, rollout, risks, and open questions
- for AI features: model and tool boundaries, grounding data, evaluation,
  safety, privacy, latency, and cost

Requirements must be observable or testable. Replace words such as "fast",
"easy", or "intuitive" with a measurable threshold or an explicit `TBD`.

## Document Topic Budgets

Use these as topic budgets, not rigid headings. Merge related topics.

- High-level design: summary, objective, goals and non-goals, context,
  requirements, architecture, components, trust boundaries, lifecycle,
  alternatives, observability, rollout, rollback, security, risks, open
  questions, references
- Deep technical design: context, architecture, invariants, data design,
  components, interfaces, feature gates, migration, implementation phases,
  constraints, risks, references
- DACI decision: status, impact, driver, approver, recommendation, contributors,
  informed, due date, evidence, decision factors, options, outcome, actions
- Runbook: trigger, severity, impact, diagnostics, mitigation, verification,
  troubleshooting, follow-up
- Project update: summary, status, progress, risks, decisions needed, next steps
- Meeting notes: summary, decisions, actions, open questions

## Technical And Decision Docs

- State the key recommendation, invariant, or system behavior early.
- Explain the path from user action to system response.
- Show component roles, boundaries, ownership, or options in tables when useful.
- Call out deployment, authentication, tenant, policy, data, security, and
  privacy boundaries when relevant.
- Keep raw payloads, exhaustive configuration, and detailed estimates out of the
  main argument unless they determine the decision.
- For consequential decisions, compare options against explicit factors and
  record ownership and next actions.

## Visuals

Add a visual when it replaces a paragraph of explanation, such as architecture,
request or data flow, sequence, lifecycle, rollback, or an option comparison.
Skip decorative images. Use the same terms in labels as in the text.

- Diagrams: write Mermaid. In Markdown, use a fenced `mermaid` block. In
  Confluence, publish through the site's Mermaid macro as described in
  [references/confluence-visuals.md](references/confluence-visuals.md).
- Illustrations and mockups: use the image generation tool only when the user
  asks for images in the request. Keep text out of generated images and put
  labels in the caption.
- Screenshots and charts: use files the user provides, or render charts from
  the data with code. Do not draw data charts with image generation.
- Attach and embed image files in Confluence as described in the same
  reference.

## Style And Links

- Prefer short paragraphs, concrete bullets, and system-specific language.
- Do not add sections just because a template contains them.
- Do not repeat the same idea across the summary, context, and conclusion.
- Avoid em dashes, adjacent hyphens, semicolons, and stock AI phrasing.
- Link descriptive words instead of pasting bare URLs.
- Put a source link next to a sourced claim. Add a final `References` section
  only when a consolidated source list helps the reader.
- Do not end with a generic conclusion. End with the decision, owner, or next
  action when one exists.
