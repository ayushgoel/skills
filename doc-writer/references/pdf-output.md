# PDF Output

Use this mode to create, review, or export a document as PDF. It covers document
delivery, not arbitrary PDF forensics, form automation, signing, redaction, or
complex page manipulation.

## Produce The PDF

- Author in the source format best suited to the requested document, then use a
  deterministic available renderer or exporter.
- Match the intended page size, orientation, margins, fonts, and print behavior.
- Keep text selectable and searchable where possible. Preserve working links,
  bookmarks, document title, language, and accessibility structure when the
  toolchain supports them.
- Embed or substitute fonts deliberately. Do not accept silent font replacement
  when it materially changes pagination or readability.
- Avoid rasterizing an entire document unless the requested source requires it.

## Validate The Artifact

1. Confirm the file opens and its page count is plausible.
2. Extract text from representative pages to catch blank or raster-only output.
3. Render representative pages to images and inspect the title, dense pages,
   tables or diagrams, page boundaries, and final page.
4. Check for clipped content, broken links, missing glyphs, bad page breaks,
   unreadable scaling, unexpected blank pages, and stale headers or footers.
5. For a revised PDF, compare the intended content and layout changes against
   the previous artifact.

Report the output path, exporter used, pages inspected, and any fidelity or
accessibility limitation. A converter's zero exit status is not sufficient
validation when appearance matters.
