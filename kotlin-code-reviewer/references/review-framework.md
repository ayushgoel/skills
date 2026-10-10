# Review Framework

Four levels of analysis. Work top-down: architectural blockers before implementation details.

---

## 1. Architecture & System level

Ask: does this change compromise system integrity?

- **Separation of concerns** — Does logic belong in this module? Flag leaky abstractions (e.g., business logic in a DTO or repository).
- **Scalability & state** — Does this introduce statefulness that breaks horizontal scaling (shared mutable state, in-memory caches that need coordination)?
- **API contracts** — Does a change to a shared library or public API risk breaking upstream consumers or downstream dependents? Check for removed/renamed symbols.
- **Infrastructure** — If GraphQL schema, Terraform, or HCL is modified: audit for resource-leak risks and security misconfigurations.
- **Event / messaging contracts** — If Kafka topics or event schemas are touched, flag any backward-incompatibility.

---

## 2. Design & Idiomatic quality

Ask: is the right tool being used in the right place?

- **Patterns** — Is the pattern appropriate? (e.g., Strategy vs. Factory; Flow vs. suspend function; Sealed class hierarchy vs. an open class with subclasses).
- **Coroutines** — No blocking calls (`Thread.sleep`, `runBlocking` in a suspend context, synchronous IO) inside coroutine scopes. Prefer `Flow` for multi-value reactive streams; prefer `suspend fun` for single-value async operations.
- **Null safety** — Report `!!` only when the value can be null on a reachable path in the changed code. Prefer `?.let`, `?: return`, or `requireNotNull` with a message.

---

## 3. Implementation details

Ask: will this break in production?

- **Edge cases** — Off-by-one errors, empty collections, null inputs, concurrent modification.
- **Resource management** — Unclosed streams, sockets, database connections. Prefer `use {}` blocks.
- **Performance** — N+1 queries, expensive operations on the main thread, unnecessary object allocations in hot paths, string concatenation in loops (use `StringBuilder` or `buildString`).
- **Security** — Hard-coded secrets or credentials, SQL/prompt injection, unauthorized data exposure, missing input validation.
- **Error handling** — Swallowed exceptions (`catch (e: Exception) {}`), missing error propagation, `Result`/`Either` not checked.

---

## 4. Library-first / minimalist architecture

Ask before approving any new code: *does this need to exist?*

- **Stdlib first** — Before accepting a new utility, check whether Kotlin stdlib, Java 8+ API, or an existing project dependency already provides it:
  - Manual list splitting → `chunked()`, `windowed()`
  - Manual null checks → `?.let`, `?: error()`
  - Custom result wrapper → `kotlin.Result` or `Arrow Either`
  - Custom retry logic → Ktor's built-in retry, Resilience4j
  - Manual string joining → `joinToString()`
- **Kotlin language features** — Flag boilerplate replaceable by:
  - `Delegated Properties` (`by lazy`, `by Delegates.observable`)
  - `Value Classes` (`@JvmInline value class`) for type-safe wrappers with zero overhead
  - `Sealed Interfaces` / `Sealed Classes` for exhaustive state modeling
  - `Data Classes` for value objects (avoid manual `equals`/`hashCode`)
  - `object` declarations for singletons
- **Redundancy** — If a new class/function duplicates something already in the codebase, flag it and point to the existing implementation.
