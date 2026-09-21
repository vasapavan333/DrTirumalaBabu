# Working in this repo

Website for a psychiatrist's practice. Plain HTML/CSS/JS — no framework, no
npm, no bundler. 43 pages.

**Two kinds of page, and the difference matters:**

| | Pages | Edit by |
| --- | --- | --- |
| Hand-written | `index`, `about`, `services`, `contact`, `privacy` | editing the `.html` directly |
| Generated | `conditions`, `therapies`, and the 36 detail pages (22 conditions, 11 therapies, 3 services) | editing `tools/content_*.py`, then `python tools/build_pages.py` |

Editing a generated page's HTML by hand works until the next build, and then it
is gone. `conditions.html` is a hybrid: its `<head>` is hand-written, its
`<main>` is regenerated.

`tools/build_pages.py` also owns several regions of the hand-written pages, and
rewrites them on every run:

- the **JSON-LD block** on every page. `base_graph()` reads the site-wide
  nodes out of `index.html`, so the clinic's address, phone numbers and
  opening hours have exactly one home: edit them in `index.html` and rebuild.
- the **primary nav and the mobile panel**, including the three dropdowns.
- the **services accordion** inside `services.html`.

Those regions are wrapped in `<!-- nav:start -->` / `<!-- nav:end -->` style
markers. Edit inside a marked region and the next build discards it; edit the
Python instead.

**A slug does not make a page.** `PAGE_EXISTS` in `build_pages.py` is the set
of slugs that have copy, and every link decision consults it. Add a slug in
`content_pages.py` without copy and you get no page and no link to it — which
is deliberate, so the audit never sees a dead internal link mid-way through
adding something.

## Where things live

| Change | File |
| --- | --- |
| Homepage, About, Services, Contact copy | the `.html` file itself |
| A condition's card, its Telugu subtitle, the category it sits in | `tools/content_pages.py` |
| A therapy, or whether it is offered at the clinic | `tools/content_pages.py` |
| Which service links to its own page and which to a condition | `tools/content_pages.py` → `SERVICES` |
| The long-form copy of a condition page (10 sections) | `tools/content_detail.py` |
| The short copy of a condition page (5 sections) | `tools/content_short.py` |
| A therapy page | `tools/content_therapy.py` |
| A service page | `tools/content_service.py` |
| The site-wide FAQs (shown on `contact.html`) | `tools/content_pages.py` → `GENERAL_FAQS` |
| Clinic address, phones, hours, geo — anywhere in schema | `index.html` JSON-LD, then rebuild |
| Header / footer / sprite used by generated pages | `tools/chrome/*.html` |
| Colours, type scale, spacing, components | `assets/css/site.css` (tokens in `:root`) |
| Nav, scroll-spy, reveal, map facade, form | `assets/js/site.js` |
| Portrait, clinic photos, icons, share card | `tools/prepare_images.py` (sources in `Images/`) |
| Webfont subsets | `tools/build_fonts.py` (upstream files in `tools/fonts-src/`) |
| Clinic mark | `tools/prepare_logo.py` (source `Images/logo-source.png`) |
| Provisional values and launch blockers | `TODO-CONTENT.md` |

## After editing content

```bash
python tools/build_pages.py   # only if you touched tools/content_*.py or chrome/
python tools/audit.py         # always
```

## After any change

```bash
python tools/audit.py
```

Must print `no problems found`. It checks per-page SEO tags, title/description
uniqueness and length, heading hierarchy, image alt text and dimensions, form
labelling, internal links and anchors, missing local assets, JSON-LD validity,
sitemap coverage, banned marketing claims, and remaining launch placeholders.

If images changed: `python tools/prepare_images.py` first. If the logo changed,
`python tools/prepare_logo.py` before that — the favicons and the share card
are built from its output.
If copy gained an unusual character: `python tools/build_fonts.py` too — the
audit will not catch a missing glyph, but a tofu box on the page will.

Preview over http (`preview.cmd`, or `python -m http.server 4181`), never
`file://` — browsers block webfonts on `file://` and the page silently falls
back to system faces.

## Content constraints

This is a medical site for a real doctor. Some things are deliberately absent
rather than filled in:

- **Never invent testimonials, patient numbers, success rates, awards or years
  of experience.** No reviews section exists on purpose.
- **Never write copy that guarantees an outcome**, and never use superlatives
  ("best psychiatrist in Guntur", "No. 1", "100% recovery"). The audit fails the
  build on these.
