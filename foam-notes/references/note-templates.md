# Note Templates

Optional structures for creating and updating notes in the active Foam workspace. Use only the sections the material needs; do not add empty or repetitive sections to match a template. Resolve placeholders to real filenames and headings before writing links.

---

## Template 1 — New Concept Note

Use for: a self-contained topic with clear definition, mechanics, and trade-offs.  
Examples in repo: `RAG.md`, `Kafka.md`, `Cache.md`

```markdown
# {Title}

**Parent:** [[Parent Note]]

## What is {Title}?

{1–3 sentence definition. State what it is and the problem it solves.}

---

## How it works

{Explain the mechanism. Use prose for reasoning; bullets for steps or properties.}

---

## Key concepts

* **{Term}** — {definition}
* **{Term}** — {definition}

---

## When to use

| Situation | Use {Title} when… |
|---|---|
| {scenario} | {reason} |
| {scenario} | {reason} |

---

## Trade-offs

* **Pros:** {…}
* **Cons / Limitations:** {…}
```

---

## Template 2 — Technology / Tool Note

Use for: a specific product, library, or platform.  
Examples in repo: `Redis.md`, `Apache Cassandra.md`, `Amazon DynamoDB.md`, `Kubernetes.md`

```markdown
# {Tool Name}

**Parent:** [[Parent Note]]

## What is {Tool Name}?

{1–2 sentence description of what the tool is and its primary use case.}

---

## Core features

* **{Feature}** — {description}
* **{Feature}** — {description}

---

## Architecture

{How the tool works internally. Use headings for major components.}

### {Component}

{description}

---

## Common use cases

1. {use case}
2. {use case}

---

## Gotchas / Limitations

* {limitation}
* {limitation}

---

## Comparison

| Feature | {Tool} | {Alternative} |
|---|---|---|
| {aspect} | {…} | {…} |
```

---

## Template 3 — Pattern / Practice Note

Use for: design patterns, engineering practices, principles.  
Examples in repo: `AI Agent Design Patterns.md`, `CQRS.md`, `12 factor app.md`

```markdown
# {Pattern Name}

**Parent:** [[Parent Note]]

## Problem

{What problem does this pattern address?}

---

## Solution

{How the pattern solves it.}

---

## Structure

{Diagram description or bullet breakdown of the pattern's components.}

---

## When to apply

* {condition}
* {condition}

---

## When NOT to apply

* {anti-condition}

---

## Appendix #1: Worked example

{Substantial scenario or code sketch, with its assumptions and sources. Keep each diagram beside the step or explanation it illustrates. Refer to this appendix from the main body. Brief clarifying examples may instead remain inline.}
```

---

## Template 4 — Integrating existing notes

Read the whole note and search related notes before editing. Merge new information into its canonical section, consolidating overlapping explanations. Preserve unique facts, caveats, sources, and useful images. Reorder or rewrite existing prose when necessary to restore topic boundaries.

Use this optional structure for a substantial supporting example:

```markdown
The worked implementation is in [[Existing Note#Appendix #1: Implementation example|Appendix #1: Implementation example]].

## Appendix #1: Implementation example

{Case-specific context, assumptions, implementation, evidence, sources, and images.}
```

Keep conceptual material in the body and foreign subjects in their existing owning notes. Do not split a note or impose a word limit merely because it is long.

---

## Verification checklist (for both new and update workflows)

After writing, verify:

- [ ] Non-root note has exactly one resolved `**Parent:** [[wikilink]]`
- [ ] Every `[[link]]` in the note resolves to a real `.md` file (check with `rg --files -g '*.md'`)
- [ ] Parent reflects the narrowest structural category; no reciprocal parent link was added
- [ ] Inline links are retained or added only where the prose needs a concrete cross-reference
- [ ] `_HOME.md` is updated only when adding a top-level domain
- [ ] No YAML frontmatter was added
- [ ] Whole-note topic coherence reviewed; no duplicated conceptual explanation
- [ ] Substantial examples support the topic and sit in referenced, numbered appendices
- [ ] Moved material retains unique meaning, sources, assumptions, and caveats
- [ ] Each image remains beside its specific explanation; illustrated subsections were not replaced by a detached gallery
- [ ] Image targets resolve and previously referenced images remain referenced, unless an authorized deletion accounts for them
- [ ] Any orphan-asset cleanup stayed within scope; exact duplicates were verified before deletion
- [ ] Heading links still resolve after moves or renames

For image inspection, placement, and authorized cleanup, use the [image rules](foam-conventions.md#image-placement-and-cleanup). Inventory counts complement a contextual review; neither replaces the other.
