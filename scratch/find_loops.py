#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

target_file = Path(r"c:\Karetnikov_Lineage\scripts\build_lineage_dataset.py")
lines = target_file.read_text(encoding="utf-8").splitlines()

for i, line in enumerate(lines):
    if "range(1, 128)" in line or "build_collateral_relatives" in line or "def main" in line:
        print(f"Line {i+1}: {line}")
