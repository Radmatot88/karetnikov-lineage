with open("src/styles/heritage.css", "r", encoding="utf-8") as f:
    css = f.read()

import re
colors = set(re.findall(r'#[0-9a-fA-F]{3,8}|rgba?\([^)]+\)', css))
print(f"Total distinct color definitions: {len(colors)}")
# Check specific colors
for c in ["#07090e", "#0e121b", "#141a26", "#1c2536", "#d4af37", "#f3dc8a", "#f1f5f9", "#94a3b8", "#64748b"]:
    count = css.count(c)
    print(f"{c}: {count} occurrences")
