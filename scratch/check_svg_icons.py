import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'<g id="icon-clan-[^"]+">.*?</g>', text, re.DOTALL)
print('Clan SVG icons found in index.astro:', len(matches))
for m in matches:
    print(m[:200])
    print('---')
