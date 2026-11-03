import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'id="icon-[^"]+"', text)
print('Total SVG symbol IDs found:', len(matches))
for m in matches:
    print(' ', m)