- **Unverified facts get labelled, not stated.** The registration number carries
  "As provided by the clinic; pending independent verification" — remove that
  line only once it is actually verified.
- FAQ answers are written once, in Python, and the build emits both the visible
  `<details>` copy and the `FAQPage` JSON-LD from that one source. Do not
  hand-edit either copy in the HTML — they will drift, and a page that says one
  thing to a reader and another to a search engine is the failure mode this
  arrangement exists to prevent.
- **No page may let a reader diagnose themselves.** Every symptom list carries
  the "this is a description, not a checklist" framing, causes are always
  contributors rather than *the* cause, screening questionnaires are described
  as aids to assessment and never as tests, and no page names a medicine or a
  dose. These rules are restated at the top of `tools/content_pages.py`.
- **A therapy is only described as offered at the clinic when that is
  confirmed.** Today that is CBT, family therapy and couple therapy, which
  appear on the clinic's own poster; everything else says "may be recommended
  or referred".
- Emergency numbers (112, 108, Tele-MANAS 14416) are real and load-bearing.
  Verify before changing.

## Design and performance constraints

- **No frameworks, no icon fonts, no CDN scripts, no third-party anything.**
  Icons are one inline SVG sprite at the top of `index.html`. Fonts are
  self-hosted and subset in `assets/fonts/` — never swap them for a Google
  Fonts `<link>`. Keeping the critical path near 200 KB uncompressed is the
  point of the stack.
- **The design is warm editorial**: Newsreader for display, Inter for text,
  ivory/sand surfaces, brass hairlines, navy-tinted shadows, the arched
  portrait. Every colour, size, radius and shadow is a token in the `:root`
  block — change the token, not the rule. Do not introduce a cool grey
  (`#f5f8fb` and friends); it fights the ivory and the page goes clinical.
- **The primary nav has three dropdowns**, opened by `:hover` and
  `:focus-within` and not by a script. The top-level item stays an ordinary
  link to the full page, which is what a tap does on a touch screen and what a
  crawler follows. `.nav__menu::before` is an invisible strip bridging the gap
  between the link and the panel — without it the menu closes before the
  pointer arrives. The desktop nav starts at **1150px**, not 1100: six items,
  three carets and the CTA do not fit below that with usable spacing.
- **Services, conditions and therapies are accordion lists, not card grids.**
  Each item is a `<details>` row (`.accordion` in section 23 of the CSS) —
  plain HTML, no JavaScript, so the rows still open if a script fails and
  find-in-page can expand them. Several may be open at once; do not add a
  script that closes the others. The `<h3>` lives inside the `<summary>` so a
  screen reader's heading list still enumerates every item while the rows are
  closed, and so the condition names stay indexable.
- **The site is English only.** Telugu subtitles and a Telugu translation layer
  both existed and were both removed at the client's request in September 2026,
  along with the Noto Sans Telugu webfont. Do not reintroduce either without
  asking — and if Telugu ever comes back, `tools/build_fonts.py` needs its face
  restored too, or every Telugu character renders as an empty box.
- The Google Map stays a **click-to-load facade**. Do not replace it with an
  always-loaded iframe.
- **`tools/prepare_images.py` cannot rebuild the hero portrait.** The source
  in `Images/` is not the photo it was built from, so the step refuses and
  keeps the published file. Do not delete `assets/img/doctor-tirumala-babu*` —
  they cannot be regenerated. TODO-CONTENT.md §14 has the fix.
- Every `<img>` needs `alt`, `width` and `height`. Below-the-fold images need
  `loading="lazy"`; the hero portrait is preloaded and must not be lazy.
- Scroll reveals are gated on `prefers-reduced-motion` and have a 4-second
  failsafe in `site.js`. Keep both — content must never be able to stay
  invisible.
- Animate transform and opacity only.

## Brand

The site's name is **Dr. Tirumala Babu's Psychiatry Clinic**; the doctor's own
name is **Dr. Manchikalapudi Tirumala Babu**. Both are correct and neither
replaces the other — the clinic name is the brand in the header, footer, share
card and manifest; the doctor's full name is what appears in the hero card, the
About section, the contact panel and the `Physician` schema. The venue is
Maruthi Hospital and Diagnostics, and the `MedicalClinic` schema keeps that
name; do not rename it to the clinic brand, because the hospital is a real
separate entity.

The strapline is "Compassionate care for a healthier mind and a happier life".

