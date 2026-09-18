#!/usr/bin/env python3
"""Subset the self-hosted webfonts down to the characters this site actually uses.

    pip install fonttools brotli
    python tools/build_fonts.py

Sources are the upstream variable fonts, kept in tools/fonts-src/ so the build
is reproducible without a network call:

    newsreader-latin-wght-normal.woff2       display serif  (headings)
    inter-latin-wght-normal.woff2            text sans      (body, UI)
    noto-sans-telugu-telugu-wght-normal.woff2  Telugu subtitles

Outputs go to assets/fonts/ as .woff2, and the script prints the before/after
size of each so a regression is obvious.

Why subset: the Telugu face ships ~121 KB of glyphs for a language whose use on
this site is a couple of dozen short phrases. Cutting it to the characters
actually present, and pinning its weight axis, roughly quarters it. The Latin
faces lose the accented ranges the copy never uses, halving each.

Re-run this after adding copy in a new script or an unusual character — the
audit will not catch a missing glyph, but a tofu box on the page will.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(__file__).resolve().parent / "fonts-src"
OUT = ROOT / "assets" / "fonts"
PAGES = ["index.html", "privacy.html"]

# Always keep these, whether or not they appear in today's copy: the digits and
# punctuation any future edit will reach for, plus the typographic characters
# the design relies on.
ALWAYS = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    " .,:;!?'\"()[]{}/\\|@#$%^&*_+-=<>~`"
    "‘’“”"  # curly quotes
    "–—"  # en dash, em dash
    " ·•…"  # nbsp, middot, bullet, ellipsis
    "×°₹©"  # multiply, degree, rupee, copyright
    "→←"  # arrows
)

FONTS = [
    # (source file, output stem, characters it needs, weight to pin)
    # pin=None keeps the variable weight axis; the Latin faces need it because
    # the design uses several weights. The Telugu face is only ever drawn at one
    # weight, so pinning it drops the variation tables.
    ("newsreader-latin-wght-normal.woff2", "newsreader-display", "latin", None),
    ("inter-latin-wght-normal.woff2", "inter-text", "latin", None),
    ("noto-sans-telugu-telugu-wght-normal.woff2", "noto-telugu", "telugu", 500),
]


def page_text() -> str:
    """Everything a visitor can read, with markup, scripts and styles removed."""
    out = []
    for name in PAGES:
        path = ROOT / name
        if not path.exists():
            continue
        raw = path.read_text(encoding="utf-8")
        raw = re.sub(r"<(script|style|svg)\b.*?</\1>", " ", raw, flags=re.S | re.I)
        raw = re.sub(r"<!--.*?-->", " ", raw, flags=re.S)
        # Attribute values are readable too: alt text, placeholders, titles.
        for attr in ("alt", "placeholder", "title", "content", "aria-label", "value"):
            out += re.findall(rf'{attr}="([^"]*)"', raw, flags=re.I)
        out.append(re.sub(r"<[^>]+>", " ", raw))
    return " ".join(out)


def is_telugu(ch: str) -> bool:
    return "ఀ" <= ch <= "౿"


def main() -> int:
    try:
        from fontTools import subset  # noqa: F401
    except ImportError:
        print("fonttools is not installed:  pip install fonttools brotli")
        return 1

    OUT.mkdir(parents=True, exist_ok=True)
    text = page_text()
    used = set(text)

    latin = sorted({c for c in used if c.isprintable() and not is_telugu(c) and ord(c) < 0x2200})
    latin = sorted(set(latin) | set(ALWAYS))
    telugu = sorted({c for c in used if is_telugu(c)} | {"‌", "‍"})

    print(f"latin glyphs: {len(latin)}   telugu glyphs: {len(telugu)}")
    if not telugu:
        print("  ! no Telugu found in the pages — the Telugu font will be skipped")

    total_before = total_after = 0
    for source, stem, which, pin in FONTS:
        src = SRC / source
        if not src.exists():
            print(f"  ! missing source {source} — see the docstring")
            continue
        chars = latin if which == "latin" else telugu
        if not chars:
            continue

        subset_input = src
        tmp = None
        if pin is not None:
            from fontTools.ttLib import TTFont
            from fontTools.varLib import instancer

            font = instancer.instantiateVariableFont(
                TTFont(src), {"wght": pin}, inplace=False, updateFontNames=False
            )
            tmp = OUT / f".{stem}-pinned.ttf"
            font.flavor = None
            font.save(tmp)
            subset_input = tmp

        dest = OUT / f"{stem}.woff2"
        argv = [
            str(subset_input),
            f"--text={''.join(chars)}",
            # The full weight axis is kept — clamping it saves almost nothing
            # once the glyph set is this small, and it keeps the CSS free to
            # use any weight between 400 and 700.
            "--layout-features=kern,liga,clig,calt,mark,mkmk,abvs,blws,psts,akhn,half,pres,rphf,vatu",
            "--flavor=woff2",
            "--no-hinting",
            "--desubroutinize",
            "--drop-tables+=DSIG",
            f"--output-file={dest}",
        ]
        from fontTools.subset import main as subset_main

        subset_main(argv)
        if tmp is not None:
            tmp.unlink(missing_ok=True)
        before, after = src.stat().st_size, dest.stat().st_size
        total_before += before
        total_after += after
        print(f"  {stem}.woff2  {before / 1024:6.1f} KB -> {after / 1024:5.1f} KB")

    print(f"  total     {total_before / 1024:6.1f} KB -> {total_after / 1024:5.1f} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
