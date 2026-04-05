# Note Templates

Copy-paste templates for creating and updating notes in the open Foam workspace (paths are relative to the workspace root; see parent `SKILL.md`, **Overview**).

---

## Template 1 — New Concept Note

Use for: a self-contained topic with clear definition, mechanics, and trade-offs.  
Examples in repo: `RAG.md`, `Kafka.md`, `Cache.md`

```markdown
# {Title}

**Related:** [[Link A]] | [[Link B]] | [[Link C]]

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

---

## Related patterns

{Optional. Prose or bullets linking to complementary or competing approaches.}
```

---

## Template 2 — Technology / Tool Note

Use for: a specific product, library, or platform.  
Examples in repo: `Redis.md`, `Apache Cassandra.md`, `Amazon DynamoDB.md`, `Kubernetes.md`

```markdown
# {Tool Name}

**Related:** [[Link A]] | [[Link B]] | [[Link C]]

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

**Related:** [[Link A]] | [[Link B]] | [[Link C]]

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

## Examples

{Concrete scenario or code sketch illustrating the pattern.}
```

---

## Template 4 — Update Patch (not a file template)

When **updating** an existing note, only write the new fragment to insert — never rewrite the whole note. Use this shape:

```markdown
## {New Section Heading}

{New content derived from the source. Same style as the surrounding note.}
```

Or, for a new bullet inside an existing section:

```markdown
* **{New Term}** — {definition from source}
```

Or, for an updated **Related** line (append only):

```markdown
**Related:** [[Existing A]] | [[Existing B]] | [[New Link]]
```

---

## Linking Checklist (for both new and update workflows)

After writing, verify:

- [ ] `**Related:**` line has at least one resolved `[[wikilink]]`
- [ ] Every `[[link]]` in the note resolves to a real `.md` file (check with Glob)
- [ ] At least one existing note has been updated to link back to this note
- [ ] If the topic is in a hub area (`_HOME.md` section), a wikilink was added there
- [ ] No YAML frontmatter was added
- [ ] No duplicate content from an existing note
