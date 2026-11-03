#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Применение эпистемического обогащения в scripts/build_lineage_dataset.py.
"""

from pathlib import Path

target_file = Path(r"c:\Karetnikov_Lineage\scripts\build_lineage_dataset.py")
content = target_file.read_text(encoding="utf-8")

# 1. Перед nodes.append(node) вставляем определение полей
tagging_code = '''        is_fact = (n in FACT_AHNENTAFELS_DIRECT)
        node["is_fact_confirmed"] = is_fact
        if is_fact:
            node["epistemic_level"] = "LEVEL_1_FACT"
            node["fact_certificate"] = FACT_CERTIFICATES.get(n)
        elif n in (12, 16, 18, 28, 56) or node.get("status") == "FAMILY_ORAL":
            node["epistemic_level"] = "LEVEL_2_PRIMARY_HYPOTHESIS"
            node["fact_certificate"] = None
        elif node.get("status") == "ARCHIVE_CANDIDATE":
            node["epistemic_level"] = "LEVEL_3_SECONDARY_HYPOTHESIS"
            node["fact_certificate"] = None
        elif node.get("status") == "UNKNOWN_SLOT":
            node["epistemic_level"] = "LEVEL_0_UNKNOWN"
            node["fact_certificate"] = None
        else:
            node["epistemic_level"] = "LEVEL_4_TERTIARY_HYPOTHESIS"
            node["fact_certificate"] = None

        nodes.append(node)'''

content = content.replace("        nodes.append(node)", tagging_code, 1)

# 2. В build_collateral_relatives:
content = content.replace(
    'def build_collateral_relatives():\n    """Боковые родственные ветви (подтвержденные братья и сестры)."""\n    return [',
    'def build_collateral_relatives():\n    """Боковые родственные ветви (подтвержденные братья и сестры)."""\n    relatives = ['
)

collateral_return = '''    ]
    for c in relatives:
        ah = c["ahnentafel"]
        is_fact = (ah in FACT_AHNENTAFELS_COLLATERAL)
        c["is_fact_confirmed"] = is_fact
        if is_fact:
            c["epistemic_level"] = "LEVEL_1_FACT"
            c["fact_certificate"] = FACT_CERTIFICATES.get(ah)
        elif ah == 403:
            c["epistemic_level"] = "LEVEL_2_PRIMARY_HYPOTHESIS"
            c["fact_certificate"] = None
        else:
            c["epistemic_level"] = "LEVEL_3_SECONDARY_HYPOTHESIS"
            c["fact_certificate"] = None
    return relatives'''

content = content.replace(
    '            }\n        }\n    ]\n\n\ndef build_floating_hypotheses():',
    '            }\n        }' + '\n' + collateral_return + '\n\n\ndef build_floating_hypotheses():'
)

# 3. В main() добавляем stats
stats_code = '''    facts_direct_count = sum(1 for x in nodes if x.get("is_fact_confirmed"))
    facts_collateral_count = sum(1 for x in collateral if x.get("is_fact_confirmed"))
    facts_total_count = facts_direct_count + facts_collateral_count

    payload = {
        "meta": {
            "project": "Karetnikov Sovereign Heritage Archive",
            "owner": "Граф Каретников (Каретников Дмитрий Иванович)",
            "ui_role_title": "Администратор и Хранитель архива (Дмитрий Иванович Каретников)",
            "generated_at": datetime.now().isoformat(),
            "generations_count": 7,
            "total_direct_slots": 127,
            "collateral_count": len(collateral),
            "floating_hypotheses_count": len(floating),
            "stats": {
                "facts_count": facts_total_count,
                "facts_direct_count": facts_direct_count,
                "facts_collateral_count": facts_collateral_count,
                "total_all_nodes": len(nodes) + len(collateral),
                "confirmed_doc": confirmed_count,'''

content = content.replace(
    '''    payload = {
        "meta": {
            "project": "Karetnikov Sovereign Heritage Archive",
            "owner": "Граф Каретников (Каретников Дмитрий Иванович)",
            "ui_role_title": "Администратор и Хранитель архива (Дмитрий Иванович Каретников)",
            "generated_at": datetime.now().isoformat(),
            "generations_count": 7,
            "total_direct_slots": 127,
            "collateral_count": len(collateral),
            "floating_hypotheses_count": len(floating),
            "stats": {
                "confirmed_doc": confirmed_count,''',
    stats_code
)

target_file.write_text(content, encoding="utf-8")
print("[OK] Successfully injected facts enrichment into build_lineage_dataset.py")
