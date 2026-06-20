---
name: foam-notes
description: "Use when the user wants to add a note from an article, mailing list, or reading; update existing notes with new knowledge; link notes into a Foam knowledge graph; or capture any learning into the knowledge base. Triggers: 'add a note about X', 'update my notes on Y', 'I just read about Z', 'add this to my foam repo', 'link this note'."
---

# Foam Notes

## Overview

Maintains a Foam knowledge graph **in the active workspace**. Do not ask for a vault path — assume the user has the Foam repository open.

**Default: update existing notes. Create new files only as a last resort.**

Reference docs:
- Style rules and formatting: [`references/foam-conventions.md`](references/foam-conventions.md)
- Note templates: [`references/note-templates.md`](references/note-templates.md)

---

## Workflow

### Step 1 — Find the right home

1. **Confirm scope** — use the workspace root containing `.md` files and hub pages like `_HOME.md`.
2. **Search for candidates** — run `rg` or `grep` for the topic in filenames, `**Related:**` lines, and `##` headings. No good search string? Glob all `*.md` files.
3. **Check for parent topics** — if no exact match, ask: *does this content belong inside an existing note as a `##` section?*

**Decision (stop at first match):**

1. Exact or near-exact filename match → **Update Note Workflow**
2. Sub-topic, variant, or application of an existing note → **Update Note Workflow** (add `##` section)
3. Spans multiple notes as new connective insight → **Update Note Workflow** on each
4. Genuinely standalone with no plausible parent → **New Note Workflow**

> When in doubt between 2/3 and 4, choose update. New files add navigation cost; subsections are free.

---

### New Note Workflow

1. **Name** — Title Case with spaces (`Vector Databases.md`). No date prefix, no underscores.
2. **Draft** using the template in `references/note-templates.md`.
3. **Link** — pick 3–8 genuinely related notes for `**Related:**`.
4. **Back-link** — open each related note and add a reciprocal `[[wikilink]]`.
5. **Check `_HOME.md`** — add a wikilink if the topic belongs to an existing section.
6. **Write** — see `references/foam-conventions.md`. Use only information from the source.

---

### Update Note Workflow

1. **Read** the existing note fully before touching it.
2. **Diff** — identify only information *not already present* (same concept restated = already present).
3. **Merge** — add new subsections or bullets; do **not** rewrite or reorder existing content.
4. **Update `**Related:**`** if the source introduces new connections.
5. **No timestamps** — git history tracks changes.

---

### Link Quality Rules

- Every note needs `**Related:**` with at least one `[[wikilink]]`.
- Glob `*.md` to confirm a file exists before writing any link. Never invent a target.
- Prefer specific notes over broad hubs (`_HOME.md`) unless the topic truly belongs there.

---

## Example

**User:** "Add a note from this thread. Topic is log-structured merge trees."

1. Search for `lsm`, `merge tree`, `log-structured` from workspace root.
2. No exact match, but `Storage Engines.md` covers B-Trees and compaction — LSM trees are a sub-topic.
3. **Update `Storage Engines.md`** with a new `## Log-Structured Merge Trees` section.
4. Only if the content is too large to fit cleanly does it graduate to its own file, linked back from `Storage Engines.md`.

---

## Common Mistakes

| Mistake | Correct behavior |
|---|---|
| Creating a new file for every new term | Check for a parent note first — add a `##` section instead |
| Rewriting existing prose to "improve" it | Merge only; preserve existing wording |
| Inventing wikilink targets | Glob `*.md` to confirm the file exists first |
| Adding YAML frontmatter | The repo has no frontmatter — skip it |
| Adding "Updated:" timestamps | Git history serves this purpose |
| Duplicating content that exists in another note | Link to the other note instead |

---

## Quick Reference

| Situation | Action |
|---|---|
| Topic file exists | Update — add only new info |
| Sub-topic / variant of existing note | Add `##` section inside that note |
| Insight spanning multiple notes | Update each relevant note |
| No filename match, parent concept exists | Add `##` section to parent |
| Genuinely standalone, no parent | New note workflow |
| Source contradicts existing note | Add note under relevant section; don't silently overwrite |
