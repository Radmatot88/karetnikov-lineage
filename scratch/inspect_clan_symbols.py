import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    text = f.read()

for clan_id in ['icon-clan-karetnikov', 'icon-clan-kumanin', 'icon-clan-zubkov', 'icon-clan-yukhin']:
    m = re.search(rf'<symbol id="{clan_id}"[^>]*>.*?</symbol>', text, re.DOTALL)
    if m:
        print(f'=== {clan_id} ===')
        print(m.group(0))
