import os
import re

brothers = ["Павел Иванович", "Косма Иванович", "Кузьма Иванович", "Михаил Иванович", "Дмитрий Иванович", "Федор Иванович", "Фёдор Иванович", "Григорий Иванович"]

for root, dirs, files in os.walk(r"C:\Karetnikov_Lineage"):
    if any(p in root for p in [".git", "node_modules", ".astro"]):
        continue
    for f in files:
        if f.endswith(('.md', '.json', '.ged', '.txt')):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                    for b in brothers:
                        if b in content:
                            print(f"[{b}] found in {p}")
            except Exception as e:
                pass
