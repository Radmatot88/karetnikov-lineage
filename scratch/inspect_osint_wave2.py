import json

with open(r"C:\Karetnikov_Lineage\data\vault\osint_wave2_findings.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Keys in osint_wave2_findings.json:", data.keys())

# Let's inspect the entire json structure or relevant parts
for k, v in data.items():
    print(f"\n--- KEY: {k} ---")
    if isinstance(v, list):
        print(f"List with {len(v)} items")
        for item in v:
            item_str = json.dumps(item, ensure_ascii=False)
            if any(term in item_str for term in ["Дмитрий", "1913", "Иван Дмитриевич", "Марина Антоновна", "Капрова", "Владимировка", "Шаталовка"]):
                print(json.dumps(item, ensure_ascii=False, indent=2))
    elif isinstance(v, dict):
        print(f"Dict with {len(v)} keys")
        for subk, subv in v.items():
            sub_str = json.dumps(subv, ensure_ascii=False)
            if any(term in sub_str for term in ["Дмитрий", "1913", "Иван Дмитриевич", "Марина Антоновна", "Капрова", "Владимировка", "Шаталовка"]):
                print(f"Subkey: {subk}")
                print(json.dumps(subv, ensure_ascii=False, indent=2))
    else:
        print(v)
