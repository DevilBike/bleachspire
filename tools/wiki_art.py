# bleachspire/tools/wiki_art.py
"""Find a Bleach Wiki picture that fits one card's art brief.

The wiki (bleach.fandom.com) keeps a scene or character image for almost every
moment in the manga and anime, with descriptive file names such as
"E202 Kenpachi kendo strike.png".  This module searches its File namespace,
scores the hits against the brief we wrote in data/card_map.csv and downloads
the best one.

Nothing here writes into the repository; callers get bytes and metadata back.
"""

from __future__ import annotations

import json
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageOps

API = "https://bleach.fandom.com/api.php"
USER_AGENT = "bleachspire-art/0.3 (personal graphics-only StS2 mod)"
CACHE = Path(__file__).resolve().parent.parent / ".cache" / "wiki"

# Very common English words carry no signal in a file name.
STOP = {
    "a", "an", "the", "of", "in", "on", "at", "to", "and", "or", "with", "his",
    "her", "its", "their", "as", "by", "for", "from", "into", "onto", "over",
    "under", "after", "before", "while", "still", "mid", "up", "down", "out",
    "off", "one", "two", "s", "vs", "against", "being", "has", "have", "is",
    "are", "that", "this", "him", "them", "she", "he", "it", "no", "not",
}

# File names that almost never make good card art.
BAD = {
    "chapter", "volume", "cover", "logo", "icon", "symbol", "map", "sprite",
    "card", "banner", "stamp", "sig", "signature", "user", "wiki", "poll",
    "template", "anime", "manga", "episode", "gallery", "category", "artbook",
    "fortnite", "skin", "cosplay", "figure", "toy", "merch", "render",
    "wallpaper", "fanart", "meme", "quiz", "doll", "plush", "minecraft",
    "swimsuit", "bikini", "maid",
    "insignia", "emblem", "badge", "crest", "flag", "seal", "kanji", "tattoo",
}

ALIASES = {
    "soi fon": "sui-feng",
    "yoruichi shihoin": "yoruichi shihōin",
    "sosuke aizen": "sōsuke aizen",
    "genryusai yamamoto": "genryūsai shigekuni yamamoto",
    "szayelaporro granz": "szayelaporro granz",
    "jushiro ukitake": "jūshirō ukitake",
    "marechiyo omaeda": "marechiyo ōmaeda",
    "yasutora sado chad": "yasutora sado",
    "squad 11": "11th division",
    "squad 12": "12th division",
    "onmitsukido": "onmitsukidō",
    "gotei 13": "gotei 13",
}


def strip_accents(text: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c))


def tokens(text: str) -> list[str]:
    text = strip_accents(text.lower())
    # Wiki names glue chapter numbers onto words ("194Nake"); split those first.
    text = re.sub(r"(?<=[0-9])(?=[a-z])|(?<=[a-z])(?=[0-9])", " ", text)
    return [t for t in re.split(r"[^a-z0-9]+", text) if t and t not in STOP]


@dataclass
class Candidate:
    title: str
    url: str
    width: int
    height: int
    score: float = 0.0
    look_hits: int = 0
    reason: str = ""


def _api(params: dict[str, str], retries: int = 3) -> dict:
    params = {"format": "json", "formatversion": "2", **params}
    url = f"{API}?{urllib.parse.urlencode(params)}"
    last: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=45) as resp:
                return json.load(resp)
        except (urllib.error.URLError, TimeoutError) as exc:  # transient
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"wiki api failed: {last}")


