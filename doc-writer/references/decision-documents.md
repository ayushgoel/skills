# Decision Documents

Use for a choice that needs evaluation or alignment, including DACIs, proposals,
and exploratory option briefs. Help the reader understand what needs deciding,
what the options mean, and what would justify the choice.

## Frame The Choice

- Make the decision and its scope clear. Separate what this group can decide
  from dependencies or decisions owned elsewhere.
- Explain the problem, constraints, and evidence that materially affect the
  choice. Keep enough context beside the options to make the tradeoffs legible.
- Distinguish exploration, a recommendation, and an agreed outcome. An options
  brief can remain open when its purpose is to prepare a later discussion.
- Use DACI roles, status, and deadlines when that process applies. Preserve known
  participants and authority; mark missing ownership rather than inventing it.

## Support The Judgment

- Compare credible options against the factors that matter for this decision.
  A table helps when readers need to compare the same factors across options;
  prose may work better for a narrow choice. Avoid filler alternatives or
  invented scores that make a preferred option look inevitable.
- When recommending an option, explain its tradeoffs, costs, dependencies, and
  remaining uncertainty. State what evidence could change the recommendation.
- Separate an interim delivery choice from the target state. Explain the
  consequences of deferring work and the path forward where known.
- Include objections or open questions when they affect the choice. Link to
  detailed build contracts rather than making the decision page own them too.
- If the choice is already made and the task is to preserve its rationale, use
  [decision-records.md](decision-records.md). Retain the history of a DACI when
  recording its outcome; a new page is not automatically necessary.

## Visual Indicators And Status

- Use labelled badges to make document state, impact or priority, and factor
  importance easy to scan. Keep their meanings separate: `IN REVIEW` describes
  the document's state; `HIGH` impact describes its consequences; `HIGH`,
  `MEDIUM`, or `LOW` weighting describes how much a decision factor matters.
  Use the labels supported by the evidence and the team's conventions.
- In option comparisons, use `+` for an advantage, `−` for a disadvantage, and
  `=` for a neutral or mixed assessment against the factor. Accompany each
  indicator with a concise explanation. Make unvalidated assumptions and unknowns
  explicit rather than letting a neutral symbol imply certainty.
- Apply indicators consistently against the same criteria across options.
  Explain the convention when needed, and keep the comparison understandable
  without color. Do not choose a winner by counting pluses: factor importance,
  constraints, and unresolved risks determine the recommendation.
- Mark the recommended option visibly while keeping recommendation distinct from
  approval. A `RECOMMENDED` label does not mean the decision is accepted.
- In Confluence, use native status lozenges and supported emoji, such as `:plus:`,
  `:minus:`, and a neutral/equal icon such as `:equal-gry:` where installed. Reuse
  established page conventions and resolve custom icons from the site rather
  than hardcoding their IDs. In Markdown or plain text, use equivalent readable
  labels and symbols.
