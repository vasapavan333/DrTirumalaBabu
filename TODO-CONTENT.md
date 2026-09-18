# Before launch — provisional content

Everything here is either a placeholder, or real information taken from the
clinic's print material that has not been confirmed for the website. Each entry
says exactly where to change it.

Run `python tools/audit.py` after each change.

---

## 1. Domain — blocks launch

`REPLACE-WITH-DOMAIN.example` appears **17 times**. Nothing about canonicals,
sharing or the sitemap works until it is replaced.

| File | What |
| --- | --- |
| `index.html` | canonical, `og:url`, `og:image`, `twitter:image`, and 9 `@id`/`url`/`image` fields inside the JSON-LD block |
| `privacy.html` | canonical, `og:url`, `og:image` |
| `sitemap.xml` | both `<loc>` entries |
| `robots.txt` | the `Sitemap:` line |

Fastest way, once the domain is known:

```bash
grep -rl 'REPLACE-WITH-DOMAIN.example' . --exclude-dir=tools --exclude-dir=Images \
  | xargs sed -i 's#https://REPLACE-WITH-DOMAIN.example#https://your-real-domain.in#g'
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

## 11. Medical review

The service descriptions, condition wording and all six FAQ answers are written
in a cautious, non-diagnostic register, but **they have not been reviewed by the
doctor.** Have Dr. Tirumala Babu read the Services, Conditions and FAQ sections
before launch — the FAQ answers are also duplicated inside the `FAQPage`
JSON-LD in `index.html`, so any edit needs to be made in both places.
