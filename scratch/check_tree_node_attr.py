with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = re.findall(r'data-[a-z0-9_-]+="[^"]*"', text)
unique_data = set([m for m in matches if "ahn" in m or "node" in m or "proband" in m])
print("Data attributes with ahn/node/proband:")
for d in sorted(list(unique_data))[:20]:
    print(" ", d)
