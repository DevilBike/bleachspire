"""Build the Bleach reskin mod into dist/bleachspire/.

Usage:  python tools/build_mod.py

Every image under art/cards/<pool>/<card_id>.png replaces that card's art in
both places the game draws it:

  small (hand, deck, rewards)  res://images/atlases/card_atlas.sprites/<pool>/<card_id>.tres
  big   (card inspect view)    res://images/packed/card_portraits/<pool>/<card_id>.png

Each base-game path gets a `.remap` file pointing at a small .tres under
res://bleachspire/, which loads our .ctex texture. Nothing else in the game is touched, so gameplay is
exactly the base game's. The manifest declares affects_gameplay: false.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from PIL import Image, ImageOps

sys.path.insert(0, str(Path(__file__).resolve().parent))
from godot_pack import make_ctex, make_remap, make_texture_tres, write_pck  # noqa: E402
from make_drop import is_placeholder  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ART_CARDS = ROOT / "art" / "cards"
DROP = ROOT / "drop"
DIST = ROOT / "dist"

MOD_ID = "bleachspire"
MANIFEST = {
    "id": MOD_ID,
    "name": "Bleach Spire",
    "author": "DevilBike",
    "description": "Graphics-only Bleach reskin. Replaces card art only; gameplay is unchanged.",
    "version": "0.1.0",
    "has_pck": True,
    "has_dll": False,
    "dependencies": [],
    "affects_gameplay": False,
    "min_game_version": "0.111.0",
}

# Card portrait sizes. The community docs give 500x380 (or multiples) for card
# art; the big inspect view uses the 2x size.
SMALL_SIZE = (500, 380)
BIG_SIZE = (1000, 760)


def card_files(art: Image.Image, pool: str, card_id: str) -> dict[str, bytes]:
    ours = f"res://{MOD_ID}/cards/{pool}/{card_id}"
    small = ImageOps.fit(art, SMALL_SIZE, Image.LANCZOS)
    big = ImageOps.fit(art, BIG_SIZE, Image.LANCZOS)
    return {
        f"{ours}_small.ctex": make_ctex(small),
        f"{ours}_big.ctex": make_ctex(big),
        f"{ours}_small.tres": make_texture_tres(f"{ours}_small.ctex"),
        f"{ours}_big.tres": make_texture_tres(f"{ours}_big.ctex"),
        f"res://images/atlases/card_atlas.sprites/{pool}/{card_id}.tres.remap": make_remap(f"{ours}_small.tres"),
        f"res://images/packed/card_portraits/{pool}/{card_id}.png.remap": make_remap(f"{ours}_big.tres"),
    }


def art_sources(art_dir: Path = ART_CARDS, drop_dir: Path = DROP) -> dict[tuple[str, str], Path]:
    """Map (pool, card_id) -> image. drop/<wave>/<pool>/<id>.png wins over
    art/cards/<pool>/<id>.png; placeholders from tools/make_drop.py are skipped."""
    found: dict[tuple[str, str], Path] = {}
    for png in sorted(art_dir.glob("*/*.png")):
        found[(png.parent.name, png.stem)] = png
    for png in sorted(drop_dir.glob("*/*/*.png")):
        if png.parent.name == "characters" or is_placeholder(png):
            continue
        found[(png.parent.name, png.stem)] = png
    return found


def collect(art_dir: Path = ART_CARDS, drop_dir: Path = DROP) -> dict[str, bytes]:
    files: dict[str, bytes] = {}
    for (pool, card_id), png in sorted(art_sources(art_dir, drop_dir).items()):
        with Image.open(png) as art:
            art.load()
            files.update(card_files(art, pool, card_id))
    return files


def build(out_dir: Path = DIST / MOD_ID, art_dir: Path = ART_CARDS, drop_dir: Path = DROP) -> list[str]:
    files = collect(art_dir, drop_dir)
    if not files:
        raise SystemExit(f"no art found under {drop_dir} or {art_dir} (placeholders are skipped)")
    out_dir.mkdir(parents=True, exist_ok=True)
    write_pck(out_dir / f"{MOD_ID}.pck", files)
    (out_dir / f"{MOD_ID}.json").write_text(json.dumps(MANIFEST, indent=2) + "\n", encoding="utf-8")
    return sorted(files)


if __name__ == "__main__":
    paths = build()
    cards = sum(1 for p in paths if p.endswith(".tres.remap"))
    print(f"built {DIST / MOD_ID} with {cards} card(s), {len(paths)} pack entries")
