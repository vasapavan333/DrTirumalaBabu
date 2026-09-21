#!/usr/bin/env python3
"""Generate the condition pages, the conditions index and the therapies page.

    python tools/build_pages.py

Why a generator lives in a hand-written site: there are twenty-two conditions
sharing one ten-section structure. Writing them by hand guarantees they drift
apart, and a drifting medical page is a page whose safety wording is missing
from some copies and not others. So these pages — and only these — are built:

    conditions.html                 rewritten between <main> and </main>
    therapies.html                  generated whole
    <slug>.html for each condition  generated whole, where content exists

Everything else (index, about, services, contact, privacy) stays hand-edited.
This script also repairs and rewrites the JSON-LD block on every page, because
four of them carried a malformed graph after the multi-page restructure.

Content lives in:
    tools/content_pages.py    categories, the 22 conditions, the therapies
    tools/content_detail.py   the long-form copy for pages that have one

Shared chrome (sprite, header, footer, floating buttons) is lifted from the
hand-written pages into tools/chrome/*.html so the generated pages cannot fall
out of step with them. Re-extract those fragments if the header ever changes:

    sed -n '/===== header /,/<\\/header>/p' conditions.html > tools/chrome/header.html

Run `python tools/audit.py` afterwards. It must print `no problems found`.
"""

from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from content_detail import DETAIL  # noqa: E402
from content_pages import (  # noqa: E402
    CATEGORIES,
    INSTAGRAM_LABEL,
    INSTAGRAM_URL,
    CITY,
    CLINIC,
    CONDITIONS,
    DOCTOR,
    GENERAL_FAQS,
    SERVICES,
    THERAPIES,
    THERAPY_BY_KEY,
)
from content_service import SERVICE_DETAIL  # noqa: E402
from content_short import SHORT  # noqa: E402
from content_therapy import THERAPY_DETAIL  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CHROME = Path(__file__).resolve().parent / "chrome"
DOMAIN = "https://drtirumalababu.com"

CAT_LABEL = {key: label for key, label, _ in CATEGORIES}

# A slug alone does not make a page. Something has to have written the copy
# for it, and until that happens nothing links to it — which is how the audit
# is kept free of dead internal links while pages are being added one at a
# time. Every "does this link exist?" decision in this file consults this set.
PAGE_EXISTS = (
    set(DETAIL)
    | set(SHORT)
    | set(SERVICE_DETAIL)
    | {t["page"] for t in THERAPIES if t["key"] in THERAPY_DETAIL and t["page"]}
)


def cond_target(c: dict) -> str | None:
    """The page a condition card links to, or None if it has no page yet."""
    return c["page"] if c.get("page") in PAGE_EXISTS else None


def service_target(s: dict) -> str | None:
    """A service links to its own page, or across to a condition page."""
    for slug in (s.get("page"), s.get("link")):
        if slug and slug in PAGE_EXISTS:
            return slug
    return None


def therapy_target(t: dict) -> str | None:
    return t["page"] if t.get("page") in PAGE_EXISTS else None

# Pages whose <main> is hand-written but whose JSON-LD this script owns.
HAND_WRITTEN = [
    "index.html",
    "about.html",
    "services.html",
    "contact.html",
    "privacy.html",
]

# Every page needs exactly one <h1>, and these three lost theirs when the
# single-page site was split up: their lead heading stayed an <h2> because it
# had been a section heading on the old one-page layout. Promoting it is the
# whole fix — the copy does not change.
H1_PROMOTE = {
    "about.html": "about-title",
    "services.html": "services-title",
    "contact.html": "cta-title",
}

# Regions of a hand-written page that this build owns and rewrites. Each entry
# is the regex that finds the region in a page the build has not touched yet.
# Once rewritten, the region carries HTML comment markers and is found by
# those instead — the generated nav contains nested <ul>s, which a non-greedy
# "up to the first </ul>" pattern would cut in half on the second run.
REGIONS = {
    "nav": re.compile(r'[ \t]*<ul class="nav__list">.*?</ul>\n', re.S),
    "navpanel": re.compile(
        r'[ \t]*<div class="nav__panel" id="nav-panel" hidden>.*?\n      </div>\n', re.S
    ),
    "servicelist": re.compile(
        r'[ \t]*<div class="accordion">.*?\n          </div>\n', re.S
    ),
}


# ---------------------------------------------------------------------------
# small helpers
# ---------------------------------------------------------------------------


def text(value: str) -> str:
    """Markup-bearing copy -> plain text, for meta tags and JSON-LD."""
    return html.unescape(re.sub(r"<[^>]+>", "", value)).strip()


def attr(value: str) -> str:
    """Plain text -> safe attribute value."""
    return html.escape(text(value), quote=True)


def icon(name: str, cls: str = "icon") -> str:
    return f'<svg class="{cls}" aria-hidden="true"><use href="#{name}" /></svg>'


def chrome(name: str) -> str:
    return (CHROME / f"{name}.html").read_text(encoding="utf-8").rstrip("\n")


REGION_INDENT = {"nav": "          ", "navpanel": "      ", "servicelist": "          "}


def replace_region(raw: str, name: str, new: str) -> str:
    """Swap out a region this build owns, leaving markers for the next run."""
    start, end = f"<!-- {name}:start -->", f"<!-- {name}:end -->"
    pad = REGION_INDENT[name]
    block = f"{pad}{start}\n{new}\n{pad}{end}\n"
    marked = re.compile(
        r"[ \t]*" + re.escape(start) + r".*?" + re.escape(end) + r"\n", re.S
    )
    if marked.search(raw):
        return marked.sub(lambda _: block, raw, count=1)
    if not REGIONS[name].search(raw):
        return raw
    return REGIONS[name].sub(lambda _: block, raw, count=1)


# ---------------------------------------------------------------------------
# navigation
# ---------------------------------------------------------------------------
#
# The primary nav carries dropdowns for Services, Conditions and Therapies.
# They are opened by CSS — :hover and :focus-within — and not by a script, so
# they work with the keyboard, survive a script failing to load, and cost
# nothing at runtime. The top-level item stays an ordinary link to the full
# page, which is what a tap does on a touch screen and what a crawler follows.


def menu_links(items: list[tuple[str, str]]) -> str:
    return "\n".join(
        f'                      <li><a href="{href}">{label}</a></li>'
        for label, href in items
    )


def nav_menu(title: str, all_href: str, all_label: str,
             columns: list[tuple[str, list[tuple[str, str]]]]) -> str:
    """One dropdown panel. Columns may be unlabelled (pass "" as the heading)."""
    cols = []
    for heading, items in columns:
        head = (
            f'                    <p class="nav__menu-head">{heading}</p>\n'
            if heading else ""
        )
        cols.append(
            f"""                  <div class="nav__menu-col">
{head}                    <ul>
{menu_links(items)}
                    </ul>
                  </div>"""
        )
    return f"""              <div class="nav__menu">
                <div class="shell nav__menu-inner">
{chr(10).join(cols)}
                  <div class="nav__menu-col nav__menu-col--all">
                    <a class="nav__menu-all" href="{all_href}">
                      {all_label}
                      {icon('i-arrow')}
                    </a>
                  </div>
                </div>
              </div>"""


