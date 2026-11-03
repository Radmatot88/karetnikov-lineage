with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("--- LINES 25-78 (Gate) ---")
print("".join(lines[25:78]))

print("--- LINES 78-108 (Topbar) ---")
print("".join(lines[78:108]))

print("--- LINES 310-335 (Mobile Bottom Nav) ---")
print("".join(lines[310:335]))

print("--- LINES 335-355 (Dossier Drawer Header) ---")
print("".join(lines[335:355]))
