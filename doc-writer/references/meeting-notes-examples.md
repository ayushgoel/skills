# Meeting Notes Examples

These examples are synthetic. They show selection and rendering, not a required
number of bullets or live owners, links, or deadlines.

## From Conversation To Outcomes

Source, import review on 24 November 2026. Confirmed participants: Maya and Lee.

> The call starts with audio trouble and a demo of yesterday's screen. Several
> people debate a queue and two storage options, but select none. The team agrees
> to retry failed rows only; successful rows must not be reprocessed. Retries
> will be enabled only after the load test passes. Maya commits to updating the
> retry specification by Friday, 27 November. Lee will measure upload latency;
> no deadline is given. Someone suggests a future dashboard, without agreement.

Useful notes:

- Retry failed rows only; keep successful rows untouched.
- Enable retries after the load test passes.
- [ ] Maya: update the retry specification by 27 November.
- [ ] Lee: measure upload latency.

The audio trouble, demo, storage debate, and dashboard suggestion add no decided
outcome or agreed action. They do not belong in a longer appendix or Slack thread.

## Confluence Rendering Of The Same Entry

This is an HTML body fragment for the shared date/notes/links table. Owners stay
plain text because no verified account IDs were supplied. Replace them with
native mentions only after identity resolution. No recording URL was supplied,
so the example does not invent one. Follow the live body-format contract before
using this pattern in a real write.

```html
<table data-width="760" data-layout="default" data-number-column="true">
  <thead>
    <tr>
      <th data-colwidth="100"><p>Date</p></th>
      <th data-colwidth="460"><p>Notes</p></th>
      <th data-colwidth="200"><p>Attendees + Links</p></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td data-colwidth="100">
        <p><time datetime="2026-11-24">24 Nov 2026</time></p>
      </td>
      <td data-colwidth="460">
        <p><strong>Import retries</strong></p>
        <ul>
          <li>Retry failed rows only; keep successful rows untouched.</li>
          <li>Enable retries after the load test passes.</li>
        </ul>
        <p><strong>Actions</strong></p>
        <ul data-type="task-list">
          <li data-type="task-item"><input type="checkbox"> Maya: update the retry specification by <time datetime="2026-11-27">27 Nov 2026</time>.</li>
          <li data-type="task-item"><input type="checkbox"> Lee: measure upload latency.</li>
        </ul>
      </td>
      <td data-colwidth="200">
        <p>Maya, Lee</p>
        <p>Recording link not supplied.</p>
      </td>
    </tr>
  </tbody>
</table>
```

In Markdown, use ordinary bullets and `- [ ]` actions. In Slack, use concise
bullets and verified Slack mentions where available. Neither is a substitute
for native Confluence task elements when publishing an HTML page body.

## An Action Without A Settled Decision

Source:

> The team considers launching on Friday but makes no decision. Nora agrees to
> confirm retention requirements with Security before release approval. Nobody
> assigns a deadline.

Useful note:

- [ ] Nora: confirm retention requirements with Security before release approval.

Do not report a Friday launch or manufacture a due date. The action already
expresses the blocker; another "open questions" summary would repeat it.

## No Important Outcome

Source:

> Participants exchange status updates, discuss possible dashboard layouts, and
> say they might revisit them. No decision or follow-up is agreed.

In-session result: "No important decisions or action items recorded."

Do not generate a padded meeting-note entry or send a recap for this recording.