def nav_list() -> str:
    services = [
        (s["name"], f"{service_target(s)}.html")
        for s in SERVICES
        if service_target(s)
    ]
    therapies = [
        (t["menu"], f"{therapy_target(t)}.html")
        for t in THERAPIES
        if therapy_target(t)
    ]
    condition_cols = []
    for key, label, _ in CATEGORIES:
        items = [
            (c["name"].split(" (")[0], f"{cond_target(c)}.html")
            for c in CONDITIONS
            if c["cat"] == key and cond_target(c)
        ]
        if items:
            condition_cols.append((label, items))

    def split(items, parts):
        size = -(-len(items) // parts)
        return [("", items[i:i + size]) for i in range(0, len(items), size)]

    entries = [
        ('<li><a href="index.html">Home</a></li>'),
        ('<li><a href="about.html">About</a></li>'),
    ]
    for label, href, cols in (
        ("Services", "services.html", split(services, 2) if services else []),
        ("Conditions", "conditions.html", condition_cols),
        ("Therapies", "therapies.html", split(therapies, 3) if therapies else []),
    ):
        if not cols:
            entries.append(f'<li><a href="{href}">{label}</a></li>')
            continue
        entries.append(
            f"""<li class="nav__has-menu">
              <a href="{href}" class="nav__top">{label}</a>
{nav_menu(label, href, f"All {label.lower()}", cols)}
            </li>"""
        )
    entries.append('<li><a href="contact.html">Contact</a></li>')
    entries.append(
        f'''<li class="nav__social-item">
              <a class="nav__social" href="{INSTAGRAM_URL}" target="_blank"
                 rel="noopener me" title="{INSTAGRAM_LABEL}"
                 aria-label="{INSTAGRAM_LABEL} (opens in a new tab)">
                {icon('i-instagram')}
                <span class="visually-hidden">{INSTAGRAM_LABEL}</span>
              </a>
            </li>'''
    )
    body = "\n".join(f"            {e}" for e in entries)
    return f"""          <ul class="nav__list">
{body}
          </ul>"""


def nav_panel() -> str:
    """The mobile panel. <details> groups, so it also needs no script."""

    def group(label: str, href: str, items: list[tuple[str, str]]) -> str:
        if not items:
            return f'            <li><a href="{href}">{label}</a></li>' 
        links = "\n".join(
            f'                  <li><a href="{h}">{n}</a></li>' for n, h in items
        )
        return f"""            <li>
              <details class="nav__group">
                <summary>{label}</summary>
                <ul>
                  <li><a href="{href}">All {label.lower()}</a></li>
{links}
                </ul>
              </details>
            </li>"""

    services = [(s["name"], f"{service_target(s)}.html")
                for s in SERVICES if service_target(s)]
    conditions = [(c["name"].split(" (")[0], f"{cond_target(c)}.html")
                  for c in CONDITIONS if cond_target(c)]
    therapies = [(t["menu"], f"{therapy_target(t)}.html")
                 for t in THERAPIES if therapy_target(t)]

    return f"""      <div class="nav__panel" id="nav-panel" hidden>
        <div class="shell">
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Doctor</a></li>
{group("Services", "services.html", services)}
{group("Conditions", "conditions.html", conditions)}
{group("Therapies", "therapies.html", therapies)}
            <li><a href="services.html#process">How It Works</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li>
              <a href="{INSTAGRAM_URL}" target="_blank" rel="noopener me">
                {INSTAGRAM_LABEL}
              </a>
            </li>
          </ul>
          <a class="btn btn--primary" href="contact.html#appointment">
            {icon('i-calendar')}
            Book Appointment
          </a>
        </div>
      </div>"""


def apply_nav(raw: str) -> str:
    raw = replace_region(raw, "nav", nav_list())
    return replace_region(raw, "navpanel", nav_panel())


CONDITION_BY_SLUG = {c["page"]: c for c in CONDITIONS if c.get("page")}


def services_list() -> str:
    """The accordion on services.html, with each row linking onward.

    Seven of the ten rows link to a condition page rather than to a service
    page of their own, and the link text says so — "Read about depression"
    rather than "read more", so that nobody clicks expecting a different page
    about the service and lands on the condition.
    """
    rows = []
    for s in SERVICES:
        target = service_target(s)
        more = ""
        if target:
            if s.get("page"):
                label = "More about this service"
            else:
                cond = CONDITION_BY_SLUG.get(target)
                label = f"Read about {cond['short']}" if cond else "Read more"
            more = f"""
                <a class="card__more" href="{target}.html">
                  {label}
                  {icon('i-arrow')}
                </a>"""
        rows.append(
            accordion_row(s["icon"], s["name"],
                          f"                <p>{s['card']}</p>{more}")
        )
    return f"""          <div class="accordion">
{chr(10).join(rows)}
          </div>"""


# ---------------------------------------------------------------------------
# structured data
# ---------------------------------------------------------------------------


def base_graph() -> list[dict]:
    """The site-wide nodes, read from index.html so there is one source.

    index.html is hand-edited and its graph is the canonical one; copying it
    here means a change to the clinic's address or phone number propagates to
    every generated page on the next build.
    """
    raw = (ROOT / "index.html").read_text(encoding="utf-8")
    block = re.search(
        r'<script type="application/ld\+json">(.*?)</script>', raw, re.S
    )
    if not block:
        raise SystemExit("index.html has no JSON-LD block to copy from")
    graph = json.loads(block.group(1))["@graph"]
    keep = ("WebSite", "Organization", "Physician", "MedicalClinic")
    return [n for n in graph if n.get("@type") in keep]


def breadcrumb(url: str, trail: list[tuple[str, str]]) -> dict:
    return {
        "@type": "BreadcrumbList",
        "@id": f"{url}#breadcrumb",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i,
                "name": name,
                "item": f"{DOMAIN}/{href}" if href else url,
            }
            for i, (name, href) in enumerate(trail, 1)
        ],
    }


def faq_node(url: str, faqs: list[tuple[str, str]]) -> dict:
    return {
        "@type": "FAQPage",
        "@id": f"{url}#faq",
        "mainEntity": [
            {
                "@type": "Question",
                "name": text(q),
                "acceptedAnswer": {"@type": "Answer", "text": text(a)},
            }
            for q, a in faqs
        ],
    }


def webpage_node(url: str, title: str, desc: str, condition: str | None) -> dict:
    node: dict = {
        "@type": "MedicalWebPage",
        "@id": f"{url}#webpage",
        "url": url,
        "name": text(title),
        "description": text(desc),
        "inLanguage": "en-IN",
        "isPartOf": {"@id": f"{DOMAIN}/#website"},
        "about": {"@id": f"{DOMAIN}/#physician"},
        "breadcrumb": {"@id": f"{url}#breadcrumb"},
        "reviewedBy": {"@id": f"{DOMAIN}/#physician"},
    }
    if condition:
        node["about"] = {
            "@type": "MedicalCondition",
            "name": text(condition),
        }
        node["mainContentOfPage"] = {"@type": "WebPageElement", "cssSelector": "#main"}
    return node


def jsonld(nodes: list[dict]) -> str:
    body = json.dumps({"@context": "https://schema.org", "@graph": nodes}, indent=2)
    body = "\n".join("      " + line for line in body.split("\n"))
    return (
        '    <script type="application/ld+json">\n'
        f"{body}\n"
        "    </script>"
    )


