# Design Documents

Use to take a concrete problem through to a reasoned, workable solution. Explain
how the design meets the goals within the project's principles and constraints.
Scale detail to the problem's complexity and uncertainty, and let the argument
and existing document determine the section order.

## Explain The Mechanism

- Make the problem, relevant requirements, and proposed approach understandable
  early. Give context the space it needs rather than imposing a summary length.
- Distinguish fixed constraints from negotiable choices. Non-goals should name
  plausible capabilities intentionally excluded from scope.
- Explain component responsibilities and the important paths through the system.
  Use flows or sequences when order matters, component views when boundaries
  matter, and state models when lifecycle behavior matters.
- Make guarantees, assumptions, and scope boundaries explicit. Address ownership,
  tenancy, authentication, data handling, and security where they shape behavior.
- Include contracts, schemas, or worked examples when a reviewer needs them to
  judge the design. Keep examples consistent across the explanation. Move
  exhaustive detail out of the main argument when it is not needed there.
  Use short code or schema excerpts when they clarify a consequential behavior.
- Distinguish current behavior, the proposed design, and later aspirations at the
  point where a reader could confuse them.

## Show The Solution

- Include explanatory diagrams or images as part of the design. Choose the views
  the problem needs, such as system context, architecture, data flow, sequence,
  lifecycle, or an interface mockup. Use enough views to explain the solution
  without imposing a fixed number or requiring every diagram type.
- Make the important relationships, boundaries, or behavior visible and explain
  how the visual supports the solution. Keep labels and examples consistent with
  the surrounding text.
- Produce the actual visuals in the document's destination, using the shared
  visual guidance. Do not leave image placeholders or just describe diagrams
  that should be added later. Check that the visuals render and remain legible.

## Make The Design Reviewable

- Address failure modes, edge cases, scale, operability, compatibility, migration,
  rollout, or rollback in proportion to the change. Explain the cases that could
  invalidate the approach rather than adding empty sections for every topic.
- Explain why the approach fits the goals and compare credible alternatives
  where they affect the choice. Link to relevant decision records. A diagram
  supports the reasoning; it does not establish feasibility on its own.
- When using prototype evidence, state which assumptions it tests and what
  remains unproven.
- Surface uncertainties where they affect the design. Gather open questions
  separately when that helps review, without repeating every caveat in a table.
- Keep essential constraints and rationale visible. Choose panels, lists, and
  expands for comprehension, without requiring a particular macro or note style.
- Link to the owning [requirements](requirements.md) rather than reproducing a
  full requirements catalogue. Respect the project's
  [principles](principles-documents.md); use
  [north-star-documents.md](north-star-documents.md) when the task is to present
  the project's future vision.

## Review And Evolution

Recommend early review by relevant owners and specialists where it would resolve
uncertainty; follow existing review requirements. Keep the current design accurate
as implementation evolves; preserve historical decisions and link superseding ones.
