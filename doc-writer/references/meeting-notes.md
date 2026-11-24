# Meeting Notes

Write the outcomes a reader needs to act on. Select important decisions and
concrete action items, rather than retelling the meeting. Use the
[reference examples](meeting-notes-examples.md) to calibrate selection and style.

## Select What Matters

- Keep settled decisions that change scope, behavior, priorities, ownership, or
  delivery. Preserve conditions and exceptions that affect their meaning.
- Keep agreed actions with a concrete deliverable or next step. Include the
  owner and deadline only when established by the source. An unassigned but
  agreed action stays unassigned; a suggestion is not an action.
- Include a blocker or unresolved question only when it explains a selected
  decision or agreed action. Express it through that outcome where possible.
- Drop debate, rejected or unselected ideas, speaker-by-speaker accounts,
  repeated explanations, routine status, demos, and social or logistical chatter.
  Retain a brief reason only when it is needed to understand a decision or act.
- If no important decision or agreed action remains, report that briefly in-session.
  Do not pad the notes, create tasks from speculation, or publish a recap merely
  because a recording exists.

## Write Direct Points

- Use concise bullets with one distinct outcome per point. Lead with what was
  decided or what someone will do. Replace "the team discussed and agreed that"
  with the actual decision; replace "follow up" with the specific next step.
- Group related outcomes under a short topic label when useful. Use decision
  and action labels when they help scanning; omit empty categories.
- Do not repeat the same item in a summary, topic breakdown, and action list.
  Actions belong in the task list; decisions belong in the outcome bullets.
- Keep verification notes, discarded discussion, and source timestamps in the
  working evidence unless the reader needs a specific source link. Concision
  must not remove a decision's material condition or uncertainty.

## Confluence Meeting Log

For Confluence meeting-notes documents, use the requested three-column log:

| Date | Notes | Attendees + Links |
| --- | --- | --- |
| Meeting date | Short topic label, important decision bullets, and action items | Verified participants and relevant recording/document links |

Add the newest meeting first, following the existing page's ordering if it
differs. Identify the occurrence by date and source recording, so a second
recording on the same date does not overwrite another meeting. Preserve useful
existing rows and their table layout; do not repeat old notes in each new row.

Use confirmed participants when available; invitees are not confirmed attendees.
Keep links and participant context in the last column rather than interrupting
every bullet. Do not rewrite earlier entries to make later decisions look as
though they were made earlier.

## Native Confluence Elements

- Before a Confluence write, read `twg confluence content body-formats html` and
  follow the current HTML contract. Use native elements, not storage XML,
  Markdown checkbox text, or Unicode checkbox characters pasted into HTML.
- Render real actions as `<ul data-type="task-list">` with
  `<li data-type="task-item"><input type="checkbox"> ...</li>` entries.
  New open actions are unchecked. Preserve existing task identity and state on
  edits; do not mark completion without evidence or recreate old tasks.
- Render meeting dates and stated due dates with
  `<time datetime="YYYY-MM-DD">...</time>`. Resolve relative deadlines against
  the meeting date and timezone only when unambiguous. Leave missing deadlines
  absent and durations as text.
- Use native mentions only with verified Atlassian account IDs. A Slack user ID
  is not an Atlassian ID. Otherwise keep the owner's plain name. Never copy
  example IDs, source-local node IDs, or fabricated identities into a real page.
- After an authorized write, read the page back and verify task-list/task-item
  elements, completion state, date values, mentions, links, and preserved rows.
  A readable text rendering alone does not verify native task or date elements.

For Slack, carry over the same selected outcomes as short bullets and actions,
using Slack's own mentions and links. Do not paste Confluence HTML into Slack or
add a longer discussion recap in a thread. Formatting a draft does not authorize
publishing a page, sending a message, or creating work items elsewhere.
