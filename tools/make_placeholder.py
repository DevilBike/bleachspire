"""Draw an obviously-fake test card image so we can see the mod is working.

Usage:  python tools/make_placeholder.py ironclad strike_ironclad
Writes art/cards/<pool>/<card_id>.png (1000x760).
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
W, H = 1000, 760


def draw(label: str) -> Image.Image:
    img = Image.new("RGB", (W, H), (20, 22, 30))
    d = ImageDraw.Draw(img)
    # Hazard stripes so it can't be mistaken for real art.
    for x in range(-H, W, 80):
        d.polygon([(x, H), (x + 40, H), (x + 40 + H, 0), (x + H, 0)], fill=(235, 120, 30))
    d.rectangle([60, 210, W - 60, H - 210], fill=(20, 22, 30))
    big = ImageFont.load_default(size=150)
    small = ImageFont.load_default(size=44)
    d.text((W / 2, H / 2 - 30), "TEST", font=big, fill=(255, 255, 255), anchor="mm")
    d.text((W / 2, H / 2 + 85), label, font=small, fill=(235, 120, 30), anchor="mm")
    return img


if __name__ == "__main__":
    pool, card_id = sys.argv[1], sys.argv[2]
    out = ROOT / "art" / "cards" / pool / f"{card_id}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    draw(f"bleachspire: {card_id}").save(out)
    print(out)
