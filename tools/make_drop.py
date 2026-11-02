"""Create the drop folder: one placeholder image per thing to reskin.

Usage:  python tools/make_drop.py

Writes drop/<wave>/<pool>/<card_id>.png for every in-game card and
drop/1-every-run/characters/<character>/<name>.png for every static character
image, ordered by how often you see them in a run. To add art, save your image
over the placeholder with the same name (any size; it is cropped to fit).
The build skips anything that is still a placeholder.
"""

from __future__ import annotations

import csv
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from PIL.PngImagePlugin import PngInfo

ROOT = Path(__file__).resolve().parent.parent
DROP = ROOT / "drop"
MARK_KEY, MARK_VALUE = "bleachspire", "placeholder"


def is_placeholder(path: Path) -> bool:
    with Image.open(path) as img:
        return getattr(img, "text", {}).get(MARK_KEY) == MARK_VALUE


def placeholder(path: Path, size: tuple[int, int], lines: list[str]) -> None:
    if path.exists() and not is_placeholder(path):
        return  # never overwrite real art
    img = Image.new("RGB", size, (48, 48, 56))
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default(size=max(10, size[1] // 12))
    y = size[1] // 2 - len(lines) * size[1] // 24
    for line in lines:
        d.text((size[0] // 2, y), line, font=font, fill=(200, 200, 210), anchor="mm")
        y += size[1] // 10
    info = PngInfo()
    info.add_text(MARK_KEY, MARK_VALUE)
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, pnginfo=info, optimize=True)


def main() -> None:
    n = 0
    with open(ROOT / "data/card_map.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r["drop_file"]:
                continue
            w, h = (int(v) for v in r["small_size"].split("x"))
            placeholder(ROOT / r["drop_file"], (w, h), [r["name"], r["bleach_character"], r["look_for"][:28]])
            n += 1
    with open(ROOT / "data/character_map.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            name = Path(r["game_path"]).stem
            placeholder(DROP / "1-every-run" / "characters" / r["character"] / f"{name}.png", (256, 256), [r["character"], r["kind"]])
            n += 1
    print(f"{n} placeholders under {DROP}")


if __name__ == "__main__":
    main()
