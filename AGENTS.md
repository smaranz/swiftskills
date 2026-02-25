# AGENTS.md

## Cursor Cloud specific instructions

This is a **Python-only content generation project** (no web server, no database, no containers). All scripts use the Python 3 standard library only — no `pip install` is needed.

### Running the project

- **Generators** (produce `SKILL.md` files): `python3 generate_skills.py`, `python3 generate_swift_skills.py`, `python3 generate_platform_skills.py`, `python3 generate_ai_skills.py`, `python3 generate_frontend_skills.py`
- **Verification** (validates all generated skills): `python3 verify_skills.py`
- `generate_frontend_skills.py` works fully offline; the other four generators fetch from `docs.developer.apple.com` and require internet access.
- There is a non-critical `SyntaxWarning` in `rork_snippets.py:450` (invalid escape sequence) that does not affect output.

### Linting / testing

There is no dedicated linter or test framework configured. The verification script (`verify_skills.py`) is the project's test suite — it checks every `SKILL.md` for required sections (YAML metadata, Rork snippet header, elite tips header, quality description).
