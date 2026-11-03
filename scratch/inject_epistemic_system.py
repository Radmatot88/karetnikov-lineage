#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Обновление scripts/build_lineage_dataset.py для внедрения полей:
- is_fact_confirmed
- epistemic_level
- fact_certificate
"""

from pathlib import Path
import re

target_file = Path(r"c:\Karetnikov_Lineage\scripts\build_lineage_dataset.py")
content = target_file.read_text(encoding="utf-8")

# Заменим блок создания node в known
old_known_block = '''        if n in known:
            item = known[n]
            node = {
                "id": f"P{n:03d}",
                "ahnentafel": n,
                "is_collateral": False,
                "generation": gen,
                "generation_label": GEN_LABELS[gen],
                "era": GEN_ERA[gen],
                "branch": branch,
                "sub_clan": sub_clan,
                "full_name": item["full_name"],
                "surname": item["surname"],
                "maiden_name": item.get("maiden_name"),
                "first_name": item["first_name"],
                "patronymic": item["patronymic"],
                "gender": item["gender"],
                "birth_date": item["birth_date"],
                "birth_year": item["birth_year"],
                "death_date": item["death_date"],
                "birth_place": item["birth_place"],
                "status": item["status"],
                "confidence": item["confidence"],
                "role_label": item["role_label"],
                "notes": item["notes"],
                "sources": item["sources"],
                "photo_url": None,
                "father_ahnentafel": father_id,
                "mother_ahnentafel": mother_id,
                "child_ahnentafel": child_id
            }'''

new_known_block = '''        is_fact = (n in FACT_AHNENTAFELS_DIRECT)
        cert = FACT_CERTIFICATES.get(n) if is_fact else None

        if n in known:
            item = known[n]
            if is_fact:
                lvl = "LEVEL_1_FACT"
            elif n in (12, 16, 18, 28, 56) or item.get("status") == "FAMILY_ORAL":
                lvl = "LEVEL_2_PRIMARY_HYPOTHESIS"
            elif item.get("status") == "ARCHIVE_CANDIDATE":
                lvl = "LEVEL_3_SECONDARY_HYPOTHESIS"
            else:
                lvl = "LEVEL_0_UNKNOWN"

            node = {
                "id": f"P{n:03d}",
                "ahnentafel": n,
                "is_collateral": False,
                "is_fact_confirmed": is_fact,
                "epistemic_level": lvl,
                "fact_certificate": cert,
                "generation": gen,
                "generation_label": GEN_LABELS[gen],
                "era": GEN_ERA[gen],
                "branch": branch,
                "sub_clan": sub_clan,
                "full_name": item["full_name"],
                "surname": item["surname"],
                "maiden_name": item.get("maiden_name"),
                "first_name": item["first_name"],
                "patronymic": item["patronymic"],
                "gender": item["gender"],
                "birth_date": item["birth_date"],
                "birth_year": item["birth_year"],
                "death_date": item["death_date"],
                "birth_place": item["birth_place"],
                "status": item["status"],
                "confidence": item["confidence"],
                "role_label": item["role_label"],
                "notes": item["notes"],
                "sources": item["sources"],
                "photo_url": None,
                "father_ahnentafel": father_id,
                "mother_ahnentafel": mother_id,
                "child_ahnentafel": child_id
            }'''

# Заменим блок fallback else
old_fallback_block = '''            node = {
                "id": f"P{n:03d}",
                "ahnentafel": n,
                "is_collateral": False,
                "generation": gen,
                "generation_label": GEN_LABELS[gen],
                "era": GEN_ERA[gen],
                "branch": branch,
                "sub_clan": sub_clan,
                "full_name": f"Слот №{n} ({sub_clan.split('(')[0].strip()})",
                "surname": sub_clan.split()[1] if "Род" in sub_clan else "Уточняется",
                "maiden_name": None,
                "first_name": "Ожидает архивной выписки",
                "patronymic": "",
                "gender": gender,
                "birth_date": GEN_ERA[gen].split("(")[0].strip(),
                "birth_year": GEN_ERA[gen][:4],
                "death_date": None,
                "birth_place": region,
                "status": "UNKNOWN_SLOT",
                "confidence": 10,
                "role_label": f"{role_prefix} ({gen} колено, слот №{n})",
                "notes": f"Прямой слот №{n} по системе Соса-Страдоница ({GEN_LABELS[gen]}). Раскрывается при подъеме записи о рождении/браке потомка №{child_id} в архиве: {target_archive}.",
                "sources": [f"Целевой фонд: {target_archive}"],
                "photo_url": None,
                "father_ahnentafel": father_id,
                "mother_ahnentafel": mother_id,
                "child_ahnentafel": child_id
            }'''

new_fallback_block = '''            node = {
                "id": f"P{n:03d}",
                "ahnentafel": n,
                "is_collateral": False,
                "is_fact_confirmed": False,
                "epistemic_level": "LEVEL_0_UNKNOWN",
                "fact_certificate": None,
                "generation": gen,
                "generation_label": GEN_LABELS[gen],
                "era": GEN_ERA[gen],
                "branch": branch,
                "sub_clan": sub_clan,
                "full_name": f"Слот №{n} ({sub_clan.split('(')[0].strip()})",
                "surname": sub_clan.split()[1] if "Род" in sub_clan else "Уточняется",
                "maiden_name": None,
                "first_name": "Ожидает архивной выписки",
                "patronymic": "",
                "gender": gender,
                "birth_date": GEN_ERA[gen].split("(")[0].strip(),
                "birth_year": GEN_ERA[gen][:4],
                "death_date": None,
                "birth_place": region,
                "status": "UNKNOWN_SLOT",
                "confidence": 10,
                "role_label": f"{role_prefix} ({gen} колено, слот №{n})",
                "notes": f"Прямой слот №{n} по системе Соса-Страдоница ({GEN_LABELS[gen]}). Раскрывается при подъеме записи о рождении/браке потомка №{child_id} в архиве: {target_archive}.",
                "sources": [f"Целевой фонд: {target_archive}"],
                "photo_url": None,
                "father_ahnentafel": father_id,
                "mother_ahnentafel": mother_id,
                "child_ahnentafel": child_id
            }'''

# Заменим возврат collateral_relatives
old_collateral_end = '''    ]


def build_archive_leads():'''

new_collateral_end = '''    ]
    for c in relatives:
        ah = c["ahnentafel"]
        is_fact = (ah in FACT_AHNENTAFELS_COLLATERAL)
        c["is_fact_confirmed"] = is_fact
        c["fact_certificate"] = FACT_CERTIFICATES.get(ah) if is_fact else None
        if is_fact:
            c["epistemic_level"] = "LEVEL_1_FACT"
        elif ah == 403:
            c["epistemic_level"] = "LEVEL_2_PRIMARY_HYPOTHESIS"
        else:
            c["epistemic_level"] = "LEVEL_3_SECONDARY_HYPOTHESIS"
    return relatives


def build_archive_leads():'''

# Проверим, как объявлен список в build_collateral_relatives:
# return [ ... ] -> relatives = [ ... ]; return relatives
content = content.replace(old_known_block, new_known_block)
content = content.replace(old_fallback_block, new_fallback_block)

# В build_collateral_relatives заменяем 'return [' на 'relatives = ['
content = content.replace('def build_collateral_relatives():\n    """Боковые родственные ветви (родные братья деда и родной брат мамы + оренбургские потомки)."""\n    return [',
                          'def build_collateral_relatives():\n    """Боковые родственные ветви (родные братья деда и родной брат мамы + оренбургские потомки)."""\n    relatives = [')
content = content.replace(old_collateral_end, new_collateral_end)

# Обновим stats в main():
stats_replacement = '''    facts_count = sum(1 for x in nodes if x.get("is_fact_confirmed")) + sum(1 for x in collateral if x.get("is_fact_confirmed"))
    payload = {
        "meta": {
            "project": "Karetnikov Sovereign Heritage Archive",
            "owner": "Граф Каретников (Каретников Дмитрий Иванович)",
            "generated_at": datetime.now().isoformat(),
            "generations_count": 7,
            "total_direct_slots": 127,
            "collateral_count": len(collateral),
            "stats": {
                "facts_count": facts_count,
                "total_all_nodes": len(nodes) + len(collateral),
                "confirmed_doc": confirmed_count,
                "family_oral": oral_count,
                "archive_candidate": candidate_count,
                "unknown_slot": unknown_count,
                "active_knowledge_nodes": confirmed_count + oral_count + candidate_count + len(collateral),
                "completion_Gen1_3_percent": 100,
                "completion_Gen4_percent": 50
            },'''

content = re.sub(r'payload = \{\s*"meta": \{\s*"project": "Karetnikov Sovereign Heritage Archive",\s*"owner": "Граф Каретников \(Каретников Дмитрий Иванович\)",\s*"generated_at": datetime\.now\(\)\.isoformat\(\),\s*"generations_count": 7,\s*"total_direct_slots": 127,\s*"collateral_count": len\(collateral\),\s*"stats": \{\s*"confirmed_doc": confirmed_count,',
                 stats_replacement, content)

target_file.write_text(content, encoding="utf-8")
print("[OK] Upgraded build_lineage_dataset.py with epistemic system")
