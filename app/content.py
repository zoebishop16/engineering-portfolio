"""Loads site content from the content/ folder once at startup.

Everything is parsed and rendered to HTML up front, so requests only
look up data that is already in memory.
"""

import re
from dataclasses import dataclass, field
from pathlib import Path

import markdown
import yaml

CONTENT_DIR = Path(__file__).resolve().parent.parent / "content"

FRONT_MATTER = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)
# A markdown image on its own line becomes a captioned figure.
STANDALONE_IMAGE = re.compile(r"^!\[([^\]]*)\]\(([^)]+)\)\s*$", re.M)


@dataclass
class Project:
    slug: str
    title: str
    category: str
    year: str
    order: int
    summary: str
    tags: list[str]
    thumbnail: str
    html: str = field(repr=False)

    def as_dict(self, include_html: bool = False) -> dict:
        data = {
            "slug": self.slug,
            "title": self.title,
            "category": self.category,
            "year": self.year,
            "summary": self.summary,
            "tags": self.tags,
            "thumbnail": self.thumbnail,
            "url": f"/projects/{self.slug}",
        }
        if include_html:
            data["html"] = self.html
        return data


def _figure(match: re.Match) -> str:
    alt, src = match.group(1), match.group(2)
    return (
        f'<figure><img src="{src}" alt="{alt}" loading="lazy" decoding="async">'
        f"<figcaption>{alt}</figcaption></figure>"
    )


def _render_markdown(text: str) -> str:
    text = STANDALONE_IMAGE.sub(_figure, text)
    return markdown.markdown(text, extensions=["extra", "sane_lists"])


def _load_project(path: Path) -> Project:
    meta_text, body = FRONT_MATTER.match(path.read_text(encoding="utf-8")).groups()
    meta = yaml.safe_load(meta_text)
    return Project(
        slug=path.stem,
        title=meta["title"],
        category=meta.get("category", ""),
        year=str(meta.get("year") or ""),
        order=meta.get("order", 99),
        summary=meta.get("summary", ""),
        tags=meta.get("tags", []),
        thumbnail=meta["thumbnail"],
        html=_render_markdown(body),
    )


def _load_yaml(name: str) -> dict:
    return yaml.safe_load((CONTENT_DIR / name).read_text(encoding="utf-8"))


SITE = _load_yaml("site.yaml")
RESUME = _load_yaml("resume.yaml")
PROJECTS = sorted(
    (_load_project(p) for p in (CONTENT_DIR / "projects").glob("*.md")),
    key=lambda p: p.order,
)
PROJECTS_BY_SLUG = {p.slug: p for p in PROJECTS}
