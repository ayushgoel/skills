# Kotlin Review Output

Use the severity order and findings-first structure from `review-code`. This
reference adds Kotlin-specific content requirements.

## Finding Template

```markdown
### [High] Blocking I/O runs on the request dispatcher

**File:** `src/main/kotlin/example/Handler.kt:42`
**Impact:** Concurrent requests can exhaust request threads when the database is
slow.
**Evidence:** `loadRecord()` performs synchronous JDBC I/O directly inside the
suspending handler.
**Correction:** Move the blocking call behind the existing repository boundary
that runs on the configured I/O dispatcher.
```

For each Kotlin finding:

- Name the affected runtime behavior, contract, or lifecycle.
- Include the file and line where the defect is visible.
- Identify the triggering input, coroutine state, caller, or deployment
  condition.
- Point to the existing Kotlin, JVM, library, or project mechanism that provides
  the smallest correction.
- Include replacement code only when it is short, complete, and safe to apply.
- Explain a design trade-off only for material architecture or API findings.

## Review Completion

Before returning the review, confirm:

- Findings are ordered by Blocker, High, Medium, then Low.
- Each finding is introduced or exposed by the reviewed change.
- Coroutine claims account for cancellation, context, and lifecycle.
- API claims account for Kotlin, Java, serialization, and downstream consumers
  where applicable.
- Kotlin style suggestions are omitted unless they prevent a material defect.
- The response says clearly when there are no actionable findings and records
  remaining test gaps or uncertainty.
