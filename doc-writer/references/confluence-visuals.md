# Confluence Visuals

Use this reference to publish diagrams and images to Confluence with `twg`.
Author the page body with `--format html` and load
`twg confluence content body-formats html` before writing.

## Mermaid Diagrams

Confluence renders a Mermaid code block as plain text. Publish diagrams through
a Mermaid app macro installed on the site.

### Find The Macro

1. Reuse a macro on a page the user points to. Otherwise find one with CQL, for
   example `macro = "mermaid-diagram" and type = page`. A site can have more
   than one Mermaid app, so prefer the one the user already uses.
2. Fetch that page with `--format html --body-only` and copy one macro block:
   its `data-type`, `data-extension-key`, `data-extension-type`, and
   `data-parameters`, plus the element that holds the Mermaid source.
3. Keep discovered keys in the task's working directory. Do not store
   site-specific keys, account IDs, or cloud IDs in this skill.

### Forge "Mermaid diagram" Pattern

A common app renders a code block chosen by position. Its block looks like this:

```html
<div data-type="extension"
     data-extension-key="<APP_ID>/<ENV_ID>/static/mermaid-diagram"
     data-extension-type="com.atlassian.ecosystem"
     data-layout="default"
     data-parameters='{"layout":"extension","guestParams":{"index":<N>},"forgeEnvironment":"PRODUCTION","extensionId":"ari:cloud:ecosystem::extension/<APP_ID>/<ENV_ID>/static/mermaid-diagram","extensionTitle":"Mermaid diagram"}'>Mermaid diagram</div>
<details>
  <summary>Diagram source</summary>
  <pre><code>flowchart LR
    A[Client] --&gt; B[Service]
    B --&gt; C[(Store)]</code></pre>
</details>
```

- Keep the source accessible without distracting from the rendered diagram.
  An expand directly after the macro is useful; choose a descriptive title
  suited to the page, such as `Diagram source`.
- `guestParams.index` is the zero-based position of the source among all code
  blocks on the page, including non-Mermaid ones. Put the source right after the
  macro, so the index equals the number of code blocks earlier on the page.
- Recompute every index after adding, removing, or reordering code blocks above
  a diagram. A stale index renders the wrong block.
- Drop page-specific context copied from the source page, such as
  `embeddedMacroContext`, and omit `macroId`. Use a new `localId` or omit it.
- Escape `<`, `>`, and `&` in the Mermaid source inside `<code>`.

For a different app, follow the parameter shape of the copied block instead.

## Images And Files

1. Create the page or draft first. Attachments belong to a content item.
2. Upload with `twg confluence content attachments upload --id <content-id> --file <path> -y`.
3. Read the attachment's `fileId` from the upload output or from
   `twg confluence content attachments list --id <content-id>`.
4. Embed it with the collection `contentId-<content-id>`:

```html
<figure data-type="media-single" data-layout="center" data-width="80" data-width-type="percentage">
  <div data-type="media" data-media-type="file" data-id="<FILE_ID>" data-collection="contentId-<content-id>" data-alt="<short description>"></div>
  <figcaption>What the reader should notice</figcaption>
</figure>
```

Choose image width for legibility in the page layout. Dense diagrams may need
more width than small screenshots; preserve useful existing sizing and check
that labels remain readable.

## Verify

1. Re-fetch the page with `--format html --body-only`.
2. Confirm each diagram macro kept its extension key, each index points at its
   own source block, and each image has a media node with the expected `fileId`.
3. The API cannot show rendered output. The first time a macro pattern is used
   on a site, ask the user to confirm the diagram renders.
