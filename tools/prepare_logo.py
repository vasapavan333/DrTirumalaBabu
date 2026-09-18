#!/usr/bin/env python3
"""Turn the supplied logo into clean transparent web assets.

    python tools/prepare_logo.py

Input:  Images/logo-source.png
Output: assets/img/logo.png, logo@2x.png, logo.webp  (transparent)

The file the clinic supplied is a flattened screenshot: its "transparency" is a
grey-and-white checkerboard painted into the pixels, and there is a very faint
pale-blue circle drawn around the mark. Both have to go, and a plain
"delete the light pixels" key does not work, because the human figure inside
the cross is white too.

So the mark is rebuilt from its own colours instead:

  teal   = saturated, green/blue-leaning pixels  -> the cross and the ribbon
  dark   = low-value pixels                      -> the charcoal orbit
  figure = solid white areas, told apart from the checkerboard by texture

The figure is the awkward one. It is pure white, and so are half the
checkerboard squares, so no colour threshold can separate them — and it is not
fully enclosed by the teal either, so filling holes does not find it. What does
separate them is scale: the checkerboard squares are 25px, so a 55px window
placed anywhere on the checkerboard always catches a grey square, while the
same window inside the figure sees nothing but white. Those confident interior
pixels become seeds, and the white regions containing a seed are kept whole.

The faint pale-blue circle around the mark is dropped on purpose: at 44px in
the header it would only read as noise.
"""

from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import binary_closing, label

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "Images" / "logo-source.png"
OUT = ROOT / "assets" / "img"

# Widths to emit. The header draws the mark at 44px, the footer at 52px, so 2x
# of the largest is plenty; the OG card and icons are built from the master.
SIZES = {"logo.png": 128, "logo@2x.png": 256}
MASTER = 512

PAD = 0.04  # breathing room around the mark, as a fraction of its longest side

# The checkerboard in the supplied file: 25px squares, grey 0.808 / white 1.0.
CHECKER_SQUARE = 25


def build_alpha(rgb: np.ndarray) -> np.ndarray:
    a = rgb.astype(np.float32) / 255.0
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    mx, mn = a.max(2), a.min(2)
    sat = mx - mn

    # The teal: clearly saturated and leaning green/blue rather than red.
    # The threshold has to clear the faint pale-blue circle drawn around the
    # mark (saturation ~0.11); the real teal sits near 0.50, so 0.28 separates
    # them cleanly. If it were included, the circle would close a loop and
    # fill_holes below would flood the whole disc with checkerboard.
    teal = (sat > 0.28) & (g > r) & (b > r) & (mx > 0.25)
    # The charcoal orbit: simply dark. The checkerboard never goes below ~0.78.
    dark = mx < 0.62

    teal = binary_closing(teal, structure=np.ones((3, 3)), iterations=2)
    dark = binary_closing(dark, structure=np.ones((3, 3)), iterations=1)

    # The white figure. Two things make it separable from the checkerboard:
    #   - "white" is strict enough to exclude the grey squares (0.81), so the
    #     board's white squares are left touching each other only at corners,
    #     and 4-connected labelling keeps every one of them a separate region;
    #   - the figure is far larger than one 25px square, so an area threshold
    #     of a few squares keeps it and drops them.
    white = (sat < 0.07) & (mx > 0.93)
    labels, count = label(white)  # 4-connectivity on purpose
    sizes = np.bincount(labels.ravel())
    min_area = 6 * CHECKER_SQUARE**2
    keep = np.where(sizes > min_area)[0]
    keep = keep[keep != 0]
    figure = np.isin(labels, keep) if keep.size else np.zeros_like(white)
    print(f"  figure: kept {keep.size} of {count} white regions (>{min_area}px)")

    # Bridge the anti-aliased seams between the three masks. Where white figure
    # meets teal there is a 2px band that is neither strict-white nor
    # strongly-saturated, and without this it shows as a transparent hairline
    # once the logo sits on anything other than white.
    mask = binary_closing(
        teal | dark | figure, structure=np.ones((3, 3)), iterations=3
    ).astype(np.float32)
    # One pixel of feather so the edges do not look cut out with scissors.
    soft = Image.fromarray((mask * 255).astype("uint8")).filter(
        ImageFilter.GaussianBlur(0.7)
    )
    return np.asarray(soft).astype(np.float32) / 255.0


def main() -> int:
    if not SRC.exists():
        print(f"missing {SRC.relative_to(ROOT)}")
        return 1

    OUT.mkdir(parents=True, exist_ok=True)
    rgb = np.asarray(Image.open(SRC).convert("RGB"))
    alpha = build_alpha(rgb)

    # Where the mark is opaque, keep its own colour; elsewhere the colour is
    # irrelevant but must not be checkerboard grey, or a halo shows at the
    # edges when the image is scaled down. Bleed the nearest logo colour out.
    solid = alpha > 0.5
    if not solid.any():
        print("no logo pixels found — check the thresholds")
        return 1

    filled = rgb.copy()
    bleed = Image.fromarray(rgb).filter(ImageFilter.GaussianBlur(6))
    filled[~solid] = np.asarray(bleed)[~solid]

    out = np.dstack([filled, (alpha * 255).astype(np.uint8)])
    img = Image.fromarray(out, "RGBA")

    # Trim to the mark, then pad evenly so every export is centred.
    ys, xs = np.where(solid)
    img = img.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
    side = max(img.width, img.height)
    pad = round(side * PAD)
    canvas = Image.new("RGBA", (side + 2 * pad, side + 2 * pad), (0, 0, 0, 0))
    canvas.paste(img, ((canvas.width - img.width) // 2, (canvas.height - img.height) // 2))

    master = canvas.resize((MASTER, MASTER), Image.LANCZOS)
    master.save(OUT / "logo-master.png", "PNG", optimize=True)
    print(f"  logo-master.png  {MASTER}x{MASTER}")

    for name, size in SIZES.items():
        master.resize((size, size), Image.LANCZOS).save(
            OUT / name, "PNG", optimize=True
        )
        print(f"  {name}  {size}x{size}  {(OUT / name).stat().st_size / 1024:.1f} KB")

    master.resize((256, 256), Image.LANCZOS).save(
        OUT / "logo.webp", "WEBP", quality=92, method=6
    )
    print(f"  logo.webp  256x256  {(OUT / 'logo.webp').stat().st_size / 1024:.1f} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
