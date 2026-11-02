"""Write docs/ART_GUIDE.md from data/card_map.csv and data/character_map.csv.

Usage:  python tools/art_guide.py
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

WHO = [
    ("Ironclad", "Kenpachi Zaraki", "Berserker who loves taking hits: Strength, self-damage, Exhaust"),
    ("Silent", "Soi Fon", "Stealth-force assassin with a poison blade: Poison, Shivs, discard"),
    ("Defect", "Not decided (Kisuke Urahara suggested)", "Inventor with gadgets: orbs"),
    ("Regent", "Byakuya Kuchiki", "Noble whose Senbonzakura becomes countless blades: blade and stars"),
    ("Necrobinder", "Mayuri Kurotsuchi, with Nemu as Osty", "Mad scientist with a loyal companion: the Osty cards are Nemu"),
]

WAVE_TITLES = {
    "1-every-run": "Wave 1: every run",
    "2-most-runs": "Wave 2: most runs (commons)",
    "3-often": "Wave 3: often (uncommons)",
    "4-sometimes": "Wave 4: sometimes (rares, curses, tokens)",
    "5-rare": "Wave 5: rarely (ancient, event, quest)",
}

HEADER = """# Art guide

How to fill the mod with Bleach art. You collect the images yourself; this guide says what to look for and where each file goes.

## Who is who

| Slay the Spire 2 | Bleach | Why |
|---|---|---|
{who}

Chosen by Bike. To swap, change `BLEACH_CHARACTER` in `tools/asset_map.py` and `data/bleach_matches.csv`, then rerun `tools/asset_map.py`, `tools/make_drop.py` and `tools/art_guide.py`.

## Where to look (official sources)

- **VIZ Media Bleach page** (https://viz.com/bleach): English manga volumes and covers, plus links to the official Shonen Jump reader.
- **Bleach: Thousand-Year Blood War anime**: the official site and its key visuals, and screenshots you take yourself from the episodes on the streaming service you use.
- **Bleach: Brave Souls** (https://bleach-bravesouls.com): official character art from the KLab mobile game.
- **Bleach: Rebirth of Souls**: official screenshots and press art from Bandai Namco.
- Your own manga volumes or art books (for example *Bleach: All Colour But The Black*).

Card art shows at 250x190 (tall "ancient" cards 250x351) and in the big view at 4x that, so aim for at least 1000x760 and a landscape crop with the subject centred. Any size works; the build crops to fit.

## How to add an image

1. Open `drop/<wave>/<pool>/`. Every card already has a grey placeholder with its name.
2. Save your image over the placeholder, keeping the same file name (PNG or JPG renamed to .png both work).
3. Run `python tools/build_mod.py`. Placeholders are skipped, so a half-filled folder still builds.

Character images in `drop/1-every-run/characters/` are listed now and get wired into the build in the next step.
"""


def main() -> None:
    cards = list(csv.DictReader(open(DATA / "card_map.csv", encoding="utf-8")))
    chars = list(csv.DictReader(open(DATA / "character_map.csv", encoding="utf-8")))
    out = [HEADER.format(who="\n".join(f"| {a} | {b} | {c} |" for a, b, c in WHO))]
    for wave, title in WAVE_TITLES.items():
        rows = [r for r in cards if r["wave"] == wave]
        out.append(f"\n## {title} ({len(rows)} cards)\n")
        if wave == "1-every-run":
            out.append(f"\nAlso {len(chars)} character images: select screen, top-bar icons, map markers, energy icons and orbs (`drop/1-every-run/characters/`).\n")
        out.append("\n| Card | Pool | Bleach | Look for | File |\n|---|---|---|---|---|\n")
        for r in rows:
            look = r["look_for"] or "_suggestion coming_"
            out.append(f"| {r['name']} | {r['pool']} | {r['bleach_character']} | {look} | `{r['drop_file']}` |\n")
    (ROOT / "docs" / "ART_GUIDE.md").write_text("".join(out), encoding="utf-8")
    done = sum(bool(r["look_for"]) for r in cards if r["in_game"] == "yes")
    print(f"wrote docs/ART_GUIDE.md ({done} of {sum(r['in_game'] == 'yes' for r in cards)} cards have a suggestion)")


if __name__ == "__main__":
    main()
