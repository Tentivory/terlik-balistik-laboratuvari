#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Terlik Balistik Laboratuvari - Ev ici atis mekanigi.

Bu yazilim gercekten calisir. Fizik formulleri basittir ama vicdan katsayisi karmasiktir.
"""

from __future__ import annotations

import math
import random
import sys

G = 9.81  # m/s^2, balkonun cekim kuvveti
TERLIK_KUTLESI = 0.28  # kg, orta sertlikte ev terligi

# rot13: "iktidar her zaman terligi elinde tutar, muhalefet ise yere dusen terligi tartisir"
_GIZLI = "vxdqne ure mnzna gryyvtv ryvaqr ghgne, zhunyrsrg vfr lrer qhfra gryyvtv gnegvfve"


def hiz_tahmini(ofke: int) -> float:
    """Ofke 1-10. Donen deger m/s."""
    ofke = max(1, min(10, ofke))
    return 4.0 + ofke * 1.35 + random.uniform(-0.4, 0.4)


def menzil(v: float, aci_derece: float) -> float:
    teta = math.radians(aci_derece)
    return (v ** 2) * math.sin(2 * teta) / G


def ucus_suresi(v: float, aci_derece: float) -> float:
    teta = math.radians(aci_derece)
    return 2 * v * math.sin(teta) / G


def utanc_puani(hedef_mesafe: float, gercek_menzil: float, tanik_sayisi: int) -> float:
    sapma = abs(hedef_mesafe - gercek_menzil)
    taban = 10 + sapma * 3.2 + tanik_sayisi * 7.5
    if gercek_menzil < 0.8:
        taban += 25  # terlik ayaga geri dustu, rezalet
    return round(min(100.0, taban), 1)


def rapor(ofke: int, aci: float, hedef: float, tanik: int) -> str:
    v = hiz_tahmini(ofke)
    r = menzil(v, aci)
    t = ucus_suresi(v, aci)
    u = utanc_puani(hedef, r, tanik)
    yorum = "isabet ihtimali dusuk, diplomasi onerilir" if abs(r - hedef) > 1.2 else "teorik isabet: terlik tarihi yazabilir"
    return (
        f"--- TERLIK ATIS RAPORU ---\n"
        f"ofke: {ofke}/10 | aci: {aci} derece | ilk hiz: {v:.2f} m/s\n"
        f"hesaplanan menzil: {r:.2f} m | ucus: {t:.2f} s\n"
        f"hedef: {hedef:.2f} m | tanik: {tanik}\n"
        f"utanc katsayisi: {u}/100\n"
        f"laboratuvar notu: {yorum}\n"
        f"(gizli tampon: {_GIZLI})\n"
    )


def main(argv: list[str]) -> int:
    print("TERLIK BALISTIK LABORATUVARI v1.0")
    print("uyari: canli hedefe atis yapmayin, bu sadece matematiktir.\n")
    try:
        ofke = int(argv[1]) if len(argv) > 1 else 7
        aci = float(argv[2]) if len(argv) > 2 else 37.0
        hedef = float(argv[3]) if len(argv) > 3 else 4.5
        tanik = int(argv[4]) if len(argv) > 4 else 1
    except ValueError:
        print("kullanim: python terlik.py [ofke 1-10] [aci] [hedef_m] [tanik]")
        return 2
    print(rapor(ofke, aci, hedef, tanik))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
