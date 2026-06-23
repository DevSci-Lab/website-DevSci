# AGENTS.md

## Project

Flask + Frozen-Flask bilingual (ES/EN) static site for DevSciLab. Built output in `docs/` is committed for GitHub Pages.

## Commands

```bash
python app.py              # Dev server at http://127.0.0.1:5000/
python freeze.py           # Build static site -> docs/ (adds CNAME)
python translate_site.py templates/<file>_en.html  # Auto-translate EN->ES via Google Translate
```

No test suite, linter, or CI is configured.

## Architecture

- **Templates**: `templates/{page}_{lang}.html` — auto-discovered by `freeze.py`. No `app.py` changes needed for new pages.
- **Shared layout**: `templates/base.html`
- **Blog**: Markdown files in `content/blog/` with YAML frontmatter (`title`, `date`, `category`, `lang`). Filename convention: `YYYY-MM-DD-slug-{en,es}.md`.
- **Static assets**: `static/assets/`, `static/images/`
- **Build output**: `docs/` — Frozen-Flask destination, committed to repo for GitHub Pages.

## Conventions

- Routes: `/<lang>/` for index, `/<lang>/<page>/` for pages, `/<lang>/blog/<path>/` for posts.
- Supported languages: `es`, `en` only (hardcoded in `app.py`).
- Blog `category` frontmatter can be a string or a list.
- After editing EN templates, run `translate_site.py` then manually review the generated `_es.html`.
- Blog translations are manual (copy `.md`, change `lang` in frontmatter, translate text).

## Git Workflow

- Never work directly on `main`. Branch naming: `name/task-short` (e.g., `silvia/textos-home`).
- PRs reviewed and merged via GitHub.
