with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = [(m.start(), text[m.start()-50:m.start()+250]) for m in re.finditer(r'unlockVaultWithPassword', text)]
for pos, snip in matches:
    print(f"--- MATCH AT {pos} ---")
    print(snip)
