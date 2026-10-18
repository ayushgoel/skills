# Principles Documents

Use to establish the principles a project follows: its non-variable commitments
and the boundaries within which designs and decisions are made. Treat established
principles as constraints, and keep proposed principles distinguishable from
those the project has adopted.

## Make The Principles Usable

- State each principle clearly enough that a reader can apply it to a real
  design choice. Explain its scope and rationale, especially where it rules out
  an otherwise plausible approach.
- Show practical consequences, examples, or tradeoffs when they clarify the
  commitment. Choose the explanation each principle needs rather than imposing
  the same subsections on every one.
- Separate what is fixed from implementation choices that remain open. A design
  can change within a principle without changing the principle itself.
- Avoid generic aspirations that cannot guide a choice. Preserve precise terms
  where the principle depends on them, and link to the relevant decisions or
  requirements rather than duplicating their detail.

## Keep The Project's Commitments Clear

- Distinguish adopted principles from proposals, assumptions, and temporary
  delivery compromises. An interim implementation does not silently redefine
  an enduring principle.
- If a principle is explicitly changed, record the changed commitment and its
  rationale and identify affected guidance within the requested scope.
- Keep the focus on what the project follows. Use
  [north-star-documents.md](north-star-documents.md) for the future vision and
  [design-documents.md](design-documents.md) for a particular solution.
