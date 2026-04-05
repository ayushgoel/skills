# Output Format

Structure every code review using the four severity tiers below. Each finding must include a fix and a "why".

---

## Severity tiers

| Tier | Label | When to use |
|---|---|---|
| 🔴 | **Architectural & Design Blocker** | Compromises system integrity, public API contract, horizontal scalability, or long-term maintainability. Must be resolved before merge. |
| 🟡 | **Implementation & Safety** | Concrete bugs, security issues, resource leaks, edge-case failures, performance regressions. Should be resolved before merge. |
| 🟢 | **Idiomatic & AI Suggestions** | Kotlin idiom improvements, stdlib replacements, prompt clarity fixes, style. Non-blocking; apply at your discretion. |
| 💬 | **Architectural Clarification** | High-level questions about design intent that need an answer before the review can be completed. |

---

## Finding template

Use this structure for every finding:

```
### [TIER EMOJI] [Short title]

**File:** `path/to/File.kt`, line N  
**Why this matters:** [one sentence on the architectural or safety implication]

**Current code:**
[code block showing the problematic snippet]

**Fix:**
[copy-pasteable replacement code block]

**Trade-off / context:** [explanation of why the fix is better — pattern, stdlib, perf, safety]
```

---

## Review summary header

Open every review with a brief summary before the findings:

```
## Review: <branch or PR name>

**Scope:** <modules / layers touched>  
**Blast radius:** <list of callers / consumers affected>  
**Overall verdict:** [Approve / Approve with minor changes / Changes requested / Blocked]

---
```

Then list findings grouped by tier (🔴 first, then 🟡, 🟢, 💬).

---

## Example finding

```
### 🔴 Shared mutable state breaks horizontal scaling

**File:** `src/main/kotlin/cache/UserCache.kt`, line 34  
**Why this matters:** A `HashMap` stored as a companion object property is shared across all coroutines and threads. Under multiple pod replicas this cache is invisible to other instances, causing stale reads and inconsistent behaviour.

**Current code:**
```kotlin
companion object {
    private val cache = HashMap<String, User>()
}
```

**Fix:**
```kotlin
// Inject a distributed cache (e.g. Redis via Lettuce or Spring Cache)
class UserRepository(private val cache: UserCachePort) { ... }
```

**Trade-off:** Moving to an injected cache interface adds one abstraction layer but makes the implementation testable, swappable (in-memory for tests, Redis in prod), and horizontally safe.
```

---

## Checklist before submitting the review

- [ ] Every 🔴 finding has a copy-pasteable fix.
- [ ] Every 🟡 finding has a fix and a stated edge case or failure mode.
- [ ] Blast-radius grep results are referenced where relevant.
- [ ] No finding lacks a "why this matters" sentence.
- [ ] Overall verdict is stated clearly at the top.
