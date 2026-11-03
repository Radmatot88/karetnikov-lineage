import json

with open(r"C:\Karetnikov_Lineage\data\vault\osint_wave2_findings.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Find any dict or item where name has "Дмитрий" or "Иван Дмитриевич" or "1913"
def recursive_search(obj, path=""):
    if isinstance(obj, dict):
        obj_str = json.dumps(obj, ensure_ascii=False)
        if "Каретников Иван Дмитриевич" in obj_str or "Каретников Дмитрий Иванович" in obj_str or "1913" in obj_str:
            # check if this is an item
            if "full_name" in obj or "id" in obj:
                print(f"PATH: {path}")
                print(json.dumps(obj, ensure_ascii=False, indent=2))
                print("-" * 50)
            else:
                for k, v in obj.items():
                    recursive_search(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            recursive_search(item, f"{path}[{idx}]")

recursive_search(data)
