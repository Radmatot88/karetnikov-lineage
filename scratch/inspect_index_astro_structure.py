import re

with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

# Find script tag
script_starts = [i for i, l in enumerate(lines) if "<script" in l]
script_ends = [i for i, l in enumerate(lines) if "</script>" in l]
print(f"Script tags start at: {script_starts}, end at: {script_ends}")

# Find key IDs in HTML template
key_ids = ["fortressGate", "view-scroll", "view-tree", "view-fan", "view-radar", "view-heraldry", "dossierDrawer", "mobileBottomNav", "topbar"]
for kid in key_ids:
    matches = [(i+1, l.strip()[:60]) for i, l in enumerate(lines) if kid in l]
    print(f"Key '{kid}': {matches}")
