"""Render every page to static HTML in dist/ for hosts like GitHub Pages.

Usage: python freeze.py [--base-path /RepoName]

Pages use root-relative links ("/projects", "/static/..."). When the site is
served from a subfolder, such as a GitHub Pages project site at
username.github.io/RepoName/, pass that folder as --base-path (or set the
BASE_PATH environment variable) and every link is prefixed with it.
"""

import argparse
import os
import re
import shutil

from fastapi.testclient import TestClient

from app.content import PROJECTS
from app.main import ROOT, app

DIST = ROOT / "dist"
ROUTES = ["/", "/resume", "/projects"] + [f"/projects/{p.slug}" for p in PROJECTS]
API_ROUTES = ["/api/profile", "/api/resume", "/api/projects"] + [f"/api/projects/{p.slug}" for p in PROJECTS]

# Root-relative links in HTML attributes, e.g. href="/resume" or src="/static/...".
# The (?!/) skips protocol-relative URLs like "//example.com".
HTML_LINK = re.compile(r'((?:href|src)=")/(?!/)')
# Site paths inside JSON strings, e.g. "url": "/projects/..." or "/static/...".
JSON_LINK = re.compile(r'"/(projects|static)/')


def normalize(base: str) -> str:
    base = base.strip().strip("/")
    return f"/{base}" if base else ""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--base-path", default=os.environ.get("BASE_PATH", ""))
    base = normalize(parser.parse_args().base_path)

    shutil.rmtree(DIST, ignore_errors=True)
    shutil.copytree(ROOT / "static", DIST / "static")
    client = TestClient(app)

    for route in ROUTES:
        html = client.get(route).raise_for_status().text
        if base:
            html = HTML_LINK.sub(rf"\1{base}/", html)
        out = DIST / route.strip("/") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")

    for route in API_ROUTES:
        data = client.get(route).raise_for_status().text
        if base:
            data = JSON_LINK.sub(rf'"{base}/\1/', data)
        out = DIST / f"{route.strip('/')}.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(data, encoding="utf-8")

    (DIST / ".nojekyll").touch()
    print(f"Wrote {len(ROUTES)} pages and {len(API_ROUTES)} API files to {DIST} (base path: {base or '/'})")


if __name__ == "__main__":
    main()
