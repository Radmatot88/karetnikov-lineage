import os
import re

query = r"Капров|Марина Антоновна|1885|Иван Дмитриевич|Шаталовк"
for root, dirs, files in os.walk(r"C:\Karetnikov_Lineage"):
    if any(p in root for p in [".git", "node_modules", ".astro"]):
        continue
    for f in files:
        if f.endswith(('.md', '.json', '.ged', '.txt')):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                    matches = list(re.finditer(query, content, re.IGNORECASE))
                    if matches:
                        print(f"File {p}: {len(matches)} matches")
                        for m in matches[:5]:
                            start = max(0, m.start() - 50)
                            end = min(len(content), m.end() + 50)
                            snippet = content[start:end].replace('\n', ' ')
                            print(f"   [{snippet}]")
            except Exception as e:
                pass