def search(query: str, limit: int = 20, thumb_width: int = 1600) -> list[Candidate]:
    """Search the File namespace for `query`, newest cache first."""
    CACHE.mkdir(parents=True, exist_ok=True)
    key = re.sub(r"[^a-z0-9]+", "_", f"{query}_{limit}".lower())[:120]
    path = CACHE / f"{key}.json"
    if path.exists():
        raw = json.loads(path.read_text(encoding="utf-8"))
    else:
        data = _api(
            {
                "action": "query",
                "generator": "search",
                "gsrsearch": f"file:{query}",
                "gsrnamespace": "6",
                "gsrlimit": str(limit),
                "prop": "imageinfo",
                "iiprop": "url|size|mime",
                "iiurlwidth": str(thumb_width),
            }
        )
        pages = data.get("query", {}).get("pages", [])
        raw = []
        for page in pages:
            info = (page.get("imageinfo") or [{}])[0]
            if not info.get("url"):
                continue
            if info.get("mime") not in ("image/png", "image/jpeg", "image/webp"):
                continue
            raw.append(
                {
                    "title": page["title"],
                    "url": info.get("thumburl") or info["url"],
                    "origin": info["url"],
                    "width": info.get("width", 0),
                    "height": info.get("height", 0),
                }
            )
        path.write_text(json.dumps(raw, indent=1), encoding="utf-8")
        time.sleep(0.3)
    return [Candidate(c["title"], c["url"], c["width"], c["height"]) for c in raw]


def names_for(character: str) -> list[str]:
    """The brief's name plus the wiki's spelling when they differ."""
    alias = ALIASES.get(strip_accents(character.lower()))
    names = [alias, character] if alias else [character]
    return list(dict.fromkeys(n for n in names if n))


_CAST: dict[str, set[str]] | None = None


