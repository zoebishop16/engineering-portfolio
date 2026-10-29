from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .content import PROJECTS, PROJECTS_BY_SLUG, RESUME, SITE

ROOT = Path(__file__).resolve().parent.parent

app = FastAPI(title="Zoe Bishop — Engineering Portfolio", docs_url="/api/docs", redoc_url=None)
app.add_middleware(GZipMiddleware, minimum_size=500)


class CachedStaticFiles(StaticFiles):
    """Static files with a browser cache header so repeat visits load instantly."""

    async def get_response(self, path, scope):
        response = await super().get_response(path, scope)
        if response.status_code == 200:
            response.headers["Cache-Control"] = "public, max-age=86400"
        return response


app.mount("/static", CachedStaticFiles(directory=ROOT / "static"), name="static")
templates = Jinja2Templates(directory=ROOT / "templates")
templates.env.globals["site"] = SITE
# Changes whenever the stylesheet changes, so browsers never use a stale cached copy.
templates.env.globals["css_version"] = int((ROOT / "static/css/style.css").stat().st_mtime)


def render(request: Request, template: str, active: str, **context) -> HTMLResponse:
    return templates.TemplateResponse(request, template, {"active": active, **context})


# ---- Pages ----------------------------------------------------------------


@app.get("/", response_class=HTMLResponse)
def about(request: Request):
    return render(request, "about.html", "about", featured=PROJECTS[:3])


@app.get("/resume", response_class=HTMLResponse)
def resume(request: Request):
    return render(request, "resume.html", "resume", resume=RESUME)


@app.get("/projects", response_class=HTMLResponse)
def projects(request: Request):
    return render(request, "projects.html", "projects", projects=PROJECTS)


@app.get("/projects/{slug}", response_class=HTMLResponse)
def project_detail(request: Request, slug: str):
    project = PROJECTS_BY_SLUG.get(slug)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    index = PROJECTS.index(project)
    return render(
        request,
        "project.html",
        "projects",
        project=project,
        prev=PROJECTS[index - 1] if index > 0 else None,
        next=PROJECTS[index + 1] if index < len(PROJECTS) - 1 else None,
    )


# ---- JSON API -------------------------------------------------------------


@app.get("/api/profile")
def api_profile():
    return SITE


@app.get("/api/resume")
def api_resume():
    return RESUME


@app.get("/api/projects")
def api_projects():
    return [p.as_dict() for p in PROJECTS]


@app.get("/api/projects/{slug}")
def api_project(slug: str):
    project = PROJECTS_BY_SLUG.get(slug)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project.as_dict(include_html=True)


@app.get("/api/health")
def health():
    return {"status": "ok"}
