#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

p = Path(r"c:\Karetnikov_Lineage\src\pages\index.astro")
content = p.read_text(encoding="utf-8")

old_text = """    // Exact 19 verified fact Ahnentafels (11 direct + 8 collateral)
    const CONFIRMED_FACT_AHNENTAFELS = new Set([
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14,
      301, 401, 402, 4011, 4012, 701, 702, 801
    ]);"""

new_text = """    // Exact verified fact Ahnentafels (12 direct + collateral)
    const CONFIRMED_FACT_AHNENTAFELS = new Set([
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 28,
      301, 401, 402, 4011, 4012, 701, 702, 801, 11201, 1201, 1202, 1001
    ]);"""

# Normalize CRLF
content_norm = content.replace("\r\n", "\n")
old_norm = old_text.replace("\r\n", "\n")
new_norm = new_text.replace("\r\n", "\n")

if old_norm in content_norm:
    content_norm = content_norm.replace(old_norm, new_norm, 1)
    # Restore CRLF if needed
    if "\r\n" in content:
        content_norm = content_norm.replace("\n", "\r\n")
    p.write_text(content_norm, encoding="utf-8")
    print("[OK] CONFIRMED_FACT_AHNENTAFELS updated in src/pages/index.astro")
else:
    print("[WARN] old_norm not found in index.astro")
