# Dr. Tirumala Babu's Psychiatry Clinic

*Compassionate care for a healthier mind and a happier life.*

Single-page website for the psychiatry practice of **Dr. Manchikalapudi
Tirumala Babu**, M.B.B.S., M.D. (Psychiatry), at **Maruthi Hospital and
Diagnostics**, M.G. Inner Ring Road, Phase-II, Guntur.

Plain HTML, CSS and JavaScript. No framework, no npm, no build step, no runtime
dependency. Double-click **`preview.cmd`** to view it locally (see
[Local preview](#local-preview) — opening `index.html` straight from Explorer
silently drops the web fonts).

---

## Before it goes live

Read **[TODO-CONTENT.md](TODO-CONTENT.md)** first. It lists every value that is
provisional — the domain placeholder, the registration number, the consulting
hours, the experience line — with the exact file and constant to change.

The single most important one: replace `drtirumalababu.com` with the
real domain in `index.html`, `privacy.html`, `sitemap.xml` and `robots.txt`.
`tools/audit.py` counts the remaining occurrences on every run.

---

## Layout

```
index.html              the whole site — 11 sections
privacy.html            privacy policy (linked from the footer)
preview.cmd             double-click to preview properly (see below)
assets/css/site.css     one stylesheet, tokens at the top
assets/js/site.js       nav, scroll-spy, reveal, click-to-load map, form
assets/fonts/           self-hosted, subset webfonts
assets/img/             generated web images (WebP + JPEG/PNG pairs)
Images/                 original client files — source only, not served
tools/prepare_logo.py   keys the clinic mark out of the supplied file
tools/prepare_images.py regenerates everything else in assets/img/
tools/build_fonts.py    re-subsets the fonts in assets/fonts/
tools/audit.py          pre-flight checks; must print "no problems found"
favicon.ico  sitemap.xml  robots.txt  site.webmanifest
```

## Editing

- **Copy, phone numbers, hours, services, conditions, FAQs** — `index.html`.
  It is hand-written and readable; each section is delimited by a comment
  banner (`<!-- ===== services ===== -->`).
- **Design** — `assets/css/site.css`. Every colour, font size, radius and
  spacing step is a custom property in the `:root` block at the top; change a
  token there rather than a rule further down.
- **Behaviour** — `assets/js/site.js`.
- **Images** — drop new originals into `Images/`, then run
  `python tools/prepare_images.py`. The doctor's portrait comes from
  `Images/DoctorProfile.jpg`; to swap it, replace that file and adjust
  `PORTRAIT_TRIM` / `PORTRAIT_FOCUS` at the top of the script.
- **Fonts** — after adding copy with unusual characters, run
  `python tools/build_fonts.py` so the subset still covers every glyph.
- **The logo** — `Images/logo-source.png` is the file the clinic supplied.
  `python tools/prepare_logo.py` produces the transparent `assets/img/logo.*`,
  and `prepare_images.py` then builds the favicons and the share card from
  them, so **run prepare_logo.py first** if both need rebuilding.

After any change:

```bash
python tools/audit.py
```

It must print `no problems found`. It checks per-page SEO tags, title and
description uniqueness and length, heading hierarchy, image alt text and
dimensions, form labelling, internal links and anchors, missing local assets,
JSON-LD validity, sitemap coverage, and it fails the build on marketing
superlatives ("best psychiatrist", "100% recovery", "guaranteed results") or a
visible launch placeholder.

## Local preview

**Double-click `preview.cmd`.** It serves the folder at
<http://localhost:4181/> and opens your browser.

Do not open `index.html` directly from Explorer. Browsers refuse to load web
fonts from a `file://` page, so you would see fallback typefaces instead of
Newsreader and Inter, and the Telugu subtitles may not render. Everything else
works either way — it is only the fonts — but the page looks wrong enough to be
misleading. On a real web host this does not apply.

The command-line equivalent is `python -m http.server 4181`.

## Deploying

Copy everything **except** `tools/` and `Images/` to the web root. Any static
host works: GitHub Pages, Netlify, Cloudflare Pages, Hostinger, plain nginx.
Serve over HTTPS.

---

## Brand

The lockup is the clinic mark plus the name and strapline, in the header, the
footer and the share card:

> **Dr. Tirumala Babu's Psychiatry Clinic**
> COMPASSIONATE CARE FOR A HEALTHIER MIND AND A HAPPIER LIFE

The strapline is 57 characters and must stay on one line, so it only appears in
the header at 1260px and above; below that the clinic name carries it alone,
and the full lockup still shows in the footer. On the navy footer the mark sits
on a white disc, because its charcoal orbit otherwise disappears into the
background.

The file the clinic supplied was a flattened screenshot — its transparency was
a grey-and-white checkerboard painted into the pixels, with a faint pale-blue
circle around the mark. `tools/prepare_logo.py` rebuilds it properly: teal and
charcoal come from colour thresholds, the white figure is separated from the
identically-white checkerboard squares by area (the squares are 25px and get
labelled individually under 4-connectivity; the figure is thousands of pixels),
and the faint circle is dropped because at 44px it only reads as noise. The
result is a genuinely transparent PNG/WebP that sits cleanly on white, ivory
and navy.

## Design

**Warm editorial.** The page reads as paper rather than as a screen: ivory
`#fbf8f3` and sand `#f4eee4` surfaces instead of cool blue-grey, brass `#b08a45`
hairlines, navy-tinted shadows (black on ivory goes grey and dead), and the
portrait in a tall arch that is echoed in the decorative shapes around it.

| Role | Value |
| --- | --- |
| Primary | navy `#102a44`, deepening to `#0a1a2c` |
| Secondary | teal `#0e7d8a` |
| Accent (CTA only) | clay `#b8540f` |
| Hairlines, numerals | brass `#b08a45` |
| Surfaces | white, ivory `#fbf8f3`, sand `#f4eee4` |

The palette starts from the clinic's own print material and is deepened for
screen contrast — the poster's bright orange only reached 3.2:1 against white
text, so the accent was darkened until it cleared 4.87:1. Every text/background
pairing on the site is measured and passes WCAG AA.

**Typography** is [Newsreader](https://fonts.google.com/specimen/Newsreader) for
display and [Inter](https://fonts.google.com/specimen/Inter) for text, with
Noto Sans Telugu for the Telugu subtitles. All three are self-hosted in
`assets/fonts/` and subset to the characters this site actually uses, so there
is no Google Fonts request, nothing to track visitors with, and the page works
offline. `tools/build_fonts.py` rebuilds them:

```
newsreader-display.woff2   56.7 KB -> 33.3 KB
inter-text.woff2           47.1 KB -> 23.7 KB
noto-telugu.woff2         121.1 KB -> 11.2 KB   (subset + weight pinned)
```

Both Latin faces are preloaded because they paint above the fold. The Telugu
face is `unicode-range` gated, so it never blocks anything.

## Performance

The critical path — HTML + CSS + JS + both Latin fonts + the hero portrait — is
about **199 KB uncompressed**. The fonts are already compressed, and gzip takes
the rest down hard, so it lands near 105 KB over the wire. What keeps it there:

- No framework, no jQuery, no icon font. Icons are one inline SVG sprite.
- Fonts are self-hosted, subset, and `font-display: swap`.
- Images are WebP with JPEG fallbacks, sized to their display box, with
  `width`/`height` on every tag so nothing shifts as they load.
- The hero portrait is preloaded; everything below the fold is `loading="lazy"`.
- The Google Map is a **click-to-load facade** — the iframe is only requested
  when a visitor asks for the map, so the page never pays for a third-party
  frame on first load.
- `site.js` is `defer`red, and the page is fully readable without it.

## Accessibility

- Skip link, one `<h1>`, no skipped heading levels.
- Every image has descriptive alt text; decorative SVG is `aria-hidden`.
- Every form control has a `<label>`; the submit result is announced via
  `role="status"`.
- Visible focus ring on every interactive element.
- Call and appointment buttons are at least 48 px tall.
- The FAQ uses native `<details>`/`<summary>` — it works with JavaScript off.
- `prefers-reduced-motion: reduce` disables every transition and the scroll
  reveal; reveals also have a 4-second failsafe so content can never stay
  invisible.

## SEO

Unique title and meta description, canonical, Open Graph and Twitter card, and
a 1200×630 share card. Structured data (JSON-LD): `Physician` with
qualifications and address, `MedicalClinic` with the full NAP and opening hours,
and `FAQPage` matching the on-page questions. Copy targets local intent
naturally — psychiatrist in Guntur, psychiatry consultation, depression and
anxiety treatment, de-addiction support — without superlatives.

## Content rules this site follows

These are deliberate, and `tools/audit.py` enforces the last one:

- No invented testimonials, patient counts, success rates or awards.
- No outcome guarantees. Existing copy says outcomes vary and no result is
  promised — keep that register.
- No superlatives ("best psychiatrist in Guntur", "No. 1", "100% recovery").
- Unverified details are labelled as such rather than stated as fact — see the
  registration number line in the About section.
- The emergency callout carries real, current numbers: 112, 108, and Tele-MANAS
  (14416 / 1-800-891-4416), the Government of India's 24×7 mental health
  helpline.
