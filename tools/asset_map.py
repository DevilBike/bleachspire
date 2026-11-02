"""Build the asset map: every card, character image and rig part to reskin.

Usage:
  python tools/asset_map.py --ref <bleachspire_ref folder> --index <sts2_pck_index.tsv> --meta ref/card_meta.json

Inputs are extracted read-only from the game's pack on the player's PC and are
NOT committed (they are the game's files). Outputs go to data/ and are safe to
commit: they hold only ids, names, paths and sizes.

  data/card_map.csv       one row per card art
  data/character_map.csv  one row per static character image
  data/rig_parts.csv      one row per part of each animated (Spine) rig
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

CHARACTERS = ["ironclad", "silent", "defect", "regent", "necrobinder"]
POOL_ORDER = CHARACTERS + ["colorless", "event", "curse", "status", "token", "quest"]


# How often you see a card decides when to reskin it.
WAVES = {
    "Basic": "1-every-run", "Status": "1-every-run",
    "Common": "2-most-runs",
    "Uncommon": "3-often",
    "Rare": "4-sometimes", "Curse": "4-sometimes", "Token": "4-sometimes",
    "Ancient": "5-rare", "Event": "5-rare", "Quest": "5-rare",
}

# A few constructors are too complex for tools/card_meta.py to read.
RARITY_FALLBACK = {"spoils_map": "Quest?", "sovereign_blade": "Token?", "the_scythe": "Rare?"}

BLEACH_CHARACTER = {
    "ironclad": "Kenpachi Zaraki",
    "silent": "Soi Fon",
    "defect": "Kisuke Urahara",
    "regent": "Byakuya Kuchiki",  # Senbonzakura
    "necrobinder": "Mayuri Kurotsuchi",
}


def load_matches() -> dict[str, dict]:
    path = DATA / "bleach_matches.csv"
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as f:
        return {r["card_id"]: r for r in csv.DictReader(f)}


def card_rows(ref: Path, index_paths: set[str], meta: dict) -> list[dict]:
    matches = load_matches()
    loc = json.loads((ref / "localization/eng/cards.json").read_text(encoding="utf-8"))
    sheet = json.loads((ref / "images/atlases/card_atlas.tpsheet").read_text(encoding="utf-8"))
    rows = []
    for tex in sheet["textures"]:
        for sprite in tex["sprites"]:
            name = sprite["filename"].removesuffix(".png")
            if "/" not in name:
                continue  # root placeholders (beta.png, ancient_beta.png)
            pool, card_id = name.split("/", 1)
            w, h = sprite["region"]["w"], sprite["region"]["h"]
            key = card_id.upper()
            big = f"images/packed/card_portraits/{pool}/{card_id}.png"
            m = meta.get(card_id, {})
            in_game = f"{key}.title" in loc
            # "<pool>/<card_id>" wins when two pools share an id (e.g. scavenge)
            match = matches.get(f"{pool}/{card_id}") or matches.get(card_id, {})
            rarity = m.get("rarity") or RARITY_FALLBACK.get(card_id, "Uncommon?")
            wave = WAVES.get(rarity.rstrip("?"), "3-often") if in_game else "unused"
            rows.append({
                "wave": wave,
                "pool": pool,
                "card_id": card_id,
                "name": loc.get(f"{key}.title", ""),
                "in_game": "yes" if in_game else "no (unused art)",
                "rarity": rarity,
                "type": m.get("type", ""),
                "shape": "tall (ancient)" if h > 300 else "standard",
                "small_size": f"{w}x{h}",
                "small_path": f"images/atlases/card_atlas.sprites/{name}.tres",
                "big_path": big if big + ".import" in index_paths else "",
                "drop_file": f"drop/{wave}/{pool}/{card_id}.png" if in_game else "",
                "bleach_character": match.get("bleach_character") or BLEACH_CHARACTER.get(pool, ""),
                "look_for": match.get("look_for", ""),
                "status": "todo",
            })
    rows.sort(key=lambda r: (r["wave"], POOL_ORDER.index(r["pool"]) if r["pool"] in POOL_ORDER else 99, r["name"] or r["card_id"]))
    return rows


STATIC_PATTERNS = [
    ("character select", r"^images/packed/character_select/char_select_{c}(_locked)?\.png\.import$"),
    ("top bar icon", r"^images/ui/top_panel/character_icon_{c}(_outline)?\.png\.import$"),
    ("map marker", r"^images/packed/map/icons/map_marker_{c}\.png\.import$"),
    ("map marker", r"^images/atlases/ui_atlas\.sprites/map/icons/map_marker_{c}\.tres$"),
    ("energy icon (text)", r"^images/packed/sprite_fonts/{c}_energy_icon\.png\.import$"),
    ("energy icon (card)", r"^images/atlases/ui_atlas\.sprites/card/energy_{c}\.tres$"),
    ("energy orb layer", r"^images/ui/combat/energy_counters/{c}/.*\.png\.import$"),
    ("achievement", r"^images/packed/achievements/unlocked/character_skill_{c}\d\.png\.import$"),
    ("character select background", r"^animations/character_select/{c}/.*_bg\.png\.import$"),
]


def character_rows(index_paths: set[str]) -> list[dict]:
    rows = []
    for c in CHARACTERS:
        for kind, pattern in STATIC_PATTERNS:
            rx = re.compile(pattern.format(c=c))
            for p in sorted(index_paths):
                if rx.match(p):
                    rows.append({"character": c, "bleach_character": BLEACH_CHARACTER[c] or "TBD", "kind": kind, "game_path": p.removesuffix(".import"), "status": "todo"})
    return rows


RIG_KINDS = {
    "": "combat",
    "characterselect_": "character select",
    "_shop": "merchant",
    "restsite_": "rest site",
}


def parse_spine_atlas(text: str) -> list[dict]:
    """Parse a libGDX/Spine 4 .atlas text into regions with source sizes."""
    regions, page, scale = [], None, 1.0
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        i += 1
        if not line:
            page = None
            continue
        if page is None:
            page, scale = line, 1.0
            while i < len(lines) and ":" in lines[i]:
                k, v = lines[i].split(":", 1)
                if k.strip() == "scale":
                    scale = float(v)
                i += 1
            continue
        region = {"page": page, "name": line, "rotate": "no"}
        while i < len(lines) and ":" in lines[i]:
            k, v = (s.strip() for s in lines[i].split(":", 1))
            if k == "bounds":
                x, y, w, h = map(int, v.split(","))
                region.update(x=x, y=y, w=w, h=h)
            elif k == "offsets":
                ox, oy, ow, oh = map(int, v.split(","))
                region.update(orig_w=ow, orig_h=oh)
            elif k == "rotate":
                region["rotate"] = "yes" if v in ("true", "90") else v
            i += 1
        ow, oh = region.get("orig_w", region.get("w", 0)), region.get("orig_h", region.get("h", 0))
        region["source_size"] = f"{round(ow / scale)}x{round(oh / scale)}"
        region["packed_size"] = f"{region.get('w', 0)}x{region.get('h', 0)}"
        regions.append(region)
    return regions


def rig_rows(ref: Path) -> list[dict]:
    rows = []
    for spatlas in sorted((ref / ".godot/imported").glob("*.spatlas")):
        stem = spatlas.name.split(".atlas-")[0]
        if stem.startswith("characterselect_"):
            rig, who = "character select", stem.removeprefix("characterselect_")
        elif stem.endswith("_shop"):
            rig, who = "merchant", stem.removesuffix("_shop")
        elif stem.startswith("restsite_"):
            rig, who = "rest site", stem.removeprefix("restsite_")
        else:
            rig, who = "combat", stem
        character = "necrobinder" if who == "osty" else "regent" if who == "regent_weapon" else who
        part_of = {"osty": " (Osty)", "regent_weapon": " (weapon)"}.get(who, "")
        text = json.loads(spatlas.read_text(encoding="utf-8"))["atlas_data"]
        for r in parse_spine_atlas(text):
            rows.append({
                "character": character,
                "rig": rig + part_of,
                "atlas_page": r["page"],
                "part": r["name"],
                "source_size": r["source_size"],
                "packed_size": r["packed_size"],
                "rotated_in_atlas": r["rotate"],
            })
    rows.sort(key=lambda r: (CHARACTERS.index(r["character"]), r["rig"], r["part"]))
    return rows


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", type=Path, required=True)
    ap.add_argument("--index", type=Path, required=True)
    ap.add_argument("--meta", type=Path, required=True, help="output of tools/card_meta.py")
    args = ap.parse_args()
    index_paths = {line.split("\t", 1)[1].strip() for line in args.index.read_text(encoding="utf-8").splitlines() if "\t" in line}

    meta = json.loads(args.meta.read_text(encoding="utf-8"))
    cards = card_rows(args.ref, index_paths, meta)
    chars = character_rows(index_paths)
    rigs = rig_rows(args.ref)
    write_csv(DATA / "card_map.csv", cards)
    write_csv(DATA / "character_map.csv", chars)
    write_csv(DATA / "rig_parts.csv", rigs)
    live = sum(r["in_game"] == "yes" for r in cards)
    print(f"cards: {len(cards)} art ({live} in game), character images: {len(chars)}, rig parts: {len(rigs)}")


if __name__ == "__main__":
    main()
