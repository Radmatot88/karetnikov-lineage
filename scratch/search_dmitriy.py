import os
import json
import re

def search_text_files(base_dir, query):
    results = []
    for root, dirs, files in os.walk(base_dir):
        if "node_modules" in root or ".git" in root or ".astro" in root:
            continue
        for f in files:
            if f.endswith(('.md', '.json', '.ged', '.txt', '.ts', '.mjs')):
                path = os.path.join(root, f)
                try:
                    with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                        content = fp.read()
                        if re.search(query, content, re.IGNORECASE):
                            results.append(path)
                except Exception as e:
                    pass
    return results

if __name__ == "__main__":
    base = r"C:\Karetnikov_Lineage"
    print("Files matching 'Дмитрий' or '1913':")
    matches = search_text_files(base, r"1913|Дмитрий|Владимировк|Шаталовк")
    for m in matches:
        print(m)
