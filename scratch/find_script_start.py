with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = re.findall(r'addEventListener\(["\']DOMContentLoaded["\']', text)
print("DOMContentLoaded listeners:", matches)
# Check what is at the start of <script is:inline>
pos = text.find("<script is:inline>")
print(text[pos:pos+400])