# ---------------------------------------------------------------------------
# page shell
# ---------------------------------------------------------------------------


def head(slug: str, title: str, desc: str, og_alt: str, graph: list[dict]) -> str:
    url = f"{DOMAIN}/{slug}"
    t, d, a = attr(title), attr(desc), attr(og_alt)
    return f"""  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="author" content="{DOCTOR}" />
    <title>{t}</title>
    <meta name="description" content="{d}" />
    <meta name="theme-color" content="#102a44" />
    <meta name="robots" content="index, follow, max-image-preview:large" />
    <link rel="canonical" href="{url}" />

    <meta property="og:type" content="article" />
    <meta property="og:locale" content="en_IN" />
    <meta property="og:site_name" content="Dr. Tirumala Babu Psychiatry" />
    <meta property="og:title" content="{t}" />
    <meta property="og:description" content="{d}" />
    <meta property="og:url" content="{url}" />
    <meta property="og:image" content="{DOMAIN}/assets/img/og-card.jpg" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta property="og:image:alt" content="{a}" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{t}" />
    <meta name="twitter:description" content="{d}" />
    <meta name="twitter:image" content="{DOMAIN}/assets/img/og-card.jpg" />

    <link rel="icon" href="favicon.ico" sizes="any" />
    <link rel="icon" href="assets/img/favicon-32.png" type="image/png" sizes="32x32" />
    <link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png" />
    <link rel="manifest" href="site.webmanifest" />

    <!-- Self-hosted, subset webfonts (see tools/build_fonts.py). Both Latin
         faces paint above the fold, so both are preloaded; the Telugu face is
         unicode-range gated and loads on its own. -->
    <link rel="preload" href="assets/fonts/inter-text.woff2" as="font" type="font/woff2" crossorigin />
    <link rel="preload" href="assets/fonts/newsreader-display.woff2" as="font" type="font/woff2" crossorigin />
    <link rel="stylesheet" href="assets/css/site.css" />

    <script>
      document.documentElement.className = "js";
    </script>

{jsonld(graph)}
  </head>"""


