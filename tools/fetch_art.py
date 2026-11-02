# bleachspire/tools/fetch_art.py
"""Fill drop/ with the Bleach pictures the art guide asks for.

Usage:
    python tools/fetch_art.py --wave 1-every-run
    python tools/fetch_art.py --pool ironclad --limit 5 --dry-run
    python tools/fetch_art.py                 # every card still on a placeholder

For each card in data/card_map.csv the tool searches Bleach Wiki for a file
whose name matches the card's Bleach brief, downloads it, crops it to the card
size and saves it over the placeholder.  Provenance (query, file, URL) is
appended to data/art_sources.csv so any pick can be checked or redone.

Real art already in drop/ is never overwritten unless --force is given.
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter
import io
import sys
import time
import traceback
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_drop import is_placeholder, placeholder  # noqa: E402
import clean_art  # noqa: E402
import wiki_art  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "data" / "card_map.csv"
SOURCES = ROOT / "data" / "art_sources.csv"
FIELDS = [
    "card_id", "wave", "pool", "name", "bleach_character", "look_for",
    "query", "source_file", "source_url", "source_size", "score", "drop_file", "status", "clean",
]


def load_cards() -> list[dict]:
    with open(CARDS, encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if r["drop_file"]]


def load_sources() -> dict[str, dict]:
    """Provenance keyed by pool/card_id; an id alone is ambiguous across pools."""
    if not SOURCES.exists():
        return {}
    with open(SOURCES, encoding="utf-8") as f:
        return {f"{r['pool']}/{r['card_id']}": r for r in csv.DictReader(f) if r.get("pool")}


def save_sources(rows: dict[str, dict]) -> None:
    with open(SOURCES, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for key in sorted(rows):
            w.writerow({k: rows[key].get(k, "") for k in FIELDS})


def card_size(row: dict) -> tuple[int, int]:
    """The big inspect view is 4x the in-hand card (250x190 -> 1000x760)."""
    w, h = (int(v) for v in row["small_size"].split("x"))
    return w * 4, h * 4


def take(row: dict, force: bool, avoid: frozenset[str]) -> tuple[bool, str, dict]:
    """Fetch one card. Returns (saved, note, provenance)."""
    target = ROOT / row["drop_file"]
    if target.exists() and not force and not is_placeholder(target):
        return False, "already has art", {"status": "kept"}
    if not row["bleach_character"]:
        return False, "no bleach brief", {"status": "no-brief"}

    rejected = []
    for hit in wiki_art.ranked(row["bleach_character"], row["look_for"], avoid=avoid):
        blob = wiki_art.download(hit.url)
        art = wiki_art.prepare(blob, card_size(row))
        art, note = clean_art.clean(art)
        if art is None:
            rejected.append(f"{hit.title}: {note}")
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        art.save(target, optimize=True)
        return True, f"{hit.title} ({hit.score}, {note})", {
            "query": "ranked",
            "source_file": hit.title,
            "source_url": hit.url,
            "source_size": f"{hit.width}x{hit.height}",
            "score": hit.score,
            "drop_file": row["drop_file"],
            "status": "fetched",
            "clean": note,
        }

    # Nothing usable: leave a marked placeholder so the card falls back to the
    # game's own art and the next run knows it still needs a picture.
    placeholder(target, tuple(int(v) for v in row["small_size"].split("x")), [row["name"]])
    return False, f"no usable picture ({len(rejected)} rejected)", {
        "status": "no-match",
        "clean": rejected[0] if rejected else "",
        "query": "; ".join(rejected[:3]),
    }


def main() -> int:
    # Wiki file names carry macrons (ShihÃ…Âin, Kannonbiraha); keep the console calm.
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("--wave")
    ap.add_argument("--pool")
    ap.add_argument("--card")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--force", action="store_true", help="refetch even if real art exists")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--dups", action="store_true", help="redo cards sharing a picture with another card")
    ap.add_argument("--missing-source", action="store_true", help="redo cards with no recorded source")
    ap.add_argument("--flagged", action="store_true", help="redo cards whose picture was cleaned or rejected")
    ap.add_argument("--delay", type=float, default=0.25)
    args = ap.parse_args()

    rows = load_cards()
    if args.wave:
        rows = [r for r in rows if r["wave"] == args.wave]
    if args.pool:
        rows = [r for r in rows if r["pool"] == args.pool]
    if args.card:
        rows = [r for r in rows if r["card_id"] == args.card]
    if args.limit:
        rows = rows[: args.limit]

    sources = load_sources()
    # A card id can exist in two pools (the_gambit, scavenge), so key by both.
    key_of = lambda r: f"{r['pool']}/{r['card_id']}"

    if args.dups:
        seen = Counter(
            wiki_art.image_key(s["source_url"]) for s in sources.values() if s.get("source_url")
        )
        rows = [
            r for r in rows
            if sources.get(key_of(r), {}).get("source_url")
            and seen[wiki_art.image_key(sources[key_of(r)]["source_url"])] > 1
        ]
    if args.missing_source:
        rows = [r for r in rows if not sources.get(key_of(r), {}).get("source_url")]
    if args.flagged:
        rows = [
            r for r in rows
            if (sources.get(key_of(r), {}).get("clean") or "clean") != "clean"
        ]

    selected = {key_of(r) for r in rows}
    used = {
        wiki_art.image_key(s["source_url"])
        for k, s in sources.items()
        if k not in selected and s.get("source_url")
    }
    saved = failed = 0
    for i, row in enumerate(rows, 1):
        if args.dry_run:
            hit, query = wiki_art.best(row["bleach_character"], row["look_for"], avoid=frozenset(used))
            label = f"{hit.title} ({hit.score})" if hit else "NO MATCH"
            print(f"[{i}/{len(rows)}] {row['card_id']:<24} {label}   <- {query}")
            if hit:
                used.add(wiki_art.image_key(hit.url))
            continue
        started = time.perf_counter()
        try:
            ok, note, prov = take(row, args.force, frozenset(used))
        except Exception as exc:  # keep going, report at the end
            failed += 1
            print(f"[{i}/{len(rows)}] {row['card_id']:<24} ERROR {exc}")
            traceback.print_exc(limit=1)
            continue
        merged = {**row, **prov, "source_size": prov.get("source_size", "")}
        sources[key_of(row)] = merged
        if prov.get("source_url"):
            used.add(wiki_art.image_key(prov["source_url"]))
        if ok:
            saved += 1
        print(f"[{i}/{len(rows)}] {row['card_id']:<24} {note}  ({time.perf_counter() - started:.1f}s)")
        time.sleep(args.delay)

    if not args.dry_run:
        save_sources(sources)
        print(f"done: {saved} new image(s), {failed} error(s), sources -> {SOURCES.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
