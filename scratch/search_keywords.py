import json

with open('data/research_sprint/local_corpus_harvest.json', 'r', encoding='utf-8') as f:
    text = f.read()

keywords = ['куман', 'шуструй', 'ломов', 'зубков']
for kw in keywords:
    count = text.lower().count(kw)
    print(f"Keyword '{kw}': {count} occurrences")
