import re

with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    text = f.read()

# Emoji regex covering standard emojis
emoji_pattern = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # geometric shapes extended
    "\U0001F800-\U0001F8FF"  # supplemental arrows
    "\U0001F900-\U0001F9FF"  # supplemental symbols and pictographs
    "\U0001FA00-\U0001FA6F"  # chess symbols
    "\U0001FA70-\U0001FAFF"  # symbols and pictographs extended-a
    "\U00002702-\U000027B0"  # dingbats
    "\U000024C2-\U0001F251"
    "\U00002600-\U000026FF"  # misc symbols (cross, stars, etc)
    "]+", flags=re.UNICODE
)

lines = text.split("\n")
emojis_found = []
for i, l in enumerate(lines):
    matches = emoji_pattern.findall(l)
    if matches:
        emojis_found.append((i+1, matches, l.strip()[:90]))

print(f"Total lines with emojis: {len(emojis_found)}")
for line_no, emjs, snippet in emojis_found[:40]:
    print(f"L{line_no}: {emjs} | {snippet}")
if len(emojis_found) > 40:
    print(f"... and {len(emojis_found) - 40} more lines")
