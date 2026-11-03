#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Глубокий парсер локальных корпусов Графа Каретникова:
1. C:\\Серкин, Циолковский (24 тома Архаического Кодекса, codex_data.js, references/, knowledge_graph.jsonl)
2. C:\\Prime_Lead_Bussiness\\scratch\\ig_vault и data\\instagram_vault (все 37 сохраненных рилсов, URL, GitHub-репозитории)
3. C:\\Родословная_ИИ (паспорт и дорожная карта)

Сохраняет структурированный дамп зацепок в C:\\Karetnikov_Lineage\\data\\research_sprint\\local_corpus_harvest.json
"""

import json
import re
from pathlib import Path

OUT_DIR = Path(r"C:\Karetnikov_Lineage\data\research_sprint")
OUT_DIR.mkdir(parents=True, exist_ok=True)

SERKIN_DIR = Path(r"C:\Серкин, Циолковский")
IG_SCRATCH_DIR = Path(r"C:\Prime_Lead_Bussiness\scratch\ig_vault")
IG_DATA_DIR = Path(r"C:\Prime_Lead_Bussiness\data\instagram_vault")

ARCHIVE_REGEX = re.compile(
    r"(РГАДА|РГИА|ГАПО|ЦГАСО|ГАОО|ОР РГБ|Фонд\s*\d+|Ф\.\s*\d+|Разрядн\w+\s+приказ|Приказ\w*\s+тайных\s+дел|Аптекарск\w+\s+приказ|Преображенск\w+\s+приказ|Столбц\w+\s+\w+\s+стола|Приказные\s+дела\s+старых\s+лет)",
    re.IGNORECASE
)

GEO_CLAN_REGEX = re.compile(
    r"(Каретников\w*|Юхин\w*|Зубков\w*|Куманин\w*|Ломов\w*|Шустру\w*|Пенз\w*|Самар\w*|Оренбург\w*|Бузулук\w*|Симбирск\w*|Арзамас\w*|Темников\w*|Алатыр\w*|Саратов\w*|Переслав\w*|однодворц\w*|засечн\w+\s+черт\w*|Алён\w+\s+Арзамасск\w*|Степан\w*\s+Разин\w*|масон\w*)",
    re.IGNORECASE
)

URL_REGEX = re.compile(r"https?://[^\s\"')>\]<]+|[a-zA-Z0-9_-]+\.(?:ru|org|com|su|wiki|pro|io|dev)(?:/[^\s\"')>\]<]*)?")


def scan_serkin_codex():
    codex_hits = []
    archive_ciphers = set()
    files_scanned = 0

    if not SERKIN_DIR.exists():
        return {"error": "SERKIN_DIR not found"}

    md_files = list(SERKIN_DIR.rglob("*.md"))
    for fp in md_files:
        if "node_modules" in str(fp) or ".git" in str(fp):
            continue
        files_scanned += 1
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        lines = text.splitlines()
        for idx, line in enumerate(lines, start=1):
            arch_m = ARCHIVE_REGEX.findall(line)
            geo_m = GEO_CLAN_REGEX.findall(line)
            if arch_m:
                for a in arch_m:
                    archive_ciphers.add(a.strip())
            if arch_m or geo_m:
                # Записываем контекстную зацепку
                rel_path = str(fp.relative_to(SERKIN_DIR))
                if "archaic_codex" in rel_path or "death_magic" in rel_path or "loki" in rel_path or geo_m:
                    codex_hits.append({
                        "file": rel_path,
                        "line": idx,
                        "archive_matches": list(set(arch_m)),
                        "geo_or_clan_matches": list(set(geo_m)),
                        "snippet": line.strip()[:300]
                    })

    return {
        "files_scanned": files_scanned,
        "unique_archive_markers": sorted(archive_ciphers),
        "total_hits": len(codex_hits),
        "hits": codex_hits[:250]
    }


def scan_instagram_vault():
    reels_summary = []
    if IG_SCRATCH_DIR.exists():
        for meta_fp in sorted(IG_SCRATCH_DIR.glob("*/metadata.json")):
            try:
                data = json.loads(meta_fp.read_text(encoding="utf-8", errors="ignore"))
                caption = data.get("caption", "") or ""
                dom_text = data.get("dom_text", "") or ""
                combined = caption + "\n" + dom_text
                urls = sorted(set(URL_REGEX.findall(combined)))
                frames = data.get("frames", [])
                reels_summary.append({
                    "shortcode": data.get("shortcode", meta_fp.parent.name),
                    "url": data.get("url"),
                    "extracted_at": data.get("extracted_at"),
                    "github_hints": data.get("github_hints", []),
                    "extracted_urls_and_domains": urls,
                    "frames_count": len(frames),
                    "frames": frames,
                    "caption_excerpt": caption[:600]
                })
            except Exception as e:
                reels_summary.append({"shortcode": meta_fp.parent.name, "error": str(e)})
    return reels_summary


def main():
    serkin_report = scan_serkin_codex()
    ig_report = scan_instagram_vault()

    payload = {
        "serkin_tsiolkovsky_scan": serkin_report,
        "instagram_vault_scan": {
            "total_reels_in_scratch": len(ig_report),
            "reels": ig_report
        }
    }

    out_path = OUT_DIR / "local_corpus_harvest.json"
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] Scanned {serkin_report.get('files_scanned', 0)} files in Serkin-Tsiolkovsky ({serkin_report.get('total_hits', 0)} hits) and {len(ig_report)} IG reels.")
    print(f"[OK] Saved harvest to: {out_path}")


if __name__ == "__main__":
    main()
