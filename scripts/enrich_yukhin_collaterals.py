import json
from datetime import datetime

with open("data/vault/lineage_graph.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 1. Update direct nodes
for node in data["nodes"]:
    if node["id"] == "P002":
        node["birth_date"] = "03.01.1969"
        node["birth_year"] = "1969"
        node["death_date"] = "05.01.2025"
        node["death_year"] = "2025"
        node["is_alive"] = False
        if "dossier_12_rubrics" in node and "rubric_03_life_milestones" in node["dossier_12_rubrics"]:
            node["dossier_12_rubrics"]["rubric_03_life_milestones"]["birth_date_display"] = "03.01.1969"
            node["dossier_12_rubrics"]["rubric_03_life_milestones"]["birth_year"] = "1969"
            node["dossier_12_rubrics"]["rubric_03_life_milestones"]["death_date_display"] = "05.01.2025"
            node["dossier_12_rubrics"]["rubric_03_life_milestones"]["death_year"] = "2025"
            node["dossier_12_rubrics"]["rubric_03_life_milestones"]["is_alive"] = False
    elif node["id"] == "P004":
        node["birth_date"] = "1937"
        node["birth_year"] = "1937"
        node["death_date"] = "2000"
        node["death_year"] = "2000"
        node["is_alive"] = False
        if "dossier_12_rubrics" in node and "rubric_03_life_milestones" in node["dossier_12_rubrics"]:
            node["dossier_12_rubrics"]["rubric_03_life_milestones"]["birth_date_display"] = "1937"
            node["dossier_12_rubrics"]["rubric_03_life_milestones"]["birth_year"] = "1937"
            node["dossier_12_rubrics"]["rubric_03_life_milestones"]["death_date_display"] = "2000"
            node["dossier_12_rubrics"]["rubric_03_life_milestones"]["death_year"] = "2000"
            node["dossier_12_rubrics"]["rubric_03_life_milestones"]["is_alive"] = False
    elif node["id"] == "P005":
        node["birth_date"] = "1936"
        node["birth_year"] = "1936"
        node["death_date"] = "2011 / 2013"
        node["death_year"] = "2011 / 2013"
        node["is_alive"] = False
        if "dossier_12_rubrics" in node and "rubric_03_life_milestones" in node["dossier_12_rubrics"]:
            node["dossier_12_rubrics"]["rubric_03_life_milestones"]["birth_date_display"] = "1936"
            node["dossier_12_rubrics"]["rubric_03_life_milestones"]["birth_year"] = "1936"
            node["dossier_12_rubrics"]["rubric_03_life_milestones"]["death_date_display"] = "2011 / 2013"
            node["dossier_12_rubrics"]["rubric_03_life_milestones"]["death_year"] = "2011 / 2013"
            node["dossier_12_rubrics"]["rubric_03_life_milestones"]["is_alive"] = False

# 2. Check and append C048, C049, C050, C051
collaterals = data.get("collateral_nodes", [])
existing_ids = {c["id"] for c in collaterals}

new_nodes = [
    {
        "id": "C048",
        "ahnentafel": 1002,
        "node_type": "COLLATERAL_RELATIVE",
        "visibility": "public_family",
        "is_collateral": True,
        "sibling_of_ahnentafel": 5,
        "parent_ahnentafel": 10,
        "generation": 3,
        "generation_label": "III колено — Родные братья бабушки Клавдии",
        "era": "XX век",
        "branch": "paternal",
        "sub_clan": "Род Юхиных (с. Четыровка на р. Кондурче)",
        "full_name": "Юхин Василий Петрович",
        "surname": "Юхин",
        "first_name": "Василий",
        "patronymic": "Петрович",
        "gender": "M",
        "birth_date": "~1920–1935",
        "birth_year": "~1920–1935",
        "death_date": "XX век",
        "death_year": "XX век",
        "is_alive": False,
        "birth_place": "Самарская (Куйбышевская) обл., Кошкинский р-н, с. Четыровка",
        "status": "ARCHIVE_CANDIDATE",
        "confidence": 75,
        "role_label": "Вероятный родной брат бабушки Клавдии Петровны Юхиной (Двоюродный дед)",
        "notes": "Вероятный родной брат бабушки Клавдии Петровны Каретниковой (Юхиной, #5), сын прадеда Петра Юхина (#10) из старинного села Четыровка на реке Кондурче.",
        "sources": [
            "Семейная память и архивно-историческое досье рода Юхиных (Кошкинский район)",
            "АИС ЦГАСО Ф. 32 (Метрические книги Самарского уезда)"
        ],
        "photo_url": None,
        "burial_info": {
            "status": "DECEASED",
            "cemetery": "Самарская область",
            "plot": None,
            "confirmed": False
        },
        "is_fact_confirmed": False,
        "epistemic_level": "LEVEL_3_ARCHIVE_CANDIDATE"
    },
    {
        "id": "C049",
        "ahnentafel": 1003,
        "node_type": "COLLATERAL_RELATIVE",
        "visibility": "public_family",
        "is_collateral": True,
        "sibling_of_ahnentafel": 5,
        "parent_ahnentafel": 10,
        "generation": 3,
        "generation_label": "III колено — Родные братья бабушки Клавдии",
        "era": "XX век",
        "branch": "paternal",
        "sub_clan": "Род Юхиных (с. Четыровка на р. Кондурче)",
        "full_name": "Юхин Михаил Петрович",
        "surname": "Юхин",
        "first_name": "Михаил",
        "patronymic": "Петрович",
        "gender": "M",
        "birth_date": "~1900–1920",
        "birth_year": "~1900–1920",
        "death_date": "XX век",
        "death_year": "XX век",
        "is_alive": False,
        "birth_place": "Самарская (Куйбышевская) обл., Кошкинский р-н, с. Четыровка",
        "status": "ARCHIVE_CANDIDATE",
        "confidence": 75,
        "role_label": "Вероятный родной брат бабушки Клавдии Петровны Юхиной (Двоюродный дед)",
        "notes": "Вероятный родной брат бабушки Клавдии Петровны Каретниковой (Юхиной, #5), сын прадеда Петра Юхина (#10). Вероятный отец участника Великой Отечественной войны Николая Михайловича Юхина (р. 1926).",
        "sources": [
            "Семейная память и архивно-историческое досье рода Юхиных (Кошкинский район)",
            "ЦАМО РФ («Память Народа»)"
        ],
        "photo_url": None,
        "burial_info": {
            "status": "DECEASED",
            "cemetery": "Самарская область",
            "plot": None,
            "confirmed": False
        },
        "is_fact_confirmed": False,
        "epistemic_level": "LEVEL_3_ARCHIVE_CANDIDATE"
    },
    {
        "id": "C050",
        "ahnentafel": 1004,
        "node_type": "COLLATERAL_RELATIVE",
        "visibility": "public_family",
        "is_collateral": True,
        "sibling_of_ahnentafel": 5,
        "parent_ahnentafel": 10,
        "generation": 3,
        "generation_label": "III колено — Сельский учитель и краевед Четыровки",
        "era": "XX век",
        "branch": "paternal",
        "sub_clan": "Род Юхиных (с. Четыровка на р. Кондурче)",
        "full_name": "Юхин Борис Иванович",
        "surname": "Юхин",
        "first_name": "Борис",
        "patronymic": "Иванович",
        "gender": "M",
        "birth_date": "XX век",
        "birth_year": "XX век",
        "death_date": "XX век",
        "death_year": "XX век",
        "is_alive": False,
        "birth_place": "Самарская (Куйбышевская) обл., Кошкинский р-н, с. Четыровка",
        "status": "FAMILY_ORAL",
        "confidence": 85,
        "role_label": "Сельский учитель, просветитель и краевед села Четыровка",
        "notes": "Уважаемый сельский педагог, учитель и краевед-подвижник села Четыровка Кошкинского района на реке Кондурче. Собирал устные воспоминания старожилов д. Четыровка и с. Надеждино, сохранил для потомков память об основании села государственными крестьянами-переселенцами в 1840-х годах.",
        "sources": [
            "Семейная память рода Юхиных (85%)",
            "Краеведческие хроники Кошкинского района Самарской области"
        ],
        "photo_url": None,
        "burial_info": {
            "status": "DECEASED",
            "cemetery": "с. Четыровка Кошкинского р-на",
            "plot": None,
            "confirmed": False
        },
        "is_fact_confirmed": True,
        "epistemic_level": "LEVEL_2_FAMILY_ORAL"
    },
    {
        "id": "C051",
        "ahnentafel": 1005,
        "node_type": "COLLATERAL_RELATIVE",
        "visibility": "public_family",
        "is_collateral": True,
        "sibling_of_ahnentafel": None,
        "parent_ahnentafel": None,
        "generation": 3,
        "generation_label": "III колено — Ветеран Великой Отечественной войны",
        "era": "1926 — после 1985",
        "branch": "paternal",
        "sub_clan": "Род Юхиных (д. Дмитриевка / с. Четыровка)",
        "full_name": "Юхин Николай Михайлович",
        "surname": "Юхин",
        "first_name": "Николай",
        "patronymic": "Михайлович",
        "gender": "M",
        "birth_date": "1926",
        "birth_year": "1926",
        "death_date": "После 1985",
        "death_year": "После 1985",
        "is_alive": False,
        "birth_place": "Куйбышевская обл., Кошкинский р-н, д. Дмитриевка (5 км от с. Четыровка)",
        "status": "ARCHIVE_CANDIDATE",
        "confidence": 75,
        "role_label": "Ветеран ВОВ • Красноармеец 5 зсд, сапер 33 осапб, орден Отеч. войны II ст.",
        "notes": "Уроженец деревни Дмитриевка Кошкинского района (5 км от с. Четыровка). Призван Елховским РВК в 1943 г., красноармеец 5-й запасной стрелковой дивизии, сапер 33-го отдельного саперного батальона. Кавалер ордена Отечественной войны II ст. (1985 г.). Вероятный сын Михаила Петровича Юхина.",
        "sources": [
            "ЦАМО РФ («Память Народа» / Юбилейная картотека 1985 г., запись № 1524856087)"
        ],
        "photo_url": None,
        "burial_info": {
            "status": "DECEASED",
            "cemetery": "Самарская область",
            "plot": None,
            "confirmed": False
        },
        "is_fact_confirmed": True,
        "epistemic_level": "LEVEL_3_ARCHIVE_CANDIDATE"
    }
]

for n in new_nodes:
    if n["id"] not in existing_ids:
        collaterals.append(n)
        existing_ids.add(n["id"])

data["collateral_nodes"] = collaterals
data["meta"]["collateral_count"] = len(collaterals)

# 3. Recount stats
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

print(f"Successfully updated lineage_graph.json. Total collaterals: {len(collaterals)}, total facts: {total_facts}")
