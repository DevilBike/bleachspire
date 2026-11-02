"""Round-trip checks: build the mod, read the pack back, decode the textures."""

import json
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import build_mod  # noqa: E402
from godot_pack import read_ctex, read_pck_file, read_pck_index  # noqa: E402


def test_build_round_trip(tmp_path):
    art = tmp_path / "art"
    (art / "ironclad").mkdir(parents=True)
    Image.new("RGB", (1000, 760), (10, 200, 30)).save(art / "ironclad" / "strike_ironclad.png")

    out = tmp_path / "out"
    drop = tmp_path / "drop"
    (drop / "1-every-run" / "ironclad").mkdir(parents=True)
    from make_drop import placeholder
    placeholder(drop / "1-every-run" / "ironclad" / "bash.png", (250, 190), ["Bash"])
    build_mod.build(out_dir=out, art_dir=art, drop_dir=drop)

    manifest = json.loads((out / "bleachspire.json").read_text())
    assert manifest["affects_gameplay"] is False
    assert manifest["has_dll"] is False and manifest["has_pck"] is True

    pck = out / "bleachspire.pck"
    info = read_pck_index(pck)
    assert info.format_version == 3
    assert info.godot_version == (4, 5, 1)
    by_path = {e.path: e for e in info.entries}
    assert set(by_path) == {
        "res://bleachspire/cards/ironclad/strike_ironclad_small.ctex",
        "res://bleachspire/cards/ironclad/strike_ironclad_big.ctex",
        "res://bleachspire/cards/ironclad/strike_ironclad_small.tres",
        "res://bleachspire/cards/ironclad/strike_ironclad_big.tres",
        "res://images/atlases/card_atlas.sprites/ironclad/strike_ironclad.tres.remap",
        "res://images/packed/card_portraits/ironclad/strike_ironclad.png.remap",
    }
    # bash.png is still a placeholder, so it must not be in the pack.
    # Only images and remaps: no scripts, scenes or data that could change gameplay.
    assert all(p.endswith((".ctex", ".tres", ".remap")) for p in by_path)

    remap = read_pck_file(pck, by_path["res://images/atlases/card_atlas.sprites/ironclad/strike_ironclad.tres.remap"])
    assert remap.decode() == '[remap]\n\npath="res://bleachspire/cards/ironclad/strike_ironclad_small.tres"\n'
    tres = read_pck_file(pck, by_path["res://bleachspire/cards/ironclad/strike_ironclad_small.tres"]).decode()
    assert tres.startswith('[gd_resource type="CompressedTexture2D" format=3]')
    assert 'load_path = "res://bleachspire/cards/ironclad/strike_ironclad_small.ctex"' in tres

    small = read_ctex(read_pck_file(pck, by_path["res://bleachspire/cards/ironclad/strike_ironclad_small.ctex"]))
    assert small.size == (500, 380)
    assert small.convert("RGB").getpixel((250, 190)) == (10, 200, 30)
    big = read_ctex(read_pck_file(pck, by_path["res://bleachspire/cards/ironclad/strike_ironclad_big.ctex"]))
    assert big.size == (1000, 760)
