"""Read each card's cost, type and rarity from the game's sts2.dll.

Usage:  python tools/card_meta.py <path to sts2.dll> <out.json>
Needs:  pip install dnfile

Every card class in MegaCrit.Sts2.Core.Models.Cards calls the CardModel
constructor as base(cost, CardType, CardRarity, ...). We read those first
integer constants from each constructor's IL. Read-only; nothing is patched.
"""

import json
import re
import sys

import dnfile

RARITY = ["None", "Basic", "Common", "Uncommon", "Rare", "Ancient", "Event", "Token", "Status", "Curse", "Quest"]
TYPE = ["None", "Attack", "Skill", "Power", "Status", "Curse", "Quest"]


def method_body(pe, rva: int) -> bytes:
    data, off = pe.__data__, pe.get_offset_from_rva(rva)
    if data[off] & 3 == 2:  # tiny header
        return data[off + 1 : off + 1 + (data[off] >> 2)]
    flags = int.from_bytes(data[off : off + 2], "little")
    size = int.from_bytes(data[off + 4 : off + 8], "little")
    start = off + (flags >> 12) * 4
    return data[start : start + size]


def leading_ints(code: bytes, limit: int = 4) -> list[int]:
    out, i = [], 0
    while i < len(code) and len(out) < limit:
        op = code[i]
        if op == 0x02:  # ldarg.0
            i += 1
        elif op == 0x15:  # ldc.i4.m1
            out.append(-1); i += 1
        elif 0x16 <= op <= 0x1E:  # ldc.i4.0..8
            out.append(op - 0x16); i += 1
        elif op == 0x1F:  # ldc.i4.s
            out.append(int.from_bytes(code[i + 1 : i + 2], "little", signed=True)); i += 2
        elif op == 0x20:  # ldc.i4
            out.append(int.from_bytes(code[i + 1 : i + 5], "little", signed=True)); i += 5
        else:
            break
    return out


def snake(name: str) -> str:
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", "_", name).lower()


def main() -> None:
    pe = dnfile.dnPE(sys.argv[1])
    cards = {}
    for td in pe.net.mdtables.TypeDef:
        if str(td.TypeNamespace) != "MegaCrit.Sts2.Core.Models.Cards":
            continue
        for m in td.MethodList:
            row = m.row
            if str(row.Name) != ".ctor" or not row.Rva:
                continue
            ints = leading_ints(method_body(pe, row.Rva))
            if len(ints) >= 3 and 0 <= ints[1] < len(TYPE) and 0 <= ints[2] < len(RARITY):
                cards[snake(str(td.TypeName))] = {"cost": ints[0], "type": TYPE[ints[1]], "rarity": RARITY[ints[2]]}
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        json.dump(cards, f, indent=1, sort_keys=True)
    print(f"{len(cards)} cards")


if __name__ == "__main__":
    main()
