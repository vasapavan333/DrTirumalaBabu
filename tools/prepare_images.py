#!/usr/bin/env python3
"""Build the site's web images from the originals in images/.

Run from the project root:  python tools/prepare_images.py

Sources (Images/, not served):
  DoctorProfile.jpg            -> doctor portrait (the approved studio headshot)
  Hospital Entrance.jpg        -> clinic photos
  Reception.jpg
  Lab.jpg
  poster-maruthi-hospital.png  -> fallback portrait, if the headshot is removed

Outputs land in assets/img/ as WebP + JPEG/PNG pairs.

The studio headshot carries a band of white padding down its right-hand side.
PORTRAIT_TRIM cuts it off; everything after that is plain resize-and-crop, so
swapping in a different photo usually means adjusting PORTRAIT_TRIM and nothing
else. Set PORTRAIT_SOURCE to None to fall back to cutting the doctor out of the
print poster (the old behaviour, kept because it still works).
"""

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "Images"
OUT = ROOT / "assets" / "img"
OUT.mkdir(parents=True, exist_ok=True)

# The approved studio headshot. Set to None to fall back to the poster crop.
PORTRAIT_SOURCE = "DoctorProfile.jpg"

# DoctorProfile.jpg is 1318x1102 with ~340px of white padding on the right.
PORTRAIT_TRIM = (0, 0, 976, 1102)

# Crop box of the portrait inside poster-maruthi-hospital.png (1023x1537).
POSTER_CROP = (48, 345, 405, 770)

# Vertical framing of each portrait crop: 0 keeps the top of the frame, 1 the
# bottom. Nudge these when the photo changes rather than re-cropping by hand.
PORTRAIT_FOCUS = {"hero": 0.0, "square": 0.06}

NAVY = (13, 42, 74)
TEAL = (14, 125, 138)
NEUTRAL = np.array([0.955, 0.962, 0.972])
BACKDROP = np.array([0.66, 0.80, 0.85])


def _hsv_planes(a):
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    mx = a.max(2)
    d = mx - a.min(2)
    dd = np.where(d == 0, 1.0, d)
    h = np.where(mx == r, 60 * (((g - b) / dd) % 6), 0.0)
    h = np.where((mx == g) & (mx != r), 60 * (((b - r) / dd) + 2), h)
    h = np.where((mx == b) & (mx != r) & (mx != g), 60 * (((r - g) / dd) + 4), h)
    s = np.where(mx == 0, 0, d / np.where(mx == 0, 1, mx))
    return h, s, mx, d


def _blur_mask(mask, radius):
    img = Image.fromarray((mask * 255).astype("uint8")).filter(
        ImageFilter.GaussianBlur(radius)
    )
    return np.asarray(img).astype(np.float32) / 255.0


def build_portrait():
    """Cut the doctor out of the poster and neutralise the poster artwork."""
    if PORTRAIT_SOURCE and (SRC / PORTRAIT_SOURCE).exists():
        base = Image.open(SRC / PORTRAIT_SOURCE).convert("RGB")
        if PORTRAIT_TRIM:
            base = base.crop(PORTRAIT_TRIM)
        # A touch of contrast and warmth so the studio grey sits with the
        # site's ivory surfaces instead of reading as a flat cut-out.
        base = ImageEnhance.Contrast(base).enhance(1.04)
        base = ImageEnhance.Color(base).enhance(1.05)
    else:
        base = Image.open(SRC / "poster-maruthi-hospital.png").convert("RGB")
        base = base.crop(POSTER_CROP)

        a = np.asarray(base).astype(np.float32) / 255.0
        h, s, mx, d = _hsv_planes(a)
        height, width, _ = a.shape

        # The poster puts a magenta blob behind the shoulders. Recolour it to a
        # soft teal so the portrait sits inside the site palette.
        magenta = (
            (d > 1e-6) & (h >= 298) & (h <= 352) & (s > 0.28) & (mx > 0.22)
        ).astype(np.float32)
        mk = _blur_mask(magenta, 2.0)
        repl = np.clip(BACKDROP * (0.56 + 0.54 * mx[..., None]), 0, 1)
        a = np.clip(a * (1 - mk[..., None]) + repl * mk[..., None], 0, 1)

        # The poster's orange ring clips the left and right borders, and its arc
        # cuts the top-right corner. Flatten both to the neutral backdrop.
        xs = np.arange(width)[None, :]
        ys = np.arange(height)[:, None]
        edge = ((xs < 0.10 * width) | (xs > 0.88 * width)).astype(np.float32)
        h2, s2, mx2, d2 = _hsv_planes(a)
        ring = (
            (d2 > 1e-6) & (h2 >= 12) & (h2 <= 48) & (s2 > 0.45) & (mx2 > 0.40)
        ).astype(np.float32) * edge
        corner = (
            (xs > 0.78 * width)
            & (ys < 0.34 * height)
            & (h2 >= 6)
            & (h2 <= 62)
            & (s2 > 0.18)
        ).astype(np.float32)
        ok = _blur_mask(np.clip(ring + corner, 0, 1), 2.2)
        a = np.clip(a * (1 - ok[..., None]) + NEUTRAL * ok[..., None], 0, 1)

        base = Image.fromarray((a * 255).astype("uint8"))
        base = base.resize(
            (int(base.width * 2.2), int(base.height * 2.2)), Image.LANCZOS
        ).filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=3))
        base = ImageEnhance.Color(base).enhance(1.04)

    # Hero portrait, 4:5 — sits inside the arched frame.
    hero = _cover(base, 760, 950, focus_y=PORTRAIT_FOCUS["hero"])
    _save_pair(hero, "doctor-tirumala-babu", quality=84)

    # Square crop for the about card, the hero name chip and the share card.
    square = _cover(base, 720, 720, focus_y=PORTRAIT_FOCUS["square"])
    _save_pair(square, "doctor-tirumala-babu-square", quality=84)
    return square


