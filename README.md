# engineering-portfolio

Zoe Bishop's engineering portfolio — a FastAPI site with About, Resume, and Projects pages plus a JSON API.

## Run locally

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/uvicorn app.main:app --reload
```

Open http://localhost:8000. API docs are at http://localhost:8000/api/docs.

## Editing content

All content lives in `content/` — no code changes needed:

- `content/site.yaml` — name, tagline, contact links, About text, highlight stats
- `content/resume.yaml` — education, experience, projects, activities, skills
- `content/projects/*.md` — one Markdown file per project (front matter + body).
  `order` sets the position on the Projects page; the first three are featured on About.

Images go in `static/images/` (card thumbnails in `static/images/thumbs/`), and the resume PDF is `static/files/Zoe-Bishop-Resume.pdf`.
Restart the server (or rely on `--reload`) after editing content.

## API

| Endpoint | Returns |
| --- | --- |
| `GET /api/profile` | Name, contact info, About text |
| `GET /api/resume` | Full resume as structured JSON |
| `GET /api/projects` | Project list |
| `GET /api/projects/{slug}` | One project, including rendered HTML |

## Static export

`python freeze.py` renders every page (and the API as `.json` files) into `dist/` for static hosts such as GitHub Pages.
Links are root-relative, so host it at a domain root (e.g. `username.github.io` or a custom domain).
