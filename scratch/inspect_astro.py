#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

astro_path = Path(r"c:\Karetnikov_Lineage\src\pages\index.astro")
content = astro_path.read_text(encoding="utf-8")

print(f"File size: {len(content)} characters, {len(content.splitlines())} lines")
