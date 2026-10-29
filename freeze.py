"""Render every page to static HTML in dist/ for hosts like GitHub Pages.

Usage: python freeze.py
"""

import shutil
from pathlib import Path

from fastapi.testclient import TestClient

from app.content import PROJECTS
from app.main import ROOT, app

DIST = ROOT / "dist"
ROUTES = ["/", "/resume", "/projects"] + [f"/projects/{p.slug}" for p in PROJECTS]
API_ROUTES = ["/api/profile", "/api/resume", "/api/projects"] + [f"/api/projects/{p.slug}" for p in PROJECTS]


def main() -> None:
    shutil.rmtree(DIST, ignore_errors=True)
    shutil.copytree(ROOT / "static", DIST / "static")
    client = TestClient(app)
    for route in ROUTES:
        out = DIST / route.strip("/") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(client.get(route).raise_for_status().text, encoding="utf-8")
    for route in API_ROUTES:
        out = DIST / f"{route.strip('/')}.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(client.get(route).raise_for_status().text, encoding="utf-8")
    (DIST / ".nojekyll").touch()
    print(f"Wrote {len(ROUTES)} pages and {len(API_ROUTES)} API files to {DIST}")


if __name__ == "__main__":
    main()
