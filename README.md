# Skills

Personal agent skills. Each skill is a directory that contains `SKILL.md` (and optional files such as `references/`).

## Quick start

Install any skill with:

```bash
npx skills add ayushgoel/skills --path skills/<skill-name>
```

OR install all with:

```bash
npx skills add ayushgoel/skills
```

Then invoke in your agent terminal:

```
/kotlin-code-reviewer    # Principal-level Kotlin PR review
/foam-notes              # Add or update a note in the Foam knowledge graph
```

---

## Skills

### kotlin-code-reviewer

Principal-level Kotlin PR and code reviewer. Covers architecture, library-first design, Kotlin idioms, coroutine safety, and AI agent prompt quality.

### foam-notes

Maintains a Foam knowledge graph. Open the Foam repository as the workspace before using this skill so the agent reads and writes notes in the correct project.
