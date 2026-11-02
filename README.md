# Bleach Spire

A graphics-only Bleach reskin for Slay the Spire 2 (beta branch). It swaps
images and nothing else: no code, no scripts, no game data. The manifest says
`affects_gameplay: false`, so the game treats it as cosmetic.

## How it works

StS2 runs on Godot 4.5.1. At startup its mod loader reads every `*.json`
manifest in `mods/<folder>/` and, when `has_pck` is true, mounts
`<id>.pck` on top of the game's own pack. Files in our pack win over base-game
files at the same `res://` path.

The game draws each card's art from two places:

| Where | Base-game path |
| --- | --- |
| Hand, deck, rewards | `res://images/atlases/card_atlas.sprites/<pool>/<card_id>.tres` |
| Card inspect view | `res://images/packed/card_portraits/<pool>/<card_id>.png` |

For each card we ship a `.remap` file at both paths. Godot checks for
`<path>.remap` before loading anything, so the game loads our texture
(`res://bleachspire/cards/...tres`, a CompressedTexture2D that loads our `.ctex`) instead of the original. Remapping straight to a `.ctex` does not work: the game asks for `Texture2D` and the `.ctex` loader only answers for `CompressedTexture2D`.

The build writes the `.pck` and `.ctex` formats directly in Python, so it
needs no Godot editor.

## Layout

```
art/cards/<pool>/<card_id>.png   replacement art (any size; cropped to 500x380 / 1000x760)
tools/build_mod.py               builds dist/bleachspire/{bleachspire.json, bleachspire.pck}
tools/make_placeholder.py        draws an obvious TEST image for a card
tools/list_pck.py                lists files in a .pck (ours or the game's)
tools/godot_pack.py              PCK / ctex / remap writers and readers
tests/test_build.py              round-trip test of the build
```

## Build

```
pip install -r requirements.txt
python tools/build_mod.py
pytest -q
```

## Install

1. Copy `dist/bleachspire/` into `Slay the Spire 2/mods/` so you have
   `mods/bleachspire/bleachspire.json` and `mods/bleachspire/bleachspire.pck`.
2. Launch the game, accept the mods prompt if asked, and enable
   **Bleach Spire** in the Mods menu. Restart the game.

To remove it, delete `mods/bleachspire/`.

## Asset map

`data/` lists everything to reskin, generated from the game's own files
(extracted read-only on the player's PC, never committed):

```
python tools/asset_map.py --ref <bleachspire_ref> --index <sts2_pck_index.tsv> --meta ref/card_meta.json
python tools/art_guide.py      # rewrites docs/ART_GUIDE.md
```

Bleach suggestions live in `data/bleach_matches.csv`, keyed by card id (or
`<pool>/<card_id>` when two pools share an id).

- `data/card_map.csv`: every card art (586 in game, plus 38 unused), with its
  name, sizes, game paths, where to drop the replacement, and a Bleach match.
- `data/character_map.csv`: static character images (select screen, icons,
  map markers, energy icons and orbs).
- `data/rig_parts.csv`: every part of each character's animated Spine rigs
  (combat, character select, merchant, rest site) with its source size.

## Adding art

See [docs/ART_GUIDE.md](docs/ART_GUIDE.md). In short: save each image over its
placeholder in `drop/<wave>/<pool>/` (same file name), then run the build.
`python tools/make_drop.py` recreates any missing placeholders and never
overwrites real art.
