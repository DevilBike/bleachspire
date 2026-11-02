"""Minimal writers/readers for the Godot 4.5 file formats this mod needs.

Slay the Spire 2 runs on Godot 4.5.1 (MegaCrit's "MegaDot" fork). A mod's .pck
is mounted on top of the game's own pack, so any file at the same res:// path
wins. We only ever ship images, so we need three things:

  * PCK v3 (core/io/pck_packer.cpp in Godot 4.5.1)
  * CompressedTexture2D .ctex (scene/resources/compressed_texture.cpp)
  * .remap files (core/io/resource_loader.cpp, ResourceLoader::_path_remap)

Writing these directly means the build needs only Python + Pillow, no Godot
editor. Nothing here touches scripts, scenes or game data.
"""

from __future__ import annotations

import hashlib
import io
import struct
from dataclasses import dataclass
from pathlib import Path

from PIL import Image

# --- PCK ---------------------------------------------------------------------

PACK_HEADER_MAGIC = 0x43504447  # "GDPC"
PACK_FORMAT_VERSION = 3
PACK_REL_FILEBASE = 1 << 1
PACK_ALIGNMENT = 32

# The game refuses packs made by a newer Godot than its own.
GODOT_VERSION = (4, 5, 1)


def _pad(alignment: int, n: int) -> int:
    rest = n % alignment
    return 0 if rest == 0 else alignment - rest


def write_pck(path: Path, files: dict[str, bytes]) -> None:
    """Write a Godot 4.5 PCK containing `files` (res:// path -> bytes)."""
    out = io.BytesIO()
    out.write(struct.pack("<IIIII", PACK_HEADER_MAGIC, PACK_FORMAT_VERSION, *GODOT_VERSION))
    out.write(struct.pack("<I", PACK_REL_FILEBASE))
    file_base_ofs = out.tell()
    out.write(struct.pack("<Q", 0))  # files base, patched below
    dir_base_ofs = out.tell()
    out.write(struct.pack("<Q", 0))  # directory offset, patched below
    out.write(b"\0" * 64)  # 16 reserved u32
    out.write(b"\0" * _pad(PACK_ALIGNMENT, out.tell()))
    file_base = out.tell()

    entries = []
    for res_path in sorted(files):
        data = files[res_path]
        stored = res_path.removeprefix("res://")
        ofs = out.tell()
        out.write(data)
        out.write(b"\0" * _pad(PACK_ALIGNMENT, out.tell()))
        entries.append((stored, ofs - file_base, len(data), hashlib.md5(data).digest()))

    out.write(b"\0" * _pad(PACK_ALIGNMENT, out.tell()))
    dir_offset = out.tell()
    out.write(struct.pack("<I", len(entries)))
    for stored, rel_ofs, size, md5 in entries:
        name = stored.encode("utf-8")
        padded = name + b"\0" * _pad(4, len(name))
        out.write(struct.pack("<I", len(padded)))
        out.write(padded)
        out.write(struct.pack("<QQ", rel_ofs, size))
        out.write(md5)
        out.write(struct.pack("<I", 0))  # flags: not encrypted, not a removal

    buf = out.getbuffer()
    struct.pack_into("<Q", buf, file_base_ofs, file_base)
    struct.pack_into("<Q", buf, dir_base_ofs, dir_offset)
    path.write_bytes(bytes(buf))


@dataclass
class PckEntry:
    path: str
    offset: int  # absolute offset in the .pck file
    size: int
    md5: bytes
    flags: int


@dataclass
class PckInfo:
    format_version: int
    godot_version: tuple[int, int, int]
    flags: int
    entries: list[PckEntry]


