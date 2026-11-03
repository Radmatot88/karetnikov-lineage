import re

file_path = r"C:\Users\User\.gemini\antigravity\brain\f7447a8b-4633-4bc2-9dbe-695375c5f1cd\.system_generated\steps\98\content.md"

with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

m = re.search(r"Фёдор Иванович Каретников", text)
if m:
    start = max(0, m.start() - 1000)
    end = min(len(text), m.end() + 4000)
    snippet = text[start:end]
    # strip html
    clean = re.sub(r'<[^>]+>', '\n', snippet)
    clean = re.sub(r'\n+', '\n', clean)
    print(clean)
