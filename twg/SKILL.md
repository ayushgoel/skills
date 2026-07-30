---
name: twg
description: >-
  Use for company work-data tasks through the TWG CLI, including Jira,
  Confluence, cross-product and Rovo search, indexed code search, ownership,
  status rollups, dependencies, projects, goals, incidents, and related
  engineering context. Use typed commands for known anchors and live help for
  uncertain command contracts.
---

# TWG

Use the installed `twg` CLI to gather and change company work data. Prefer a
small, authoritative evidence set over a broad artifact dump.

## Tool Boundary

- TWG owns Jira, Confluence, Rovo and cross-product search, company documents,
  people, ownership, teams, goals, projects, incidents, and status rollups.
- TWG may discover Bitbucket or GitHub artifacts when answering a cross-product
  question.
- `prflow` owns direct Bitbucket pull-request and CI actions, including PR
  comments, checks, approvals, merges, pipelines, and logs.
- Local `git`, `rg`, and repository-native tools own local source inspection and
  builds.

Do not make TWG and PRFlow compete for direct Bitbucket operations.

## CLI Contract

- Print the installed version with `twg --version`.
- Start with a typed command when the anchor and command family are known.
- Use `twg help` to inspect namespaces and `twg help <terms>` to search help.
- Before guessing a path, flag, output shape, or mutation contract, run
  `twg help describe "<command path>"`.
- If `twg` is not on `PATH`, try `$HOME/.local/bin/twg`. Treat authentication or
  command errors separately from a missing executable.
- Do not run setup, login, logout, install, update, upkeep, cache, credential, or
  environment commands unless the user asks for setup or repair.
- Do not add per-command environment overrides unless the user requests them.

## Route By Intent

| Intent | Preferred route |
| --- | --- |
| Known Jira key or URL | `twg jira workitem get` |
| Exact Jira filtering | `twg jira workitem query --jql` |
| Jira fuzzy text | `twg jira workitem search` |
| Semantic Jira discovery | `twg search ... --app jira` |
| Known Confluence URL or content ID | `twg confluence content get` |
| Fuzzy document discovery | `twg docs search`, then native content get |
| Exact Confluence filtering | Confluence search with CQL |
| Broad company topic | `twg search` with deliberate app and recency filters |
| Personal activity | `twg work query` |
| Tenant-wide work topic | `twg work search` |
| Indexed source or API usage | `twg search-code` |
| Related work and dependencies | `twg context` |
| Owner, expert, approver, or escalation | `twg responsibility`, `twg people`, or `twg user` |
| Team or leadership status | `twg pr-tree`, `twg workitem-tree`, `twg work-tree`, or `twg org-tree` |
| Direct Bitbucket PR or pipeline operation | `prflow`, not TWG |

Use native product reads for known anchors. Use search to discover candidates,
not as a substitute for exact Jira JQL, Confluence CQL, or a known URL.

## Bounded Evidence Workflow

1. Classify the anchor: person, team, project, goal, workitem, page, repository,
   service, incident, asset, or topic.
2. Resolve a supplied key, URL, ARI, email, name, or repository before searching
   broadly.
3. Run one bounded discovery query. Default to about 20 results and add app,
   type, owner, status, space, or recency filters when they improve precision.
4. Shortlist the candidates that can change the conclusion.
5. Hydrate selected candidates with product-native reads.
6. Compare authority, recency, ownership, and contradictions, then synthesize.
7. Stop when the answer, decision, risk, relationship, or next action is
   supported. Do not fetch more examples of an established pattern.

For structured output, prefer the command's advertised compact or evidence view,
for example:

```bash
twg search "<topic>" --limit 20 --output json \
  --output-summary auto --agent-fields @compact
```

Inspect live help before reusing those output flags on another command.

Search snippets are candidate evidence, not final facts. Hydrate a small,
diverse primary-source set and cite stable URLs near claims. Call out stale
sources, missing connector coverage, ACL gaps, and unresolved contradictions.

Never persist retrieved company content, tenant identifiers, private URLs, user
records, or command output in this skill source repository. Use an explicit
private workspace or temporary directory for runtime evidence.

## Jira

- Read the native workitem before relying on status, fields, comments, links, or
  ownership.
- For "what should I pick next," query actual open work or the requested board
  backlog instead of ranking broad activity.
- Before creating or updating, inspect field metadata and use returned
  `customfield_*` IDs instead of guessing display-name mappings.
- Before transitioning, list available transitions and use an advertised
  transition ID or contract.
- Before updating, transitioning, linking, commenting, or deleting, resolve the
  site and key and read current state.
- After a mutation, read the workitem again and report its key, resulting state,
  and URL.

## Confluence

- Treat search results as candidates and read selected content before summarizing
  or editing.
- Use `confluence content` for content, comments, attachments, labels,
  permissions, restrictions, history, tasks, and versions when live help
  advertises the operation.
- Use `confluence space` for space metadata and instructions, and
  `confluence tree` for hierarchy.
- Before authoring in a space, read its instructions when available.
- Before a non-trivial edit, read current content and retain the returned
  version or snapshot contract required by live help.
- Preserve macros and storage representation when exact round-tripping matters.
- Do not duplicate a page title as the first body heading.
- After a mutation, read the content again and report its URL.

## Status, Ownership, And Engineering Context

- Use tree commands for reporting-line rollups and count first. Hydrate examples
  only for risks, blockers, themes, or outliers.
- Distinguish authored work, review work, coordination, and influence.
- Do not infer project health from issue or PR counts alone.
- Resolve a workitem before looking for linked PRs, commits, branches, or repos.
- For code search, start with a concrete package, symbol, API, or behavior.
  Inspect selected source locations and de-duplicate mirrors before concluding.
- Infer ownership from multiple signals such as explicit ownership, recent
  implementation, review history, and reporting context. Do not use keyword
  matches alone.

## Mutation Safety

- Read, search, summarize, and status requests are non-mutating.
- When the user explicitly asks to create, update, comment, transition, link,
  move, archive, restore, or delete, execute after resolving the exact target and
  current state.
- For an unfamiliar, broad, consequential, or destructive mutation, inspect the
  exact live help and preview the target set before execution.
- Never guess IDs, sites, ARIs, slugs, field mappings, transition IDs, permission
  levels, or mutation flags.
- Verify every mutation with a native read. Report partial success per item
  instead of hiding it in an aggregate result.

## Failure Handling

- Stop after the first policy denial.
- After one correction, stop when the same authentication, ACL, schema,
  contract, or backend error occurs again.
- Do not turn a product or authentication error into setup work unless the user
  requested repair.
- Answer from successful evidence and state the missing coverage, remediation,
  and confidence impact.
