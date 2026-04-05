# Kotlin Idioms & Common Flags

Quick-reference patterns to check during review. Each entry shows a problematic pattern and its idiomatic replacement.

---

## Scope functions

| Smell | Idiomatic replacement |
|---|---|
| `obj.foo(); obj.bar(); return obj` | `obj.apply { foo(); bar() }` |
| `val x = nullable; if (x != null) use(x)` | `nullable?.let { use(it) }` |
| `val x = compute(); log(x); x` | `compute().also { log(it) }` |
| Chained null-safe calls with a fallback | `nullable?.let { … } ?: default` |

Use `apply` for builder-style object configuration; `let` for null-safe transformations; `run` for executing a block and returning a result; `also` for side effects without transforming the receiver; `with` for operating on a non-null receiver multiple times.

---

## Null safety

```kotlin
// ❌ crashes at runtime if null
val name = user!!.name

// ✅ safe call with fallback
val name = user?.name ?: "Unknown"

// ✅ fail fast with a clear message
val name = requireNotNull(user) { "User must not be null at this stage" }.name
```

Flag every `!!` — it must be accompanied by a comment proving it cannot be null, or replaced.

---

## Collections & stdlib

```kotlin
// ❌ manual chunking
val chunks = mutableListOf<List<Int>>()
var i = 0
while (i < list.size) { chunks += list.subList(i, minOf(i + size, list.size)); i += size }

// ✅
val chunks = list.chunked(size)

// ❌ manual string join
var s = ""; for (item in list) { if (s.isNotEmpty()) s += ", "; s += item }

// ✅
val s = list.joinToString(", ")

// ❌ filtering then mapping separately (two passes)
list.filter { it.isActive }.map { it.name }

// ✅ single pass
list.mapNotNull { if (it.isActive) it.name else null }
// or
list.asSequence().filter { it.isActive }.map { it.name }.toList() // for large lists
```

---

## Coroutines

```kotlin
// ❌ blocking call in a coroutine
suspend fun fetchData(): Data {
    Thread.sleep(1000)          // blocks the thread
    return heavyIO()
}

// ✅ use delay for suspend-friendly waiting
suspend fun fetchData(): Data {
    delay(1000)
    return withContext(Dispatchers.IO) { heavyIO() }
}

// ❌ runBlocking inside a suspend function (can deadlock)
suspend fun bad() = runBlocking { doWork() }

// ✅ just call the suspend function
suspend fun good() = doWork()

// ❌ GlobalScope (unstructured concurrency, leaks)
GlobalScope.launch { doWork() }

// ✅ use the caller's scope or a lifecycle-aware scope
viewModelScope.launch { doWork() }
```

Prefer `Flow` for streams of values; `suspend fun` for a single async result. Flag `Channel` usage where `Flow` suffices.

---

## Sealed classes & when expressions

```kotlin
// ❌ open class hierarchy with instanceof checks
if (result is Success) { ... } else if (result is Error) { ... }

// ✅ sealed class with exhaustive when
sealed class Result<out T>
data class Success<T>(val data: T) : Result<T>()
data class Error(val cause: Throwable) : Result<Nothing>()

when (result) {
    is Success -> handle(result.data)
    is Error   -> log(result.cause)
    // compiler enforces exhaustiveness — no else needed
}
```

---

## Value classes

```kotlin
// ❌ stringly-typed parameters (easy to mix up)
fun sendEmail(to: String, from: String, subject: String)

// ✅ zero-overhead wrappers
@JvmInline value class Email(val value: String)
@JvmInline value class Subject(val value: String)

fun sendEmail(to: Email, from: Email, subject: Subject)
```

---

## Data classes & immutability

```kotlin
// ❌ mutable data class used as a value object
data class Point(var x: Int, var y: Int)

// ✅ immutable; use copy() to derive new values
data class Point(val x: Int, val y: Int)
val moved = point.copy(x = point.x + 1)
```

---

## Extension functions vs. utility classes

```kotlin
// ❌ Java-style static utility
object StringUtils {
    fun capitalize(s: String): String = ...
}
StringUtils.capitalize(name)

// ✅ extension function, reads naturally
fun String.capitalize(): String = ...
name.capitalize()
```

Only create extension functions in the same module where the type is used most. Avoid polluting global scope with broad extensions on `Any`, `String`, or `List`.

---

## Delegated properties

```kotlin
// ❌ manual lazy initialization with a backing field + null check
private var _config: Config? = null
val config: Config get() { if (_config == null) _config = loadConfig(); return _config!! }

// ✅
val config: Config by lazy { loadConfig() }

// ❌ manual change tracking
var name: String = ""
    set(value) { val old = field; field = value; notifyChanged(old, value) }

// ✅
var name: String by Delegates.observable("") { _, old, new -> notifyChanged(old, new) }
```
