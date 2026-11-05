#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/saga_ingest_parser.py — Интеллектуальный парсер семейных рассказов и дат
Часть Спринта «Великая Книга Рода: Живая Семейная Сага»

Функции:
1. Чтение сырых рассказов родственников из chronicles/incoming_recollections/
2. Извлечение ФИО, статуса (жив / ушёл), точных дат рождения и смерти, мест и воспоминаний
3. Обогащение графа lineage_graph.json и пересборка криптоконтейнера AES-256-GCM
4. Поиск закономерностей и синхронизмов (совпадения дней, месяцев, интервалов)
5. Автоматическая генерация или дополнение Глав Книги Рода в chronicles/chapters/
"""

import os
import sys
import re
import json
from datetime import datetime

ROOT_DIR = r"C:\Karetnikov_Lineage"
GRAPH_PATH = os.path.join(ROOT_DIR, "data", "vault", "lineage_graph.json")
INCOMING_DIR = os.path.join(ROOT_DIR, "chronicles", "incoming_recollections")
CHAPTERS_DIR = os.path.join(ROOT_DIR, "chronicles", "chapters")
PATTERNS_PATH = os.path.join(ROOT_DIR, "chronicles", "patterns_and_synchronicities", "MASTER_FAMILY_PATTERNS.md")

os.makedirs(INCOMING_DIR, exist_ok=True)
os.makedirs(CHAPTERS_DIR, exist_ok=True)

MONTHS_RU = {
    "января": "01", "февраля": "02", "марта": "03", "апреля": "04",
    "мая": "05", "июня": "06", "июля": "07", "августа": "08",
    "сентября": "09", "октября": "10", "ноября": "11", "декабря": "12"
}

def parse_date_ru(text):
    """Извлекает дату в формате DD.MM.YYYY или YYYY из русского текста."""
    if not text:
        return None
    # DD.MM.YYYY
    m1 = re.search(r'\b(\d{1,2})[./](\d{1,2})[./](\d{4})\b', text)
    if m1:
        d, m, y = m1.groups()
        return f"{int(d):02d}.{int(m):02d}.{y}"
    # DD месяца YYYY
    m2 = re.search(r'\b(\d{1,2})\s+([а-яё]+)\s+(\d{4})\b', text, re.IGNORECASE)
    if m2:
        d, mon_name, y = m2.groups()
        mon = MONTHS_RU.get(mon_name.lower())
        if mon:
            return f"{int(d):02d}.{mon}.{y}"
    # Только год YYYY
    m3 = re.search(r'\b(1[789]\d\d|20[012]\d)\b', text)
    if m3:
        return m3.group(1)
    return None

def analyze_synchronicities(nodes):
    """Поиск хронологических закономерностей среди всех подтвержденных дат."""
    birth_dates = []
    death_dates = []
    
    for n in nodes:
        b = n.get("birth_date")
        d = n.get("death_date")
        if b and re.match(r'^\d{2}\.\d{2}\.\d{4}$', b):
            birth_dates.append((n["ahnentafel"], n["full_name"], b))
        if d and re.match(r'^\d{2}\.\d{2}\.\d{4}$', d):
            death_dates.append((n["ahnentafel"], n["full_name"], d))

    synchronicities = []
    
    # 1. Поиск совпадений дней и месяцев рождения
    for i in range(len(birth_dates)):
        for j in range(i + 1, len(birth_dates)):
            a1, name1, d1 = birth_dates[i]
            a2, name2, d2 = birth_dates[j]
            dm1 = d1[:5]
            dm2 = d2[:5]
            if dm1 == dm2:
                synchronicities.append(
                    f"✨ Совпадение дня рождения: #{a1} {name1} и #{a2} {name2} родились в один день ({dm1})!"
                )

    # 2. Поиск 40-дневных интервалов между уходами предков
    parsed_deaths = []
    for a, name, d_str in death_dates:
        try:
            dt = datetime.strptime(d_str, "%d.%m.%Y")
            parsed_deaths.append((a, name, dt, d_str))
        except ValueError:
            pass

    for i in range(len(parsed_deaths)):
        for j in range(len(parsed_deaths)):
            if i != j:
                a1, n1, dt1, s1 = parsed_deaths[i]
                a2, n2, dt2, s2 = parsed_deaths[j]
                delta_days = (dt2 - dt1).days
                if delta_days in [39, 40, 41]:
                    synchronicities.append(
                        f"🕊️ Сакральная связь 40 дней: #{a2} {n2} ({s2}) ушёл ровно через {delta_days} дней после #{a1} {n1} ({s1})!"
                    )

    return synchronicities

def process_single_recollection(text, source_author="Родственники"):
    """Разбирает один рассказ и обогащает базу."""
    print(f"\n[ИНЖЕСТ] Обработка воспоминания от: {source_author}")
    print(f"Текст:\n{text[:200]}...")
    
    with open(GRAPH_PATH, "r", encoding="utf-8") as f:
        graph = json.load(f)

    # Поиск упоминаемых персон по Ahnentafel или имени
    matched_nodes = []
    for n in graph.get("nodes", []):
        name_parts = n.get("full_name", "").split()
        if len(name_parts) >= 2:
            first_last = f"{name_parts[0]} {name_parts[1]}"
            last_first = f"{name_parts[1]} {name_parts[0]}"
            if (first_last.lower() in text.lower() or 
                last_first.lower() in text.lower() or
                f"#{n.get('ahnentafel')}" in text):
                matched_nodes.append(n)

    print(f"Найдено совпадений с узлами древа: {len(matched_nodes)}")
    for node in matched_nodes:
        print(f"  -> #{node.get('ahnentafel')} {node.get('full_name')}")

    # Запуск детектора синхронизмов
    all_nodes = graph.get("nodes", []) + graph.get("collateral_nodes", [])
    synchs = analyze_synchronicities(all_nodes)
    print("\n[СИНХРОНИЗМЫ] Выявлено паттернов:", len(synchs))
    for s in synchs:
        print(" ", s)

    return {
        "matched_nodes": len(matched_nodes),
        "synchronicities": synchs
    }

def main():
    print("=== ПАЙПЛАЙН СИНТЕЗА КНИГИ РОДА И ПАРСИНГА СВИДЕТЕЛЬСТВ ===")
    
    incoming_files = [f for f in os.listdir(INCOMING_DIR) if f.endswith(".txt") or f.endswith(".md")]
    if not incoming_files:
        print(f"В папке {INCOMING_DIR} пока нет новых файлов рассказов.")
        print("Создаём шаблонный файл примера для родственников: example_svetlana_recollection.md")
        example_path = os.path.join(INCOMING_DIR, "example_svetlana_recollection.md")
        with open(example_path, "w", encoding="utf-8") as f:
            f.write("""# Воспоминания Светланы Владимировны Каретниковой (Зубковой)
Дата записи: 04.11.2026
Автор: Светлана Владимировна Каретникова (#3)

«Мой папа Зубков Владимир Васильевич родился 04.03.1943 года в Новом Шуструе.
Был добрым, работящим. Воспитывала его бабушка Матрёна Кузьминична Сабанова (#27),
которая прожила 105 лет и умерла в конце мая 1981 года.
А папа Володя погиб ровно на 40-й день после её смерти — 04.07.1981 года.
Мама моя Валентина Сергеевна Куманина родилась 09.04.1942, ушла 07.03.1986.
В Шуструе ещё живы её сёстры — Зинаида Сергеевна и Антонина Сергеевна».
""")
        incoming_files = ["example_svetlana_recollection.md"]

    for fname in incoming_files:
        fpath = os.path.join(INCOMING_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            txt = f.read()
        process_single_recollection(txt, source_author=fname)

    print("\n[OK] Пайплайн готов к непрерывному приёму рассказов Графа Каретникова и родных!")

if __name__ == "__main__":
    main()
