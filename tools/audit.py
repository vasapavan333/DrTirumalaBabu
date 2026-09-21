#!/usr/bin/env python3
"""Pre-flight audit for the site. Run from the project root:

    python tools/audit.py

Checks, per HTML page:
  - <title> and meta description present, unique, and within sane lengths
  - canonical, Open Graph and Twitter tags present
  - exactly one <h1>, and no skipped heading levels
  - every <img> has alt text and width/height (empty alt only when aria-hidden)
  - every form control has a label (or an accessible name)
  - internal links and in-page anchors resolve
  - referenced local assets exist
  - every JSON-LD block parses
  - both pages appear in sitemap.xml
  - no unreplaced launch placeholders in the visible copy
  - no marketing superlatives or outcome guarantees in the copy

Exit status is 1 if anything failed, so it can gate a deploy.
"""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent

# Every page that ships. Keep this in step with sitemap.xml — the sitemap check
# below reads from this list, so a page added here and nowhere else will fail
# the build until it is in the sitemap too.
PAGES = sorted(p.name for p in ROOT.glob("*.html"))
PLACEHOLDER = "drtirumalababu.com"

# Copy the clinic must not make. Checked against rendered text only.
BANNED = [
    r"\bbest\s+psychiatrist\b",
    r"\bno\.?\s*1\b",
    r"\b100%\s*(recovery|cure|success)\b",
    r"\bguaranteed?\s+(recovery|cure|results?|outcomes?)\b",
    r"\bfully\s+cured?\b",
    r"\bworld[-\s]class\b",
    r"\btop\s+rated\b",
]

problems: list[str] = []
notes: list[str] = []


def fail(page: str, msg: str) -> None:
    problems.append(f"{page}: {msg}")


def note(page: str, msg: str) -> None:
    notes.append(f"{page}: {msg}")


class Page(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title = ""
        self._in_title = False
        self._in_text = True
        self._stack: list[str] = []
        self.meta: dict[str, str] = {}
        self.links: list[tuple[str, str]] = []  # (rel, href)
        self.anchors: list[str] = []
        self.ids: set[str] = set()
        self.headings: list[tuple[int, str]] = []
        self.images: list[dict] = []
        self.controls: list[dict] = []
        self.labels_for: set[str] = set()
        self.jsonld: list[str] = []
        self._in_jsonld = False
        self.text_parts: list[str] = []
        self.srcs: list[str] = []

    # -- parsing ---------------------------------------------------------
    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        self._stack.append(tag)

        if "id" in a:
            self.ids.add(a["id"])

        if tag == "title":
            self._in_title = True
        elif tag in ("script", "style", "svg"):
            self._in_text = False
            if tag == "script" and a.get("type") == "application/ld+json":
                self._in_jsonld = True
            if tag == "script" and a.get("src"):
                self.srcs.append(a["src"])
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key.lower()] = a.get("content", "")
        elif tag == "link":
            self.links.append((a.get("rel", ""), a.get("href", "")))
            if a.get("href") and a.get("rel") in ("stylesheet", "icon", "manifest",
                                                  "apple-touch-icon", "preload"):
                self.srcs.append(a["href"])
        elif tag == "a":
            if a.get("href"):
                self.anchors.append(a["href"])
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.headings.append((int(tag[1]), ""))
        elif tag == "img":
            self.images.append(a)
            if a.get("src"):
                self.srcs.append(a["src"])
        elif tag == "source":
            for part in a.get("srcset", "").split(","):
                url = part.strip().split(" ")[0]
                if url:
                    self.srcs.append(url)
        elif tag in ("input", "select", "textarea"):
            if a.get("type", "").lower() not in ("hidden", "submit", "button"):
                self.controls.append(a)
        elif tag == "label":
            if a.get("for"):
                self.labels_for.add(a["for"])

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if self._stack and self._stack[-1] == tag:
            self._stack.pop()

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag in ("script", "style", "svg"):
            self._in_text = True
            self._in_jsonld = False
        while self._stack:
            popped = self._stack.pop()
            if popped == tag:
                break

    def handle_data(self, data):
        if self._in_title:
            self.title += data.strip()
            return
        if self._in_jsonld:
            self.jsonld.append(data)
            return
        if not self._in_text:
            return
        if self.headings and self._stack and self._stack[-1] in (
            "h1", "h2", "h3", "h4", "h5", "h6"
        ):
            level, text = self.headings[-1]
            self.headings[-1] = (level, text + data.strip())
        self.text_parts.append(data)

    @property
    def text(self) -> str:
        return re.sub(r"\s+", " ", " ".join(self.text_parts))


