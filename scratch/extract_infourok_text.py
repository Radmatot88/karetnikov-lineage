import re

file_path = r"C:\Users\User\.gemini\antigravity\brain\f7447a8b-4633-4bc2-9dbe-695375c5f1cd\.system_generated\steps\98\content.md"

with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# search for Karetnikov in text
matches = list(re.finditer(r"Каретников[а-я]*", text, re.IGNORECASE))
print(f"Total mentions of Каретников: {len(matches)}")

for m in matches:
    start = max(0, m.start() - 200)
    end = min(len(text), m.end() + 200)
    print("--- MATCH ---")
    snippet = re.sub(r'<[^>]+>', ' ', text[start:end])
    snippet = re.sub(r'\s+', ' ', snippet)
    print(snippet)