def read_pck_index(path: Path) -> PckInfo:
    """Read a PCK's header and directory without loading file contents.

    Works on large packs (such as the game's own SlayTheSpire2.pck) because it
    only seeks to the directory.
    """
    with open(path, "rb") as f:
        magic, fmt, major, minor, patch, flags = struct.unpack("<6I", f.read(24))
        if magic != PACK_HEADER_MAGIC:
            raise ValueError(f"{path} is not a Godot pack")
        if fmt < 3:
            raise ValueError(f"pack format {fmt} not supported (need 3+)")
        if flags & 1:
            raise ValueError("pack directory is encrypted")
        file_base, dir_offset = struct.unpack("<QQ", f.read(16))
        f.seek(dir_offset)
        (count,) = struct.unpack("<I", f.read(4))
        entries = []
        for _ in range(count):
            (name_len,) = struct.unpack("<I", f.read(4))
            name = f.read(name_len).rstrip(b"\0").decode("utf-8")
            ofs, size = struct.unpack("<QQ", f.read(16))
            md5 = f.read(16)
            (eflags,) = struct.unpack("<I", f.read(4))
            entries.append(PckEntry("res://" + name, file_base + ofs, size, md5, eflags))
    return PckInfo(fmt, (major, minor, patch), flags, entries)


def read_pck_file(path: Path, entry: PckEntry) -> bytes:
    with open(path, "rb") as f:
        f.seek(entry.offset)
        return f.read(entry.size)


# --- CompressedTexture2D (.ctex) ----------------------------------------------

CTEX_FORMAT_VERSION = 1
DATA_FORMAT_PNG = 1
IMAGE_FORMAT_RGBA8 = 5  # Image::FORMAT_RGBA8


def make_ctex(img: Image.Image) -> bytes:
    """Encode an image as a lossless (PNG payload) Godot CompressedTexture2D."""
    img = img.convert("RGBA")
    w, h = img.size
    if w > 0xFFFF or h > 0xFFFF:
        raise ValueError("image too large for ctex")
    png = io.BytesIO()
    img.save(png, format="PNG", optimize=True)
    # Godot's PNG unpacker expects its own 4-byte "PNG " tag before the file
    # (drivers/png/image_loader_png.cpp, unpack_mem_png).
    png_bytes = b"PNG " + png.getvalue()

    out = io.BytesIO()
    out.write(b"GST2")
    out.write(struct.pack("<III", CTEX_FORMAT_VERSION, w, h))
    out.write(struct.pack("<I", 0))  # flags: no stream, no mipmaps
    out.write(struct.pack("<i", -1))  # mipmap limit (editor default)
    out.write(b"\0" * 12)  # reserved
    out.write(struct.pack("<IHHII", DATA_FORMAT_PNG, w, h, 0, IMAGE_FORMAT_RGBA8))
    out.write(struct.pack("<I", len(png_bytes)))
    out.write(png_bytes)
    return out.getvalue()


def read_ctex(data: bytes) -> Image.Image:
    """Decode a PNG-payload ctex (used by the tests to round-trip our output)."""
    if data[:4] != b"GST2":
        raise ValueError("not a ctex")
    data_format, w, h, mipmaps, _fmt = struct.unpack_from("<IHHII", data, 36)
    if data_format != DATA_FORMAT_PNG:
        raise ValueError(f"unsupported ctex data format {data_format}")
    (size,) = struct.unpack_from("<I", data, 52)
    payload = data[56 : 56 + size]
    if payload[:4] != b"PNG ":
        raise ValueError("ctex PNG payload is missing Godot's 'PNG ' tag")
    img = Image.open(io.BytesIO(payload[4:]))
    img.load()
    return img


# --- .remap --------------------------------------------------------------------


def make_remap(target_res_path: str) -> bytes:
    """A .remap file. ResourceLoader checks `<path>.remap` before loading any
    path, so this redirects a base-game resource to our texture."""
    return f'[remap]\n\npath="{target_res_path}"\n'.encode("utf-8")


def make_texture_tres(ctex_res_path: str) -> bytes:
    """A text CompressedTexture2D resource that loads our .ctex.

    The game asks for these paths with type hint "Texture2D". The .ctex loader
    only answers for "CompressedTexture2D", so remapping straight to a .ctex
    fails ("No loader found"). The text .tres loader handles every type, and
    the resource then pulls in the .ctex through its load_path.
    """
    return (
        '[gd_resource type="CompressedTexture2D" format=3]\n\n'
        f'[resource]\nload_path = "{ctex_res_path}"\n'
    ).encode("utf-8")
