# Private Runtime State

Keep only generic skill source and examples in this public repository. Live
channel IDs, meeting titles, maps, drafts, transcripts, attendee data, and send
logs belong in a user-authorized private directory outside source repositories.
An ignored subdirectory of this repo is not the runtime location. Never read or
write a private path unless the host permits it. No permitted directory means
session-only operation, with no durable dedup or saved mappings.

## Setup And Routing

Suggest `~/.meeting-minutes/` as a location, not as permission to access it.
When authorized, create the directory with user-only permissions and initialize:

- `series-channels.json` from [the disabled map](../examples/routes.example.json).
- `state.json` from [the empty state](../examples/state.example.json).
- `drafts/<safe-id>.json` only if the user wants drafts saved.

Replace example account/workspace fields with verified identifiers. Unknown or
mismatched context means stop state reuse and resolve it, or work session-only.
IDs from one account/workspace must never be reused in another. If the connected
identity can't be verified, do not persist or publish with cached identities.

A route matches `pattern` as a case-insensitive literal substring of the meeting
title, not regex or glob syntax. One active match with a non-null channel ID is
required. Multiple matches, a disabled match, or a null ID means hold and ask.
Validate the ID with live channel metadata. A saved route selects a destination;
it never grants approval, access rights, or auto-post permission. Update a map
only when the user explicitly asks to remember a confirmed route.

## State Contract

`state.json` has `version`, `context`, `lastSuccessfulScanAt`, and `videos`, an
object keyed by canonical video ARI. Each record has:

- `status`, `reason`, `sourceUpdatedAt`, and `updatedAt`.
- `draftId` and `draftPath` (null if not saved); reuse pending drafts, don't
  silently regenerate them. Changed content invalidates old approval.
- `channelId`, approved text or exact draft reference, and `includeThread`.
- `parentTs`, `replyTs`, `permalink` (null until returned or verified).

Use one status model:

| Status | Next-run behavior |
| --- | --- |
| `pending_review` | Reopen the existing draft, do not send |
| `held` | Revisit the stated blocker; do not discard the video |
| `skipped` | Preserve reason; reconsider on explicit override or changed source |
| `sending` | Interrupted/in-flight attempt; reconcile as unknown before retry |
| `partial` | Parent confirmed; only the missing reply may be resumed |
| `sent` | Skip: parent and every approved reply confirmed |
| `send_unknown` | Outcome uncertain; investigate before any retry |

Transitions: a new candidate becomes `pending_review`, `held`, or `skipped`.
Approval of an unblocked draft permits `pending_review → sending`. After each
confirmed write, save returned IDs immediately. All requested writes confirmed
means `sent`; parent confirmed/reply rejected means `partial`; any uncertain
outcome means `send_unknown`. If no thread was approved, parent confirmation
alone means `sent` and `replyTs` stays null. A known rejection with no write can
return to `pending_review` with the error recorded, but needs renewed approval.

Dry runs may save pending drafts, holds, or skip reasons when authorized, but
never mark delivery or consume approval. Advance `lastSuccessfulScanAt` only
after both lists are completely scanned and every candidate has a recoverable
record; otherwise keep the old checkpoint. Use the previous checkpoint minus
seven days for the next scan. This still misses sufficiently old, newly shared
videos; request an explicit wider backfill when completeness matters.

## Recovery And Concurrency

One writer/sender per account context. Don't run concurrent sends. Re-read and
merge current state before publication; if another run may be active, stop.
Use atomic replacement of state and don't overwrite unrelated records. Use a
safe draft filename (for example a hash of the ARI), never a raw ARI path.

A send timeout or crash after starting a send may already have delivered. Record
`send_unknown` (including which operation and any confirmed IDs); use a supported
read of the destination, with permission, to verify the exact message, or ask the
user to confirm it. Never infer success or automatically replay it. A restarted
`sending` record is also unknown. If parent succeeded, retain `parentTs` even if
the reply is unknown. Resuming a confirmed missing reply uses `threadTs=parentTs`;
it must not create another parent. Never blindly retry an external write.

If delivery succeeded but state persistence failed, report all confirmed IDs and
stop further sends until durable state or a user-confirmed recovery is available.
Don't report local state failure as Slack failure. In session-only mode warn
that duplicate prevention does not carry into the next session.

Persist the minimum needed for recovery. Never save raw API payloads, signed
thumbnail/download URLs, credentials, full transcripts, Calendar event bodies,
or attendee rosters. Saved Slack draft text is sensitive too; protect it like
the mapping and state files. Corrupt or unsupported state is a blocker, not an
empty file to overwrite. Phase 1 supplies instructions and examples, not a
background service or an executable transaction/locking implementation.
