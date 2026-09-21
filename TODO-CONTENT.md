# Before launch — provisional content

Everything here is either a placeholder, or real information taken from the
clinic's print material that has not been confirmed for the website. Each entry
says exactly where to change it.

Run `python tools/audit.py` after each change.

---

## 1. Domain — blocks launch

`drtirumalababu.com` appears across every page. Nothing about
canonicals, sharing or the sitemap works until it is replaced.

| File | What |
| --- | --- |
| all ten `.html` pages | canonical, `og:url`, `og:image`, `twitter:image`, and the `@id`/`url`/`image` fields inside the JSON-LD block |
| `sitemap.xml` | every `<loc>` entry |
| `robots.txt` | the `Sitemap:` line |

The generated pages take the domain from `DOMAIN` at the top of
`tools/build_pages.py`. Change it there as well, or the next build puts the
placeholder back.

Fastest way, once the domain is known:

```bash
grep -rl 'drtirumalababu.com' . --exclude-dir=tools --exclude-dir=Images \
  | xargs sed -i 's#https://drtirumalababu.com#https://your-real-domain.in#g'
```

Then update the `<!-- TODO -->` comments that mention it and re-run the audit —
it will report 0 placeholders.

---

## 2. Medical registration number — confirm

**Currently shown**, in the About section's qualification card, labelled:

> Medical registration no. 103992
> *As provided by the clinic; pending independent verification.*

Source: the Maruthi Hospital poster. The brief said to display it as verified
only once independently confirmed, so the caveat is on the page.

- **If confirmed against the state medical council / NMC register:** delete the
  `<small>` line inside that `<li>` in `index.html` (About section,
  `class="about__quals"`).
- **If it cannot be confirmed:** delete the whole `<li>`.

---

## 3. Years of experience — supplied but not published

The brief gives "2 Years Experience Overall" and says to publish it only once
confirmed and approved. It is therefore **commented out**, not deleted, in
`index.html` — search for `2 years of overall clinical experience`. Uncomment
the `<p>` to publish it.

---

## 4. Consulting hours — from the poster, confirm

**Currently shown as** Monday to Saturday, 6:00–9:00 PM, in five places:

- hero badge over the portrait
- the card under the About portrait
- the appointment CTA band
- the contact panel
- the footer

…and as `openingHoursSpecification` (`opens: 18:00`, `closes: 21:00`) in the
JSON-LD. Source: the Maruthi Hospital poster. If the hours differ, or if Sunday
or emergency slots exist, change all five plus the JSON-LD.

> **Conflict — resolve this one.** The clinic's own Google Business Profile
> says the place **opens at 5:30 PM**, not 6:00 PM. The poster and this website
> both say 6:00 PM. One of the two is wrong and patients use both. Confirm
> which is right, then fix whichever source is out of date — and remember the
> Google listing is edited in the Business Profile, not here.

---

## 5. Phone numbers — from the poster, confirm

| Number | Used as |
| --- | --- |
| **+91 89850 14488** | primary — every `tel:` link, the WhatsApp number (`918985014488` in `assets/js/site.js` and in the `wa.me` links), JSON-LD `telephone` |
| +91 89850 14411 | listed in contact panel and footer |
| +91 98664 83883 | listed in contact panel and footer |

**Confirm that 89850 14488 is the number that actually receives WhatsApp.** If
it is a different number, change `WHATSAPP_NUMBER` at the top of
`assets/js/site.js` and the three `wa.me/918985014488` links in `index.html`.

---

## 6. Email address — missing

There is no clinic email on the site, because none was supplied. If one exists,
add it to the contact panel's `info-list` and to the `MedicalClinic` JSON-LD.

---

## 7. Map coordinates — done, resolved from the clinic's Google listing

Taken from the Google Business Profile **Maruthi Hospital (Dr. Manchikalapudi
Tirumala Babu)**, a psychiatric hospital in Gorantla:

| | |
| --- | --- |
| Coordinates | `16.3358998, 80.4342868` |
| Google place link | `https://maps.google.com/?cid=17433443079466313291` |
| Feature ID | `0x3a358bd607e76f0d:0xf1f0081d4b94e64b` |
| Google's address | Phase-2, Maruthi Hospital, Mahatma Gandhi Inner Ring Rd, opposite Ushodaya super Market, Gorantla, Andhra Pradesh 522034 |

In use: the `data-map` embed on `.map-facade`, both *Get directions* buttons
(`maps/dir/?api=1&destination=...`), and a `geo` + `hasMap` block on the
`MedicalClinic` JSON-LD. "Gorantla" has been added to the address on the page
and in the schema, because that is the locality Google files the place under
and how map apps will match it.

