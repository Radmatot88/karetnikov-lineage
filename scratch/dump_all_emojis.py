import re

with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    lines = f.readlines()

emoji_pattern = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"
    "\U0001F300-\U0001F5FF"
    "\U0001F600-\U0001F64F"
    "\U0001F680-\U0001F6FF"
    "\U0001F700-\U0001F77F"
    "\U0001F780-\U0001F7FF"
    "\U0001F800-\U0001F8FF"
    "\U0001F900-\U0001F9FF"
    "\U0001FA00-\U0001FA6F"
    "\U0001FA70-\U0001FAFF"
    "\U00002702-\U000027B0"
    "\U00002600-\U000026FF"
    "]+", flags=re.UNICODE
)

for i, l in enumerate(lines):
    found = emoji_pattern.findall(l)
    if found:
        print(f"L{i+1}: {found} => {l.strip()[:80]}")
