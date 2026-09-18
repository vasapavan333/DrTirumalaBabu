# Working in this repo

Single-page website for a psychiatrist's practice. Plain HTML/CSS/JS — hand
written, no generator, no build step, no npm.

## Where things live

| Change | File |
| --- | --- |
| Any copy, phone number, service, condition, FAQ | `index.html` |
| Colours, type scale, spacing, components | `assets/css/site.css` (tokens in `:root`) |
| Nav, scroll-spy, reveal, map facade, form | `assets/js/site.js` |
| Portrait, clinic photos, icons, share card | `tools/prepare_images.py` (sources in `Images/`) |
| Webfont subsets | `tools/build_fonts.py` (upstream files in `tools/fonts-src/`) |
| Clinic mark | `tools/prepare_logo.py` (source `Images/logo-source.png`) |
| Provisional values and launch blockers | `TODO-CONTENT.md` |

Unlike the Siva Sakthi project, there is **no `content.py` and no generator** —
`index.html` is the source, edit it directly.

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
If copy gained unusual characters: `python tools/build_fonts.py` too — the
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
- The FAQ answers exist twice: as visible copy and inside the `FAQPage` JSON-LD.
  Edit both, or the audit's JSON stays valid while the structured data lies.
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
- The Google Map stays a **click-to-load facade**. Do not replace it with an
  always-loaded iframe.
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

## Telugu

Service and condition cards carry Telugu subtitles taken from the clinic's own
posters (`Images/poster-*.jpg`). Copy the wording from the poster rather than
translating fresh — the poster's phrasing is what patients in Guntur recognise.
They render through `--font-te` (Noto Sans Telugu / Nirmala UI), which ships
with Windows and Android; no webfont is loaded.
