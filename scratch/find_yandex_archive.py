import os
import re

query = r"83783b5b|5ed7e09a|19.09.1913|Каретников Дмитрий Иванович.*1913"
for root, dirs, files in os.walk(r"C:\Karetnikov_Lineage"):
    if any(p in root for p in [".git", "node_modules", ".astro"]):
        continue
    for f in files:
        if f.endswith(('.md', '.json', '.ged', '.txt')):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                    if re.search(query, content, re.IGNORECASE):
                        print(f"MATCH in {p}")
            except Exception as e:
                pass
