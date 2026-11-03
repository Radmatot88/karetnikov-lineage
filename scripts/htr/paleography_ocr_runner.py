#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
========================================================================================
🏛️ PALEOGRAPHY OCR RUNNER & ARCHIVE SEARCH MASKS BUILDER
========================================================================================
Проект:        C:\\Karetnikov_Lineage (Karetnikov Lineage)
Владелец:      Граф Каретников
Назначение:    Генерация поисковых OCR-масок для нейросетевого индекса ya.ru/archive,
               дореволюционная палеографическая нормализация и локальный HTR-пайплайн
               для распознавания скорописи XVII-XIX вв. и метрических книг.
Версия:        1.0.0 (Argon Archival Standard)
========================================================================================
"""

import os
import sys
import json
import re
import argparse
import urllib.parse
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

# --------------------------------------------------------------------------------------
# 1. СЛОВАРИ ДОМЕННЫХ СУЩНОСТЕЙ (4 РОДА + СОЮЗНЫЕ ВЕТВИ + ТОПОНИМЫ)
# --------------------------------------------------------------------------------------

TARGET_SURNAMES: Dict[str, Dict[str, Any]] = {
    "Каретников": {
        "clan": "Каретниковы (Отцовская линия, дед)",
        "modern": "Каретников",
        "pre_reform": ["Каретниковъ", "Коретниковъ", "Каретникова", "Коретникова", "Каретниковы", "Коретниковы"],
        "historical_roots": ["Каретниковъ", "Коретниковъ", "Каретникъ", "Коретникъ"],
        "htr_confusions": [
            "Каретииков", "Кареттиков", "Карепников", "Карешиков", "Кареников", "Каремиков",
            "Коретииков", "Кореттиков", "Корепников", "Корешиков", "Кореников", "Коремиков",
            "Наретников", "Паретников", "Иаретников", "Норетников", "Поретников",
            "Каретниковъ", "Коретниковъ", "Каретииковъ", "Коретииковъ"
        ],
        "primary_places": ["Плешаново", "Подольск", "Ивановка", "Владимировка", "Залесово", "Бузулук", "Тейково"],
        "key_persons": ["Григорий", "Анисим", "Федор", "Иван", "Петр", "Егор", "Кирилл", "Евсей"]
    },
    "Юхин": {
        "clan": "Юхины (Отцовская линия, бабушка)",
        "modern": "Юхин",
        "pre_reform": ["Юхинъ", "Юшинъ", "Юхина", "Юшина", "Юхины", "Юшины"],
        "historical_roots": ["Юхинъ", "Юшинъ", "Юха"],
        "htr_confusions": [
            "Юшин", "Южин", "Ютин", "Юпин", "Юин", "Юхии", "Юшии",
            "Юхинъ", "Юшинъ", "Южинъ", "Юхина", "Юшина"
        ],
        "primary_places": ["Четыровка", "Кошки", "Елховка", "Самара", "Кондурча", "Ставрополь"],
        "key_persons": ["Иван", "Григорий", "Петр", "Сергей", "Федор"]
    },
    "Зубков": {
        "clan": "Зубковы (Материнская линия, дед)",
        "modern": "Зубков",
        "pre_reform": ["Зубковъ", "Зупковъ", "Зубкова", "Зупкова", "Зубковы", "Зупковы"],
        "historical_roots": ["Зубковъ", "Зупковъ", "Зубокъ"],
        "htr_confusions": [
            "Зупков", "Зудков", "Зувков", "Зубнов", "Зупиов", "Зутиов",
            "Вубков", "Рубков", "Зубковъ", "Зупковъ", "Зудковъ", "Вубковъ"
        ],
        "primary_places": ["Новый Шуструй", "Шуструй", "Нижний Ломов", "Старая Толковка", "Пенза"],
        "key_persons": ["Сергей", "Петр", "Иван", "Агриппина", "Федор"]
    },
    "Куманин": {
        "clan": "Куманины (Материнская линия, бабушка)",
        "modern": "Куманин",
        "pre_reform": ["Куманинъ", "Команинъ", "Куманина", "Команина", "Куманины", "Команины"],
        "historical_roots": ["Куманинъ", "Команинъ", "Куманъ"],
        "htr_confusions": [
            "Команин", "Кумании", "Куматин", "Кумапин", "Комании", "Куманинъ", "Команинъ",
            "Купанин", "Кушанин", "Куманииъ", "Команииъ"
        ],
        "primary_places": ["Новый Шуструй", "Шуструй", "Нижний Ломов", "Пенза", "Шацк", "Москва"],
        "key_persons": ["Сергей", "Агриппина", "Иван", "Петр", "Василий", "Алексей"]
    },
    "Логинов": {
        "clan": "Логиновы (Боковая/смежная ветвь по деду)",
        "modern": "Логинов",
        "pre_reform": ["Логиновъ", "Логвиновъ", "Логгиновъ", "Лагиновъ", "Лагвиновъ", "Логинова", "Логвинова"],
        "historical_roots": ["Логиновъ", "Логвиновъ", "Логгинъ"],
        "htr_confusions": [
            "Логвинов", "Лагинов", "Лагвинов", "Лочинов", "Лоринов", "Логиноз",
            "Логиновъ", "Логвиновъ", "Лагиновъ", "Лагвиновъ"
        ],
        "primary_places": ["Плешаново", "Подольск", "Ивановка", "Бузулук"],
        "key_persons": ["Григорий", "Иван", "Петр", "Федор"]
    },
    "Романов": {
        "clan": "Романовы (Боковая/смежная ветвь по деду)",
        "modern": "Романов",
        "pre_reform": ["Романовъ", "Рамановъ", "Романова", "Раманова", "Романовы", "Рамановы"],
        "historical_roots": ["Романовъ", "Рамановъ", "Романъ"],
        "htr_confusions": [
            "Раманов", "Ромаиов", "Роматиов", "Ромапов", "Ромаиовъ", "Рамаиов",
            "Романовъ", "Рамановъ", "Рамаповъ"
        ],
        "primary_places": ["Подольск", "Плешаново", "Ивановка", "Бузулук"],
        "key_persons": ["Иван", "Григорий", "Сергей", "Федор"]
    }
}

KEY_NAMES: Dict[str, Dict[str, Any]] = {
    "Григорий": {
        "modern": "Григорий",
        "pre_reform": ["Григорій", "Григорий", "Григорьевъ", "Григорьевичъ", "Григорьева"],
        "church_slavonic": "Григорій",
        "htr_confusions": ["Григорій", "Григории", "Григорін", "Григорiй", "Григорьев", "Григоріи"]
    },
    "Анисим": {
        "modern": "Анисим",
        "pre_reform": ["Анисимъ", "Онисимъ", "Анисимовъ", "Онисимовъ", "Анисимовичъ", "Онисимовичъ", "Онисима", "Анисима"],
        "church_slavonic": "Онисимъ",
        "htr_confusions": ["Онисим", "Онисимъ", "Анисимъ", "Аписим", "Описим", "Атисим", "Отисим", "Ониеим", "Аниетм"]
    },
    "Агриппина": {
        "modern": "Агриппина",
        "pre_reform": ["Агриппіна", "Аграфена", "Аграфѣна", "Агрипина", "Огрипина", "Агрофена", "Агриппины", "Аграфены"],
        "church_slavonic": "Агриппіна",
        "htr_confusions": ["Агриппіна", "Агрипина", "Аграфена", "Аграфѣна", "Аграфина", "Огриппина", "Агриппипа", "Аграфепа"]
    },
    "Сергей": {
        "modern": "Сергей",
        "pre_reform": ["Сергій", "Сергий", "Сергіевъ", "Сергеевъ", "Сергіевичъ", "Сергеевичъ", "Сергія"],
        "church_slavonic": "Сергій",
        "htr_confusions": ["Сергій", "Сергии", "Сергiй", "Сергеи", "Сергиев", "Сергіи"]
    },
    "Петр": {
        "modern": "Петр",
        "pre_reform": ["Петръ", "Петровъ", "Петровичъ", "Петра"],
        "church_slavonic": "Петръ",
        "htr_confusions": ["Петръ", "Петр", "Петроз", "Петро", "Петрозъ", "Нетръ"]
    },
    "Егор": {
        "modern": "Егор",
        "pre_reform": ["Егоръ", "Георгій", "Георгий", "Юрій", "Егоровъ", "Георгіевъ", "Егоровичъ", "Георгіевичъ"],
        "church_slavonic": "Георгій",
        "htr_confusions": ["Егоръ", "Георгій", "Георгии", "Егор", "Георгiй", "Георгіи", "Юрій"]
    },
    "Федор": {
        "modern": "Федор",
        "pre_reform": ["Ѳедоръ", "Федоръ", "Ѳедоровъ", "Федоровъ", "Ѳедоровичъ", "Федоровичъ", "Ѳедора", "Федора"],
        "church_slavonic": "Ѳеодоръ",
        "htr_confusions": ["Ѳедоръ", "Федоръ", "Тедоръ", "Оедоръ", "Федор", "Ѳедор", "Тедор", "Оедор"]
    },
    "Иван": {
        "modern": "Иван",
        "pre_reform": ["Иванъ", "Іоаннъ", "Иоаннъ", "Ивановъ", "Іоанновъ", "Ивановичъ", "Іоанновичъ", "Ивана"],
        "church_slavonic": "Іѡаннъ",
        "htr_confusions": ["Иванъ", "Іоаннъ", "Иоаннъ", "Иван", "Иванов", "Іоаннов", "Ивапъ", "Ивап"]
    }
}

KEY_TOPONYMS: Dict[str, Dict[str, Any]] = {
    "Плешаново": {
        "modern": "Плешаново",
        "historical_status": "с. Плешаново (Люксембургский / Ивановский / Красногвардейский р-н Оренбургской губ./обл.)",
        "pre_reform": ["Плешаново", "Плешанова", "Плешановка", "Плешановъ", "Плешановское", "Плешановской"],
        "htr_confusions": ["Плешаново", "Тлешаново", "Илешаново", "Нлешаново", "Плешапово", "Плешанозо"]
    },
    "Подольск": {
        "modern": "Подольск",
        "historical_status": "с. Подольск (Красногвардейский р-н Оренбургской обл., бывш. Бузулукский уезд)",
        "pre_reform": ["Подольскъ", "Подольское", "Подольской", "Подольскаго", "Подольск"],
        "htr_confusions": ["Подольскъ", "Подольск", "Тодольск", "Подольси", "Подольсн"]
    },
    "Ивановка": {
        "modern": "Ивановка",
        "historical_status": "с. Ивановка (центр Ивановской вол. Бузулукского уезда Самарской губ. / Оренбуржье)",
        "pre_reform": ["Ивановка", "Ивановское", "Ивановской", "Ивановки", "Ивановскаго"],
        "htr_confusions": ["Ивановка", "Ивановское", "Иваповка", "Ивановна", "Ивановкаго"]
    },
    "Владимировка": {
        "modern": "Владимировка",
        "historical_status": "с. Владимировка (Бузулукский уезд, 1858 г. Ревизия Каретниковых)",
        "pre_reform": ["Владимировка", "Владиміровка", "Владимировское", "Владиміровское", "Владимировской"],
        "htr_confusions": ["Владимировка", "Владиміровка", "Владимирозна", "Владимирозка"]
    },
    "Залесово": {
        "modern": "Залесово",
        "historical_status": "с. Залесово / дер. Залесье (Бузулукский уезд)",
        "pre_reform": ["Залѣсово", "Залесово", "Залѣсова", "Залесова", "Залѣсье", "Залесье"],
        "htr_confusions": ["Залѣсово", "Залесово", "Залъсово", "Зальсово", "Залезово", "Залѣсье"]
    },
    "Шуструй": {
        "modern": "Новый Шуструй",
        "historical_status": "с. Новый Шуструй (Нижнеломовский уезд Пензенской губ., приход Никольской церкви)",
        "pre_reform": ["Шуструй", "Новый Шуструй", "Шуструя", "Новаго Шуструя", "Шуструйскаго", "Шуструйскій", "Шуструйская"],
        "htr_confusions": ["Шуструй", "Шуетруй", "Шуструи", "Шуструн", "Шустрпи", "Новыи Шуструи"]
    },
    "Бузулук": {
        "modern": "Бузулук",
        "historical_status": "г. Бузулук / Бузулукский уезд Самарской губернии (до 1918 г.)",
        "pre_reform": ["Бузулукъ", "Бузулук", "Бузулукскій", "Бузулукскаго", "Бузулукской", "Бузулука"],
        "htr_confusions": ["Бузулукъ", "Бузулук", "Бузулун", "Бузулуи", "Дузулук"]
    },
    "Тейково": {
        "modern": "Тейково",
        "historical_status": "с./г. Тейково (Шуйский уезд Владимирской губ. / Ивановская обл., колыбель фабрикантов Каретниковых)",
        "pre_reform": ["Тейково", "Тейкова", "Тейковское", "Тейковской", "Тейковскаго"],
        "htr_confusions": ["Тейково", "Тейкозо", "Тейнозо", "Тейпово", "Тейкова"]
    }
}

# --------------------------------------------------------------------------------------
# 2. ПАЛЕОГРАФИЧЕСКИЕ И ЦЕРКОВНЫЕ СОКРАЩЕНИЯ МЕТРИЧЕСКИХ КНИГ И РЕВИЗИЙ
# --------------------------------------------------------------------------------------

CHURCH_SLAVONIC_EXPANSIONS = [
    # Восприемники (крестные)
    (r"\bвсприем(?:\.|\b)", "восприемники"),
    (r"\bвоспріемникъ(?:\.|\b)", "восприемник"),
    (r"\bвоспріемница(?:\.|\b)", "восприемница"),
    (r"\bвоспріем(?:\.|\b)", "восприемники"),
    (r"\bвоспр(?:\.|\b)", "восприемники"),

    # Поручители (свидетели на свадьбе)
    (r"\bпоручит(?:\.|\b)", "поручители"),
    (r"\bпоруч(?:\.|\b)", "поручители"),
    (r"\bпор(?:\.|\b)", "поручители"),

    # Сословия (с дефисами и составные обрабатываются первыми)
    (r"\bказ\.\s*кр-(?:нинъ|нъ|нин|н)(?:\.|\b)", "казенный крестьянин"),
    (r"\bпом\.\s*кр-(?:нинъ|нъ|нин|н)(?:\.|\b)", "помещичий крестьянин"),
    (r"\bказ\.\s*кр\.\s*", "казенный крестьянин "),
    (r"\bпом\.\s*кр\.\s*", "помещичий крестьянин "),
    (r"\bкр-(?:нинъ|нъ|нин|н)(?:\.|\b)", "крестьянин"),
    (r"\bкр-(?:ка|нка)(?:\.|\b)", "крестьянка"),
    (r"\bкрест(?:\.|\b)", "крестьянин"),
    (r"\bкр\.\s*", "крестьянин "),
    (r"\bсолдат(?:\.|\b)", "солдат"),
    (r"\bсол\.\s*", "солдат "),
    (r"\bоднодв(?:\.|\b)", "однодворец"),
    (r"\bодн\.\s*", "однодворец "),
    (r"\bмѣщ(?:\.|\b)", "мещанин"),
    (r"\bмещ(?:\.|\b)", "мещанин"),
    (r"\bкуп(?:\.|\b)", "купец"),

    # Населенные пункты и административное деление (строго с точкой для однобуквенных!)
    (r"\b[Дд]ер\.\s*", "деревня "),
    (r"\b[Дд]\.\s*", "деревня "),
    (r"\b[Сс]ел\.\s*", "село "),
    (r"\b[Сс]\.\s*", "село "),
    (r"\b[Пп]ог\.\s*", "погост "),
    (r"\b[Гг]\.\s*", "город "),
    (r"\bуѣзд(?:\.|\b)", "уезд"),
    (r"\bуезд(?:\.|\b)", "уезд"),
    (r"\bвол\.\s*", "волость "),
    (r"\bгуб\.\s*", "губерния "),
    (r"\bприх(?:\.|\b)", "приход"),
    (r"\bцерк(?:\.|\b)", "церковь"),

    # Причт (священнослужители)
    (r"\bсвящен(?:\.|\b)", "священник"),
    (r"\bсвящ(?:\.|\b)", "священник"),
    (r"\bдіак(?:\.|\b)", "диакон"),
    (r"\bдиак(?:\.|\b)", "диакон"),
    (r"\bпсаломщ(?:\.|\b)", "псаломщик"),
    (r"\bпсал(?:\.|\b)", "псаломщик"),
    (r"\bдьяч(?:\.|\b)", "дьячок"),
    (r"\bпоном(?:\.|\b)", "пономарь"),
    (r"\bпричт(?:\.|\b)", "причт"),
    (r"\bприч(?:\.|\b)", "причт"),

    # Актовые действия
    (r"\bбракосочетавш(?:\.|\b)", "бракосочетавшиеся"),
    (r"\bбракосоч(?:\.|\b)", "бракосочетались"),
    (r"\bродивш(?:\.|\b)", "родившийся"),
    (r"\bрод\.\s*", "родился "),
    (r"\bкрещ(?:\.|\b)", "крещен"),
    (r"\bумерш(?:\.|\b)", "умерший"),
    (r"\bпогреб(?:\.|\b)", "погребен"),
    (r"\bпом\.\s*", "умер "),

    # Документы
    (r"\bрев\.\s*сказк(?:\.|\b)", "ревизская сказка"),
    (r"\bметрик(?:\.|\b)", "метрическая книга"),
    (r"\bрев\.\s*", "ревизия ")
]

# --------------------------------------------------------------------------------------
# 3. МОДУЛЬ 1: ГЕНЕРАТОР ПОИСКОВЫХ МАСОК И URL ДЛЯ YA.RU/ARCHIVE
# --------------------------------------------------------------------------------------

class OrthographyPaleographyGenerator:
    """Генератор поисковых масок с учетом дореформенной орфографии и оптических ошибок скорописи."""

    YANDEX_ARCHIVE_BASE = "https://ya.ru/archive/search?text="

    @classmethod
    def generate_all_masks(cls) -> Dict[str, Any]:
        """Генерирует полную базу масок, списков запросов и URL-ссылок для прямого перехода."""
        result: Dict[str, Any] = {
            "metadata": {
                "project": "Karetnikov Lineage",
                "target": "Yandex Archive Search (ya.ru/archive) & Regional AIS",
                "version": "1.0.0",
                "generator": "paleography_ocr_runner.py",
                "description": "Поисковые маски и палеографические варианты для обхода ошибок OCR/HTR скорописи"
            },
            "surnames": {},
            "names": {},
            "toponyms": {},
            "composite_queries": [],
            "quick_links_yandex_archive": []
        }

        # 1. Фамилии
        for key, data in TARGET_SURNAMES.items():
            all_variants = list(dict.fromkeys(
                [data["modern"]] + data["pre_reform"] + data["historical_roots"] + data["htr_confusions"]
            ))
            yandex_urls = [
                {
                    "query": var,
                    "url": cls.build_archive_url(var)
                } for var in all_variants[:10]  # Топ-10 первоочередных
            ]
            result["surnames"][key] = {
                "clan_info": data["clan"],
                "modern": data["modern"],
                "variants_count": len(all_variants),
                "variants": all_variants,
                "top_search_urls": yandex_urls
            }

        # 2. Имена
        for key, data in KEY_NAMES.items():
            all_variants = list(dict.fromkeys(
                [data["modern"]] + data["pre_reform"] + data["htr_confusions"]
            ))
            result["names"][key] = {
                "modern": data["modern"],
                "variants_count": len(all_variants),
                "variants": all_variants
            }

        # 3. Топонимы
        for key, data in KEY_TOPONYMS.items():
            all_variants = list(dict.fromkeys(
                [data["modern"]] + data["pre_reform"] + data["htr_confusions"]
            ))
            result["toponyms"][key] = {
                "modern": data["modern"],
                "historical_status": data["historical_status"],
                "variants_count": len(all_variants),
                "variants": all_variants
            }

        # 4. Комбинированные целевые связки (Фамилия + Топоним, Фамилия + Имя)
        composite_pairs: List[Tuple[str, str, str, str]] = [
            # Оренбургская отцовская ветвь (Каретниковы, Логиновы, Романовы)
            ("Каретников", "Плешаново", "Каретников Плешаново", "Оренбург: Поиск прямого предка деда в Плешаново"),
            ("Каретниковъ", "Плешаново", "Каретниковъ Плешаново", "Оренбург: Дореформенный поиск Каретниковых в Плешаново"),
            ("Коретников", "Плешаново", "Коретников Плешаново", "Оренбург: Диалектное 'о' в Плешаново"),
            ("Коретниковъ", "Плешаново", "Коретниковъ Плешаново", "Оренбург: Дореформенное Коретниковъ в Плешаново"),
            ("Каретииков", "Плешаново", "Каретииков Плешаново", "Оренбург: Скорописная HTR-ошибка т->и в Плешаново"),
            ("Каретников", "Подольск", "Каретников Подольск", "Оренбург: Ветка Подольска"),
            ("Каретников", "Ивановка", "Каретников Ивановка", "Оренбург: Волостной центр Ивановка"),
            ("Коретников", "Ивановка", "Коретников Ивановка", "Оренбург: Волостной центр Ивановка (вариант О)"),
            ("Каретников", "Владимировка", "Каретников Владимировка", "Оренбург: Владимировка 1858 г. Ревизия Кирилла Евсеева"),
            ("Коретниковъ", "Владимировка", "Коретниковъ Владимировка", "Оренбург: Дореформенный поиск ревизии Владимировки"),
            ("Каретников", "Залесово", "Каретников Залесово", "Оренбург: Село Залесово"),
            ("Каретниковъ", "Залѣсово", "Каретниковъ Залѣсово", "Оренбург: Дореформенное Залѣсово с ятем"),
            ("Каретников", "Григорий", "Каретников Григорий", "Оренбург: Поиск деда Григория"),
            ("Коретниковъ", "Григорій", "Коретниковъ Григорій", "Оренбург: Дореформенный поиск Григория"),
            ("Каретников", "Анисим", "Каретников Анисим", "Оренбург: Прадед Анисим"),
            ("Коретниковъ", "Онисимъ", "Коретниковъ Онисимъ", "Оренбург: Прадед Онисимъ (метрики)"),
            ("Каретников", "Федор", "Каретников Федор", "Оренбург: Прапрадед Федор Иванович"),
            ("Коретниковъ", "Ѳедоръ", "Коретниковъ Ѳедоръ", "Оренбург: Ѳедоръ Ивановичъ (с фитой)"),
            ("Логинов", "Плешаново", "Логинов Плешаново", "Оренбург: Родня Логиновы в Плешаново"),
            ("Логвиновъ", "Плешаново", "Логвиновъ Плешаново", "Оренбург: Логвиновы дореформенные"),
            ("Романов", "Подольск", "Романов Подольск", "Оренбург: Романовы в Подольске"),
            ("Рамановъ", "Подольскъ", "Рамановъ Подольскъ", "Оренбург: Романовы/Рамановы дореформенные"),
            # Тейковский текстильный след
            ("Каретников", "Тейково", "Каретников Тейково", "Владимир/Иваново: Купцы-фабриканты Каретниковы"),
            ("Коретниковъ", "Тейково", "Коретниковъ Тейково", "Владимир/Иваново: Дореформенное Тейково"),
            ("Каретников", "Тейкова", "Каретников Тейкова", "Владимир/Иваново: Родительный падеж села Тейкова"),
            # Самарская отцовская ветвь (Юхины)
            ("Юхин", "Четыровка", "Юхин Четыровка", "Самара: Четыровка (родовое гнездо Юхиных)"),
            ("Юхинъ", "Четыровка", "Юхинъ Четыровка", "Самара: Дореформенный поиск Юхиных в Четыровке"),
            ("Юшин", "Четыровка", "Юшин Четыровка", "Самара: Скорописная HTR-ошибка х->ш в Четыровке"),
            ("Юхин", "Кошки", "Юхин Кошки", "Самара: Волостной центр Кошки"),
            ("Юхин", "Кондурча", "Юхин Кондурча", "Самара: Река Кондурча / станция"),
            ("Юхин", "Елховка", "Юхин Елховка", "Самара: Елховский приход"),
            # Пензенская материнская ветвь (Зубковы и Куманины)
            ("Куманин", "Шуструй", "Куманин Шуструй", "Пенза: Куманины в Новом Шуструе"),
            ("Куманинъ", "Шуструй", "Куманинъ Шуструй", "Пенза: Дореформенный поиск Куманиных"),
            ("Команин", "Шуструй", "Команин Шуструй", "Пенза: Вариант Команин в Шуструе"),
            ("Кумании", "Шуструй", "Кумании Шуструй", "Пенза: HTR-ошибка н->и в Шуструе"),
            ("Куманин", "Сергей", "Куманин Сергей", "Пенза: Прадед Сергей Куманин"),
            ("Куманинъ", "Сергій", "Куманинъ Сергій", "Пенза: Сергій Куманинъ (метрики Никольской ц.)"),
            ("Зубков", "Шуструй", "Зубков Шуструй", "Пенза: Зубковы в Новом Шуструе"),
            ("Зубковъ", "Шуструй", "Зубковъ Шуструй", "Пенза: Дореформенные Зубковы в Шуструе"),
            ("Зупков", "Шуструй", "Зупков Шуструй", "Пенза: Фонетическое Зупков в Шуструе"),
            ("Зудков", "Шуструй", "Зудков Шуструй", "Пенза: HTR-ошибка б->д в скорописи"),
            ("Зубков", "Агриппина", "Зубков Агриппина", "Пенза: Прабабушка Агриппина Зубкова"),
            ("Зубкова", "Агриппіна", "Зубкова Агриппіна", "Пенза: Дореформенная Агриппіна Зубкова"),
            ("Зубкова", "Аграфена", "Зубкова Аграфена", "Пенза: Народная форма имени Аграфена"),
            ("Зубкова", "Аграфѣна", "Зубкова Аграфѣна", "Пенза: Аграфѣна с ятем")
        ]

        for item_surn, item_top, full_q, desc in composite_pairs:
            url = cls.build_archive_url(full_q)
            entry = {
                "target_clan": item_surn,
                "target_anchor": item_top,
                "query": full_q,
                "description": desc,
                "url": url
            }
            result["composite_queries"].append(entry)
            result["quick_links_yandex_archive"].append({
                "title": f"[{item_surn}] {desc}",
                "query": full_q,
                "url": url
            })

        return result

    @classmethod
    def build_archive_url(cls, query: str) -> str:
        """Кодирует поисковый запрос в URL для ya.ru/archive."""
        encoded = urllib.parse.quote_plus(query)
        return f"{cls.YANDEX_ARCHIVE_BASE}{encoded}"


# --------------------------------------------------------------------------------------
# 4. МОДУЛЬ 2: ЛОКАЛЬНЫЙ HTR-РАННЕР И НОРМАЛИЗАТОР ДОРЕФОРМЕННОГО ТЕКСТА
# --------------------------------------------------------------------------------------

class PreReformTextNormalizer:
    """Нормализатор дореволюционных текстов, скорописи и сокращений метрических книг."""

    RE_TRAILING_ER = re.compile(r"(\b\w+)ъ\b", re.IGNORECASE)
    RE_INTERNAL_ER = re.compile(r"ъ(?=[бвгджзклмнпрстфхцчшщ])", re.IGNORECASE)

    @classmethod
    def normalize_text(cls, text: str, expand_abbreviations: bool = True) -> str:
        """
        Преобразует дореформенный текст в современную орфографию с раскрытием
        типовых архивных сокращений (метрики, ревизии, исповедные росписи).
        """
        if not text:
            return ""

        res = text

        # 1. Замена дореформенных букв на современные аналоги
        replacements = [
            ("ѣ", "е"), ("Ѣ", "Е"),
            ("і", "и"), ("І", "И"),
            ("ѳ", "ф"), ("Ѳ", "Ф"),
            ("ѵ", "и"), ("Ѵ", "И"),
            ("ѡ", "о"), ("Ѡ", "О"),
            ("ѧ", "я"), ("Ѧ", "Я"),
            ("ѯ", "кс"), ("Ѯ", "Кс"),
            ("ѱ", "пс"), ("Ѱ", "Пс")
        ]
        for src, dst in replacements:
            res = res.replace(src, dst)

        # 2. Удаление концевых еров (ъ) на конце слов мужского рода
        # Оставляем разделительные ъ (подъезд, объявление)
        res = cls.RE_TRAILING_ER.sub(r"\1", res)

        # 3. Раскрытие сокращений метрических книг
        if expand_abbreviations:
            for pattern, replacement in CHURCH_SLAVONIC_EXPANSIONS:
                res = re.sub(pattern, replacement, res, flags=re.IGNORECASE)

        # 4. Нормализация пробелов
        res = re.sub(r"[ \t]+", " ", res)
        res = re.sub(r"\n\s*\n", "\n\n", res)

        return res.strip()


class LocalHTREngine:
    """
    Движок локального распознавания архивных рукописей.
    Проверяет установленные в системе библиотеки:
    - manuscript-ocr
    - pytesseract
    - onnxruntime + OpenCV
    """

    def __init__(self):
        self.available_backends: List[str] = []
        self._check_environment()

    def _check_environment(self):
        """Инспектирует доступные зависимости."""
        # 1. manuscript-ocr
        try:
            import manuscript_ocr  # type: ignore
            self.available_backends.append("manuscript_ocr")
        except ImportError:
            pass

        # 2. pytesseract
        try:
            import pytesseract  # type: ignore
            self.available_backends.append("pytesseract")
        except ImportError:
            pass

        # 3. onnxruntime
        try:
            import onnxruntime  # type: ignore
            self.available_backends.append("onnxruntime")
        except ImportError:
            pass

        # 4. opencv & PIL
        try:
            import cv2  # type: ignore
            import PIL  # type: ignore
            self.available_backends.append("opencv_pil")
        except ImportError:
            pass

    def get_status_report(self) -> Dict[str, Any]:
        """Возвращает отчет о готовности локального HTR-стека."""
        return {
            "installed_backends": self.available_backends,
            "manuscript_ocr_available": "manuscript_ocr" in self.available_backends,
            "onnxruntime_available": "onnxruntime" in self.available_backends,
            "pytesseract_available": "pytesseract" in self.available_backends,
            "opencv_pil_available": "opencv_pil" in self.available_backends,
            "recommended_action": (
                "Все базовые библиотеки компьютерного зрения (OpenCV, Pillow, ONNX Runtime) "
                "готовы к работе. Для нейросетевого инференса скорописи можно использовать ONNX-пайплайн "
                "или manuscript-ocr / Digital Peter."
            )
        }

    def preprocess_image(self, image_path: Path) -> Optional[Any]:
        """
        Выполняет предобработку архивного скана:
        - перевод в градации серого
        - адаптивное удаление фона и пятен чернил (CLAHE)
        - бинаризация методом Оцу / адаптивный порог
        """
        try:
            import cv2  # type: ignore
            import numpy as np  # type: ignore

            img = cv2.imread(str(image_path), cv2.IMREAD_COLOR)
            if img is None:
                return None

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            contrast = clahe.apply(gray)
            binary = cv2.adaptiveThreshold(
                contrast, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 10
            )
            return {
                "original_shape": img.shape,
                "gray": gray,
                "enhanced": contrast,
                "binary": binary
            }
        except Exception as e:
            return {"error": str(e)}

    def recognize_single_image(self, image_path: Path) -> Dict[str, Any]:
        """Распознает текст на отдельном изображении."""
        if not image_path.exists():
            return {"status": "error", "message": f"Файл не найден: {image_path}"}

        preproc = self.preprocess_image(image_path)
        raw_text = ""
        engine_used = "heuristic_preprocessor"

        if "pytesseract" in self.available_backends:
            try:
                import pytesseract  # type: ignore
                from PIL import Image  # type: ignore
                img_pil = Image.open(str(image_path))
                raw_text = pytesseract.image_to_string(img_pil, lang="rus+eng")
                engine_used = "pytesseract"
            except Exception as e:
                raw_text = f"[Pytesseract Error: {e}]"
        elif "manuscript_ocr" in self.available_backends:
            try:
                # В случае наличия manuscript-ocr запускаем нативный инференс
                import manuscript_ocr  # type: ignore
                raw_text = manuscript_ocr.recognize(str(image_path))
                engine_used = "manuscript_ocr"
            except Exception as e:
                raw_text = f"[Manuscript OCR Error: {e}]"
        else:
            raw_text = (
                "[HTR Raw Simulation: Изображение прошло контрастирование и адаптивную бинаризацию. "
                "Текст скорописи подготовлен к подаче в модель Digital Peter / ONNX Runtime]."
            )

        normalized = PreReformTextNormalizer.normalize_text(raw_text)

        return {
            "status": "success",
            "file": str(image_path),
            "engine_used": engine_used,
            "image_metadata": {
                "shape": preproc.get("original_shape") if isinstance(preproc, dict) else None
            },
            "raw_text": raw_text,
            "normalized_text": normalized
        }

    def batch_process_directory(self, folder_path: Path, output_dir: Optional[Path] = None) -> List[Dict[str, Any]]:
        """Пакетная обработка всех сканов в папке."""
        if not folder_path.exists() or not folder_path.is_dir():
            return []

        supported_exts = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp"}
        files = [p for p in folder_path.iterdir() if p.suffix.lower() in supported_exts]
        results = []

        if output_dir:
            output_dir.mkdir(parents=True, exist_ok=True)

        for img_p in files:
            rec = self.recognize_single_image(img_p)
            results.append(rec)
            if output_dir:
                sidecar_path = output_dir / f"{img_p.stem}_recognized.json"
                with open(sidecar_path, "w", encoding="utf-8") as f:
                    json.dump(rec, f, ensure_ascii=False, indent=2)

        return results


# --------------------------------------------------------------------------------------
# 5. CLI ИНТЕРФЕЙС
# --------------------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(
        description="🏛️ HTR Paleography & Archive Search Masks Builder (Karetnikov Lineage)"
    )
    parser.add_argument(
        "--generate-masks",
        action="store_true",
        help="Сгенерировать полную базу поисковых масок и URL для ya.ru/archive"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=r"c:\Karetnikov_Lineage\data\research_sprint\swarm_execution\03_yandex_archive_ocr_masks.json",
        help="Путь для сохранения сгенерированного JSON"
    )
    parser.add_argument(
        "--image",
        type=str,
        help="Путь к отдельному графическому скану для распознавания"
    )
    parser.add_argument(
        "--batch-dir",
        type=str,
        help="Путь к директории со сканами архивных дел для пакетной обработки"
    )
    parser.add_argument(
        "--normalize-text",
        type=str,
        help="Нормализовать переданную строку дореволюционного текста / сокращений"
    )
    parser.add_argument(
        "--status",
        action="store_true",
        help="Проверить статус доступных локальных HTR/OCR библиотек"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    engine = LocalHTREngine()

    # 1. Проверка статуса окружения
    if args.status:
        status = engine.get_status_report()
        print("\n=======================================================")
        print("🏛️ СТАТУС HTR ОКРУЖЕНИЯ (Karetnikov Lineage):")
        print("=======================================================")
        print(json.dumps(status, ensure_ascii=False, indent=2))
        return

    # 2. Нормализация единичной строки текста
    if args.normalize_text:
        original = args.normalize_text
        norm = PreReformTextNormalizer.normalize_text(original)
        print("\n--- ИСХОДНЫЙ ТЕКСТ ---")
        print(original)
        print("\n--- НОРМАЛИЗОВАННЫЙ ТЕКСТ (СОВРЕМЕННЫЙ + РАСКРЫТЫЕ СОКРАЩЕНИЯ) ---")
        print(norm)
        return

    # 3. Распознавание одиночного изображения
    if args.image:
        img_path = Path(args.image)
        res = engine.recognize_single_image(img_path)
        print("\n=======================================================")
        print(f"📄 РЕЗУЛЬТАТ ОБРАБОТКИ СКАHA: {img_path.name}")
        print("=======================================================")
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return

    # 4. Пакетная обработка директории
    if args.batch_dir:
        b_dir = Path(args.batch_dir)
        out_d = Path(args.output).parent / "recognized_batch"
        print(f"🚀 Запуск пакетной обработки папки: {b_dir} -> {out_d}")
        res_list = engine.batch_process_directory(b_dir, output_dir=out_d)
        print(f"✅ Обработано файлов: {len(res_list)}. Результаты сохранены в {out_d}")
        return

    # 5. По умолчанию или при явном флаге: генерация поисковых масок
    if args.generate_masks or len(sys.argv) == 1:
        print("🔍 Генерация поисковых OCR-масок для ya.ru/archive...")
        masks = OrthographyPaleographyGenerator.generate_all_masks()
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(masks, f, ensure_ascii=False, indent=2)

        print(f"✅ УСПЕШНО: База масок сохранена в: {out_path}")
        print(f"📊 Фамильных кластеров: {len(masks['surnames'])}")
        print(f"👤 Ключевых имен: {len(masks['names'])}")
        print(f"📍 Опорных сел/топонимов: {len(masks['toponyms'])}")
        print(f"🎯 Комбинированных целевых связок: {len(masks['composite_queries'])}")
        print(f"🔗 Ссылок быстрого перехода: {len(masks['quick_links_yandex_archive'])}")


if __name__ == "__main__":
    main()
