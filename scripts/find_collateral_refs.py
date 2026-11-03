#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re

src_dir = Path(r"c:\Karetnikov_Lineage\src")
matches = []
for p in src_dir.rglob("*.*"):
    if p.suffix in [".astro", ".ts", ".js", ".tsx"]:
        try:
            txt = p.read_text(encoding="utf-8")
            if "collateral" in txt.lower():
                matches.append(str(p.relative_to(src_dir.parent)))
        except Exception:
            pass

print("Files referencing collateral:")
for m in matches:
    print(f"- {m}")
