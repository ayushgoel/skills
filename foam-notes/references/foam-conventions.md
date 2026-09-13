# Foam Repo Conventions

Style guide for the open Foam workspace (scope is the workspace root; see parent `SKILL.md`, **Overview**). Notes use a sparse parent tree for structure and selective inline links for reader navigation.

## Table of Contents

1. [File naming](#1-file-naming)
2. [Note structure](#2-note-structure)
3. [Wikilinks](#3-wikilinks)
4. [Writing style](#4-writing-style)
5. [Formatting rules](#5-formatting-rules)
6. [What not to do](#6-what-not-to-do)

---

## 1. File naming

- **Title Case with spaces**: `Vector Databases.md`, `Context Engineering.md`
- Parentheses are fine for disambiguation: `Artificial Intelligence (AI).md`
- Hyphens in compound proper nouns only: `API-Security.md`, `12 factor app.md`
- No date prefixes, no underscores, no numeric IDs
- The wikilink `[[Vector Databases]]` must exactly match the filename minus `.md`

---

## 2. Note structure

Every note follows this skeleton (see `note-templates.md` for full copy-paste versions):

```
# Title

**Parent:** [[Parent Note]]

## Section Heading

Content…

---

## Another Section

Content…
```

Rules:
- H1 title = filename without `.md`
- Every non-root note has exactly one `**Parent:**` line, always the **second non-blank line** (right after the title)
- Top-level domain notes use `**Parent:** [[_HOME]]`; `_HOME.md` has no parent
- `---` horizontal rules separate major sections; do not use them inside sections
- No YAML frontmatter block (the repo deliberately does not use it)
- No "Last updated" line — git history tracks this

---

## 3. Wikilinks

**Syntax:** `[[Exact Filename Without Extension]]`

Examples from the repo:
- `[[Artificial Intelligence (AI)]]` → links to `Artificial Intelligence (AI).md`
- `[[AI Agent Design Patterns]]` → links to `AI Agent Design Patterns.md`
- `[[system design]]` → links to `system design.md` (lowercase OK if filename is lowercase)

**Parent line format:**
```
**Parent:** [[Parent Note]]
```
Exactly one resolved wikilink, no pipe, no period.

**Inline links** within prose or bullets:
```
See [[Kafka]] for the streaming model.
* Uses [[Consistent Hashing]] to distribute load.
```

**Structural links:** Each non-root note has one parent. Do not add a reciprocal parent link; the child-to-parent direction is enough to keep the structural graph tree-shaped.

**Inline links:** Preserve or add ordinary inline links when the prose makes a concrete dependency, comparison, or invitation to a deeper explanation. Do not add broad “see also” lists merely because topics are related.

**Never invent a link target.** Glob `*.md` from the workspace root to confirm a target file exists before linking.

---

## 4. Writing style

**Register:** Dense and precise. Match the style of `RAG.md`, `Kafka.md`, `AI Agents.md`, and `Context Engineering.md`. These notes are reference material, not tutorials.

**Key term bolding:** Bold a term **on first use only** in each note. `**Retrieval-Augmented Generation**` not repeated-bold throughout.

**No filler sentences:**
- Avoid: "This is a very important concept in modern software engineering."
- Prefer: state the concept, then its significance directly.

**Explanations vs. lists:**
- Use bullet lists for properties, options, steps, comparisons.
- Use prose paragraphs for mechanisms, trade-offs, or anything that needs connective reasoning.
- Do not force everything into bullets.

**Analogies:** Use them when they genuinely clarify a concept (e.g., the RAG "open-book exam" analogy). Skip them when the concept is already concrete.

**Consistency with existing notes:** If the repo already has a term for a concept (e.g., "vector store" vs. "vector database"), match the existing term.

---

## 5. Formatting rules

| Element | Convention |
|---|---|
| Bold | `**term**` — key concept, first use |
| Code / identifiers | `` `inline code` `` for commands, config keys, code terms |
| Tables | Markdown GFM tables with header row |
| Images | `![alt text](image-NNN.png)` — only if the image file exists locally |
| Horizontal rule | `---` between major sections only |
| Numbered lists | For ordered steps or ranked items |
| Bullet lists | For unordered collections |
| Heading levels | `##` for major sections, `###` for sub-sections; never skip levels |

---

## 6. What not to do

- **No YAML frontmatter** — the repo style has no `---` frontmatter blocks
- **No "References" section** unless the URL is genuinely useful to revisit
- **No "Updated:" timestamps** — use git
- **No empty wikilinks** `[[]]`
- **No orphan notes** — every non-root note must have one resolved `Parent` link
- **No multi-note Related lists or reciprocal parent links** — they turn hierarchy into a dense graph
- **No duplicate content** — if information already exists in another note, link to it rather than copy it
- **No hallucinated facts** — content must come from the source material provided
- **No motivational padding** — "In today's rapidly evolving landscape…" is banned
