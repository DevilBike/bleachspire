# bleachspire/tools/clean_art.py
"""Decide whether a picture is usable card art, and clean it up if it is.

Three jobs, all on a PIL image:

* `colour_ok`  - reject black-and-white manga scans and washed-out line art,
                 while keeping genuinely dark colour frames.
* `bubble_mask` - find speech bubbles (white blobs with text inside).
* `clean`       - paint over those bubbles with the surrounding picture.

Only numpy and Pillow are used; there is no OpenCV on this machine.
"""

from __future__ import annotations

import numpy as np
from PIL import Image, ImageFilter

# A picture is "black and white" below this saturation, and "washed out" when
# it is also bright. Dark night frames keep their low saturation but are dim.
GREY_SAT = 10.0
MUTED_SAT = 35.0
PALE_VALUE = 140.0

# Speech bubbles are white areas of a certain size that sit inside the frame.
WHITE_LEVEL = 244
DETECT_WIDTH = 480          # detection runs small, so labelling stays quick
MIN_BUBBLE = 0.004          # of the frame
MAX_BUBBLE = 0.22


def colour_stats(img: Image.Image) -> tuple[float, float]:
    hsv = img.convert("HSV")
    sat = np.asarray(hsv.split()[1], dtype=np.float32).mean()
    val = np.asarray(hsv.split()[2], dtype=np.float32).mean()
    return float(sat), float(val)


def colour_ok(img: Image.Image) -> bool:
    """True for colour art, including dark frames; False for scans and line art."""
    sat, val = colour_stats(img)
    if sat < GREY_SAT:
        return False
    if sat < MUTED_SAT and val >= PALE_VALUE:
        return False
    return True


def _label(mask: np.ndarray) -> tuple[np.ndarray, int]:
    """4-connected component labelling, small images only."""
    height, width = mask.shape
    labels = np.zeros((height, width), dtype=np.int32)
    count = 0
    for y0, x0 in zip(*np.nonzero(mask)):
        if labels[y0, x0]:
            continue
        count += 1
        labels[y0, x0] = count
        stack = [(y0, x0)]
        while stack:
            y, x = stack.pop()
            for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if 0 <= ny < height and 0 <= nx < width and mask[ny, nx] and not labels[ny, nx]:
                    labels[ny, nx] = count
                    stack.append((ny, nx))
    return labels, count


def bubble_mask(img: Image.Image) -> np.ndarray:
    """Boolean mask at full resolution covering speech bubbles, if any.

    Bubbles are found as near-white blobs whose bounding box is mostly white
    (the text inside splits the white, so the box is judged, not the blob),
    that sit away from the frame edge and are not tiny specks.
    """
    small = img.convert("RGB").resize(
        (DETECT_WIDTH, max(1, round(img.height * DETECT_WIDTH / img.width))), Image.BOX
    )
    arr = np.asarray(small, dtype=np.uint8)
    white = (arr.min(axis=2) >= WHITE_LEVEL)
    grey = arr[..., 0] * 0.299 + arr[..., 1] * 0.587 + arr[..., 2] * 0.114
    labels, count = _label(white)
    if count == 0:
        return np.zeros((img.height, img.width), dtype=bool)

    height, width = white.shape
    area = height * width
    out = np.zeros_like(white)
    total = 0
    for idx in range(1, count + 1):
        ys, xs = np.nonzero(labels == idx)
        if ys.size == 0:
            continue
        y0, y1, x0, x1 = ys.min(), ys.max(), xs.min(), xs.max()
        box_area = (y1 - y0 + 1) * (x1 - x0 + 1)
        if box_area < area * MIN_BUBBLE or box_area > area * MAX_BUBBLE:
            continue
        if y0 <= 1 or x0 <= 1 or y1 >= height - 2 or x1 >= width - 2:
            continue
        box = white[y0 : y1 + 1, x0 : x1 + 1]
        if box.mean() < 0.45:          # not mostly white: likely a lit surface
            continue
        aspect = (x1 - x0 + 1) / max(1, (y1 - y0 + 1))
        if aspect < 0.25 or aspect > 6:
            continue
        # A speech bubble is drawn with an outline, so the ring just outside the
        # white is dark. A white sky, a shirt or a highlight has no such ring.
        pad = 3
        ey0, ex0 = max(0, y0 - pad), max(0, x0 - pad)
        ey1, ex1 = min(height - 1, y1 + pad), min(width - 1, x1 + pad)
        ring = np.zeros((height, width), dtype=bool)
        ring[ey0 : ey1 + 1, ex0 : ex1 + 1] = True
        ring[y0 : y1 + 1, x0 : x1 + 1] = False
        rim = grey[ring]
        if rim.size == 0 or np.median(rim) > 115 or (rim < 130).mean() < 0.6:
            continue
        # Words in the bubble are dark strokes inside the white; a white coat or
        # a highlight has almost none, and a dark patch has far too many.
        inside = grey[y0 : y1 + 1, x0 : x1 + 1]
        ink = (inside < 90).mean()
        if not 0.01 <= ink <= 0.25:
            continue
        # Bubble paper is flat: the white inside barely varies. Clothing is
        # shaded, so its "white" has a wide spread.
        paper = inside[inside > 240]
        if paper.size < inside.size * 0.55 or paper.std() > 9:
            continue
        out[y0 : y1 + 1, x0 : x1 + 1] = True
        total += box_area

    if not out.any():
        return out
    mask_img = Image.fromarray((out * 255).astype(np.uint8)).resize(img.size, Image.NEAREST)
    mask = np.asarray(mask_img) > 127
    return np.asarray(Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(11))) > 127


