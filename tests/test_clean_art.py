"""Checks for the colour filter and the speech-bubble cleaner."""

import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import clean_art  # noqa: E402


def colour_image(size=(600, 400)):
    """Coloured, textured, not white: a stand-in for an anime frame."""
    y, x = np.mgrid[0 : size[1], 0 : size[0]]
    arr = np.stack(
        [
            (x * 255 // size[0]),
            (y * 255 // size[1]),
            ((x + y) * 255 // (size[0] + size[1])),
        ],
        axis=2,
    ).astype(np.uint8)
    return Image.fromarray(arr)


def test_greyscale_is_rejected():
    grey = Image.new("RGB", (400, 300), (180, 180, 180))
    assert not clean_art.colour_ok(grey)


def test_colour_is_accepted():
    assert clean_art.colour_ok(colour_image())


def test_dark_frame_is_kept():
    dark = Image.new("RGB", (400, 300), (14, 18, 30))
    dark.putpixel((200, 150), (255, 40, 40))
    sat, val = clean_art.colour_stats(dark)
    assert val < clean_art.PALE_VALUE
    assert clean_art.colour_ok(dark)


def test_washed_out_line_art_is_rejected():
    pale = Image.new("RGB", (400, 300), (238, 240, 246))
    pale.paste(colour_image((80, 60)).resize((80, 60)), (10, 10))
    assert not clean_art.colour_ok(pale)


def test_bubble_is_found_and_filled():
    base = colour_image((600, 400))
    draw = ImageDraw.Draw(base)
    draw.ellipse([330, 60, 520, 200], fill=(252, 252, 252), outline=(15, 15, 15), width=6)
    mask = clean_art.bubble_mask(base)
    assert mask.any(), "bubble not detected"
    fixed = clean_art.inpaint(base, mask)
    before = np.asarray(base, dtype=np.float32)
    after = np.asarray(fixed, dtype=np.float32)
    assert np.abs(before - after)[mask].mean() > 20, "bubble area barely changed"
    assert np.abs(before - after)[~mask].max() < 2, "pixels outside the bubble changed"


def test_clean_reports_rejection():
    grey = Image.new("RGB", (400, 300), (170, 170, 170))
    art, note = clean_art.clean(grey)
    assert art is None and "not colour" in note


def test_plain_colour_has_no_bubbles():
    assert not clean_art.bubble_mask(colour_image()).any()
