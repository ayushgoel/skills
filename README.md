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
| `doc-writer` | Writing and reviewing technical docs, design docs, decision records, runbooks, project updates, and Confluence content. |
| `write-code` | Implementing features and making focused code changes with clean-code and commit discipline. |
| `review-code` | General code and pull-request review, with findings prioritized by severity and design impact. |
| `kotlin-code-reviewer` | Principal-level Kotlin review covering architecture, idioms, coroutines, libraries, and agentic code. |
| `foam-notes` | Adding or updating notes in an open Foam knowledge-base workspace. |
| `portfolio-analysis` | Analyzing a stock-portfolio CSV and producing evidence-based buy, hold, or sell assessments. |

Use `doc-writer`, `write-code`, and `review-code` for routine work. Add
`kotlin-code-reviewer` when the code under review is Kotlin. The remaining
skills are task-specific.

