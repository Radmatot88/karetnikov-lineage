import json

with open(r"C:\Karetnikov_Lineage\data\vault\osint_wave2_findings.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Look at 1_orenburg_karetnikovs in detail
ob = data.get("branch_findings", {}).get("1_orenburg_karetnikovs", {})
print("1_orenburg_karetnikovs keys:", ob.keys())

for k in ob:
    val = ob[k]
    val_str = json.dumps(val, ensure_ascii=False)
    if any(x in val_str for x in ["Дмитрий", "Иван Дмитриевич", "1913", "Владимировка", "Шаталовка"]):
        print(f"\n=== KEY: {k} ===")
        print(json.dumps(val, ensure_ascii=False, indent=2))
