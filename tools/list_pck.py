"""List the files inside a Godot .pck (ours or the game's).

Usage:  python tools/list_pck.py <file.pck> [substring]
Example: python tools/list_pck.py "<game>/SlayTheSpire2.pck" card_portraits
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from godot_pack import read_pck_index  # noqa: E402

if __name__ == "__main__":
    info = read_pck_index(Path(sys.argv[1]))
    needle = sys.argv[2] if len(sys.argv) > 2 else ""
    print(f"# pack v{info.format_version}, Godot {'.'.join(map(str, info.godot_version))}, {len(info.entries)} files")
    for e in info.entries:
        if needle in e.path:
            print(f"{e.size:>10}  {e.path}")