def shell(slug: str, title: str, desc: str, og_alt: str, graph: list[dict], main: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en" class="no-js">
{head(slug, title, desc, og_alt, graph)}

  <body>
    <!-- The "Home" and brand links target this, not the header. The header is
         position:sticky, so its own layout position travels with the scroll. -->
    <span id="top"></span>
    <a class="skip-link" href="#main">Skip to content</a>

{chrome('sprite')}

{apply_nav(chrome('header'))}

{main}

{chrome('footer')}

{chrome('fab')}

    <script src="assets/js/site.js" defer></script>
  </body>
</html>
"""


# ---------------------------------------------------------------------------
# reusable sections
# ---------------------------------------------------------------------------


def emergency_callout(extra: str = "") -> str:
    lead = extra or (
        "<strong>If there is immediate danger, do not wait for an appointment.</strong>"
    )
    return f"""          <div class="callout">
            {icon('i-alert')}
            <p>
              {lead}
              Call <a href="tel:112">112</a> for emergency services or
              <a href="tel:108">108</a> for an ambulance. For free mental health
              support at any hour, Tele-MANAS &mdash; the Government of India
              helpline &mdash; is on <a href="tel:14416">14416</a> or
              <a href="tel:18008914416">1-800-891-4416</a>.
            </p>
          </div>"""


def cta_band(heading: str, body: str, anchor: str = "appointment") -> str:
    wa = (
        "https://wa.me/918985014488?text=Hello%2C%20I%20would%20like%20to%20"
        "request%20an%20appointment%20with%20Dr.%20Tirumala%20Babu."
    )
    return f"""      <section class="cta-band" id="{anchor}" aria-labelledby="cta-title">
        <div class="shell">
          <div class="cta-band__inner">
            <p class="eyebrow">Appointments</p>
            <h2 id="cta-title">{heading}</h2>
            <p>{body}</p>
            <div class="btn-row">
              <a class="btn btn--onnavy" href="tel:+918985014488">
                {icon('i-phone')}
                Call now
              </a>
              <a class="btn btn--accent" href="{wa}" rel="noopener" target="_blank">
                {icon('i-whatsapp')}
                Book on WhatsApp
              </a>
              <a class="btn btn--outline-light" href="contact.html#appointment">
                {icon('i-calendar')}
                Send an enquiry
              </a>
            </div>
            <p class="cta-band__note">
              Consulting hours are Monday to Saturday, 6:00&ndash;9:00&nbsp;PM, by
              appointment. This website does not confirm bookings on its own
              &mdash; the clinic confirms a time with you.
            </p>
          </div>
        </div>
      </section>"""


def accordion_row(icon_name: str, title: str, body: str,
                  row_id: str = "") -> str:
    """One <details> row for an accordion list.

    The heading lives inside the <summary> rather than wrapping it, which is
    what the HTML spec allows and what lets a screen reader's heading list
    still enumerate every service, condition and therapy while the rows are
    closed. No JavaScript: the browser opens and closes these itself, and
    find-in-page expands a row to reveal a match.
    """
    ident = f' id="{row_id}"' if row_id else ""

    return f"""            <details{ident}>
              <summary>
                {icon(icon_name)}
                <div class="accordion__title">
                  <h3>{title}</h3>
                </div>
              </summary>
              <div class="accordion__body">
{body}
              </div>
            </details>"""


def faq_section(faqs: list[tuple[str, str]], intro: str) -> str:
    items = "\n".join(
        f"""            <details>
              <summary>{q}</summary>
              <div class="faq__answer">
                <p>{a}</p>
              </div>
            </details>"""
        for q, a in faqs
    )
    return f"""      <section class="section" id="faq" aria-labelledby="faq-title">
        <div class="shell">
          <div class="section__head section__head--center">
            <p class="eyebrow">Questions</p>
            <h2 id="faq-title">Frequently asked questions</h2>
            <p class="lede">{intro}</p>
          </div>

          <div class="faq">
{items}
          </div>
        </div>
      </section>"""


# ---------------------------------------------------------------------------
# condition detail page
# ---------------------------------------------------------------------------


def condition_page(slug: str) -> str:
    d = DETAIL[slug]
    url = f"{DOMAIN}/{slug}.html"
    name = d["name"]

    graph = base_graph()
    graph.append(
        breadcrumb(
            url,
            [
                ("Home", ""),
                ("Conditions", "conditions.html"),
                (name, f"{slug}.html"),
            ],
        )
    )
    graph.append(webpage_node(url, d["title"], d["meta"], name))
    graph.append(faq_node(url, d["faqs"]))

    parts: list[str] = ['    <main id="main">']

    # 1 + 2 — page title and short introduction
    parts.append(f"""      <section class="section section--tint" id="overview" aria-labelledby="page-title">
        <div class="shell">
          <div class="section__head section__head--center">
            <p class="eyebrow">{CAT_LABEL.get(d['category'], d['category'])}</p>
            <h1 id="page-title">{d['keyword'][:1].upper() + d['keyword'][1:]}</h1>
            <p class="lede">{d['intro']}</p>
            <div class="btn-row btn-row--center btn-row--spaced">
              <a class="btn btn--primary" href="contact.html#appointment">
                {icon('i-calendar')}
                Book an appointment
              </a>
              <a class="btn btn--ghost" href="tel:+918985014488">
                {icon('i-phone')}
                +91 89850 14488
              </a>
            </div>
          </div>
        </div>
      </section>""")

    # 3 — what is this condition
    what = "\n".join(f"              <p>{p}</p>" for p in d["what"])
    urgent = ""
    if d["urgent"]:
        urgent = "\n" + emergency_callout(d.get("urgent_text", ""))
    parts.append(f"""      <section class="section" id="what" aria-labelledby="what-title">
        <div class="shell">
          <div class="section__head">
            <p class="eyebrow">Overview</p>
            <h2 id="what-title">What is {name.lower()}?</h2>
          </div>
          <div class="prose">
{what}
          </div>
{urgent}
        </div>
      </section>""")

    # 4 — symptoms
    groups = "\n".join(
        f"""            <article class="card card--list">
              <h3>{group}</h3>
              <ul>
{chr(10).join(f'                <li>{item}</li>' for item in items)}
              </ul>
            </article>"""
        for group, items in d["symptoms"]
    )
    symptoms_note = d.get(
        "symptoms_note",
        "This is a description, not a checklist to diagnose yourself with. "
        "Most people recognise some of these at some point. What matters "
        "clinically is how many are present, how long they have lasted and how "
        "much they are affecting day-to-day life &mdash; which is what an "
        "assessment is for.",
    )
    parts.append(f"""      <section class="section section--alt" id="symptoms" aria-labelledby="symptoms-title">
        <div class="shell">
          <div class="section__head">
            <p class="eyebrow">Symptoms</p>
            <h2 id="symptoms-title">Signs and symptoms</h2>
            <p class="lede">{symptoms_note}</p>
          </div>

          <div class="cards">
{groups}
          </div>
        </div>
      </section>""")

    # 5 — causes and risk factors
    causes = "\n".join(
        f"""            <article class="card">
              <h3>{label}</h3>
              <p>{body}</p>
            </article>"""
        for label, body in d["causes"]
    )
    parts.append(f"""      <section class="section" id="causes" aria-labelledby="causes-title">
        <div class="shell">
          <div class="section__head">
            <p class="eyebrow">Causes</p>
            <h2 id="causes-title">Causes and risk factors</h2>
            <p class="lede">{d['causes_note']}</p>
          </div>

          <div class="cards">
{causes}
          </div>
        </div>
      </section>""")

    # 6 — when to consult a psychiatrist
    when = "\n".join(
        f"""            <li>
              {icon('i-check')}
              <span>{item}</span>
            </li>"""
        for item in d["when"]
    )
    parts.append(f"""      <section class="section section--alt" id="when" aria-labelledby="when-title">
        <div class="shell">
          <div class="section__head section__head--center">
            <p class="eyebrow">When to seek help</p>
            <h2 id="when-title">When to consult a psychiatrist</h2>
            <p class="lede">
              There is no threshold you have to cross before asking. These are
              the situations where an assessment is usually worth arranging
              rather than waiting.
            </p>
          </div>

          <ul class="conditions">
{when}
          </ul>
        </div>
      </section>""")

    # 7 — diagnosis
    diagnosis = "\n".join(
        f"""            <li class="step">
              <h3>{label}</h3>
              <p>{body}</p>
            </li>"""
        for label, body in d["diagnosis"]
    )
    parts.append(f"""      <section class="section" id="diagnosis" aria-labelledby="diagnosis-title">
        <div class="shell">
          <div class="section__head">
            <p class="eyebrow">Diagnosis</p>
            <h2 id="diagnosis-title">How {name.lower()} is assessed</h2>
            <p class="lede">
              There is no blood test or scan that diagnoses this. The
              assessment is clinical &mdash; a structured conversation, a
              history, and tests only where something physical needs ruling
              out.
            </p>
          </div>

          <ol class="steps">
{diagnosis}
          </ol>

          <p class="note note--wide">
            Screening questionnaires are aids to an assessment, not diagnostic
            tests. A score on its own does not establish or rule out a
            diagnosis, and it is not a substitute for seeing a doctor.
          </p>
        </div>
      </section>""")

    # 8 — treatment and management
    treatment = "\n".join(
        f"""            <article class="card">
              <h3>{label}</h3>
              <p>{body}</p>
            </article>"""
        for label, body in d["treatment"]
    )
    parts.append(f"""      <section class="section section--alt" id="treatment" aria-labelledby="treatment-title">
        <div class="shell">
          <div class="section__head">
            <p class="eyebrow">Treatment</p>
            <h2 id="treatment-title">Treatment and management</h2>
            <p class="lede">{d['treatment_note']}</p>
          </div>

          <div class="cards">
{treatment}
          </div>

          <p class="note note--wide">
            This page does not name medicines or doses, and nothing here is a
            treatment plan. What is appropriate depends on the individual
            assessment, and is decided with you in the consultation.
          </p>
        </div>
      </section>""")

    # 9 — non-pharmacological therapies
    parts.append(therapies_section(d["therapies"]))

    # 10 — FAQs
    parts.append(
        faq_section(
            d["faqs"],
            f"Common questions about {name.lower()} and what to expect from a "
            f"consultation at {CLINIC}, {CITY}.",
        )
    )

    # 11 — appointment CTA
    parts.append(
        cta_band(
            "Talk to a psychiatrist about this",
            f"{DOCTOR} consults at {CLINIC}, {CITY}. Call the clinic to "
            "discuss your concerns and request an appointment.",
        )
    )

    parts.append("    </main>")
    main = "\n\n".join(parts)

    og_alt = f"{d['keyword']} with {DOCTOR}"
    return shell(f"{slug}.html", d["title"], d["meta"], og_alt, graph, main)


# ---------------------------------------------------------------------------
# shared section builders for the shorter page templates
# ---------------------------------------------------------------------------


def page_hero(eyebrow: str, title: str, lede: str, extra: str = "",
              second: tuple[str, str, str] | None = None) -> str:
    """The tinted opening section every generated page starts with."""
    alt = second or ("i-phone", "tel:+918985014488", "+91 89850 14488")
    return f"""      <section class="section section--tint" id="overview" aria-labelledby="page-title">
        <div class="shell">
          <div class="section__head section__head--center">
            <p class="eyebrow">{eyebrow}</p>
            <h1 id="page-title">{title}</h1>
            <p class="lede">{lede}</p>
{extra}            <div class="btn-row btn-row--center btn-row--spaced">
              <a class="btn btn--primary" href="contact.html#appointment">
                {icon('i-calendar')}
                Book an appointment
              </a>
              <a class="btn btn--ghost" href="{alt[1]}">
                {icon(alt[0])}
                {alt[2]}
              </a>
            </div>
          </div>
        </div>
      </section>"""


def check_list(items: list[str]) -> str:
    return "\n".join(
        f"""            <li>
              {icon('i-check')}
              <span>{item}</span>
            </li>"""
        for item in items
    )


def label_cards(pairs: list[tuple[str, str]]) -> str:
    return "\n".join(
        f"""            <article class="card">
              <h3>{label}</h3>
              <p>{body}</p>
            </article>"""
        for label, body in pairs
    )


def therapy_rows_for(keys: list[str]) -> tuple[str, int]:
    """The "approaches that may help" accordion, shared by both templates."""
    used = [THERAPY_BY_KEY[k] for k in keys if k in THERAPY_BY_KEY]
    rows = []
    for t in used:
        target = therapy_target(t)
        more = ""
        if target:
            more = f"""
                <a class="card__more" href="{target}.html">
                  About this therapy
                  {icon('i-arrow')}
                </a>"""
        rows.append(
            accordion_row(t["icon"], t["name"],
                          f"                <p>{t['what']}</p>{more}")
        )
    return "\n".join(rows), len(used)


def therapies_section(keys: list[str]) -> str:
    rows, count = therapy_rows_for(keys)
    if not rows:
        return ""
    return f"""      <section class="section" id="therapies" aria-labelledby="therapies-title">
        <div class="shell">
          <div class="section__head">
            <p class="eyebrow">Therapies</p>
            <h2 id="therapies-title">Approaches that may form part of treatment</h2>
            <p class="lede">
              Talking and behavioural approaches are part of the picture for
              many people &mdash; sometimes on their own, sometimes alongside
              medication. Which of these is suitable, and whether it is
              provided here or through a referral, is decided in the
              consultation.
            </p>
          </div>

          <div class="accordion">
{rows}
          </div>
          <p class="accordion__meta">{count} approaches &mdash; tap any one to read about it</p>

          <div class="btn-row btn-row--spaced">
            <a class="btn btn--ghost" href="therapies.html">
              {icon('i-leaf')}
              See all therapies
            </a>
          </div>
        </div>
      </section>"""


# ---------------------------------------------------------------------------
# short condition page
# ---------------------------------------------------------------------------


def short_condition_page(slug: str) -> str:
    d = SHORT[slug]
    url = f"{DOMAIN}/{slug}.html"
    name = d["name"]
    short_name = name.split(" (")[0]

    graph = base_graph()
    graph.append(breadcrumb(url, [("Home", ""), ("Conditions", "conditions.html"),
                                  (short_name, f"{slug}.html")]))
    graph.append(webpage_node(url, d["title"], d["meta"], short_name))
    graph.append(faq_node(url, d["faqs"]))

    parts = ['    <main id="main">']

    parts.append(page_hero(
        d["category"],
        d["keyword"][:1].upper() + d["keyword"][1:],
        d["intro"],
    ))

    what = "\n".join(f"              <p>{p}</p>" for p in d["what"])
    urgent = "\n" + emergency_callout(d.get("urgent_text", "")) if d["urgent"] else ""
    parts.append(f"""      <section class="section" id="what" aria-labelledby="what-title">
        <div class="shell">
          <div class="section__head">
            <p class="eyebrow">Overview</p>
            <h2 id="what-title">What is {short_name.lower()}?</h2>
          </div>
          <div class="prose">
{what}
          </div>
{urgent}
        </div>
      </section>""")

    parts.append(f"""      <section class="section section--alt" id="symptoms" aria-labelledby="symptoms-title">
        <div class="shell">
          <div class="section__head">
            <p class="eyebrow">Symptoms</p>
            <h2 id="symptoms-title">Signs and symptoms</h2>
            <p class="lede">
              This is a description, not a checklist to diagnose yourself with.
              Most people will recognise something here at some point. What
              matters clinically is how many are present, how long they have
              lasted and how much they are affecting daily life &mdash; which
              is what an assessment is for.
            </p>
          </div>

          <ul class="conditions">
{check_list(d['symptoms'])}
          </ul>
        </div>
      </section>""")

    parts.append(f"""      <section class="section" id="when" aria-labelledby="when-title">
        <div class="shell">
          <div class="section__head section__head--center">
            <p class="eyebrow">When to seek help</p>
            <h2 id="when-title">When to consult a psychiatrist</h2>
            <p class="lede">
              There is no threshold you have to cross before asking. These are
              the situations where an assessment is usually worth arranging
              rather than waiting.
            </p>
          </div>

          <ul class="conditions">
{check_list(d['when'])}
          </ul>
        </div>
      </section>""")

    parts.append(f"""      <section class="section section--alt" id="treatment" aria-labelledby="treatment-title">
        <div class="shell">
          <div class="section__head">
            <p class="eyebrow">Treatment</p>
            <h2 id="treatment-title">Treatment and management</h2>
            <p class="lede">
              What follows depends entirely on the assessment. Nothing below is
              a treatment plan, and no page can produce one without seeing the
              individual.
            </p>
          </div>

          <div class="cards">
{label_cards(d['treatment'])}
          </div>

          <p class="note note--wide">
            This page names no medicines and no doses, and makes no promise
            about how long anything takes. Screening questionnaires, where they
            are used, are aids to an assessment rather than diagnostic tests.
          </p>
        </div>
      </section>""")

    therapies = therapies_section(d.get("therapies", []))
    if therapies:
        parts.append(therapies)

    parts.append(faq_section(
        d["faqs"],
        f"Common questions about {short_name.lower()} and what to expect from "
        f"a consultation at {CLINIC}, {CITY}.",
    ))

    parts.append(cta_band(
        "Talk to a psychiatrist about this",
        f"{DOCTOR} consults at {CLINIC}, {CITY}. Call the clinic to discuss "
        "your concerns and request an appointment.",
    ))

    parts.append("    </main>")
    og_alt = f"{d['keyword']} with {DOCTOR}"
    return shell(f"{slug}.html", d["title"], d["meta"], og_alt, graph,
                 "\n\n".join(parts))


# ---------------------------------------------------------------------------
# therapy page
# ---------------------------------------------------------------------------


def therapy_page(t: dict) -> str:
    slug = t["page"]
    d = THERAPY_DETAIL[t["key"]]
    url = f"{DOMAIN}/{slug}.html"
    name = t["name"]

    graph = base_graph()
    graph.append(breadcrumb(url, [("Home", ""), ("Therapies", "therapies.html"),
                                  (text(name), f"{slug}.html")]))
    graph.append(webpage_node(url, d["title"], d["meta"], None))
    graph.append(faq_node(url, d["faqs"]))

    tag = ('<span class="tag tag--offered">Offered at the clinic</span>'
           if t["offered"]
           else '<span class="tag">May be recommended or referred</span>')
    availability = (
        "This therapy is provided at the clinic where the assessment indicates "
        "it is appropriate."
        if t["offered"] else
        "This approach may be recommended as part of your care. Where it is "
        "not provided at the clinic itself, a referral can be arranged "
        "&mdash; the consultation will tell you which applies."
    )

    parts = ['    <main id="main">']

    parts.append(page_hero(
        "Therapy",
        name,
        d["intro"],
        extra=f'            <p class="tag-row">{tag}</p>\n',
        second=("i-stetho", "conditions.html", "Conditions we treat"),
    ))

    parts.append(f"""      <section class="section" id="what" aria-labelledby="what-title">
        <div class="shell">
          <div class="section__head">
            <p class="eyebrow">Overview</p>
            <h2 id="what-title">What it is</h2>
          </div>
          <div class="prose">
              <p>{t['what']}</p>
              <p>{t['helps']}</p>
          </div>
        </div>
      </section>""")

    parts.append(f"""      <section class="section section--alt" id="session" aria-labelledby="session-title">
        <div class="shell">
          <div class="section__head">
            <p class="eyebrow">In practice</p>
            <h2 id="session-title">What a session involves</h2>
          </div>
          <div class="prose">
              <p>{d['session']}</p>
          </div>
        </div>
      </section>""")

    parts.append(f"""      <section class="section" id="suits" aria-labelledby="suits-title">
        <div class="shell">
          <div class="section__head">
            <p class="eyebrow">Suitability</p>
            <h2 id="suits-title">Who it tends to suit</h2>
          </div>

          <ul class="conditions">
{check_list(d['suits'])}
          </ul>

          <div class="section__head section__head--sub">
            <h2 id="limits-title">What it does not do</h2>
            <p class="lede">
              Stated plainly, because a page that lists only benefits is an
              advertisement rather than an explanation.
            </p>
          </div>

          <ul class="conditions">
{check_list(d['limits'])}
          </ul>
        </div>
      </section>""")

    used = "\n".join(f"            <li>{icon('i-check-circle')}<span>{u}</span></li>"
                     for u in t["used"])
    parts.append(f"""      <section class="section section--alt" id="used-for" aria-labelledby="used-title">
        <div class="shell">
          <div class="section__head">
            <p class="eyebrow">Commonly used for</p>
            <h2 id="used-title">Conditions this is used in</h2>
          </div>

          <ul class="conditions">
{used}
          </ul>

          <p class="note note--wide">{availability}</p>
        </div>
      </section>""")

    parts.append(faq_section(
        d["faqs"],
        # Drop the bracketed acronym before lowercasing, or the sentence
        # reads "cognitive behavioural therapy (cbt)".
        f"Common questions about {text(name).split(' (')[0].lower()} and how it "
        "fits with the rest of your care.",
    ))

    parts.append(cta_band(
        "Ask whether this approach suits you",
        f"{DOCTOR} consults at {CLINIC}, {CITY}. Call the clinic to request an "
        "appointment and talk through the options.",
    ))

    parts.append("    </main>")
    og_alt = f"{text(name)} in {CITY}"
    return shell(f"{slug}.html", d["title"], d["meta"], og_alt, graph,
                 "\n\n".join(parts))


# ---------------------------------------------------------------------------
# service page
# ---------------------------------------------------------------------------


def service_page(slug: str) -> str:
    d = SERVICE_DETAIL[slug]
    url = f"{DOMAIN}/{slug}.html"

    graph = base_graph()
    graph.append(breadcrumb(url, [("Home", ""), ("Services", "services.html"),
                                  (d["name"], f"{slug}.html")]))
    graph.append(webpage_node(url, d["title"], d["meta"], None))
    graph.append(faq_node(url, d["faqs"]))

    parts = ['    <main id="main">']
    parts.append(page_hero(
        "Services",
        d["keyword"][:1].upper() + d["keyword"][1:],
        d["intro"],
    ))

    for i, (heading, items) in enumerate(d["sections"]):
        alt = " section--alt" if i % 2 == 0 else ""
        hid = f"sec-{i}"
        # Short items read as a list; long ones read as prose. Deciding by
        # length keeps the copy files free of layout instructions.
        as_list = len(items) >= 3 and max(len(x) for x in items) <= 220
        if as_list:
            body = f"""          <ul class="conditions">
{check_list(items)}
          </ul>"""
        else:
            paras = "\n".join(f"              <p>{p}</p>" for p in items)
            body = f"""          <div class="prose">
{paras}
          </div>"""
        parts.append(f"""      <section class="section{alt}" id="{hid}" aria-labelledby="{hid}-title">
        <div class="shell">
          <div class="section__head">
            <h2 id="{hid}-title">{heading}</h2>
          </div>

{body}
        </div>
      </section>""")

    parts.append(faq_section(
        d["faqs"],
        f"Common questions about {d['keyword']} at {CLINIC}.",
    ))

    parts.append(cta_band(
        "Request an appointment",
        f"{DOCTOR} consults at {CLINIC}, {CITY}. Call the clinic to arrange a "
        "time that suits you.",
    ))

    parts.append("    </main>")
    og_alt = f"{d['keyword']} with {DOCTOR}"
    return shell(f"{slug}.html", d["title"], d["meta"], og_alt, graph,
                 "\n\n".join(parts))


# ---------------------------------------------------------------------------
# conditions index
# ---------------------------------------------------------------------------


def condition_card(c: dict) -> str:
    more = ""
    target = cond_target(c)
    if target:
        more = f"""
                <a class="card__more" href="{target}.html">
                  Read about {c['short']}
                  {icon('i-arrow')}
                </a>"""
    return accordion_row(
        c["icon"], c["name"], f"                <p>{c['card']}</p>{more}"
    )


def conditions_main() -> str:
    parts: list[str] = ['    <main id="main">']

    parts.append("""      <section class="section section--tint" id="conditions" aria-labelledby="page-title">
        <div class="shell">
          <div class="section__head section__head--center">
            <p class="eyebrow">Conditions</p>
            <h1 id="page-title">Conditions we assess and treat</h1>
            <p class="lede">
              Psychiatric, neurological, de-addiction and psychosomatic
              concerns seen at the clinic, grouped by the kind of difficulty
              they involve. Persistent sadness, excessive worry, sleep
              difficulties or a change in daily functioning can all be reasons
              to seek support &mdash; none of them on its own means something
              is wrong, and an assessment is what tells you more.
            </p>
            <div class="btn-row btn-row--center btn-row--spaced">
              <a class="btn btn--primary" href="contact.html#appointment">
                """ + icon("i-calendar") + """
                Book an appointment
              </a>
              <a class="btn btn--ghost" href="therapies.html">
                """ + icon("i-leaf") + """
                Therapies offered
              </a>
            </div>
          </div>

""" + emergency_callout() + """

          <ul class="jump" aria-label="Jump to a category">
""" + "\n".join(
        f"""            <li>
              <a href="#{key}">{label}
                <span class="count">{len([c for c in CONDITIONS if c['cat'] == key])}</span>
              </a>
            </li>"""
        for key, label, _ in CATEGORIES
    ) + """
          </ul>
        </div>
      </section>""")

    # All four categories share one <section>. Four separate sections meant
    # four lots of section padding and four full-size section heads, which is
    # most of what made this page a long scroll.
    groups = []
    for key, label, blurb in CATEGORIES:
        members = [c for c in CONDITIONS if c["cat"] == key]
        rows = "\n".join(condition_card(c) for c in members)
        groups.append(f"""          <div class="cat-group" id="{key}">
            <div class="cat-group__head">
              <h2 id="{key}-title">{label}</h2>
              <p>{blurb} &middot; {len(members)} concerns</p>
            </div>

            <div class="accordion">
{rows}
            </div>
          </div>""")

    parts.append("""      <section class="section section--alt" aria-label="Conditions by category">
        <div class="shell">
""" + "\n\n".join(groups) + """
        </div>
      </section>""")

    parts.append("""      <section class="section section--alt" id="note" aria-labelledby="note-title">
        <div class="shell">
          <div class="section__head section__head--center">
            <p class="eyebrow">Please note</p>
            <h2 id="note-title">Reading a list is not a diagnosis</h2>
            <p class="lede">
              The descriptions on this page are written to help you decide
              whether to seek an assessment, not to let you diagnose yourself
              or someone else. Many of these conditions share symptoms, and
              several common physical illnesses can produce the same picture.
              What separates them is a clinical assessment.
            </p>
          </div>

          <p class="note note--wide">
            Availability of a particular service on a given day depends on the
            clinical assessment and the clinic&rsquo;s schedule. Where a
            concern is better managed elsewhere, or needs inpatient care, the
            consultation will say so and a referral can be arranged.
          </p>
        </div>
      </section>""")

    parts.append(
        cta_band(
            "Not sure which of these fits? That is what the consultation is for.",
            f"{DOCTOR} consults at {CLINIC}, {CITY}. Call the clinic to "
            "describe what you are noticing and request an appointment.",
        )
    )

    parts.append("    </main>")
    return "\n\n".join(parts)


# ---------------------------------------------------------------------------
# therapies page
# ---------------------------------------------------------------------------


def therapies_page() -> str:
    slug = "therapies.html"
    url = f"{DOMAIN}/{slug}"
    title = f"Psychotherapy and Counselling in {CITY} | Dr. M. Tirumala Babu"
    desc = (
        "Non-pharmacological treatment approaches in psychiatry — CBT, family "
        "and couple therapy, psychoeducation, motivational interviewing and "
        "more, explained plainly. Guntur."
    )

    faqs = [
        (
            "Is therapy an alternative to medication?",
            "Sometimes, and sometimes not. For some concerns a talking or "
            "behavioural approach is the main treatment; for others medication "
            "is what makes therapy possible in the first place; often the two "
            "are used together. It depends on the condition, its severity and "
            "the individual assessment, so it is not something this page can "
            "answer for you.",
        ),
        (
            "Which of these therapies are available at the clinic?",
            "Cognitive behavioural therapy, family therapy and couple therapy "
            "are offered here. The other approaches described on this page may "
            "be recommended as part of your care, and where they are not "
            "provided at the clinic a referral can be arranged.",
        ),
        (
            "How many sessions will I need?",
            "That is decided case by case. Structured therapies such as CBT are "
            "usually time-limited and reviewed as they go; supportive work may "
            "continue for as long as it is useful. Nobody can give you a number "
            "before an assessment, and any promise of a fixed course of "
            "treatment before then should be treated with caution.",
        ),
        (
            "Can family members be involved?",
            "Yes, and for several conditions it is actively useful. Family "
            "therapy and psychoeducation involve relatives directly. Even in "
            "individual work, family members are often included in explaining "
            "the condition and in planning for difficult periods.",
        ),
        (
            "Is what I say in a session confidential?",
            "Sessions are treated as confidential medical information, in line "
            "with professional practice and applicable law. If you have "
            "questions about what is recorded or shared, you are welcome to ask "
            "at the start.",
        ),
    ]

    graph = base_graph()
    graph.append(
        breadcrumb(url, [("Home", ""), ("Therapies", slug)])
    )
    graph.append(webpage_node(url, title, desc, None))
    graph.append(faq_node(url, faqs))

    def card(t: dict) -> str:
        tag = (
            '<span class="tag tag--offered">Offered at the clinic</span>'
            if t["offered"]
            else '<span class="tag">May be recommended or referred</span>'
        )
        used = "\n".join(f"                  <li>{u}</li>" for u in t["used"])
        # The tag repeats what the section heading already says. It is kept
        # because these rows are linked to directly from the condition pages,
        # and a reader arriving at #cbt never sees the heading.
        return accordion_row(
            t["icon"],
            t["name"],
            f"""                {tag}
                <p>{t['what']}</p>
                <p>{t['helps']}</p>
                <p><b>Commonly used for</b></p>
                <ul>
{used}
                </ul>""",
            row_id=t["key"],
        )

    offered = [t for t in THERAPIES if t["offered"]]
    referred = [t for t in THERAPIES if not t["offered"]]

    main = "\n\n".join(
        [
            '    <main id="main">',
            f"""      <section class="section section--tint" id="overview" aria-labelledby="page-title">
        <div class="shell">
          <div class="section__head section__head--center">
            <p class="eyebrow">Therapies</p>
            <h1 id="page-title">Non-pharmacological therapies</h1>
            <p class="lede">
              Psychiatric care is not only prescriptions. Talking, behavioural
              and family-based approaches are a large part of it &mdash;
              sometimes as the main treatment, sometimes alongside medication,
              and sometimes as what makes stopping medication possible later.
              This page explains the approaches in plain language so you know
              what is being suggested and why.
            </p>
            <div class="btn-row btn-row--center btn-row--spaced">
              <a class="btn btn--primary" href="contact.html#appointment">
                {icon('i-calendar')}
                Book an appointment
              </a>
              <a class="btn btn--ghost" href="conditions.html">
                {icon('i-stetho')}
                Conditions we treat
              </a>
            </div>
          </div>

          <p class="note note--wide">
            Which approach suits you is a clinical decision, not a menu choice.
            No therapy works for every condition, and none of them guarantees
            an outcome. The consultation is where the options, and the reasons
            behind them, are discussed with you.
          </p>
        </div>
      </section>""",
            f"""      <section class="section" id="offered" aria-labelledby="offered-title">
        <div class="shell">
          <div class="section__head">
            <p class="eyebrow">At this clinic</p>
            <h2 id="offered-title">Therapies offered here</h2>
            <p class="lede">
              These are provided at {CLINIC}, {CITY}, where the assessment
              indicates they are appropriate.
            </p>
          </div>

          <div class="accordion">
{chr(10).join(card(t) for t in offered)}
          </div>
        </div>
      </section>""",
            f"""      <section class="section section--alt" id="approaches" aria-labelledby="approaches-title">
        <div class="shell">
          <div class="section__head">
            <p class="eyebrow">Other approaches</p>
            <h2 id="approaches-title">Approaches that may be recommended or referred</h2>
            <p class="lede">
              These are part of psychiatric practice and may form part of your
              care. Where an approach is not provided at the clinic itself, a
              referral can be arranged &mdash; the consultation will tell you
              which applies.
            </p>
          </div>

          <div class="accordion">
{chr(10).join(card(t) for t in referred)}
          </div>
        </div>
      </section>""",
            faq_section(
                faqs,
                "Common questions about therapy, how it fits with medication "
                "and what is available at the clinic.",
            ),
            cta_band(
                "Discuss which approach fits your situation",
                f"{DOCTOR} consults at {CLINIC}, {CITY}. Call the clinic to "
                "request an appointment and talk through the options.",
            ),
            "    </main>",
        ]
    )

    og_alt = f"Non-pharmacological therapies in psychiatry, {CITY}"
    return shell(slug, title, desc, og_alt, graph, main)


# ---------------------------------------------------------------------------
# repairs to the hand-written pages
# ---------------------------------------------------------------------------


def replace_main(raw: str, main: str) -> str:
    start = raw.index('<main id="main">')
    end = raw.index("</main>") + len("</main>")
    indent = raw.rfind("\n", 0, start) + 1
    return raw[:indent] + main + raw[end:]


def replace_jsonld(raw: str, graph: list[dict]) -> str:
    pattern = re.compile(
        r'[ \t]*<script type="application/ld\+json">.*?</script>', re.S
    )
    if not pattern.search(raw):
        # privacy.html shipped without structured data. Give it some.
        return raw.replace("  </head>", jsonld(graph) + "\n  </head>", 1)
    return pattern.sub(lambda _: jsonld(graph), raw, count=1)


def general_faq_section() -> str:
    return faq_section(
        GENERAL_FAQS,
        "Practical questions about consultations, confidentiality, family "
        f"involvement and reaching the clinic in {CITY}.",
    )


def patch_hand_written() -> list[str]:
    """Rewrite the nav and the JSON-LD of the hand-edited pages.

    Four of them carried a malformed graph after the restructure: the FAQPage
    wrapper had been spliced out, leaving a stray brace and a run of orphan
    Question objects. An invalid block is ignored wholesale by search engines,
    so every one of those pages was publishing no structured data at all.
    """
    touched = []
    for name in HAND_WRITTEN:
        path = ROOT / name
        raw = path.read_text(encoding="utf-8")
        before = raw

        raw = apply_nav(raw)

        if name == "services.html":
            raw = replace_region(raw, "servicelist", services_list())

        if name in H1_PROMOTE:
            # Rewrite the open and close tags together, in one substitution
            # anchored on the <h2> itself. An earlier version opened the tag
            # and then hunted for the next </h2> separately, which on a second
            # run walked past the real end of the heading and closed some
            # other section's <h2> with </h1>. Matching the pair at once is
            # also idempotent: once the heading is an <h1>, this finds nothing.
            hid = H1_PROMOTE[name]
            raw = re.sub(
                rf'<h2 id="{hid}">(.*?)</h2>',
                rf'<h1 id="{hid}">\1</h1>',
                raw,
                count=1,
                flags=re.S,
            )

        url = f"{DOMAIN}/" if name == "index.html" else f"{DOMAIN}/{name}"
        graph = base_graph()
        if name != "index.html":
            title = re.search(r"<title>(.*?)</title>", raw, re.S).group(1).strip()
            desc = re.search(
                r'<meta\s+name="description"\s+content="([^"]*)"', raw, re.S
            )
            if desc is None:
                desc = re.search(
                    r'name="description"\s*\n\s*content="([^"]*)"', raw, re.S
                )
            graph.append(
                breadcrumb(url, [("Home", ""), (text(title).split("|")[0].strip(), name)])
            )
            graph.append(
                webpage_node(url, title, desc.group(1) if desc else title, None)
            )

        # contact.html carries the five general FAQs, so it carries the schema.
        if name == "contact.html":
            graph.append(faq_node(url, GENERAL_FAQS))
            if "<details>" not in raw:
                marker = '      <section class="cta-band"'
                if marker in raw:
                    raw = raw.replace(
                        marker, general_faq_section() + "\n\n" + marker, 1
                    )

        raw = replace_jsonld(raw, graph)

        if raw != before:
            path.write_text(raw, encoding="utf-8")
            touched.append(name)
    return touched


# ---------------------------------------------------------------------------
# sitemap
# ---------------------------------------------------------------------------


def rebuild_sitemap(pages: list[str]) -> None:
    path = ROOT / "sitemap.xml"
    date = re.search(r"<lastmod>([^<]+)</lastmod>", path.read_text(encoding="utf-8"))
    lastmod = date.group(1) if date else "2026-09-20"
    entries = []
    for name, priority, freq in pages:
        loc = f"{DOMAIN}/" if name == "index.html" else f"{DOMAIN}/{name}"
        entries.append(
            f"  <url>\n"
            f"    <loc>{loc}</loc>\n"
            f"    <lastmod>{lastmod}</lastmod>\n"
            f"    <changefreq>{freq}</changefreq>\n"
            f"    <priority>{priority}</priority>\n"
            f"  </url>"
        )
    path.write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(entries)
        + "\n</urlset>\n",
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------


def main() -> int:
    written: list[str] = []

    # 1. the hand-written pages: nav + structured data
    touched = patch_hand_written()
    for name in touched:
        print(f"  patched  {name}")

    # 2. conditions.html — head stays, <main> is regenerated
    path = ROOT / "conditions.html"
    raw = apply_nav(path.read_text(encoding="utf-8"))
    raw = replace_main(raw, conditions_main())
    url = f"{DOMAIN}/conditions.html"
    graph = base_graph()
    graph.append(breadcrumb(url, [("Home", ""), ("Conditions", "conditions.html")]))
    graph.append(
        webpage_node(
            url,
            re.search(r"<title>(.*?)</title>", raw, re.S).group(1).strip(),
            re.search(r'content="([^"]*)"\s*\n?\s*/>\s*\n\s*<meta name="theme-color"', raw, re.S).group(1)
            if re.search(r'content="([^"]*)"\s*\n?\s*/>\s*\n\s*<meta name="theme-color"', raw, re.S)
            else "",
            None,
        )
    )
    raw = replace_jsonld(raw, graph)
    path.write_text(raw, encoding="utf-8")
    written.append("conditions.html")
    print("  rebuilt  conditions.html")

    # 3. therapies.html
    (ROOT / "therapies.html").write_text(therapies_page(), encoding="utf-8")
    written.append("therapies.html")
    print("  built    therapies.html")

    # 4. one page per condition — the long template where content_detail.py
    #    has it, the short one otherwise
    for c in CONDITIONS:
        slug = cond_target(c)
        if not slug:
            print(f"  ! {c['name']} has no copy yet — no page, and nothing links to it")
            continue
        body = condition_page(slug) if slug in DETAIL else short_condition_page(slug)
        (ROOT / f"{slug}.html").write_text(body, encoding="utf-8")
        written.append(f"{slug}.html")
        print(f"  built    {slug}.html")

    # 5. one page per therapy
    for t in THERAPIES:
        slug = therapy_target(t)
        if not slug:
            continue
        (ROOT / f"{slug}.html").write_text(therapy_page(t), encoding="utf-8")
        written.append(f"{slug}.html")
        print(f"  built    {slug}.html")

    # 6. the three services that are a service rather than a condition
    for slug in SERVICE_DETAIL:
        (ROOT / f"{slug}.html").write_text(service_page(slug), encoding="utf-8")
        written.append(f"{slug}.html")
        print(f"  built    {slug}.html")

    # 7. sitemap
    sitemap_pages = [
        ("index.html", "1.0", "monthly"),
        ("about.html", "0.8", "yearly"),
        ("services.html", "0.8", "monthly"),
        ("conditions.html", "0.8", "monthly"),
        ("therapies.html", "0.8", "monthly"),
        ("contact.html", "0.9", "monthly"),
        ("privacy.html", "0.3", "yearly"),
    ]
    sitemap_pages += [(f"{s}.html", "0.8", "monthly") for s in SERVICE_DETAIL]
    sitemap_pages += [
        (f"{cond_target(c)}.html", "0.7", "yearly")
        for c in CONDITIONS if cond_target(c)
    ]
    sitemap_pages += [
        (f"{therapy_target(t)}.html", "0.6", "yearly")
        for t in THERAPIES if therapy_target(t)
    ]
    rebuild_sitemap(sitemap_pages)
    print("  rebuilt  sitemap.xml")

    print(f"\n{len(written)} page(s) generated. Now run: python tools/audit.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
