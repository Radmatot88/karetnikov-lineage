with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = re.findall(r'style="[^"]*(?:color|background)[^"]*"', text)
print(f"Total inline style elements: {len(matches)}")
# Let's inspect suspicious colors: #6ee7b7, #38bdf8, #fbbf24, #07090e, rgba(0,0,0
for m in set(matches):
    if any(k in m for k in ["#6ee7b7", "#38bdf8", "#fbbf24", "#07090e", "#10b981", "#f59e0b", "color:#cbd5e1"]):
        print("Suspicious inline style:", m)
