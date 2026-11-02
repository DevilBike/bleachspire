"""Offline checks for the wiki art matcher: scoring, aliases, query order, crop."""

import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import wiki_art  # noqa: E402


def cand(title, width=1920, height=1080):
    return wiki_art.Candidate(title, "https://example.invalid/x.png", width, height)


def test_tokens_drop_filler():
    assert wiki_art.tokens("Kenpachi's two-handed Kendo overhead slash (vs Nnoitra)") == [
        "kenpachi", "handed", "kendo", "overhead", "slash", "nnoitra",
    ]
    # Chapter numbers are glued to the name on the wiki; keep the name readable.
    assert wiki_art.tokens("194Nake, Benihime") == ["194", "nake", "benihime"]
    assert wiki_art.strip_accents("Shihōin") == "Shihoin"


def test_alias_leads_the_query():
    names = wiki_art.names_for("Soi Fon")
    assert names[0] == "sui-feng"
    assert wiki_art.queries("Soi Fon", "Suzumebachi stinger")[0].startswith("sui-feng")


def test_scene_beats_bare_portrait():
    brief = "Kenpachi's two-handed Kendo overhead slash (vs Nnoitra)"
    portrait = wiki_art.score(cand("File:Kenpachi Zaraki.png"), "Kenpachi Zaraki", brief)
    scene = wiki_art.score(cand("File:E202 Kenpachi kendo strike.png"), "Kenpachi Zaraki", brief)
    assert scene.score > portrait.score
    assert scene.look_hits >= 1 and portrait.look_hits == 0


def test_source_name_alone_still_matches():
    brief = "Nake, Benihime blast"
    hit = wiki_art.score(cand("File:194Nake, Benihime.png"), "Kisuke Urahara", brief)
    assert hit.look_hits == 2
    assert hit.score >= 2.0


def test_junk_names_lose():
    brief = "Kenpachi kendo slash"
    good = wiki_art.score(cand("File:Kenpachi kendo strike.png"), "Kenpachi Zaraki", brief)
    junk = wiki_art.score(cand("File:Kenpachi Fortnite skin.png"), "Kenpachi Zaraki", brief)
    assert good.score > junk.score


def test_prepare_crops_and_flattens_alpha():
    src = Image.new("RGBA", (400, 900), (255, 0, 0, 0))
    for x in range(200):
        for y in range(900):
            src.putpixel((x, y), (0, 255, 0, 255))
    art = wiki_art.prepare(_png_bytes(src), (1000, 760))
    assert art.size == (1000, 760)
    assert art.mode == "RGB"


def _png_bytes(img):
    from io import BytesIO

    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()
