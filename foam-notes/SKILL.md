---
name: foam-notes
description: "Helps maintain and grow a Foam knowledge graph in the workspace where the Foam repository is open. Use this skill when the user wants to add a new note from an article, mailing list, or reading; update an existing note with new information from a source; link a note correctly into the knowledge graph; check whether a topic already exists before creating a new file; or keep language and formatting consistent across all notes. Triggers on requests like 'add a note about X', 'update my notes on Y', 'I just read about Z', 'add this to my foam repo', 'link this note to the graph', or any request to capture reading/learning into the knowledge base."
---

# Foam Notes

## Overview

This skill maintains a Foam knowledge graph **in the active Cursor workspace**. Treat the **workspace root** (or, if multiple roots are open, the root folder that contains the Foam notes) as the only scope for Glob, read, and write. Do not ask for a vault path; assume the user already opened the Foam repository.

Notes capture knowledge from mailing lists, articles, and readings. The two core workflows are:

1. **New topic** — create a well-linked note
2. **Existing topic** — merge only new information, preserving what is already there

For style rules and formatting details, read [`references/foam-conventions.md`](references/foam-conventions.md).  
For copy-paste note templates, read [`references/note-templates.md`](references/note-templates.md).

The reference docs say “the workspace”; that means that root for the current task.

---

## Workflow

### Step 1 — Determine new vs. existing

Before writing anything:

1. **Confirm scope** — Use the workspace root that holds the Foam graph. If unclear among multiple workspace folders, prefer the one that already contains note `.md` files and hub pages such as `_HOME.md`.
2. **Find candidate notes**
   - If the user gave a **usable topic string** (title, keywords, or note name), narrow first: search from that root with `rg` or `grep` for that string in filenames, `**Related:**` lines, and markdown headings (`#` / `##`), then open plausible files.
   - If there is no good search string, or search results are inconclusive, list every `.md` file under that root (Glob `*.md` from the workspace root downward).
3. Check for an exact or near-exact filename match for the topic.
4. If still unclear, scan the `**Related:**` lines and section headings of candidate files.

**Decision:**

- Match found → follow **Update Note Workflow** below.
- No match → follow **New Note Workflow** below.

---

### New Note Workflow

1. **Name the file** — Title Case with spaces, matching what a reader would search for (e.g. `Vector Databases.md`). No date prefix, no underscores.
2. **Draft the note** using the template in `references/note-templates.md`.
3. **Find related notes** — List all `.md` files under the workspace root (reuse Step 1’s listing if it already covered the tree), then pick 3–8 that are genuinely related. Add them to the `**Related:**` line.
4. **Back-link** — Open each related note and add a wikilink back to the new note where it naturally fits (a `**Related:**` line, an inline mention, or a new bullet).
5. **Check `_HOME.md`** — If the topic belongs to an existing section (Technical Knowledge, Specific Technologies, Career & Leadership, etc.), add a wikilink there.
6. **Write the content** — Follow the style guide in `references/foam-conventions.md`. Use only information from the source; do not hallucinate facts.

---

### Update Note Workflow

1. **Read the existing note** fully before touching it.
2. **Diff against the source** — identify only information that is *not already present* (same concept restated differently counts as already present).
3. **Merge new information** in-place:
   - Add new subsections under the appropriate existing heading, or append a new `##` heading at the end.
   - Do **not** rewrite or reorder existing content unless it is directly contradicted by the new source.
   - Do **not** change wording of existing sentences for stylistic preference.
4. **Update the `**Related:**` line** if the source introduces connections to notes not already listed.
5. **Do not** add a "Updated: …" timestamp or change-log — the git history serves that purpose.

---

### Link Quality Rules

- Every note must have a `**Related:**` line with at least one `[[wikilink]]`.
- Links must resolve to real filenames (Glob from the workspace root). Never invent a link target.
- If a natural parent or sibling concept does not have a note yet, note it to the user but do not block the current note.
- Prefer linking to specific notes over broad hub notes (`General.md`, `_HOME.md`) unless the topic truly belongs there.

---

### Language and Consistency Rules

- Read `references/foam-conventions.md` before writing any content.
- Match the register and density of neighboring notes on similar topics. (RAG.md, AI Agents.md, and Kafka.md are good style anchors — dense, precise, minimal padding.)
- Bold key terms on first use. Use `**term**` not _term_.
- Bullet lists for enumerable facts; prose paragraphs for conceptual explanations.
- No motivational filler ("In today's world…", "This is important because…").
- No YAML frontmatter — the repo does not use it.
- No trailing "References" section unless the source URL is genuinely useful to revisit.

---

## Example

**User:** “Add a note from this mailing-list thread: [paste]. Topic is log-structured merge trees.”

**Agent:**

1. Uses the open Foam workspace as scope.
2. Runs a targeted search for `lsm`, `merge tree`, `log-structured`, and similar from the workspace root; if nothing matches, lists all `.md` files.
3. Finds no existing `Log-Structured Merge Trees.md` (or equivalent); chooses **New Note Workflow**.
4. Reads `references/note-templates.md` and `references/foam-conventions.md`.
5. Creates `Log-Structured Merge Trees.md` with a full `**Related:**` line, sections from the template, and facts only from the paste.
6. Opens 3–6 related notes (e.g. storage engines, B-trees), adds `[[Log-Structured Merge Trees]]` to their `**Related:**` or body where it fits, and adds the new note to `_HOME.md` if a section applies.

---

## Quick Reference

| Situation | Action |
|---|---|
| Topic file exists | Update workflow — add only new info |
| Topic file missing | New note workflow — create + link |
| Partial match (sub-topic of existing) | Add a new `##` section inside the existing note |
| Huge new topic with distinct subtopics | Create a new file + link from the parent note |
| Source contradicts existing note | Add a note under the relevant section, do not silently overwrite |