def cast() -> dict[str, set[str]]:
    """Every Bleach subject the card map names, with its tokens."""
    global _CAST
    if _CAST is None:
        import csv
        from pathlib import Path

        root = Path(__file__).resolve().parent.parent
        found: dict[str, set[str]] = {}
        with open(root / "data" / "card_map.csv", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                name = row.get("bleach_character", "")
                toks = set(tokens(name))
                if toks:
                    found[name] = toks
        _CAST = found
    return _CAST


def _names_other_cast(title_tokens: set[str], char_tokens: set[str]) -> bool:
    """True when the file name contains a full, different cast name."""
    for name, toks in cast().items():
        if toks == char_tokens or toks & char_tokens:
            continue
        if len(toks) >= 2 and toks <= title_tokens:
            return True
        if len(toks) == 1 and next(iter(toks)) in title_tokens and len(next(iter(toks))) > 4:
            return True
    return False


def score(cand: Candidate, character: str, look_for: str) -> Candidate:
    """How well a file name matches the brief. Higher is better."""
    title_tokens = set(tokens(cand.title))
    char_tokens: set[str] = set()
    for name in names_for(character):
        char_tokens |= set(tokens(name))
    look_tokens = set(tokens(look_for)) - char_tokens or set(tokens(look_for))

    char_hits = len(char_tokens & title_tokens)
    look_hits = len(look_tokens & title_tokens)
    bad_hits = len(BAD & title_tokens)
    # How much of the brief the file name actually covers, scale-free.
    coverage = look_hits / max(1, min(len(look_tokens), 4))

    value = 2.0 * min(char_hits, 2) / 2 + 3.4 * coverage
    # The wiki often names a scene by what happens ("Nake, Benihime") and leaves
    # the character out. Only trust that when at least two brief words match.
    if char_hits == 0:
        value += 0.9 if look_hits >= 2 else -0.5
    if cand.width >= 1000:
        value += 0.4
    if cand.width > cand.height:
        value += 0.3
    if cand.width < 400 or cand.height < 300:
        value -= 0.9
    value -= 1.6 * bad_hits
    if coverage == 0:
        value -= 0.6  # a portrait, not the moment the card is about
    # A file that names a different member of the cast is the wrong character,
    # however well the rest of the name reads.
    if char_hits == 0 and _names_other_cast(title_tokens, char_tokens):
        value -= 2.5

    cand.score = round(value, 2)
    cand.look_hits = look_hits
    cand.reason = f"char={char_hits} look={look_hits} bad={bad_hits} {cand.width}x{cand.height}"
    return cand


def queries(character: str, look_for: str) -> list[str]:
    """Search phrases, most specific first. Long words are the rare ones."""
    char_tokens = {t for name in names_for(character) for t in tokens(name)}
    keywords = sorted(
        {t for t in tokens(look_for) if t not in char_tokens and t not in BAD and len(t) > 3},
        key=len,
        reverse=True,
    )[:3]

    out: list[str] = []
    for name in names_for(character):
        if len(keywords) >= 2:
            out.append(" ".join([name, *keywords[:2]]))
        if keywords:
            out.append(" ".join([name, keywords[0]]))
        out.append(name)
    # A generic subject ("Hollow", "Shinigami") names no scene at all, so let
    # the brief itself be a query too.
    if len(keywords) >= 2:
        out.append(" ".join(keywords[:3]))
    return list(dict.fromkeys(out))


def page_images(character: str, limit: int = 200) -> list[Candidate]:
    """Every File the wiki uses on the character's own article."""
    name = names_for(character)[0]
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"page_{re.sub(r'[^a-z0-9]+', '_', name.lower())}.json"
    if path.exists():
        raw = json.loads(path.read_text(encoding="utf-8"))
    else:
        data = _api(
            {
                "action": "query",
                "titles": name,
                "prop": "images",
                "imlimit": str(limit),
            }
        )
        titles = []
        for page in data.get("query", {}).get("pages", []):
            for img in page.get("images", []):
                if img["title"].lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                    titles.append(img["title"])
        raw = []
        for start in range(0, len(titles), 40):
            chunk = titles[start : start + 40]
            info = _api(
                {
                    "action": "query",
                    "titles": "|".join(chunk),
                    "prop": "imageinfo",
                    "iiprop": "url|size|mime",
                    "iiurlwidth": "1600",
                }
            )
            for page in info.get("query", {}).get("pages", []):
                ii = (page.get("imageinfo") or [{}])[0]
                if ii.get("url"):
                    raw.append(
                        {
                            "title": page["title"],
                            "url": ii.get("thumburl") or ii["url"],
                            "origin": ii["url"],
                            "width": ii.get("width", 0),
                            "height": ii.get("height", 0),
                        }
                    )
        path.write_text(json.dumps(raw, indent=1), encoding="utf-8")
        time.sleep(0.3)
    return [Candidate(c["title"], c["url"], c["width"], c["height"]) for c in raw]


def portrait(character: str) -> Candidate | None:
    """The wiki article's own lead image: a clean picture of the character."""
    name = names_for(character)[0]
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"lead_{re.sub(r'[^a-z0-9]+', '_', name.lower())}.json"
    if path.exists():
        raw = json.loads(path.read_text(encoding="utf-8"))
        return Candidate(**raw) if raw else None
    data = _api(
        {
            "action": "query",
            "titles": name,
            "prop": "pageimages",
            "piprop": "original|thumbnail",
            "pithumbsize": "1600",
        }
    )
    found: Candidate | None = None
    for page in data.get("query", {}).get("pages", []):
        src = (page.get("thumbnail") or {}).get("source") or (page.get("original") or {}).get("source")
        if not src:
            continue
        info = _api(
            {
                "action": "query",
                "titles": "File:" + urllib.parse.unquote(src.rsplit("/", 1)[-1]),
                "prop": "imageinfo",
                "iiprop": "size",
            }
        )
        size = (0, 0)
        for p in info.get("query", {}).get("pages", []):
            ii = (p.get("imageinfo") or [{}])[0]
            size = (ii.get("width", 0), ii.get("height", 0))
        found = Candidate(f"File:{name}", src, size[0], size[1])
        break
    path.write_text(json.dumps(found.__dict__ if found else None), encoding="utf-8")
    return found


def image_key(url: str) -> str:
    """Identity of a wiki file across the several URL spellings of it.

    Fandom serves the same picture as `<name>/revision/latest?cb=…`,
    `<name>/revision/latest/scale-to-width-down/1600?cb=…` and `<name>/1600?cb=…`.
    Drop the query, the transform segments and the trailing width, and what is
    left is the file name.
    """
    segments = [s for s in url.split("?")[0].split("/") if s]
    while segments and (
        segments[-1].isdigit()
        or segments[-1].lower() in {"latest", "revision", "scale-to-width-down"}
    ):
        segments.pop()
    return urllib.parse.unquote(segments[-1]).lower() if segments else ""


def best(
    character: str,
    look_for: str,
    minimum: float = 2.0,
    avoid: frozenset[str] = frozenset(),
) -> tuple[Candidate | None, str]:
    """Return the best-scoring candidate and the query that found it.

    `avoid` holds image keys (see image_key) used by another card, so two cards
    do not end up with the same picture.
    """
    fallback: Candidate | None = None
    last_query = ""
    for query in queries(character, look_for):
        last_query = query
        hits = [score(c, character, look_for) for c in search(query)]
        if not hits:
            continue
        fresh = [c for c in hits if image_key(c.url) not in avoid] or hits
        top = max(fresh, key=lambda c: c.score)
        if top.score >= minimum and top.look_hits > 0 and image_key(top.url) not in avoid:
            return top, query
        if fallback is None or (image_key(top.url) not in avoid and top.score > fallback.score):
            fallback = top

    # The article's own images are curated; try those before a plain portrait.
    page_best: Candidate | None = None
    for cand in page_images(character):
        if image_key(cand.url) in avoid:
            continue
        cand = score(cand, character, look_for)
        if page_best is None or cand.score > page_best.score:
            page_best = cand
        if cand.score >= minimum and cand.look_hits > 0:
            return cand, f"page:{character}"
        if fallback is None or cand.score > fallback.score:
            fallback = cand

    if fallback is not None:
        fallback = score(fallback, character, look_for)
        if fallback.score >= minimum:
            return fallback, last_query

    # Nothing matched the moment itself. A clean picture of the character reads
    # better on a card than an unrelated still, so prefer the article portrait.
    lead = portrait(character)
    if lead is not None and image_key(lead.url) not in avoid:
        return score(lead, character, look_for), f"portrait:{character}"
    # Last resort: an article picture, but only one whose name is not junk
    # (a manga page number, a card game tile, a map).
    if page_best is not None and page_best.score >= 0.3:
        return page_best, f"page:{character}"
    return fallback, last_query


def ranked(
    character: str,
    look_for: str,
    avoid: frozenset[str] = frozenset(),
    limit: int = 10,
) -> list[Candidate]:
    """Every plausible picture for a card, best first.

    The caller downloads candidates in order until one survives its quality
    checks (colour, no speech bubbles), so a bad top hit is not fatal.
    """
    pool: list[Candidate] = []
    seen: set[str] = set()

    def add(cand: Candidate) -> None:
        key = image_key(cand.url)
        if key and key not in seen:
            seen.add(key)
            pool.append(score(cand, character, look_for))

    for query in queries(character, look_for):
        for cand in search(query):
            add(cand)
    for cand in page_images(character):
        add(cand)
    lead = portrait(character)
    if lead is not None:
        add(lead)

    fresh = [c for c in pool if image_key(c.url) not in avoid]
    if not fresh:
        # Every picture for this character is spoken for; a repeat beats a hole.
        fresh = pool
    # A negative score means the name actively argues against the card (a sign,
    # an insignia, another character). Offer those only if nothing else exists.
    decent = [c for c in fresh if c.score >= 0.0]
    if decent:
        fresh = decent
    fresh.sort(key=lambda c: (c.look_hits > 0, c.score), reverse=True)
    return fresh[:limit]


def download(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def prepare(blob: bytes, size: tuple[int, int]) -> Image.Image:
    """Decode, flatten transparency onto black, crop-to-fill the card size."""
    from io import BytesIO

    with Image.open(BytesIO(blob)) as img:
        img.load()
        if img.mode in ("RGBA", "LA", "P"):
            rgba = img.convert("RGBA")
            backdrop = Image.new("RGB", rgba.size, (0, 0, 0))
            backdrop.paste(rgba, mask=rgba.split()[-1])
            art = backdrop
        else:
            art = img.convert("RGB")
        return ImageOps.fit(art, size, Image.LANCZOS)
