---
name: kotlin-code-reviewer
description: >-
  Principal-level Kotlin code reviewer. Audits architecture, library-first
  implementation, design, implementation details, and AI agentic logic.
  Use when reviewing a PR, branch diff, or any Kotlin source file — triggered by
  requests like "review this PR", "audit this branch", "review my Kotlin code",
  or "give me a code review".
---

# Kotlin Code Reviewer

Principal-level audit of every PR or diff. Read the reference files below as needed for the full criteria.

---

## Git synchronization (run first, always)

Before reviewing any diff:

```bash
git fetch origin main
git fetch origin <BRANCH_NAME>
git diff origin/main...<BRANCH_NAME>
```

Use three-dot syntax (`...`) to isolate only branch-introduced changes.

After diffing, do a **blast-radius check** before writing feedback:

```bash
# Find callers of any modified public function or class
rg "FunctionName|ClassName" --type kotlin
# Check what modules import the modified file's package
rg "import com.example.modified.package" --type kotlin
```

---

## Review workflow

1. **Identify scope** — which modules, layers, and public APIs are touched.
2. **Blast-radius check** — grep for usages of every modified symbol.
3. **Run the five-level framework** — see [`references/review-framework.md`](references/review-framework.md).
   - Architecture & System level
   - Design & Idiomatic quality
   - Implementation details
   - AI Agent & Prompt engineering (only if `.md`/`.yaml` agent files are in the diff)
   - Library-first / minimalist architecture
4. **Write structured output** — see [`references/output-format.md`](references/output-format.md) for severity tiers and required fields.
5. **Kotlin-specific checks** — see [`references/kotlin-idioms.md`](references/kotlin-idioms.md) for idiomatic patterns, stdlib replacements, and coroutine rules.

Every issue must include a copy-pasteable fix and an explanation of the architectural trade-off.
