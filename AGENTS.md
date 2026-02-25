# AGENTS.md

## Cursor Cloud specific instructions

This is a **static Markdown knowledge library** — no web server, database, build step, or runtime dependencies. All content lives in `SKILL.md` files organized by topic.

### Repository structure

- `*/SKILL.md` — 123 agent skill files across SwiftUI, Swift language, platform, frontend, and Apple Intelligence categories
- `README.md` — project overview and structure

### Editing skills

Skills are edited directly as Markdown files. Each `SKILL.md` should contain:
- YAML frontmatter (`---` delimited) with `name` and `description`
- `## 🚀 Rork-Max Quality Snippet` with a real Swift code example
- `## 💎 Elite Implementation Tips` with topic-specific bullet points
- `## When to Use` with use-case guidance
- `## Best Practices` and/or `## Common Pitfalls`
- `## Key APIs` reference table (for doc-sourced skills)

### Linting / testing

No linter or test framework is configured. Validate skills manually by checking that each `SKILL.md` has the required sections listed above.
