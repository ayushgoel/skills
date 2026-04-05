# Skills

Personal agent skills. Each skill is a directory that contains `SKILL.md` (and optional files such as `references/`).

## Installing skills in Cursor

Skills load from a folder named after the skill, with `SKILL.md` at the root of that folder.

### Personal (all projects)

1. Ensure the target directory exists: `~/.cursor/skills/` (create it if needed).
2. Copy the skill folder (e.g. `foam-notes/`) into `~/.cursor/skills/` so you have `~/.cursor/skills/foam-notes/SKILL.md` and any sibling folders such as `references/`.
3. Restart Cursor or reload the window so skills are picked up.

Do not install custom skills under `~/.cursor/skills-cursor/`; that tree is reserved for Cursor’s built-in skills.

### Project-only (this or another repo)

1. Create `.cursor/skills/` at the repository root if it does not exist.
2. Copy the skill folder into `.cursor/skills/` (same layout as above: `.cursor/skills/foam-notes/SKILL.md`).
3. Commit the skill if the team should share it. Open that repository in Cursor when you want the skill available in that project context.

### Checklist

- [ ] `SKILL.md` lives directly inside the skill folder.
- [ ] The folder name matches the skill’s intent (often the same as the `name` field in the YAML frontmatter).
- [ ] Optional content (`references/`, `scripts/`, etc.) was copied alongside `SKILL.md`.

---

## kotlin-code-reviewer

Principal-level Kotlin PR and code reviewer. Covers architecture, library-first design, Kotlin idioms, coroutine safety, and AI agent prompt quality.

- **In this repo:** `kotlin-code-reviewer/` — copy into your Cursor skills location as described above.

---

## foam-notes

Helps maintain a Foam knowledge graph. **Open the Foam repository as the Cursor workspace** when using this skill so the agent reads and writes notes in the correct project.

- **In this repo:** `foam-notes/` — copy or symlink that folder into your Cursor skills location as described above.
