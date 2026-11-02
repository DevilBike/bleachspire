# bleachspire/tools/review.py
"""Put the current picture and a few alternatives side by side, for eyeballing.

Usage:
    python tools/review.py --keys .tmp/review_keys.json --sheet 1
    python tools/review.py --apply data/review_choices.json

The first form reserves candidate pictures for every card in the key file,
saves them under .cache/review/, and writes one sheet per six cards with the
current pick on the left. The second form copies the chosen candidates over the
cards and updates data/art_sources.csv.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import clean_art  # noqa: E402
import wiki_art  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
REVIEW = ROOT / ".cache" / "review"
SOURCES = ROOT / "data" / "art_sources.csv"
MANIFEST = ROOT / ".cache" / "review_manifest.json"
CARDS_PER_SHEET = 8
OPTIONS = 4            # current + 3 alternatives
TILE = (210, 160)

FIELDS = [
    "card_id", "wave", "pool", "name", "bleach_character", "look_for",
    "query", "source_file", "source_url", "source_size", "score", "drop_file", "status", "clean",
]


def card_rows() -> dict[str, dict]:
    with open(ROOT / "data" / "card_map.csv", encoding="utf-8") as f:
        return {f"{r['pool']}/{r['card_id']}": r for r in csv.DictReader(f) if r["drop_file"]}


def load_sources() -> dict[str, dict]:
    with open(SOURCES, encoding="utf-8") as f:
        return {f"{r['pool']}/{r['card_id']}": r for r in csv.DictReader(f)}


def gather(key: str, row: dict, src: dict | None, used: frozenset[str] = frozenset()) -> list[dict]:
    """Current picture first, then up to four alternatives that pass the cleaner."""
    folder = REVIEW / re.sub(r"[^a-z0-9]+", "_", key)
    folder.mkdir(parents=True, exist_ok=True)
    options: list[dict] = []
    avoid = set(used)

    current = ROOT / row["drop_file"]
    if current.exists():
        kept = folder / "0_current.png"
        with Image.open(current) as im:
            im.convert("RGB").save(kept)
        options.append(
            {
                "file": str(kept.relative_to(ROOT)),
                "title": (src or {}).get("source_file", "current"),
                "score": (src or {}).get("score", ""),
                "current": True,
            }
        )

    mine = wiki_art.image_key((src or {}).get("source_url", "")) if src else ""
    avoid = frozenset(set(avoid) | ({mine} if mine else set()))
    for hit in wiki_art.ranked(row["bleach_character"], row["look_for"], avoid=avoid, limit=14):
        if len(options) >= OPTIONS:
            break
        try:
            blob = wiki_art.download(hit.url)
            art = wiki_art.prepare(blob, (1000, 760))
        except Exception:
            continue
        art, _note = clean_art.clean(art)
        if art is None:
            continue
        path = folder / f"{len(options)}.png"
        art.save(path)
        options.append(
            {
                "file": str(path.relative_to(ROOT)),
                "title": hit.title,
                "score": hit.score,
                "url": hit.url,
                "current": False,
            }
        )
    return options


def draw_sheet(entries: list[dict], index: int) -> Path:
    cols = OPTIONS
    width = 20 + cols * (TILE[0] + 8)
    row_h = TILE[1] + 46
    height = 46 + len(entries) * row_h
    sheet = Image.new("RGB", (width, height), (18, 18, 24))
    draw = ImageDraw.Draw(sheet)
    head = ImageFont.load_default(size=17)
    small = ImageFont.load_default(size=12)
    draw.text((10, 8), f"Bleach Spire review - sheet {index}", font=head, fill=(240, 240, 245))

    for row_i, entry in enumerate(entries):
        y = 40 + row_i * row_h
        label = f"{entry['name']} ({entry['pool']}) - {entry['character']}"
        draw.text((10, y), label[:110], font=small, fill=(235, 150, 60))
        for col_i, option in enumerate(entry["options"]):
            x = 10 + col_i * (TILE[0] + 8)
            with Image.open(ROOT / option["file"]) as art:
                sheet.paste(art.convert("RGB").resize(TILE, Image.LANCZOS), (x, y + 16))
            tag = "cur" if option["current"] else str(col_i)
            title = str(option["title"]).replace("File:", "")[:26]
            draw.rectangle([x, y + 16, x + 26, y + 32], fill=(0, 0, 0))
            draw.text((x + 4, y + 18), tag, font=small, fill=(255, 220, 120))
            draw.text((x, y + 16 + TILE[1] + 1), title, font=small, fill=(185, 185, 195))

    out = ROOT / "out" / f"review_{index:02d}.png"
    out.parent.mkdir(exist_ok=True)
    sheet.save(out)
    return out


def build(keys_path: Path, only_sheet: int | None, fresh: bool = False) -> None:
    keys = json.loads(keys_path.read_text(encoding="utf-8"))["keys"]
    rows = card_rows()
    sources = load_sources()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
    entries = []

    for key in keys:
        row = rows[key]
        if fresh:
            manifest.pop(key, None)
        if key in manifest:
            entries.append(manifest[key])
            continue
        # Pictures already used by cards outside this batch are off the table, so
        # a set of same-character cards does not end up with one identical image.
        used = frozenset(
            wiki_art.image_key(s["source_url"])
            for k, s in sources.items()
            if k not in keys and s.get("source_url")
        ) | frozenset(wiki_art.image_key(o.get("url", "")) for e in entries for o in e["options"] if o.get("url"))
        options = gather(key, row, sources.get(key), used)
        entry = {
            "key": key,
            "name": row["name"],
            "pool": row["pool"],
            "character": row["bleach_character"],
            "look_for": row["look_for"],
            "options": options,
        }
        manifest[key] = entry
        entries.append(entry)
        print(f"{key}: {len(options)} option(s)")

    MANIFEST.parent.mkdir(exist_ok=True)
    MANIFEST.write_text(json.dumps(manifest, indent=1), encoding="utf-8")

    for i in range(0, len(entries), CARDS_PER_SHEET):
        index = i // CARDS_PER_SHEET + 1
        if only_sheet and index != only_sheet:
            continue
        print(draw_sheet(entries[i : i + CARDS_PER_SHEET], index))


def apply(choices_path: Path) -> None:
    choices = json.loads(choices_path.read_text(encoding="utf-8"))["choices"]
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    with open(SOURCES, encoding="utf-8") as f:
        sources = {f"{r['pool']}/{r['card_id']}": r for r in csv.DictReader(f)}

    changed = 0
    for key, pick in choices.items():
        if pick in (None, "", "keep"):
            continue
        entry = manifest[key]
        option = next((o for o in entry["options"] if str(o["title"]) and o["file"].endswith(f"{pick}.png")), None)
        if option is None:
            print(f"{key}: no option {pick}")
            continue
        row = sources[key]
        target = ROOT / row["drop_file"]
        with Image.open(ROOT / option["file"]) as im:
            im.convert("RGB").save(target)
        row["source_file"] = option["title"]
        row["source_url"] = option.get("url", row.get("source_url", ""))
        row["score"] = option["score"]
        row["status"] = "fetched"
        row["clean"] = "clean"
        changed += 1

    with open(SOURCES, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for key in sorted(sources):
            w.writerow({k: sources[key].get(k, "") for k in FIELDS})
    print(f"applied {changed} choice(s)")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("--keys")
    ap.add_argument("--sheet", type=int)
    ap.add_argument("--apply")
    ap.add_argument("--fresh", action="store_true", help="regather options instead of reusing the manifest")
    args = ap.parse_args()
    if args.apply:
        apply(Path(args.apply))
    elif args.keys:
        build(Path(args.keys), args.sheet, args.fresh)
    else:
        ap.error("give --keys or --apply")


if __name__ == "__main__":
    main()