def _diffuse(arr: np.ndarray, mask: np.ndarray, iterations: int) -> np.ndarray:
    """Jacobi smoothing of the masked pixels from their neighbours."""
    for _ in range(iterations):
        spread = arr.copy()
        spread[1:-1, 1:-1] = (
            arr[:-2, 1:-1] + arr[2:, 1:-1] + arr[1:-1, :-2] + arr[1:-1, 2:]
        ) * 0.25
        arr[mask] = spread[mask]
    return arr


def inpaint(img: Image.Image, mask: np.ndarray) -> Image.Image:
    """Fill the mask from its surroundings, coarse to fine.

    Solving at a few scales first lets the fill carry broad gradients (a sky, a
    wall) into the hole instead of smearing one flat colour over it.
    """
    if not mask.any():
        return img

    pyramid: list[tuple[Image.Image, np.ndarray]] = []
    work = img.convert("RGB")
    hole = mask
    while min(work.size) > 64:
        pyramid.append((work, hole))
        size = (max(1, work.width // 2), max(1, work.height // 2))
        work = work.resize(size, Image.BOX)
        hole = np.asarray(
            Image.fromarray((hole * 255).astype(np.uint8)).resize(size, Image.NEAREST)
        ) > 127

    arr = np.asarray(work, dtype=np.float32)
    arr = _diffuse(arr, hole, 240)

    for level, level_mask in reversed(pyramid):
        up = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).resize(level.size, Image.BILINEAR)
        arr = np.asarray(up, dtype=np.float32)
        # Only the hole is ours to change; resampling must not soften the rest.
        original = np.asarray(level, dtype=np.float32)
        arr[~level_mask] = original[~level_mask]
        arr = _diffuse(arr, level_mask, 40)

    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))


def clean(img: Image.Image) -> tuple[Image.Image | None, str]:
    """Return the art, or None with a reason when the picture is unusable.

    A detected speech bubble means the picture is dropped, not patched: a white
    coat or a bright wall is flat enough to look exactly like bubble paper, and
    painting over one of those smears the character. A different picture is
    always available; a smeared one cannot be undone.
    """
    if not colour_ok(img):
        sat, val = colour_stats(img)
        return None, f"not colour (sat {sat:.0f}, val {val:.0f})"
    mask = bubble_mask(img)
    if mask.any():
        return None, f"speech bubble ({mask.mean() * 100:.1f}% of frame)"
    return img, "clean"
