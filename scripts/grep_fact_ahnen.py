#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

p = Path(r"c:\Karetnikov_Lineage\src\pages\index.astro")
lines = p.read_text(encoding="utf-8").splitlines()
for idx, line in enumerate(lines):
    if "CONFIRMED_FACT_AHNENTAFELS" in line:
        start = max(0, idx - 2)
        end = min(len(lines), idx + 10)
        print(f"--- Line {idx+1} ---")
        for j in range(start, end):
            print(f"{j+1}: {lines[j]}")
