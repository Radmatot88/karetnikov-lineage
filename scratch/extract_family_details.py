import os
import re

files_to_check = [
    r"C:\Karetnikov_Lineage\data\vault\lineage_graph.json",
    r"C:\Karetnikov_Lineage\data\vault\karetnikov_lineage.ged",
    r"C:\Karetnikov_Lineage\data\research_sprint\wave3\12A_FYODOR_IVANOVICH_KARETNIKOV_DEEP_DOSSIER.md",
    r"C:\Karetnikov_Lineage\data\research_sprint\wave3\12C_VLADIMIROVKA_ZALESOVO_CLAN_CROSS_MATCHING.md",
    r"C:\Karetnikov_Lineage\data\research_sprint\FAMILY_INSIGHTS_LIVE_LOG.md",
    r"C:\Karetnikov_Lineage\MASTER_FAMILY_ORIGIN_CHRONICLE_NOTEBOOKLM.md"
]

for fpath in files_to_check:
    if os.path.exists(fpath):
        print(f"=== CHECKING {fpath} ===")
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
            lines = fp.readlines()
            for i, line in enumerate(lines):
                if any(w in line for w in ["1913", "Дмитрий Иванович", "Дмитрий", "Иван Дмитриевич", "Марина Антоновна", "Федор Иванович", "Фёдор Иванович", "Шаталовка", "Владимировка"]):
                    # print nearby context
                    start = max(0, i-2)
                    end = min(len(lines), i+3)
                    print(f"--- Line {i+1} ---")
                    for j in range(start, end):
                        print(f"{j+1}: {lines[j].strip()}")
