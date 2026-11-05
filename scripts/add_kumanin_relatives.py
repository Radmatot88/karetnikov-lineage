import json
from datetime import datetime

with open("data/vault/lineage_graph.json", "r", encoding="utf-8") as f:
    data = json.load(f)

collaterals = data.get("collateral_nodes", [])
existing_ids = {c["id"] for c in collaterals}

new_kumanins = [
    {
        "id": "C052",
        "ahnentafel": 703,
        "node_type": "COLLATERAL_RELATIVE",
        "visibility": "public_family",
        "is_collateral": True,
        "sibling_of_ahnentafel": 7,
        "parent_ahnentafel": 14,
        "generation": 3,
        "generation_label": "III колено — Родной брат бабушки Валентины",
        "era": "XX век — рубеж XXI века",
        "branch": "maternal",
        "sub_clan": "Род Куманиных (с. Новый Шуструй → г. Самара)",
        "full_name": "Куманин Николай Сергеевич",
        "surname": "Куманин",
        "first_name": "Николай",
        "patronymic": "Сергеевич",
        "gender": "M",
        "birth_date": "Уточняется у матери",
        "birth_year": "XX век",
        "death_date": "Уточняется (г. Самара)",
        "death_year": "XX век / нач. XXI века",
        "is_alive": False,
        "birth_place": "Пензенская обл., Нижнеломовский р-н, с. Новый Шуструй (предположительно)",
        "status": "FAMILY_ORAL",
        "confidence": 95,
        "role_label": "Родной брат бабушки Валентины Сергеевны (Двоюродный дед Пробанда)",
        "notes": "Родной брат бабушки Валентины Сергеевны Зубковой (Куманиной, #7), а также сестёр Зинаиды Сергеевны Котельниковой (#C007) и Антонины Сергеевны (#C008). Сын Сергея Степановича Куманина (#14) и Евдокии Григорьевны (#15). Родился предположительно в с. Новый Шуструй Пензенской области, переехал в Самару (Куйбышев), где жил, трудился и ушёл из жизни. Отец Анны Николаевны Куманиной (#C053). Точные годы жизни уточняются у Светланы Владимировны.",
        "sources": [
            "Семейные свидетельства Графа Каретникова",
            "Семейный архив линии Куманиных (с. Новый Шуструй — г. Самара)"
        ],
        "photo_url": None,
        "burial_info": {
            "status": "DECEASED",
            "cemetery": "г. Самара",
            "plot": None,
            "confirmed": False
        },
        "is_fact_confirmed": True,
        "epistemic_level": "LEVEL_2_FAMILY_ORAL"
    },
    {
        "id": "C053",
        "ahnentafel": 704,
        "node_type": "COLLATERAL_RELATIVE",
        "visibility": "public_family",
        "is_collateral": True,
        "sibling_of_ahnentafel": None,
        "parent_ahnentafel": 703,
        "generation": 2,
        "generation_label": "II колено — Двоюродная сестра матери",
        "era": "XX — XXI век",
        "branch": "maternal",
        "sub_clan": "Род Куманиных (г. Самара)",
        "full_name": "Куманина Анна Николаевна",
        "surname": "Куманина",
        "first_name": "Анна",
        "patronymic": "Николаевна",
        "gender": "F",
        "birth_date": "Уточняется",
        "birth_year": "XX век",
        "death_date": None,
        "death_year": None,
        "is_alive": True,
        "birth_place": "г. Самара (Куйбышев)",
        "status": "FAMILY_ORAL",
        "confidence": 95,
        "role_label": "Дочь Николая Сергеевича (Двоюродная сестра матери, двоюродная тётя Пробанда)",
        "notes": "Дочь Николая Сергеевича Куманина (#C052), внучка прадеда Сергея Степановича Куманина (#14) и Евдокии Григорьевны (#15). Двоюродная сестра матери Пробанда Светланы Владимировны Каретниковой (Зубковой). Проживает в г. Самаре.",
        "sources": [
            "Семейные свидетельства Графа Каретникова"
        ],
        "photo_url": None,
        "burial_info": {
            "status": "ALIVE",
            "cemetery": None,
            "plot": None,
            "confirmed": False
        },
        "is_fact_confirmed": True,
        "epistemic_level": "LEVEL_2_FAMILY_ORAL"
    }
]

for node in new_kumanins:
    if node["id"] not in existing_ids:
        collaterals.append(node)
        existing_ids.add(node["id"])

data["collateral_nodes"] = collaterals
data["meta"]["collateral_count"] = len(collaterals)

# Recount stats
confirmed_doc = sum(1 for n in data["nodes"] if n.get("status") == "CONFIRMED_DOC") + sum(1 for c in collaterals if c.get("status") == "CONFIRMED_DOC")
family_oral = sum(1 for n in data["nodes"] if n.get("status") == "FAMILY_ORAL") + sum(1 for c in collaterals if c.get("status") == "FAMILY_ORAL")
archive_candidate = sum(1 for n in data["nodes"] if n.get("status") == "ARCHIVE_CANDIDATE") + sum(1 for c in collaterals if c.get("status") == "ARCHIVE_CANDIDATE")
unknown_slot = sum(1 for n in data["nodes"] if n.get("status") == "UNKNOWN_SLOT")

facts_direct = sum(1 for n in data["nodes"] if n.get("is_fact_confirmed", False) or n.get("status") in ["CONFIRMED_DOC", "FAMILY_ORAL"])
facts_collateral = sum(1 for c in collaterals if c.get("is_fact_confirmed", False) or c.get("status") in ["CONFIRMED_DOC", "FAMILY_ORAL"])
total_facts = facts_direct + facts_collateral

data["meta"]["stats"]["total_collateral_nodes"] = len(collaterals)
data["meta"]["stats"]["total_all_nodes"] = len(data["nodes"]) + len(collaterals)
data["meta"]["stats"]["confirmed_doc"] = confirmed_doc
data["meta"]["stats"]["family_oral"] = family_oral
data["meta"]["stats"]["archive_candidate"] = archive_candidate
data["meta"]["stats"]["unknown_slot"] = unknown_slot
data["meta"]["stats"]["facts_direct_count"] = facts_direct
data["meta"]["stats"]["facts_collateral_count"] = facts_collateral
data["meta"]["stats"]["facts_count"] = total_facts
data["meta"]["stats"]["active_knowledge_nodes"] = confirmed_doc + family_oral + archive_candidate
data["meta"]["generated_at"] = datetime.now().isoformat()

with open("data/vault/lineage_graph.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully added C052 and C053. Total collaterals: {len(collaterals)}, total facts: {total_facts}")
