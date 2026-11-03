with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if i > 2500 and "scrollClearSearchBtn" in l and "<button" in l:
        lines[i] = "    const scrollClearBtn = document.getElementById('scrollClearSearchBtn');\n"
        print(f"Fixed line {i+1} to const scrollClearBtn = ...")

with open("src/pages/index.astro", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Saved.")
