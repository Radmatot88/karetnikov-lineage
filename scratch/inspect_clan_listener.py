with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    text = f.read()

import re
m = re.search(r'document\.querySelectorAll\(\'#scrollClanPills \.scroll-clan-pill\'\)\.forEach\(pill => \{.*?\}\);', text, re.DOTALL)
if m:
    print(m.group(0))
else:
    print("Could not find scrollClanPills click listener")
