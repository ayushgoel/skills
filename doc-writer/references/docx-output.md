# Word Document Output

Use this mode when creating or editing `.docx` files, including requests that
depend on comments, tracked revisions, stable pagination, or an existing Word
template.

## Preserve The Source

- Inspect the existing document before editing. Preserve useful styles,
  numbering, headers, footers, section breaks, links, captions, tables, comments,
  and revision intent unless the request changes them.
- Work from a copy when the user did not explicitly ask to replace the source.
- Do not flatten comments or tracked changes when review history is part of the
  deliverable.
- Use a document-aware library or editor. Avoid manipulating the OOXML archive
  directly unless the requested feature cannot be expressed safely otherwise.

## Create Or Edit

- Prefer semantic paragraph, heading, list, table, caption, and character styles
  over repeated manual formatting.
- Keep margins, page size, fonts, spacing, and heading hierarchy consistent.
- Make tables readable at the target page size; avoid tiny text as a substitute
  for restructuring content.
- Keep links functional and descriptive. Preserve accessibility metadata such
  as document language, heading structure, and image alt text when supported.
- For redlines, make the requested edits visible through tracked changes or
  comments rather than simulating them with colored text.

## Validate The Artifact

1. Reopen or parse the produced `.docx` to confirm it is structurally valid.
2. Render it with an available Word-compatible engine when layout matters.
3. Inspect the title, representative body pages, tables, page breaks, headers,
   footers, and the final page for clipping, overflow, orphaned headings, and
   broken numbering.
4. Confirm comments, revisions, links, and requested metadata survived.

Report the output path, what was visually inspected, and any rendering gap. Do
not claim Microsoft Word fidelity when validation used a different engine.
