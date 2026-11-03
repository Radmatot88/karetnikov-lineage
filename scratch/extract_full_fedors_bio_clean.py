import re

file_path = r"C:\Users\User\.gemini\antigravity\brain\f7447a8b-4633-4bc2-9dbe-695375c5f1cd\.system_generated\steps\98\content.md"

with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# strip html tags first
text_clean = re.sub(r'<[^>]+>', ' ', text)
text_clean = re.sub(r'\s+', ' ', text_clean)

idx = text_clean.find("Каретников родился в 1923")
if idx != -1:
    start = max(0, idx - 500)
    end = min(len(text_clean), idx + 3500)
    print(text_clean[start:end])
else:
    print("Not found by exact match")