**Two things to action on the Google listing itself:**

- It currently has **no website**. Once the domain is live, add it to the
  Business Profile — it is the single highest-value local SEO step available,
  and it is free.
- The listing has 3 reviews at 5.0. That is **not** shown on this site, per the
  no-statistics rule in section 10. If the doctor wants it, it needs to be a
  live rating rather than a number typed into the HTML, or it will go stale.

---

## 8. Doctor's portrait — done, confirm it is the approved image

The hero, About, avatar and share-card portraits are all generated from
**`Images/DoctorProfile.jpg`**, the studio headshot. The poster crop that was
used before is gone from the site; the code path still exists as a fallback
(set `PORTRAIT_SOURCE = None` in `tools/prepare_images.py`).

Still worth confirming: that this is the image the doctor wants published. To
swap it, replace `Images/DoctorProfile.jpg`, adjust `PORTRAIT_TRIM` (it strips
the white padding down the right-hand side of the current file) and
`PORTRAIT_FOCUS` if the framing needs it, then run
`python tools/prepare_images.py`.

---

## 8b. Logo — rebuilt from a flattened file

The clinic mark on the site is keyed out of `Images/logo-source.png`, which
arrived as a screenshot with a checkerboard baked in where the transparency
should have been. `tools/prepare_logo.py` reconstructs it, and the result is
clean at every size the site uses.

If the clinic has the **original vector or a real transparent PNG**, use it —
drop it in as `Images/logo-source.png` and re-run `python tools/prepare_logo.py`
(the script is tolerant: with a genuinely transparent source the colour
thresholds still find the mark). A vector original would also let the favicon
be sharper at 16px.

---

## 9. Consultation fee — supplied, not published

The Maruthi Hospital poster states **₹1,000 per 1-hour counselling session**.
It is not on the website. Fees date quickly and the brief said not to invent
them; if the doctor wants it published, the natural home is a seventh FAQ.

---

## 10. Things deliberately absent

Do not add these without real, attributable source material:

- **Testimonials / patient reviews** — none were supplied, so there is no
  reviews section. Do not write placeholder ones.
- **Patient counts, success rates, "years of experience" beyond the 2 above.**
- **Hospital accreditations, awards, insurance or emergency-services claims.**
- **Any superlative.** `tools/audit.py` fails the build on "best psychiatrist",
  "No. 1", "100% recovery", "guaranteed results", "world-class" and "top rated".

---

## 11. Medical review — blocks launch

**This is the largest remaining risk on the site.** There are now 43 pages, 36
of them generated from copy written for this project, and **none of it has been
read by Dr. Tirumala Babu.** It covers 22 conditions, 11 therapies and 3
services, in a deliberately cautious, non-diagnostic register — but a register
is not a review.

| Needs reading | Where the copy lives |
| --- | --- |
| Depression, anxiety, alcohol use — full ten-section pages | `tools/content_detail.py` |
| The other 19 conditions — five-section pages | `tools/content_short.py` |
| 11 therapy pages | `tools/content_therapy.py` |
| Consultation, counselling, de-addiction service pages | `tools/content_service.py` |
| Condition cards, therapy summaries, Telugu subtitles, the five general FAQs | `tools/content_pages.py` |
| Services, About, Contact copy | the `.html` files directly |

Edit the Python, then run `python tools/build_pages.py` — that regenerates the
HTML and the `FAQPage` JSON-LD from the same source, so the visible answer and
the structured data can no longer disagree.

Specific points to put to the doctor:

1. **Which therapies are actually offered.** Only CBT, family therapy and
   couple therapy are stated as available, because those three appear on the
   clinic's own poster. The other eight are described as "may be recommended
   or referred". Move any of them by flipping `offered=` in `THERAPIES`.
2. **The urgent-care callouts.** Bipolar disorder, schizophrenia, psychosis,
   substance use, anger management, migraine and alcohol use carry a red-flag
   callout. The migraine one tells the reader to seek emergency care for a
   sudden severe headache; the alcohol and substance ones warn that abrupt
   cessation can be dangerous. That wording is deliberately strong and should
   be confirmed.
3. **Scope.** Migraine, autism, ADHD and dementia pages describe assessment and
   management at this clinic. Confirm each is genuinely within scope, and that
   the referral wording matches what actually happens.
4. **The "what it does not do" section on every therapy page.** It states
   limitations plainly, which is unusual for a clinic website. Confirm the
   doctor is comfortable with it.