def _cover(img, width, height, focus_y=0.5):
    """Resize + centre-crop to exactly width x height."""
    scale = max(width / img.width, height / img.height)
    resized = img.resize(
        (max(1, round(img.width * scale)), max(1, round(img.height * scale))),
        Image.LANCZOS,
    )
    left = (resized.width - width) // 2
    top = int((resized.height - height) * focus_y)
    top = max(0, min(top, resized.height - height))
    return resized.crop((left, top, left + width, top + height))


def _save_pair(img, stem, quality=80):
    img.save(OUT / f"{stem}.webp", "WEBP", quality=quality, method=6)
    img.save(OUT / f"{stem}.jpg", "JPEG", quality=quality, optimize=True, progressive=True)
    print(f"  {stem}.webp / .jpg  {img.width}x{img.height}")


def build_clinic_photos():
    specs = [
        ("Hospital Entrance.jpg", "clinic-entrance", 1200, 700),
        ("Reception.jpg", "clinic-reception", 900, 675),
        ("Lab.jpg", "clinic-lab", 900, 675),
    ]
    for source, stem, width, height in specs:
        path = SRC / source
        if not path.exists():
            print(f"  ! missing {source}, skipped")
            continue
        img = Image.open(path).convert("RGB")
        _save_pair(_cover(img, width, height), stem, quality=78)


def _icon_tile(size):
    """One app icon: the clinic mark, centred on white with a navy edge.

    Uses assets/img/logo-master.png when it exists (run tools/prepare_logo.py
    first). Falls back to a drawn navy tile so this script never hard-fails on
    a fresh checkout.
    """
    logo_path = OUT / "logo-master.png"
    tile = Image.new("RGB", (size, size), (255, 255, 255))

    if logo_path.exists():
        inset = round(size * 0.13)
        mark = Image.open(logo_path).convert("RGBA")
        mark = mark.resize((size - 2 * inset, size - 2 * inset), Image.LANCZOS)
        tile.paste(mark, (inset, inset), mark)
        # A hairline keeps the white tile from disappearing into a white
        # browser toolbar or a light home screen.
        draw = ImageDraw.Draw(tile)
        draw.rectangle((0, 0, size - 1, size - 1), outline=NAVY, width=max(1, size // 40))
        return tile

    draw = ImageDraw.Draw(tile)
    draw.rectangle((0, 0, size, size), fill=NAVY)
    pad = size * 0.18
    draw.ellipse(
        (pad, pad, size - pad, size - pad),
        outline=(255, 255, 255),
        width=max(1, round(size * 0.055)),
    )
    r = size * 0.10
    cx = cy = size / 2
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=TEAL)
    return tile


def build_icons(square):
    """Favicon set and PWA icons, built from the clinic mark."""
    for size in (32, 180, 192, 512):
        name = {32: "favicon-32.png", 180: "apple-touch-icon.png"}.get(
            size, f"icon-{size}.png"
        )
        _icon_tile(size).save(OUT / name, "PNG", optimize=True)
        print(f"  {name}  {size}x{size}")

    _icon_tile(64).save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    print("  favicon.ico")


def build_og_card(square):
    """1200x630 share card: navy panel with the mark, portrait on the right."""
    card = Image.new("RGB", (1200, 630), NAVY)
    photo = _cover(square, 430, 630)
    card.paste(photo, (770, 0))

    # Soften the seam between the panel and the photo.
    seam = Image.new("RGB", (60, 630), NAVY)
    mask = Image.linear_gradient("L").rotate(270, expand=True).resize((60, 630))
    card.paste(seam, (770, 0), mask)

    logo_path = OUT / "logo-master.png"
    if logo_path.exists():
        mark = Image.open(logo_path).convert("RGBA").resize((104, 104), Image.LANCZOS)
        card.paste(mark, (64, 66), mark)

    draw = ImageDraw.Draw(card)
    draw.rectangle((0, 0, 8, 630), fill=TEAL)
    lines = [
        (64, 205, "Dr. Tirumala Babu's Psychiatry Clinic", 3.0),
        (64, 262, "Compassionate care for a healthier mind", 1.7),
        (64, 292, "and a happier life", 1.7),
        (64, 360, "Dr. Manchikalapudi Tirumala Babu", 2.1),
        (64, 400, "M.B.B.S., M.D. (Psychiatry) - Consultant Psychiatrist", 1.7),
        (64, 440, "Maruthi Hospital and Diagnostics, Guntur", 1.7),
    ]
    for x, y, text, scale in lines:
        draw.text((x, y), text, fill=(255, 255, 255), font_size=int(11 * scale))
    card.save(OUT / "og-card.jpg", "JPEG", quality=86, optimize=True)
    print("  og-card.jpg  1200x630")


if __name__ == "__main__":
    print("portrait:")
    square = build_portrait()
    print("clinic photos:")
    build_clinic_photos()
    print("icons:")
    build_icons(square)
    print("share card:")
    build_og_card(square)
    print("done")
