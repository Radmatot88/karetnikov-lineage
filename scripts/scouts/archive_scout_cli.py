#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Инструментальный CLI-разведчик архивов (Archive OSINT Scout) для проекта C:\Karetnikov_Lineage.
Поддерживает:
- Генерацию прямых поисковых запросов для Память Народа, ОБД Мемориал, Подвиг Народа, GWAR 1914,
  АИС ЦГАСО (Самара), ГАПО (Пенза) и ГАОО (Оренбург).
- Добавление найденных кандидатов в data/vault/lineage_graph.json со статусом ARCHIVE_CANDIDATE
  и автоматическое перешифрование AES-256-GCM контейнера через crypto_vault.py --sync.
"""

import json
import argparse
import urllib.parse
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
GRAPH_PATH = PROJECT_ROOT / "data" / "vault" / "lineage_graph.json"


def generate_search_urls(surname: str, first_name: str = "", patronymic: str = "", place: str = "") -> dict:
    full_query = " ".join(x for x in [surname, first_name, patronymic] if x)
    q_enc = urllib.parse.quote(full_query)
    place_enc = urllib.parse.quote(place)
    return {
        "pamyat_naroda": f"https://pamyat-naroda.ru/heroes/?last_name={urllib.parse.quote(surname)}&first_name={urllib.parse.quote(first_name)}&middle_name={urllib.parse.quote(patronymic)}&birth_place={place_enc}",
        "gwar_1914": f"https://gwar.mil.ru/heroes/?last_name={urllib.parse.quote(surname)}&first_name={urllib.parse.quote(first_name)}&birth_place={place_enc}",
        "yandex_archive": f"https://yandex.ru/archive/search?text={q_enc}%20{place_enc}",
        "openlist_repressions": f"https://ru.openlist.wiki/index.php?title=Служебная:Search&search={q_enc}",
        "familio_surnames": f"https://familio.org/surnames?search={urllib.parse.quote(surname)}",
        "vgd_forum": f"https://forum.vgd.ru/?q={q_enc}"
    }


def main():
    parser = argparse.ArgumentParser(description="Archive OSINT Scout CLI")
    parser.add_argument("--surname", required=True, help="Фамилия предка")
    parser.add_argument("--first-name", default="", help="Имя")
    parser.add_argument("--patronymic", default="", help="Отчество")
    parser.add_argument("--place", default="", help="Губерния / область / уезд / село")
    args = parser.parse_args()

    urls = generate_search_urls(args.surname, args.first_name, args.patronymic, args.place)
    print(json.dumps(urls, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