def audit_page(name: str, parsed: dict[str, Page]) -> None:
    path = ROOT / name
    if not path.exists():
        fail(name, "file is missing")
        return

    raw = path.read_text(encoding="utf-8")
    page = Page()
    page.feed(raw)
    parsed[name] = page

    # --- title & description
    if not page.title:
        fail(name, "no <title>")
    elif not 15 <= len(page.title) <= 70:
        note(name, f"title is {len(page.title)} chars (aim for 15-70): {page.title!r}")

    desc = page.meta.get("description", "")
    if not desc:
        fail(name, "no meta description")
    elif not 70 <= len(desc) <= 175:
        note(name, f"meta description is {len(desc)} chars (aim for 70-175)")

    # --- canonical / social
    rels = {rel.lower(): href for rel, href in page.links}
    if "canonical" not in rels:
        fail(name, "no canonical link")
    for tag in ("og:title", "og:description", "og:image", "og:url", "og:type"):
        if not page.meta.get(tag):
            fail(name, f"missing {tag}")
    if not page.meta.get("twitter:card") and name == "index.html":
        fail(name, "missing twitter:card")
    if not page.meta.get("viewport"):
        fail(name, "missing viewport meta")

    # --- headings
    h1s = [t for lvl, t in page.headings if lvl == 1]
    if len(h1s) != 1:
        fail(name, f"expected exactly one <h1>, found {len(h1s)}")
    previous = 0
    for level, text in page.headings:
        if previous and level > previous + 1:
            fail(name, f"heading jumps h{previous} -> h{level} at {text[:48]!r}")
        previous = level

    # --- images
    for img in page.images:
        src = img.get("src", "?")
        decorative = "alt" in img and not img["alt"].strip() and (
            img.get("aria-hidden") == "true" or img.get("role") == "presentation"
        )
        if not img.get("alt", "").strip() and not decorative:
            fail(name, f"image without alt text: {src}")
        if not (img.get("width") and img.get("height")):
            note(name, f"image without width/height (layout shift risk): {src}")

    # --- form controls
    for ctl in page.controls:
        cid = ctl.get("id", "")
        named = cid in page.labels_for or ctl.get("aria-label") or ctl.get(
            "aria-labelledby"
        )
        if not named:
            fail(name, f"form control without a label: {ctl.get('name') or cid or '?'}")

    # --- local assets referenced
    for src in page.srcs:
        if src.startswith(("http:", "https:", "data:", "//", "#")):
            continue
        target = (ROOT / unquote(src.split("?")[0])).resolve()
        if not target.exists():
            fail(name, f"missing local asset: {src}")

    # --- links
    for href in page.anchors:
        if href.startswith("#"):
            anchor = href[1:]
            if anchor and anchor not in page.ids:
                fail(name, f"in-page link to missing id: {href}")
        elif href.startswith(("http:", "https:")):
            if PLACEHOLDER in href:
                continue
        elif href.startswith(("tel:", "mailto:")):
            continue
        else:
            target_path, _, frag = href.partition("#")
            if target_path and not (ROOT / unquote(target_path)).exists():
                fail(name, f"broken internal link: {href}")

    # --- JSON-LD
    for i, block in enumerate(page.jsonld, 1):
        try:
            json.loads(block)
        except json.JSONDecodeError as exc:
            fail(name, f"JSON-LD block {i} does not parse: {exc}")

    # --- copy checks
    body_text = page.text
    if PLACEHOLDER.lower() in body_text.lower():
        fail(name, "launch placeholder is visible in the page copy")
    for pattern in BANNED:
        hit = re.search(pattern, body_text, re.I)
        if hit:
            fail(name, f"disallowed marketing claim in copy: {hit.group(0)!r}")

    # --- placeholders still in the file at all (a reminder, not a failure)
    if PLACEHOLDER in raw:
        count = raw.count(PLACEHOLDER)
        note(name, f"{count} unreplaced '{PLACEHOLDER}' placeholder(s) — set the live domain before launch")


def audit_sitemap(parsed: dict[str, Page]) -> None:
    path = ROOT / "sitemap.xml"
    if not path.exists():
        fail("sitemap.xml", "file is missing")
        return
    raw = path.read_text(encoding="utf-8")
    for page in PAGES:
        slug = "/" if page == "index.html" else f"/{page}"
        if slug not in raw:
            fail("sitemap.xml", f"{page} is not listed")
    if not (ROOT / "robots.txt").exists():
        fail("robots.txt", "file is missing")


def audit_uniqueness(parsed: dict[str, Page]) -> None:
    titles: dict[str, str] = {}
    descs: dict[str, str] = {}
    for name, page in parsed.items():
        if page.title in titles:
            fail(name, f"duplicate <title> with {titles[page.title]}")
        titles[page.title] = name
        d = page.meta.get("description", "")
        if d and d in descs:
            fail(name, f"duplicate meta description with {descs[d]}")
        descs[d] = name


def audit_weight() -> None:
    """Report the transfer weight of the critical path."""
    critical = [
        "index.html",
        "assets/css/site.css",
        "assets/js/site.js",
        "assets/fonts/inter-text.woff2",
        "assets/fonts/newsreader-display.woff2",
        "assets/img/doctor-tirumala-babu.webp",
    ]
    total = 0
    print("\nCritical path:")
    for rel in critical:
        p = ROOT / rel
        if not p.exists():
            fail(rel, "missing")
            continue
        size = p.stat().st_size
        total += size
        print(f"  {size / 1024:7.1f} KB  {rel}")
    print(f"  {total / 1024:7.1f} KB  total (uncompressed)")
    if total > 320 * 1024:
        note("build", f"critical path is {total / 1024:.0f} KB — consider trimming")


def main() -> int:
    parsed: dict[str, Page] = {}
    for page in PAGES:
        audit_page(page, parsed)
    audit_uniqueness(parsed)
    audit_sitemap(parsed)
    audit_weight()

    print()
    if notes:
        print(f"{len(notes)} note(s):")
        for n in notes:
            print(f"  - {n}")
        print()
    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print(f"  ! {p}")
        return 1
    print("no problems found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
