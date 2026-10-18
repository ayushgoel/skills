# Product And Technical Requirements

Use to establish the behavior or outcome a product or system must provide,
including PRDs and requirements supplied to another team. Keep the distinction
between an obligation and one possible implementation clear.

## Establish The Needed Behavior

- Ground requirements in the problem, users or consumers, and the outcome they
  need. Include rationale when it prevents a requirement being misunderstood.
- Make requirements observable or testable. Replace vague terms such as "fast"
  with a meaningful threshold, acceptance condition, or explicit `TBD`. Do not
  invent precision when the threshold has not been agreed.
- Identify the responsible component or team where known. Separate its
  obligations from the context about what another component does downstream.
- Distinguish current commitments, later milestones, and aspirations. Preserve
  requirement identifiers and links used for implementation or review.
- Mark material unknowns and conflicts. An approved decision can constrain a
  requirement, but a draft recommendation is not an agreed requirement.

## Choose The Relevant Coverage

For a product requirement, consider user journeys, functional behavior,
acceptance criteria, success measures, and scope. For a technical contract,
consider interfaces, lifecycle rules, invariants, limits, and failure behavior.
Cover dependencies, non-functional needs, rollout, and risks where they affect
acceptance. These are prompts for coverage, not required headings.

For AI features, consider model and tool boundaries, grounding data, evaluation,
safety, privacy, latency, and cost in relation to the actual capability.

Link to detailed designs or noun/schema definitions when they own the mechanism.
Include implementation constraints where they are real requirements, and label
optional implementation guidance so it cannot be mistaken for an obligation.
Preserve supersession notices and point to the current source rather than
silently reviving an obsolete requirements page.
