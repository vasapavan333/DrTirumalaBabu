# Content & service enhancement — 20 September 2026

Neuropsychiatric consultant brief. What changed, what to test, what is still
outstanding.

---

## 1. Files

### New pages

| File | What it is |
| --- | --- |
| `therapies.html` | Eleven non-pharmacological approaches. Split into "offered here" (CBT, family, couple) and "may be recommended or referred" (the rest). |
| `depression-treatment-guntur.html` | Full ten-section condition page. |
| `anxiety-treatment-guntur.html` | Full ten-section condition page. |
| `alcohol-de-addiction-guntur.html` | Full ten-section condition page, plus a withdrawal safety callout. |

### New tooling

| File | What it is |
| --- | --- |
| `tools/build_pages.py` | Generates the pages above, rebuilds `conditions.html`'s body, and owns the JSON-LD and the Therapies nav item on **every** page. |
| `tools/content_pages.py` | Source of truth: 4 categories, 22 conditions, 11 therapies, the 5 site-wide FAQs. |
| `tools/content_detail.py` | The long-form copy for the three condition pages. |
| `tools/chrome/*.html` | Header, footer, icon sprite and floating buttons, extracted once so the generated pages cannot drift from the hand-written ones. |

### Changed

| File | What changed |
| --- | --- |
| `conditions.html` | Rebuilt: 22 conditions in 4 categories as cards with Telugu subtitles, replacing the flat list of 9. |
| `index.html` | Title now reads *Neuropsychiatric Consultant*; meta description shortened to fit; Therapies in the nav. |
| `about.html` | Same title change; lead heading promoted to `<h1>`; description shortened. |
| `services.html` | New `<h2>` above the service grid so the page has a heading hierarchy; lead heading promoted to `<h1>`; description shortened. |
| `contact.html` | Lead heading promoted to `<h1>`; the five general FAQs restored as a visible accordion with matching schema. |
| `privacy.html` | Gained structured data (it had none). |
| `assets/css/site.css` | Two new component sections (condition/therapy pages, and the six-item header), a contrast fix, and a colour token darkened. |
| `assets/fonts/noto-telugu.woff2` | Re-subset to cover the new Telugu subtitles. |
| `sitemap.xml` | Ten pages, was two. |
| `tools/audit.py`, `tools/build_fonts.py` | Now walk every page rather than a hard-coded pair. |
| `CLAUDE.md`, `TODO-CONTENT.md` | Updated for the generator and the new launch blockers. |

---

## 2. Two defects found and fixed along the way

**Broken structured data on four pages.** `about.html`, `services.html`,
`conditions.html` and `contact.html` each carried an identical malformed
JSON-LD block — the `FAQPage` wrapper had been spliced out during the
multi-page restructure, leaving a stray brace and a run of orphaned `Question`
objects. Invalid JSON-LD is discarded wholesale, so those four pages were
publishing **no** structured data at all: no physician, no clinic, no address,
no opening hours. All ten pages now emit a valid graph from one source.

**Three pages had no `<h1>`.** `about`, `services` and `contact` led with an
`<h2>`, left over from the single-page layout. Their lead headings are now
`<h1>`; the visible copy is unchanged.

---

## 3. Testing checklist

Serve over http — `preview.cmd`, or `python -m http.server 4181` — never by
double-clicking a file, because browsers block webfonts on `file://`.

### Automated (already run, all green)

```
python tools/audit.py          -> no problems found
python tools/build_pages.py    -> regenerates cleanly
```

The audit covers all ten pages: SEO tags, title and description uniqueness and
length, one `<h1>` per page and no skipped heading levels, image alt text and
dimensions, form labelling, internal links and anchors, missing local assets,
JSON-LD validity, sitemap coverage, banned marketing claims, launch
placeholders.

Also verified here, with a headless browser:

- No horizontal scroll at 1440 / 1100 / 900 / 390 px on any page.
- Header fits at every width from 1000 px to 2560 px, in 20 px steps — the
  sixth nav item needed a spacing adjustment between 1100 px and 1440 px.
- All body text meets WCAG AA contrast. Three genuine misses were fixed: the
  WhatsApp button (4.43:1), the footer disclaimer (4.29:1) and the footer
  credit (3.77:1).
- Every section stays visible with JavaScript disabled.
- All 22 internal links resolve; FAQ accordions toggle; the mobile menu opens
  and contains the Therapies link.
- Every Telugu character on every page exists in the font subset.

### To check by hand

- [ ] **Read the medical copy.** Nothing has been reviewed by the doctor. See
      `TODO-CONTENT.md` §11 for exactly which file holds which text.
- [ ] Confirm the alcohol withdrawal warning is phrased as the clinic wants it.
- [ ] Confirm only CBT, family and couple therapy are offered at the clinic —
      that is what `therapies.html` currently states, based on the poster.
- [ ] Confirm the doctor is happy that marketing copy says *Neuropsychiatric
      Consultant* while the schema and credential lines keep *Consultant
      Psychiatrist* (the registered qualification).
- [ ] Open `conditions.html` on a phone and check the Telugu subtitles render
      as Telugu, not as boxes.
- [ ] Tap through the three condition pages on a phone: hero buttons, the
      "About this therapy" links, the FAQ accordion, the bottom CTA.
- [ ] Check the appointment form on `contact.html` still submits as before.

---

## 4. Still outstanding

1. **The domain.** `drtirumalababu.com` is still in every page, the
   sitemap, robots.txt, and in `DOMAIN` at the top of `tools/build_pages.py`.
   Nothing about canonicals, sharing or search indexing works until it is set.
2. **Opening time conflict.** The Google Business Profile says 5:30 PM; the
   poster and the site say 6:00 PM. Unresolved.
3. **No website set on the Google listing.** The highest-value free local-SEO
   step once the site is live.
4. **Medical review.** See above — this is the blocker that matters most.
5. **Nineteen condition pages** still render as cards without a page.
   `TODO-CONTENT.md` §12 has the recipe for adding one.
