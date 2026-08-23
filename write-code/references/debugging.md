# Debugging

Use this workflow when a defect is not already localized. Stop when the causal
path is established; do not perform every step mechanically.

## Establish The Failure

1. Capture the expected and actual observable behavior.
2. Find the smallest deterministic reproduction available: a focused test,
   command, request, fixture, log sequence, or code path.
3. Separate confirmed facts from assumptions. Record relevant inputs,
   environment, timing, state, and recent changes without collecting unrelated
   data.

If the failure cannot be reproduced, use the strongest substitute evidence and
state the uncertainty. Do not treat a plausible story as a confirmed cause.

## Localize The Cause

- Trace backward from the first incorrect state, not merely from the final
  error message.
- Compare a working and failing path when possible.
- Narrow the responsible boundary before editing: caller, transformation,
  persistence, external system, concurrency, configuration, or environment.
- Form one falsifiable hypothesis at a time and choose the cheapest observation
  that could disprove it.
- Prefer temporary local diagnostics. Remove instrumentation that is not useful
  in production before finishing.

## Fix And Verify

- Correct the cause at the owning boundary. Avoid masking symptoms with broad
  retries, fallbacks, null handling, or exception suppression.
- Add or adjust a focused regression test when it can reliably represent the
  failure and protect meaningful behavior.
- Re-run the original reproduction, then check adjacent failure modes and
  callers according to blast radius.
- Inspect the final diff for speculative cleanup or diagnostics that escaped
  the investigation.
