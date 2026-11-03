with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if "unlocked" in l or "fortressGate" in l:
        print(f"L{i+1}: {l.strip()[:80]}")
