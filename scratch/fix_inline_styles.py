with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    text = f.read()

# Replace low-contrast neon colors with high-contrast AAA colors
replacements = [
    ("#6ee7b7", "#146C43"),
    ("#38bdf8", "#1D4ED8"),
    ("#fbbf24", "#B45309"),
    ("#cbd5e1", "#4A423B"),
    ("color:#10b981;", "color:#146C43;"),
    ("border-color:#10b981;", "border-color:#146C43;"),
    ("color:#f59e0b;", "color:#B45309;"),
    ("border-color:#f59e0b;", "border-color:#B45309;"),
    ("background:rgba(16,185,129,0.12)", "background:#EDF7F1"),
    ("background:rgba(16, 185, 129, 0.14)", "background:#EDF7F1"),
    ("background:rgba(245,158,11,0.2)", "background:#FEF7ED"),
    ("background:rgba(245, 158, 11, 0.2)", "background:#FEF7ED"),
    ("background:rgba(245,158,11,0.25)", "background:#FEF7ED"),
    ("border-color:rgba(245,158,11,0.5)", "border-color:#B45309"),
    ("fill=\"#d4af37\"", "fill=\"#7A1C1C\""),
    ("fill=\"#07090e\"", "fill=\"#1A1715\""),
    ("stroke=\"#07090e\"", "stroke=\"#7C5E24\""),
    ("text-anchor=\"middle\" fill=\"#07090e\"", "text-anchor=\"middle\" fill=\"#FFFFFF\""),
]

for old_val, new_val in replacements:
    count = text.count(old_val)
    if count > 0:
        text = text.replace(old_val, new_val)
        print(f"Replaced '{old_val}' -> '{new_val}' ({count} times)")

with open("src/pages/index.astro", "w", encoding="utf-8") as f:
    f.write(text)

print("Saved high-contrast WCAG AAA replacements in index.astro!")
