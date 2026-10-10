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
| `doc-writer` | Writing and reviewing technical docs, PRDs, design docs, decision records, runbooks, project updates, Confluence content, and Word or PDF deliverables. |
| `write-code` | Implementing focused code changes with proportional planning, systematic debugging, simple design, and risk-based verification. |
| `review-code` | Analysis-first code, pull-request, technical-plan, and design review, with findings prioritized by severity and production impact. |
| `kotlin-code-reviewer` | Kotlin-specific review extension covering architecture, idioms, coroutines, libraries, and JVM contracts. |
| `twg` | Company work-data discovery and actions across Jira, Confluence, search, ownership, status, and engineering context. |
| `prflow` | Direct Bitbucket pull-request, review, comment, check, pipeline, log, and Renovate operations. |
| `foam-notes` | Adding or updating notes in an open Foam knowledge-base workspace. |
| `stock-screener` | Discovering stock opportunities and evaluating named companies with audited screening coverage, normalized fundamentals, valuation sensitivity, and catalyst research. |
| `portfolio-analysis` | Reconciling existing stock and fund holdings, assessing combined exposure, and making allocation decisions using stock-screener's shared company evaluator. |

Use `doc-writer`, `write-code`, and `review-code` for routine work. Add
`kotlin-code-reviewer` when the code under review is Kotlin. Use `twg` for
company context and `prflow` for direct Bitbucket PR or CI work. The remaining
skills are task-specific.

Install `stock-screener` alongside `portfolio-analysis`; it owns the shared
company evaluator and return calculator used by portfolio reviews. Stock-screener
also works independently for discovery or named-stock research.

## Public Repository Safety

Only reusable skill source and generic examples belong in this repository.
Never commit credentials, environment files, retrieved company content, tenant
or account identifiers, private URLs, personal portfolio inputs, generated
reports, command logs, or downloaded evidence.

Before committing, inspect `git status --short` and `git diff --cached`. Keep
runtime files in a private workspace or temporary directory outside this
repository.
