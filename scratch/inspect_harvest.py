import json
import os

with open('data/research_sprint/local_corpus_harvest.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Type of data:", type(data))
if isinstance(data, dict):
    print("Keys:", list(data.keys()))
    for k in data:
        val = data[k]
        print(f"Key: {k}, type: {type(val)}, len: {len(val) if hasattr(val, '__len__') else 'N/A'}")
elif isinstance(data, list):
    print("List len:", len(data))
    if len(data) > 0:
        print("First item type:", type(data[0]))
