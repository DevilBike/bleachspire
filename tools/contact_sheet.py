# bleachspire/tools/contact_sheet.py
"""One picture of everything that has been dropped in, for eyeballing.

Usage:
    python tools/contact_sheet.py --wave 1-every-run
    python tools/contact_sheet.py --all

Writes out/contact_<wave>.png: a grid of card art with the card name and the
Bleach subject underneath, so a wrong pick is obvious at a glance.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "out"
TILE = (250, 190)
COLS = 6
PAD = 10
LABEL_H = 42


def rows_for(wave: str | None, pool: str | None) -> list[dict]:
    with open(ROOT / "data" / "card_map.csv", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if r["drop_file"]]
    if wave:
        rows = [r for r in rows if r["wave"] == wave]
    if pool:
        rows = [r for r in rows if r["pool"] == pool]
    return rows


def is_real(path: Path) -> bool:
    if not path.exists():
        return False
    with Image.open(path) as img:
        return getattr(img, "text", {}).get("bleachspire") != "placeholder"


def sheet(rows: list[dict], title: str, name: str) -> Path:
    rows = [r for r in rows if is_real(ROOT / r["drop_file"])]
    if not rows:
        raise SystemExit("nothing to show: every card in that set is still a placeholder")
    cols = min(COLS, len(rows))
    grid_rows = (len(rows) + cols - 1) // cols
    width = PAD + cols * (TILE[0] + PAD)
    height = PAD + grid_rows * (TILE[1] + LABEL_H + PAD) + 40
    img = Image.new("RGB", (width, height), (18, 18, 24))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default(size=15)
    head = ImageFont.load_default(size=24)
    draw.text((PAD, 8), title, font=head, fill=(240, 240, 245))

    for i, row in enumerate(rows):
        col, line = i % cols, i // cols
        x = PAD + col * (TILE[0] + PAD)
        y = 44 + PAD + line * (TILE[1] + LABEL_H + PAD)
        with Image.open(ROOT / row["drop_file"]) as art:
            img.paste(art.convert("RGB").resize(TILE, Image.LANCZOS), (x, y))
        draw.text((x, y + TILE[1] + 2), row["name"], font=font, fill=(235, 150, 60))
        draw.text((x, y + TILE[1] + 20), row["bleach_character"][:30], font=font, fill=(190, 190, 200))

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    img.save(path, optimize=True)
    return path


def weak_rows(limit_score: float = 2.0) -> list[dict]:
    """Cards whose downloaded picture only matched the character, not the scene."""
    scores: dict[str, float] = {}
    with open(ROOT / "data" / "art_sources.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                scores[f"{r['pool']}/{r['card_id']}"] = float(r["score"] or 0)
            except ValueError:
                scores[f"{r['pool']}/{r['card_id']}"] = 0.0
    return [
        r for r in rows_for(None, None)
        if scores.get(f"{r['pool']}/{r['card_id']}", 9) < limit_score
    ]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wave")
    ap.add_argument("--pool")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--weak", action="store_true", help="only matches with a weak file name")
    args = ap.parse_args()
    if args.weak:
        path = sheet(weak_rows(), "Bleach Spire - weak matches, worth a look", "contact_weak.png")
    elif args.all:
        path = sheet(rows_for(None, args.pool), "Bleach Spire - every card with art", "contact_all.png")
    else:
        wave = args.wave or "1-every-run"
        path = sheet(rows_for(wave, args.pool), f"Bleach Spire - {wave}", f"contact_{wave}.png")
    print(path)


if __name__ == "__main__":
    main()