---

## 12. Adding or deepening a page

Every condition, therapy and the three distinct services now have a page. To
**deepen** a condition from the five-section template to the ten-section one,
move its entry from `tools/content_short.py` to `tools/content_detail.py` in
the fuller shape and rebuild — `content_detail.py` wins where a slug is in
both. To **add** something new, give it a slug in `content_pages.py` and copy
in the matching content file; until the copy exists, no page is built and
nothing links to it.

---

## 14. The portrait source does not match the published portrait — blocks image rebuilds

`Images/DoctorProfile.jpg` in the repository is **not** the photo the hero
portrait was built from. The file there is 820x1024, a background-removed
cut-out sitting on a grey-and-white checkerboard. The published
`assets/img/doctor-tirumala-babu.jpg` is the original studio photograph on a
plain grey backdrop, and `PORTRAIT_TRIM` in `tools/prepare_images.py` is set
for a 1318x1102 source that is no longer present.

Running `python tools/prepare_images.py` therefore used to replace a good hero
image with a checkerboard and a black bar down one side, silently — PIL crops
past the edge of an image without complaining. That is how it was found.

`prepare_images.py` now checks the source size, refuses the portrait step,
keeps the existing file and carries on with the rest. So nothing is broken
today, but **the portrait cannot be rebuilt until the original photograph is
put back**:

1. Put the original studio photo back in `Images/DoctorProfile.jpg`.
2. Set `PORTRAIT_TRIM` to match its dimensions.
3. Run `python tools/prepare_images.py` and check the hero on the homepage.

Until then, do not delete `assets/img/doctor-tirumala-babu*.jpg|webp` — they
cannot be regenerated.

---

## 15. Photographs on the homepage

The "Inside the clinic" band carries three images. The page used to say which
were illustrative; that line was removed at the client's request in September
2026, so nothing on the page now distinguishes them:

| Image | What it is |
| --- | --- |
| `clinic-room` | Illustrative. Carries a generative watermark; not this clinic. |
| `consultation-illustrative` | Illustrative. Also watermarked, and the person resembles the doctor in a consultation that did not take place. |
| `consultation-clinic` | A real photograph taken at the clinic. |

Three things to settle before launch:

1. **Patient consent.** The real photograph shows a patient with her face
   blurred, and the page no longer states that consent was given. Confirm the
   consent is written and on file regardless — blurring is not consent, and
   context (clinic, clothing, date) can still identify someone. Removing the
   caption removed the claim, not the obligation.
2. **The second image shows someone who resembles the doctor** in a
   consultation that did not take place, and the page presents it alongside a
   genuine clinic photograph without distinguishing them. Three real photos of
   the clinic are already built and unused —
   `assets/img/clinic-entrance`, `clinic-reception` and `clinic-lab`. Swapping
   one of those in would remove the issue entirely and show the actual
   practice.
3. **Resolution.** That photograph is 478px wide, the smallest source on the
   site. It is not upscaled, because upscaling invents detail. A
   higher-resolution original would visibly improve it, particularly on a
   phone screen.

If the clinic would rather not use illustrative images at all, delete the
first two `<figure>` blocks from the band in `index.html` and drop their
entries from `GALLERY` in `tools/prepare_images.py`.

---

## 16. Telugu — removed

The site was bilingual in two ways and is now English only:

- Telugu subtitles under every service, condition and therapy name, taken from
  the clinic's own posters. Present since the first build.
- A Telugu layer over the navigation, section headings, footer headings, the
  emergency numbers and the appointment line, added in September 2026.

Both were removed at the client's request on 21 September 2026, along with
`tools/content_te.py`, the `.te` styles, the `--font-te` token and the
Noto Sans Telugu webfont. The font build now ships two faces rather than
three, and the subset dropped from 69.9 KB to 57.0 KB.

If Telugu is wanted again, the poster wording is still in
`Images/poster-services-telugu.jpg` and the git history has the removed files
— see the commit that removed them. Restore the face in
`tools/build_fonts.py` at the same time, or every Telugu character renders as
an empty box and the audit will not catch it.

---

---

## 13. Professional title

Marketing copy now reads **Neuropsychiatric Consultant** (hero label, meta and
Open Graph descriptions, portrait alt text). The schema `jobTitle` and the
"M.B.B.S., M.D. (Psychiatry) — Consultant Psychiatrist" credential lines still
read **Consultant Psychiatrist**, deliberately: that is the registered
qualification, and it is what a search engine or a directory verifies against.
Confirm with the doctor that he is content with both appearing.
