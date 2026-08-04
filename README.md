# Skills

Personal source repository for reusable agent skills. Each top-level skill
directory contains a `SKILL.md` file and may include supporting files such as
`references/`.

## Install

Install one skill:

```bash
npx skills add ayushgoel/skills --path <skill-name>
```

For example:

```bash
npx skills add ayushgoel/skills --path doc-writer
```

Install every skill:

```bash
npx skills add ayushgoel/skills
```

## Skills

| Skill | Use it for |
| --- | --- |
| `doc-writer` | Writing and reviewing technical docs, PRDs, design docs, decision records, runbooks, project updates, and Confluence content. |
| `write-code` | Implementing features and making focused code changes with clean-code and commit discipline. |
| `review-code` | Analysis-first code and pull-request review, with findings prioritized by severity and production impact. |
| `kotlin-code-reviewer` | Kotlin-specific review extension covering architecture, idioms, coroutines, libraries, and JVM contracts. |
| `twg` | Company work-data discovery and actions across Jira, Confluence, search, ownership, status, and engineering context. |
| `prflow` | Direct Bitbucket pull-request, review, comment, check, pipeline, log, and Renovate operations. |
| `foam-notes` | Adding or updating notes in an open Foam knowledge-base workspace. |
| `portfolio-analysis` | Analyzing stocks or portfolio CSVs with two-engine return scenarios, promoter signals, and portfolio-aware actions. |

Use `doc-writer`, `write-code`, and `review-code` for routine work. Add
`kotlin-code-reviewer` when the code under review is Kotlin. Use `twg` for
company context and `prflow` for direct Bitbucket PR or CI work. The remaining
skills are task-specific.

## Public Repository Safety

Only reusable skill source and generic examples belong in this repository.
Never commit credentials, environment files, retrieved company content, tenant
or account identifiers, private URLs, personal portfolio inputs, generated
reports, command logs, or downloaded evidence.

Before committing, inspect `git status --short` and `git diff --cached`. Keep
runtime files in a private workspace or temporary directory outside this
repository.
