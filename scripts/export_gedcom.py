#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Генератор международного генеалогического файла GEDCOM 5.5.1 из data/vault/lineage_graph.json.
Позволяет импортировать древо Каретниковых — Юхиных — Зубковых — Куманиных в Gramps, Familio, FamilySearch, Geni, MyHeritage.
Включает 127 прямых предков (I-VII колена) + 47 боковых родственников.
"""

import json
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).resolve().parent.parent
GRAPH_PATH = PROJECT_ROOT / "data" / "vault" / "lineage_graph.json"
GED_PATH = PROJECT_ROOT / "data" / "vault" / "karetnikov_lineage.ged"


def export_gedcom():
    data = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    nodes = {n["ahnentafel"]: n for n in data["nodes"]}
    collateral_nodes = data.get("collateral_nodes", [])

    lines = [
        "0 HEAD",
        "1 SOUR KARETNIKOV_HERITAGE_ARCHIVE",
        "2 VERS 1.0",
        "2 NAME Karetnikov Sovereign Heritage Archive (7 Generations + Collaterals)",
        f"1 DATE {datetime.now().strftime('%d %b %Y').upper()}",
        "1 GEDC",
        "2 VERS 5.5.1",
        "2 FORM LINEAGE-LINKED",
        "1 CHAR UTF-8",
        "1 SUBM @SUBM1@",
        "0 @SUBM1@ SUBM",
        "1 NAME Каретников Дмитрий Иванович"
    ]

    # Экспортируем все активные и зарезервированные прямые узлы (1..127)
    for n_id, node in sorted(nodes.items()):
        indi_id = f"@I{n_id:03d}@"
        given = f"{node['first_name']} {node['patronymic']}".strip()
        surname = node["surname"]
        lines.append(f"0 {indi_id} INDI")
        lines.append(f"1 NAME {given} /{surname}/")
        lines.append(f"2 GIVN {given}")
        lines.append(f"2 SURN {surname}")
        lines.append(f"1 SEX {node['gender']}")
        lines.append("1 BIRT")
        if node.get("birth_date"):
            lines.append(f"2 DATE {node['birth_date']}")
        if node.get("birth_place"):
            lines.append(f"2 PLAC {node['birth_place']}")
        if node.get("death_date"):
            lines.append("1 DEAT")
            lines.append(f"2 DATE {node['death_date']}")
        lines.append(f"1 NOTE [Ahnentafel #{n_id} | {node['status']}] {node['notes']}")

        # Семья, где этот человек — ребенок (родители 2*n и 2*n+1)
        if node["generation"] < 7:
            lines.append(f"1 FAMC @F{n_id:03d}@")
        # Семья, где этот человек — супруг/родитель (для ребенка n // 2)
        if n_id > 1:
            child_n = n_id // 2
            lines.append(f"1 FAMS @F{child_n:03d}@")

    # Экспортируем боковых родственников
    for c_node in collateral_nodes:
        c_id = c_node.get("id", "")
        indi_id = f"@{c_id}@"
        first = c_node.get("first_name") or ""
        patr = c_node.get("patronymic") or ""
        given = f"{first} {patr}".strip()
        surname = c_node.get("surname") or ""
        if not surname and not given:
            given = c_node.get("full_name") or "Родственник"
        lines.append(f"0 {indi_id} INDI")
        lines.append(f"1 NAME {given} /{surname}/")
        if given:
            lines.append(f"2 GIVN {given}")
        if surname:
            lines.append(f"2 SURN {surname}")
        lines.append(f"1 SEX {c_node.get('gender', 'M')}")
        b_date = c_node.get("birth_date") or c_node.get("birth_year")
        if b_date and b_date != "Уточняется":
            lines.append("1 BIRT")
            lines.append(f"2 DATE {b_date}")
        if c_node.get("birth_place"):
            lines.append(f"2 PLAC {c_node['birth_place']}")
        if c_node.get("death_date"):
            lines.append("1 DEAT")
            lines.append(f"2 DATE {c_node['death_date']}")
        lines.append(f"1 NOTE [Collateral {c_id} | {c_node.get('role_label', '')}] {c_node.get('notes', '')}")

    # Экспортируем 63 прямые семейные ячейки (для поколений 1..6)
    for child_n in range(1, 64):
        fam_id = f"@F{child_n:03d}@"
        husb_n = 2 * child_n
        wife_n = 2 * child_n + 1
        lines.append(f"0 {fam_id} FAM")
        lines.append(f"1 HUSB @I{husb_n:03d}@")
        lines.append(f"1 WIFE @I{wife_n:03d}@")
        lines.append(f"1 CHIL @I{child_n:03d}@")

    lines.append("0 TRLR")
    GED_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[OK] Exported GEDCOM 5.5.1 ({len(nodes)} direct + {len(collateral_nodes)} collateral, 63 families) to: {GED_PATH}")


if __name__ == "__main__":
    export_gedcom()
