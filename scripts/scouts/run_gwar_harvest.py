#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Прямой запуск GWAR 1914-1918 API-разведчика (на базе ex-ussr-kinship-research/scripts/gwar.py)
по 4 фамильным кластерам Графа Каретникова + боковым ветвям.
"""

import json
import sys
from pathlib import Path

SKILL_SCRIPTS = Path(r"C:\Родословная_ИИ\references\ex-ussr-kinship-research\scripts")
sys.path.insert(0, str(SKILL_SCRIPTS))

import gwar  # noqa: E402

OUT_DIR = Path(r"C:\Karetnikov_Lineage\data\research_sprint\gwar_1914_dumps")
OUT_DIR.mkdir(parents=True, exist_ok=True)

QUERIES = [
    {"id": "zubkov_shustruy", "label": "Зубковы (Шуструй / Пензенская)", "fields": {"last_name": "Зубков", "birth_place": "Шуструй"}},
    {"id": "kumanin_penza", "label": "Куманины (Пензенская губ.)", "fields": {"last_name": "Куманин", "birth_place_gubernia": "Пензенская"}},
    {"id": "kumanin_shustruy", "label": "Куманины (Шуструй)", "fields": {"last_name": "Куманин", "birth_place": "Шуструй"}},
    {"id": "yukhin_samara", "label": "Юхины (Самарская губ.)", "fields": {"last_name": "Юхин", "birth_place_gubernia": "Самарская"}},
    {"id": "karetnikov_samara", "label": "Каретниковы (Самарская губ. / Бузулукский уезд)", "fields": {"last_name": "Каретников", "birth_place_gubernia": "Самарская"}},
    {"id": "karetnikov_orenburg", "label": "Каретниковы (Оренбургская губ.)", "fields": {"last_name": "Каретников", "birth_place_gubernia": "Оренбургская"}},
    {"id": "karetnikov_orel", "label": "Каретниковы (Орловская губ.)", "fields": {"last_name": "Каретников", "birth_place_gubernia": "Орловская"}},
    {"id": "karetnikov_vladimir", "label": "Каретниковы (Владимирская губ. / Шуйский уезд / Тейково)", "fields": {"last_name": "Каретников", "birth_place_gubernia": "Владимирская"}},
]


def summarize_hit(hit: dict) -> dict:
    src = hit.get("_source", {})
    return {
        "id": hit.get("_id"),
        "type": hit.get("_type"),
        "surname": src.get("last_name") or src.get("familia"),
        "first_name": src.get("first_name") or src.get("imya"),
        "patronymic": src.get("middle_name") or src.get("otchestvo"),
        "rank": src.get("rank"),
        "unit": src.get("military_unit_name"),
        "gubernia": src.get("birth_place_gubernia"),
        "uezd": src.get("birth_place_uezd"),
        "volost": src.get("birth_place_volost"),
        "birth_place": src.get("birth_place"),
        "marital": src.get("marital"),
        "reason": src.get("reason") or src.get("nagrazhdenie"),
        "date": src.get("date") or src.get("data_vibitiya")
    }


def main():
    client = gwar.source_client()
    entities = list(gwar.KINDS.values())
    master_summary = []

    for q in QUERIES:
        try:
            state = gwar.collect(client, q["fields"], entities, limit=100, checkpoint=None)
            hits = state.get("hits", [])
            records = [summarize_hit(h) for h in hits]
            master_summary.append({
                "id": q["id"],
                "label": q["label"],
                "query": q["fields"],
                "total_reported": state.get("total"),
                "retrieved": len(records),
                "blocked": state.get("blocked"),
                "records": records
            })
            print(f"[GWAR] {q['label']}: total={state.get('total')}, retrieved={len(records)}")
        except Exception as e:
            master_summary.append({
                "id": q["id"],
                "label": q["label"],
                "query": q["fields"],
                "error": str(e)
            })
            print(f"[GWAR ERR] {q['label']}: {e}")

    out_file = OUT_DIR / "gwar_1914_live_harvest.json"
    out_file.write_text(json.dumps(master_summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] Saved GWAR live harvest to {out_file}")


if __name__ == "__main__":
    main()
