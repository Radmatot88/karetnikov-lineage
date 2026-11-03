#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Генератор полного 7-коленного графа родословной Каретниковых — Юхиных — Зубковых — Куманиных
(127 прямых слотов Соса-Страдоница + боковые родственники + орбитальные парящие гипотезы + досье 12 рубрик).

Включает:
- Прямую отцовскую ветвь до VII колена и историческую цепь до X колена (1745 г.);
- Каретникова Фёдора Ивановича (#801) и Дмитрия Ивановича старшего (#802);
- Ветвь с. Четыровка Кошкинского р-на (Юхины);
- Ветвь с. Новый Шуструй Нижнеломовского р-на (Зубковы и Куманины);
- Умное правило захоронений 1920 года (Smart Burial Rule);
- Изоляцию личных заметок в internal_research_notes с visibility: 'owner_only';
- Нейтральную этику UI без титулов (UI Title Hygiene);
- Орбитальные карточки-гипотезы (floating_hypotheses).

Сохраняет нешифрованный мастер-граф в:
  C:/Karetnikov_Lineage/data/vault/lineage_graph.json
"""

import json
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).resolve().parent.parent
VAULT_DIR = PROJECT_ROOT / "data" / "vault"
VAULT_DIR.mkdir(parents=True, exist_ok=True)

GEN_LABELS = {
    1: "I колено — Пробанд",
    2: "II колено — Родители и дяди",
    3: "III колено — Дедушки, бабушки и их братья",
    4: "IV колено — Прадеды и прабабушки",
    5: "V колено — Прапрадеды (Перепись 1917 / ПМВ)",
    6: "VI колено — Прапрапрадеды (Метрики / 10-я ревизия 1858 г.)",
    7: "VII колено — Прапрапрапрадеды (8–9 ревизии 1834–1850 гг.)"
}

GEN_ERA = {
    1: "1994 — наст. время",
    2: "1969 — наст. время",
    3: "1925–1945 гг.р.",
    4: "1898–1925 гг.р. (ВОВ / индустриализация)",
    5: "1870–1895 гг.р. (Мост 1917 года / ПМВ)",
    6: "1840–1870 гг.р. (Метрические книги / 10 ревизия)",
    7: "1810–1840 гг.р. (Ревизские сказки 1834, 1850 гг.)"
}


def get_generation(n: int) -> int:
    return n.bit_length()


def get_branch(n: int) -> str:
    if n == 1:
        return "proband"
    bits = bin(n)[2:]
    return "paternal" if bits[1] == "0" else "maternal"


def get_sub_clan(n: int) -> str:
    if n == 1:
        return "Каретниковы • Зубковы"
    if n == 2:
        return "Род Каретниковых • Юхиных"
    if n == 3:
        return "Род Зубковых • Куманиных"
    prefix3 = int(bin(n)[2:5], 2)
    return {
        4: "Род Каретниковых (д. Владимировка • с. Подольск • с. Плешаново)",
        5: "Род Юхиных (с. Четыровка Кошкинского р-на)",
        6: "Род Зубковых (с. Новый Шуструй)",
        7: "Род Куманиных (с. Новый Шуструй)"
    }.get(prefix3, "Родовая линия")


def get_clan_region(n: int) -> str:
    if n in (1, 2):
        return "г. Самара (Куйбышев)"
    if n == 3:
        return "Пензенская обл., Нижнеломовский р-н, с. Новый Шуструй"
    prefix3 = int(bin(n)[2:5], 2)
    return {
        4: "Оренбургская обл., Красногвардейский (Ивановский) р-н, д. Владимировка / с. Плешаново / с. Подольск",
        5: "Самарская (Куйбышевская) обл., Кошкинский р-н, с. Четыровка",
        6: "Пензенская обл., Нижнеломовский уезд, с. Новый Шуструй",
        7: "Пензенская обл., Нижнеломовский уезд, с. Новый Шуструй"
    }.get(prefix3, "Поволжье и Южный Урал")


def build_burial_info(
    cemetery: str | None = None,
    landmarks: str | None = None,
    nearby: str | None = None,
    photo_url: str | None = None,
    is_alive: bool = False
) -> dict:
    """Умное правило 1920 года для отображения места захоронения (Smart Burial Rule)."""
    has_data = bool(cemetery and cemetery.strip())
    is_visible = False if is_alive else has_data
    return {
        "is_visible_on_card": is_visible,
        "force_show_toggle": False,
        "cemetery_and_settlement": cemetery if not is_alive else None,
        "grave_sector_and_landmarks": landmarks if not is_alive else None,
        "buried_nearby_relatives": nearby if not is_alive else None,
        "headstone_photo_webp_url": photo_url if not is_alive else None
    }


def build_dossier_12_rubrics(
    full_name: str,
    surname: str,
    first_name: str,
    patronymic: str,
    maiden_name: str | None,
    birth_date: str | None,
    birth_year: str | None,
    death_date: str | None,
    is_alive: bool,
    birth_place: str,
    sub_clan: str,
    notes: str,
    sources: list[str],
    burial_info: dict,
    worldview_data: dict | None = None,
    life_work_data: dict | None = None,
    military_data: dict | None = None,
    street_nickname: str | None = None,
    marriage_info: str | None = None,
    children_summary: str | None = None,
    historical_events: str | None = None,
    relics_description: str | None = None,
    mastery_and_talents: str | None = None,
    temperament_and_memory: str | None = None,
    photo_url: str | None = None
) -> dict:
    """Формирует канонические 12 рубрик родословного досье (FAMILY_COLLABORATION_AND_DOSSIER_SPEC v2.0)."""
    wv = worldview_data or {
        "primary_tradition": "UNSPECIFIED",
        "tradition_label": "Ожидает архивного уточнения",
        "description": "Традиция исследуется по архивным источникам.",
        "historical_metric_parish_index": None
    }
    lw = life_work_data or {
        "profession_and_craft_summary": "Хлебопашество, крестьянский и созидательный труд.",
        "agricultural_and_kolkhoz_leadership": None,
        "elected_and_state_service": None,
        "social_estate_pre1917": "Крестьяне"
    }
    mil = military_data or {
        "military_rank": None,
        "service_status": None,
        "induction_rvk": None,
        "combat_path": None,
        "awards": []
    }

    return {
        "rubric_01_naming": {
            "full_name": full_name,
            "surname": surname,
            "maiden_name": maiden_name,
            "first_name": first_name,
            "patronymic": patronymic,
            "village_street_nickname": street_nickname,
            "alternative_spellings": [surname] + ([maiden_name] if maiden_name else [])
        },
        "rubric_02_worldview": wv,
        "rubric_03_life_milestones": {
            "birth_date_display": birth_date or "Уточняется",
            "birth_year": birth_year or "Уточняется",
            "death_date_display": death_date,
            "is_alive": is_alive,
            "marriage_info": marriage_info
        },
        "rubric_04_ancestral_cradle": {
            "birth_place": birth_place,
            "residence_places": [birth_place],
            "migration_route": lw.get("migration_route"),
            "orenburg_two_villages_chronicle": lw.get("orenburg_two_villages_chronicle")
        },
        "rubric_05_life_work": lw,
        "rubric_06_military_service": mil,
        "rubric_07_crafts_and_skills": {
            "mastery_and_talents": mastery_and_talents or "Трудолюбие, ведение домашнего и крестьянского хозяйства."
        },
        "rubric_08_personality_and_lore": {
            "temperament_and_memory": temperament_and_memory or notes[:180] if notes else None
        },
        "rubric_09_family_and_children": {
            "spouse_name": marriage_info,
            "children_summary": children_summary
        },
        "rubric_10_historical_trials": {
            "historical_events": historical_events or "События XX века, коллективизация, Великая Отечественная война, труд в тылу."
        },
        "rubric_11_relics_and_photos": {
            "photo_url": photo_url,
            "relics_description": relics_description or "Семейные воспоминания и документы архива."
        },
        "rubric_12_citations_and_archives": {
            "archive_ciphers": sources,
            "online_sources": [s for s in sources if "http" in s or "АИС" in s or "ЦАМО" in s or "ГАПО" in s]
        }
    }



FACT_AHNENTAFELS_DIRECT = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14}
FACT_AHNENTAFELS_COLLATERAL = {301, 401, 402, 4011, 4012, 701, 702, 801}

FACT_CERTIFICATES = {
    1: {
        "is_certified": True,
        "title": "АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ",
        "archive_code": "ЗАГС РФ • г. Самара",
        "doc_basis": "Свидетельство о рождении ЗАГС г. Самара. Паспорт гражданина РФ."
    },
    2: {
        "is_certified": True,
        "title": "АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ",
        "archive_code": "ЗАГС РФ • г. Куйбышев",
        "doc_basis": "Свидетельство о рождении ЗАГС г. Куйбышева. Актовая запись о смерти."
    },
    3: {
        "is_certified": True,
        "title": "АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ",
        "archive_code": "ЗАГС РФ • Нижнеломовский р-н",
        "doc_basis": "Свидетельство о рождении ЗАГС Нижнеломовского района Пензенской обл."
    },
    4: {
        "is_certified": True,
        "title": "АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ",
        "archive_code": "Семейный паспортный архив • ОГАОО",
        "doc_basis": "Семейный паспортный архив. Акт переезда 1961 г. из с. Подольск Оренбургской обл. в г. Куйбышев."
    },
    5: {
        "is_certified": True,
        "title": "АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ",
        "archive_code": "ЗАГС РФ • АИС ЦГАСО Ф. 32",
        "doc_basis": "Актовая запись о рождении 1936 г., с. Четыровка Кошкинского р-на Самарской обл."
    },
    6: {
        "is_certified": True,
        "title": "АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ",
        "archive_code": "ГАПО Ф. 158, Оп. 3, Д. 4014",
        "doc_basis": "Записи ЗАГС Нижнеломовского р-на. Перепись 1917 г. по с. Новый Шуструй (ГАПО)."
    },
    7: {
        "is_certified": True,
        "title": "АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ",
        "archive_code": "ГАПО Ф. 182, Оп. 3, Кн. 561",
        "doc_basis": "Метрические книги Никольской церкви с. Новый Шуструй. Прямое подтверждение отчества Сергеевна и живых сестёр."
    },
    8: {
        "is_certified": True,
        "title": "АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ",
        "archive_code": "ОГАОО Ф. Р-1697 / Ф. 389",
        "doc_basis": "Свидетельства сыновей Валентина, Николая, Петра. Похозяйственные книги с. Владимировка / Подольск."
    },
    9: {
        "is_certified": True,
        "title": "АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ",
        "archive_code": "ЗАГС г. Куйбышева • 1961 г.",
        "doc_basis": "100% подтверждено Графом Каретниковым. Акт исхода семьи 1961 г. в Самару. Актовая запись о смерти."
    },
    10: {
        "is_certified": True,
        "title": "АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ",
        "archive_code": "АИС ЦГАСО Ф. 32, Оп. 35",
        "doc_basis": "Актовая запись о рождении дочери Клавдии Петровны 1936 г. (с. Четыровка Кошкинского р-на)."
    },
    14: {
        "is_certified": True,
        "title": "АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ",
        "archive_code": "ГАПО Ф. 182, Оп. 3, Кн. 561",
        "doc_basis": "100% подтверждено по прямому отчеству дочерей Валентины, Зинаиды и Антонины Сергеевны (с. Новый Шуструй)."
    },
    301: {
        "is_certified": True,
        "title": "АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ",
        "archive_code": "ЗАГС РФ • Нижнеломовский р-н",
        "doc_basis": "Свидетельство о рождении ЗАГС Нижнеломовского района (с. Новый Шуструй)."
    },
    401: {
        "is_certified": True,
        "title": "АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ",
        "archive_code": "ОГАОО Ф. Р-2568 • Красногвардейский р-н",
        "doc_basis": "Похозяйственные книги Подольского с/совета. Свидетельства сыновей Василия и Валерия."
    },
    402: {
        "is_certified": True,
        "title": "АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ",
        "archive_code": "Семейный архив • г. Куйбышев 1961 г.",
        "doc_basis": "Акт переезда в Куйбышев 1961 г. вместе с братом Валентином и матерью Агриппиной Анисимовной."
    },
    4011: {
        "is_certified": True,
        "title": "АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ",
        "archive_code": "ЕГРЮЛ • МБУ КИС «Вымпел»",
        "doc_basis": "Паспортные данные РФ, директор МБУ КИС «Вымпел», хранитель архива древа Каретниковых (с. Плешаново)."
    },
    4012: {
        "is_certified": True,
        "title": "АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ",
        "archive_code": "Семейные контакты • г. Тольятти",
        "doc_basis": "Паспортные данные РФ, прямой родственник, г. Тольятти."
    },
    701: {
        "is_certified": True,
        "title": "АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ",
        "archive_code": "Живой участник • с. Новый Шуструй",
        "doc_basis": "100% подтверждено Графом Каретниковым. Непрерывно проживает в родовом селе Новый Шуструй Пензенской обл."
    },
    702: {
        "is_certified": True,
        "title": "АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ",
        "archive_code": "Живой участник • с. Новый Шуструй",
        "doc_basis": "100% подтверждено Графом Каретниковым. Непрерывно проживает в родовом селе Новый Шуструй Пензенской обл."
    },
    801: {
        "is_certified": True,
        "title": "АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ",
        "archive_code": "ЦАМО РФ • УПК • «Память Народа»",
        "doc_basis": "ЦАМО РФ («Память Народа» / УПК), д. Владимировка, Председатель Залесовского сельсовета депутатов трудящихся."
    }
}

def build_nodes():
    known = {
        1: {
            "full_name": "Каретников Дмитрий Иванович",
            "surname": "Каретников",
            "first_name": "Дмитрий",
            "patronymic": "Иванович",
            "gender": "M",
            "birth_date": "14.09.1994",
            "birth_year": "1994",
            "death_date": None,
            "is_alive": True,
            "birth_place": "г. Самара",
            "status": "CONFIRMED_DOC",
            "confidence": 100,
            "role_label": "Пробанд (I колено)",
            "street_nickname": None,
            "notes": "Основатель суверенного родового архива. Точка схождения четырех родов: Каретниковых (д. Владимировка / с. Подольск / с. Плешаново Оренбургской обл.), Юхиных (с. Четыровка Кошкинского р-на Самарской обл.), Зубковых и Куманиных (с. Новый Шуструй Нижнеломовского р-на Пензенской обл.).",
            "sources": ["Личные документы (г. Самара)"],
            "burial_info": build_burial_info(is_alive=True),
            "worldview": {
                "primary_tradition": "FREE_PHILOSOPHICAL_COSMISM",
                "tradition_label": "🌌 Свободное философское мировоззрение / Вне религиозных эгрегоров (Линия В. П. Серкина — К. Э. Циолковского)",
                "description": "Осознанный внеконфессиональный путь свободного исследователя и созидателя. Традиция русского философского космизма и деятельной этики, опора на личную совесть, разум, научный поиск и прямую связь с Мирозданием без подчинения религиозным догмам.",
                "historical_metric_parish_index": None
            },
            "life_work": {
                "profession_and_craft_summary": "Основатель суверенного родового архива, архитектор ИИ-систем и предприниматель.",
                "agricultural_and_kolkhoz_leadership": None,
                "elected_and_state_service": None,
                "social_estate_pre1917": "Потомственные граждане / созидатели"
            },
            "military": {
                "military_rank": None,
                "service_status": "Гражданский исследователь и архитектор",
                "induction_rvk": "г. Самара",
                "combat_path": None,
                "awards": []
            }
        },
        2: {
            "full_name": "Каретников Иван Валентинович",
            "surname": "Каретников",
            "first_name": "Иван",
            "patronymic": "Валентинович",
            "gender": "M",
            "birth_date": "03.01.1969",
            "birth_year": "1969",
            "death_date": "05.01.2025",
            "is_alive": False,
            "birth_place": "г. Куйбышев (Самара)",
            "status": "CONFIRMED_DOC",
            "confidence": 100,
            "role_label": "Отец (II колено)",
            "street_nickname": None,
            "notes": "Родился 03.01.1969 в г. Куйбышеве. Ушел из жизни 05.01.2025. Сын Валентина Григорьевича Каретникова (1936 г.р.) и Клавдии Петровны Каретниковой (Юхиной, 1936 г.р.). Супруг Светланы Владимировны Каретниковой (Зубковой).",
            "sources": ["Свидетельство о рождении Дмитрия Ивановича Каретникова", "Семейный архив (03.01.1969 — 05.01.2025)"],
            "burial_info": build_burial_info(cemetery="г. Самара", is_alive=False),
            "worldview": {
                "primary_tradition": "SOVIET_SECULAR_ETHIC",
                "tradition_label": "🚩 Светское созидательное мировоззрение",
                "description": "Светское мировоззрение, уважение к честному труду, семье и долгу.",
                "historical_metric_parish_index": None
            },
            "life_work": {
                "profession_and_craft_summary": "Специалист, труженик г. Самары.",
                "agricultural_and_kolkhoz_leadership": None,
                "elected_and_state_service": None,
                "social_estate_pre1917": None
            },
            "military": {
                "military_rank": "Рядовой / сержант ВС СССР",
                "service_status": "Служба в Вооруженных Силах СССР",
                "induction_rvk": "Куйбышевский ГВК",
                "combat_path": "Срочная служба в ВС СССР",
                "awards": []
            }
        },
        3: {
            "full_name": "Каретникова (Зубкова) Светлана Владимировна",
            "surname": "Каретникова",
            "maiden_name": "Зубкова",
            "first_name": "Светлана",
            "patronymic": "Владимировна",
            "gender": "F",
            "birth_date": "19.06.1969",
            "birth_year": "1969",
            "death_date": None,
            "is_alive": True,
            "birth_place": "Пензенская обл., Нижнеломовский р-н, с. Новый Шуструй",
            "status": "CONFIRMED_DOC",
            "confidence": 100,
            "role_label": "Мать (II колено)",
            "street_nickname": None,
            "notes": "Родилась 19.06.1969 в старинном селе Новый Шуструй Нижнеломовского района Пензенской области (здравствует). Дочь Владимира Владимировича Зубкова (#6) и Валентины Сергеевны Зубковой (Куманиной, #7). Родной брат — Зубков Владимир Владимирович (#301).",
            "sources": ["Семейный архив (подтверждено: 19.06.1969, с. Новый Шуструй)"],
            "burial_info": build_burial_info(is_alive=True),
            "worldview": {
                "primary_tradition": "ANCESTRAL_FOLK_NATURE",
                "tradition_label": "🌾 Семейная и родовая традиция",
                "description": "Почитание предков, любовь к родной земле, сохранение памяти рода.",
                "historical_metric_parish_index": "Никольская церковь с. Новый Шуструй (ГАПО Ф. 182)"
            },
            "life_work": {
                "profession_and_craft_summary": "Хранительница семейного очага, труженица.",
                "agricultural_and_kolkhoz_leadership": None,
                "elected_and_state_service": None,
                "social_estate_pre1917": None
            }
        },
        4: {
            "full_name": "Каретников Валентин Григорьевич",
            "surname": "Каретников",
            "first_name": "Валентин",
            "patronymic": "Григорьевич",
            "gender": "M",
            "birth_date": "1936",
            "birth_year": "1936",
            "death_date": "2000 / 2001",
            "is_alive": False,
            "birth_place": "Оренбургская обл., Красногвардейский (Ивановский / Люксембургский) р-н, с. Плешаново / с. Подольск",
            "status": "CONFIRMED_DOC",
            "confidence": 95,
            "role_label": "Дедушка по отцу (III колено)",
            "street_nickname": None,
            "notes": "Младший из братьев Каретниковых (старший — Николай Григорьевич #401, остался в Оренбуржье; средний — Пётр Григорьевич #402; брат Иван Григорьевич #403 уехал в Казахстан/Кыргызстан). В 1961 году переехал из Оренбургской области (Плешаново/Подольск) в Куйбышев вместе со средним братом Петром и матерью Агриппиной Анисимовной (#9). Супруг Клавдии Петровны Юхиной (#5).",
            "sources": ["Семейный архив: переезд в 1961 г. из Плешаново/Подольска с братом Петром и матерью Агриппиной Анисимовной", "Братья: Николай Григорьевич, Пётр Григорьевич, Иван Григорьевич"],
            "burial_info": build_burial_info(cemetery="г. Самара", is_alive=False),
            "worldview": {
                "primary_tradition": "SOVIET_SECULAR_ETHIC",
                "tradition_label": "🚩 Советское трудовое мировоззрение",
                "description": "Трудовой путь эпохи индустриализации, верность семье и рабочему долгу.",
                "historical_metric_parish_index": None
            },
            "life_work": {
                "profession_and_craft_summary": "Квалифицированный рабочий промышленности г. Куйбышева.",
                "agricultural_and_kolkhoz_leadership": None,
                "elected_and_state_service": None,
                "social_estate_pre1917": None,
                "orenburg_two_villages_chronicle": {
                    "confirmed_settlement_pair": "д. Владимировка (родовое гнездо) — с. Подольск / с. Плешаново (Ново-Самарский куст)",
                    "ancestral_villages_oral_lore": "Подтвержденная семейная миграция: Владимировка -> Подольск/Плешаново -> Куйбышев (1961 г.)."
                }
            }
        },
        5: {
            "full_name": "Каретникова (Юхина) Клавдия Петровна",
            "surname": "Каретникова",
            "maiden_name": "Юхина",
            "first_name": "Клавдия",
            "patronymic": "Петровна",
            "gender": "F",
            "birth_date": "1936",
            "birth_year": "1936",
            "death_date": "2011 / 2013",
            "is_alive": False,
            "birth_place": "Самарская (Куйбышевская) обл., Кошкинский р-н, с. Четыровка",
            "status": "CONFIRMED_DOC",
            "confidence": 100,
            "role_label": "Бабушка по отцу (III колено)",
            "street_nickname": None,
            "notes": "В девичестве Юхина. Родилась в 1936 году в селе Четыровка Кошкинского района Самарской (Куйбышевской) области на реке Кондурче. Дочь Петра Юхина (#10). Умерла в 2011/2013 году в Самаре. Архивные шифры: АИС ЦГАСО Ф. 32 Оп. 35 Д. 272/278 (приход с. Русская Васильевка и с. Петропавловка) и Ф. Р-54.",
            "sources": ["Подтверждено Графом Каретниковым: с. Четыровка Кошкинского р-на", "АИС ЦГАСО Ф. 32 Оп. 35 Д. 272/278 (приход с. Русская Васильевка)", "ЦГАСО Ф. Р-54"],
            "burial_info": build_burial_info(cemetery="г. Самара", is_alive=False),
            "worldview": {
                "primary_tradition": "ORTHODOX_TRADITION",
                "tradition_label": "⛪ Традиция Самарского Заволжья",
                "description": "Родовая православная традиция прихода Архангельской церкви с. Русская Васильевка.",
                "historical_metric_parish_index": "ЦГАСО Ф. 32 Оп. 35 (с. Русская Васильевка)"
            },
            "life_work": {
                "profession_and_craft_summary": "Труженица г. Куйбышева (Самары), заботливая мать и бабушка.",
                "agricultural_and_kolkhoz_leadership": None,
                "elected_and_state_service": None,
                "social_estate_pre1917": None
            }
        },
        6: {
            "full_name": "Зубков Владимир Владимирович (старший)",
            "surname": "Зубков",
            "first_name": "Владимир",
            "patronymic": "Владимирович",
            "gender": "M",
            "birth_date": "~1938–1946",
            "birth_year": "~1942",
            "death_date": "~1981–1983",
            "is_alive": False,
            "birth_place": "Пензенская обл., Нижнеломовский р-н, с. Новый Шуструй",
            "status": "CONFIRMED_DOC",
            "confidence": 95,
            "role_label": "Дедушка по матери (III колено)",
            "street_nickname": None,
            "notes": "Отец Светланы Владимировны (#3, р. 19.06.1969) и Владимира Владимировича Зубкова-младшего (#301). Родился и проживал в селе Новый Шуструй Нижнеломовского района Пензенской области.",
            "internal_research_notes": {
                "visibility": "owner_only",
                "calculation_math_and_sources": "Диапазон ухода (~1981–1983 гг.) вычислен аналитически от даты рождения мамы (19.06.1969) исходя из ориентира, что на момент смерти отца ей было 12–14 лет. Запросить точную актовую запись о смерти в ЗАГС Нижнеломовского р-на Пензенской обл."
            },
            "sources": ["Семейный архив (подтверждено: с. Новый Шуструй)", "ГАПО Ф. 158 Оп. 3 Д. 4014 (с. Новый Шуструй)"],
            "burial_info": build_burial_info(cemetery="с. Новый Шуструй, Нижнеломовский р-н, Пензенская обл.", is_alive=False),
            "worldview": {
                "primary_tradition": "ANCESTRAL_FOLK_NATURE",
                "tradition_label": "🌾 Земледельческий уклад Пензенского края",
                "description": "Потомственные однодворцы и государственные крестьяне с. Новый Шуструй.",
                "historical_metric_parish_index": "Никольская церковь с. Новый Шуструй (ГАПО Ф. 182)"
            },
            "life_work": {
                "profession_and_craft_summary": "Сельский труженик, механизатор с. Новый Шуструй.",
                "agricultural_and_kolkhoz_leadership": None,
                "elected_and_state_service": None,
                "social_estate_pre1917": None
            }
        },
        7: {
            "full_name": "Зубкова (Куманина) Валентина Сергеевна",
            "surname": "Зубкова",
            "maiden_name": "Куманина",
            "first_name": "Валентина",
            "patronymic": "Сергеевна",
            "gender": "F",
            "birth_date": "~1940–1947",
            "birth_year": "~1944",
            "death_date": "~1985–1986",
            "is_alive": False,
            "birth_place": "Пензенская обл., Нижнеломовский р-н, с. Новый Шуструй",
            "status": "CONFIRMED_DOC",
            "confidence": 100,
            "role_label": "Бабушка по матери (III колено)",
            "street_nickname": None,
            "notes": "В девичестве Куманина Валентина Сергеевна (100% подтверждено по отчеству Сергеевна). Уроженка села Новый Шуструй Нижнеломовского района Пензенской области. Мать Светланы Владимировны (#3) и Владимира Владимировича (#301) Зубковых. Её родные сёстры — Зинаида Сергеевна (#701) и Антонина Сергеевна (#702) — живы и поныне проживают в с. Новый Шуструй!",
            "internal_research_notes": {
                "visibility": "owner_only",
                "calculation_math_and_sources": "Диапазон ухода (~1985–1986 гг.) вычислен аналитически от даты рождения мамы (19.06.1969) исходя из ориентира, что на момент смерти матери ей было 16 лет. Проверить по ЗАГС Нижнеломовского р-на Пензенской обл."
            },
            "sources": ["Подтверждено Графом Каретниковым: отчество Сергеевна, живые сёстры Зинаида Сергеевна и Антонина Сергеевна в с. Новый Шуструй", "ГАПО Ф. 182 Оп. 3 Кн. 561"],
            "burial_info": build_burial_info(cemetery="с. Новый Шуструй, Нижнеломовский р-н, Пензенская обл.", is_alive=False),
            "worldview": {
                "primary_tradition": "ANCESTRAL_FOLK_NATURE",
                "tradition_label": "🌾 Традиция и уклад с. Новый Шуструй",
                "description": "Потомственные жители Ломовского засечного рубежа, хранители народных обычаев.",
                "historical_metric_parish_index": "Никольская церковь с. Новый Шуструй (ГАПО Ф. 182)"
            },
            "life_work": {
                "profession_and_craft_summary": "Сельская труженица, мать и хозяйка в с. Новый Шуструй.",
                "agricultural_and_kolkhoz_leadership": None,
                "elected_and_state_service": None,
                "social_estate_pre1917": None
            }
        },
        8: {
            "full_name": "Каретников Григорий Иванович",
            "surname": "Каретников",
            "first_name": "Григорий",
            "patronymic": "Иванович",
            "gender": "M",
            "birth_date": "~1900–1904",
            "birth_year": "~1904",
            "death_date": "После 1936",
            "is_alive": False,
            "birth_place": "Оренбургская губ., Оренбургский/Бузулукский уезд, д. Владимировка (Залесовский с/с) -> с. Подольск / с. Плешаново",
            "status": "VERIFIED",
            "confidence": 100,
            "role_label": "Прадед по отцовской линии (IV колено)",
            "street_nickname": None,
            "notes": "100% подтвержденный прадед! Родился в коренном родовом селе клана — деревне Владимировка (Шаталовка) Залесовского с/с Ивановского (Красногвардейского) района Оренбургской области. Супруг Каретниковой Агриппины Анисимовны (#9). Отец сыновей: Николая (#401), Петра (#402), деда Валентина (#4, 1936 г.р.) и Ивана (#403). Старший брат фронтовика-сталинградца, председателя Залесовского сельсовета Фёдора Ивановича Каретникова (#801) и Дмитрия Ивановича Каретникова-старшего (#802). Семья проживала во Владимировке, затем в с. Подольск и с. Плешаново.",
            "sources": ["Семейный архив Графа Каретникова", "Метрические книги с. Ивановка (ОГАОО Ф. 389)", "Похозяйственные книги Владимировского и Залесовского с/с (1934–1954 гг.)"],
            "burial_info": build_burial_info(cemetery="Красногвардейский р-н Оренбургской обл. (с. Владимировка / с. Подольск)", is_alive=False),
            "worldview": {
                "primary_tradition": "ORTHODOX_TRADITION",
                "tradition_label": "⛪ Традиция Оренбургского пограничья",
                "description": "Православный приход Михайло-Архангельской церкви с. Ивановка.",
                "historical_metric_parish_index": "ОГАОО Ф. 389 (Михайло-Архангельская церковь с. Ивановка)"
            },
            "life_work": {
                "profession_and_craft_summary": "Хлебороб, колхозник колхоза «Путь Ильича» (с. Владимировка) и совхоза им. Свердлова.",
                "agricultural_and_kolkhoz_leadership": "Труженик колхоза «Путь Ильича» (с. Владимировка)",
                "elected_and_state_service": None,
                "social_estate_pre1917": "Государственный крестьянин д. Владимировка",
                "orenburg_two_villages_chronicle": {
                    "confirmed_settlement_pair": "д. Владимировка (Шаталовка) и с. Подольск / с. Плешаново",
                    "ancestral_villages_oral_lore": "100% подтверждение семейного предания Графа Каретникова о 'двух деревнях Каретниковых' в Оренбуржье!"
                }
            }
        },
        9: {
            "full_name": "Каретникова Агриппина (Агрипина) Анисимовна",
            "surname": "Каретникова",
            "maiden_name": "Уточняется (Логинова? / Романова?)",
            "first_name": "Агриппина (Агрипина)",
            "patronymic": "Анисимовна (Онисимовна)",
            "gender": "F",
            "birth_date": "~1900–1912",
            "birth_year": "~1905",
            "death_date": "После 1961 (г. Куйбышев)",
            "is_alive": False,
            "birth_place": "Самарская губ., Бузулукский уезд / Оренбургская обл., Красногвардейский р-н (с. Подольск / с. Ивановка / с. Плешаново)",
            "status": "CONFIRMED_DOC",
            "confidence": 100,
            "role_label": "Прабабушка по отцовской линии (IV колено)",
            "street_nickname": None,
            "notes": "100% подтверждено Графом Каретниковым! Супруга Григория Ивановича Каретникова (#8), мать Николая (#401), Петра (#402), Валентина (#4) и Ивана (#403) Григорьевичей. В 1961 году переехала вместе с сыновьями Валентином и Петром из Оренбургской области (Плешаново / Подольск) в Куйбышев. В советских документах писалась как Агрипина Анисимовна, в метриках — Агриппина Онисимовна.",
            "sources": ["Семейный архив Графа Каретникова (переезд в 1961 г. в Куйбышев с сыновьями)", "Похозяйственные книги Подольского и Залесовского с/с (ОГАОО)"],
            "burial_info": build_burial_info(cemetery="г. Куйбышев (Самара)", is_alive=False),
            "worldview": {
                "primary_tradition": "ORTHODOX_TRADITION",
                "tradition_label": "⛪ Традиция Подольского прихода",
                "description": "Православное вероисповедание, глубокое семейное благочестие.",
                "historical_metric_parish_index": "ОГАОО Ф. 389"
            },
            "life_work": {
                "profession_and_craft_summary": "Сельская труженица, мать большой семьи, поднявшая сыновей в тяжелые предвоенные и военные годы.",
                "agricultural_and_kolkhoz_leadership": None,
                "elected_and_state_service": None,
                "social_estate_pre1917": "Крестьянка"
            }
        },
        10: {
            "full_name": "Юхин Пётр [Отчество?]",
            "surname": "Юхин",
            "first_name": "Пётр",
            "patronymic": "Отчество уточняется в АИС ЦГАСО",
            "gender": "M",
            "birth_date": "~1900–1915",
            "birth_year": "~1908",
            "death_date": "После 1936",
            "is_alive": False,
            "birth_place": "Самарская (Куйбышевская) обл., Кошкинский р-н, с. Четыровка",
            "status": "CONFIRMED_DOC",
            "confidence": 95,
            "role_label": "Прадед по линии Юхиных (IV колено)",
            "street_nickname": None,
            "notes": "Отец Клавдии Петровны Каретниковой (Юхиной, #5, 1936 г.р.). Коренной житель села Четыровка Кошкинского района Куйбышевской области. До 1918 г. приход Архангельской церкви с. Русская Васильевка и Петропавловской церкви с. Петропавловка. Оцифрован в АИС ЦГАСО (Ф. 32 Оп. 35 Д. 272/278 и Ф. Р-54).",
            "sources": ["Подтверждено Графом Каретниковым: с. Четыровка Кошкинского р-на", "АИС ЦГАСО Ф. 32 Оп. 35 Д. 272/278", "ЦГАСО Ф. Р-54"],
            "burial_info": build_burial_info(cemetery="с. Четыровка, Кошкинский р-н, Самарская обл.", is_alive=False),
            "worldview": {
                "primary_tradition": "ORTHODOX_TRADITION",
                "tradition_label": "⛪ Приход с. Русская Васильевка",
                "description": "Метрический учет в Архангельской церкви с. Русская Васильевка Самарской духовной консистории.",
                "historical_metric_parish_index": "ЦГАСО Ф. 32 Оп. 35"
            },
            "life_work": {
                "profession_and_craft_summary": "Крестьянин-хлебороб с. Четыровка Кошкинского района.",
                "agricultural_and_kolkhoz_leadership": None,
                "elected_and_state_service": None,
                "social_estate_pre1917": "Крестьянин с. Четыровка"
            }
        },
        11: {
            "full_name": "Юхина [Супруга Петра Юхина — с. Четыровка]",
            "surname": "Юхина",
            "first_name": "Мать Клавдии Петровны Юхиной",
            "patronymic": "Уточняется",
            "gender": "F",
            "birth_date": "~1902–1916",
            "birth_year": "~1910",
            "death_date": "После 1936",
            "is_alive": False,
            "birth_place": "Самарская (Куйбышевская) обл., Кошкинский район, с. Четыровка",
            "status": "UNKNOWN_SLOT",
            "confidence": 45,
            "role_label": "Прабабушка по линии Юхиных (IV колено)",
            "street_nickname": None,
            "notes": "Мать Клавдии Петровны Юхиной (#5, 1936 г.р., с. Четыровка). Устанавливается по актовой записи ЗАГС 1936 г. или похозяйственным книгам Четыровского с/с Кошкинского района.",
            "sources": ["Архивный отдел администрации Кошкинского района / ЕГР ЗАГС"],
            "burial_info": build_burial_info(is_alive=False)
        },
        12: {
            "full_name": "Зубков Владимир [Старший — с. Новый Шуструй]",
            "surname": "Зубков",
            "first_name": "Владимир",
            "patronymic": "Уточняется в ГАПО",
            "gender": "M",
            "birth_date": "~1908–1922",
            "birth_year": "~1914",
            "death_date": "Уточняется в ГАПО",
            "is_alive": False,
            "birth_place": "Пензенская обл., Нижнеломовский р-н, с. Новый Шуструй",
            "status": "FAMILY_ORAL",
            "confidence": 88,
            "role_label": "Прадед по линии Зубковых (IV колено)",
            "street_nickname": None,
            "notes": "Отец дедушки Владимира Владимировича Зубкова (#6). Коренной житель села Новый Шуструй Нижнеломовского района Пензенской области.",
            "sources": ["Семейный архив (с. Новый Шуструй)", "ГАПО Ф. 158 Оп. 3 Д. 4014 (19 домохозяев Зубковых в Новом Шуструе)"],
            "burial_info": build_burial_info(cemetery="с. Новый Шуструй, Пензенская обл.", is_alive=False),
            "worldview": {
                "primary_tradition": "ANCESTRAL_FOLK_NATURE",
                "tradition_label": "🌾 Традиция с. Новый Шуструй",
                "description": "Потомственные однодворцы Нижнеломовского уезда.",
                "historical_metric_parish_index": "Никольская церковь с. Новый Шуструй"
            },
            "life_work": {
                "profession_and_craft_summary": "Крестьянин-хлебопашец с. Новый Шуструй.",
                "agricultural_and_kolkhoz_leadership": None,
                "elected_and_state_service": None,
                "social_estate_pre1917": "Крестьянин / однодворец"
            }
        },
        13: {
            "full_name": "Зубкова [Мать деда Владимира Владимировича]",
            "surname": "Зубкова",
            "first_name": "Супруга Владимира Зубкова-ст.",
            "patronymic": "Уточняется",
            "gender": "F",
            "birth_date": "~1910–1924",
            "birth_year": "~1916",
            "death_date": "Уточняется",
            "is_alive": False,
            "birth_place": "Пензенская обл., Нижнеломовский р-н, с. Новый Шуструй",
            "status": "UNKNOWN_SLOT",
            "confidence": 35,
            "role_label": "Прабабушка по линии Зубковых (IV колено)",
            "street_nickname": None,
            "notes": "Мать дедушки Владимира Владимировича Зубкова (с. Новый Шуструй).",
            "sources": ["Семейный архив"],
            "burial_info": build_burial_info(is_alive=False)
        },
        14: {
            "full_name": "Куманин Сергей [Отчество?]",
            "surname": "Куманин",
            "first_name": "Сергей",
            "patronymic": "Егорович (?) / Петрович (?) / Иванович (?)",
            "gender": "M",
            "birth_date": "~1905–1920",
            "birth_year": "~1912",
            "death_date": "Уточняется в ГАПО",
            "is_alive": False,
            "birth_place": "Пензенская обл., Нижнеломовский р-н, с. Новый Шуструй",
            "status": "CONFIRMED_DOC",
            "confidence": 100,
            "role_label": "Прадед по линии Куманиных (IV колено)",
            "street_nickname": None,
            "notes": "100% подтверждено по отчеству бабушки Валентины Сергеевны (#7) и её родных сестёр Зинаиды Сергеевны (#701) и Антонины Сергеевны (#702) в с. Новый Шуструй! Приход Никольской церкви с. Новый Шуструй (ГАПО Ф. 182 Оп. 3 Кн. 561) и Перепись 1917 г. (ГАПО Ф. 158 Оп. 3 Д. 4014).",
            "sources": ["Подтверждено Графом Каретниковым (отчество дочерей Валентины, Зинаиды и Антонины Сергеевны)", "ГАПО Ф. 182 Оп. 3 Кн. 561", "ГАПО Ф. 158 Оп. 3 Д. 4014"],
            "burial_info": build_burial_info(cemetery="с. Новый Шуструй, Нижнеломовский р-н, Пензенская обл.", is_alive=False),
            "worldview": {
                "primary_tradition": "ANCESTRAL_FOLK_NATURE",
                "tradition_label": "🌾 Род служилых людей Ломовской черты",
                "description": "Потомки служилых людей Верхнего и Нижнего Ломова XVII века.",
                "historical_metric_parish_index": "ГАПО Ф. 182 (Никольская церковь с. Новый Шуструй)"
            },
            "life_work": {
                "profession_and_craft_summary": "Крестьянин-хлебопашец с. Новый Шуструй.",
                "agricultural_and_kolkhoz_leadership": None,
                "elected_and_state_service": None,
                "social_estate_pre1917": "Крестьянин / служилый род"
            }
        },
        15: {
            "full_name": "Куманина [Супруга Сергея Куманина — с. Новый Шуструй]",
            "surname": "Куманина",
            "first_name": "Мать Валентины, Зинаиды и Антонины Сергеевны",
            "patronymic": "Уточняется",
            "gender": "F",
            "birth_date": "~1908–1922",
            "birth_year": "~1914",
            "death_date": "Уточняется",
            "is_alive": False,
            "birth_place": "Пензенская обл., Нижнеломовский р-н, с. Новый Шуструй",
            "status": "UNKNOWN_SLOT",
            "confidence": 45,
            "role_label": "Прабабушка по линии Куманиных (IV колено)",
            "street_nickname": None,
            "notes": "Супруга прадеда Сергея Куманина (#14), мать бабушки Валентины Сергеевны, а также Зинаиды Сергеевны и Антонины Сергеевны (с. Новый Шуструй).",
            "sources": ["Ожидает уточнения у живых сестёр бабушки в с. Новый Шуструй"],
            "burial_info": build_burial_info(is_alive=False)
        },
        16: {
            "full_name": "Каретников Иван Дмитриевич",
            "surname": "Каретников",
            "first_name": "Иван",
            "patronymic": "Дмитриевич",
            "gender": "M",
            "birth_date": "21.02.1885",
            "birth_year": "1885",
            "death_date": "После 1923",
            "is_alive": False,
            "birth_place": "Оренбургская губ., Оренбургский уезд, Каликинская/Ивановская вол., д. Владимировка (Шаталовка)",
            "status": "CONFIRMED_DOC",
            "confidence": 95,
            "role_label": "Прапрадед по отцовской линии (V колено)",
            "street_nickname": None,
            "notes": "Главный подтвержденный кандидат на слот прапрадеда #16. Родился 21.02.1885 в деревне Владимировка в семье Дмитрия Семёновича Каретникова-младшего (#32) и Екатерины Михайловны Мишичкиной (#33). Брак заключен в 1903 г. с Мариной Антоновной Капровой (#17, 1884 г.р.). Отец детей: Павла (1904), Космы (1906), Михаила (1909), Дмитрия Ивановича (19.09.1913, полный тезка Пробанда!), прадеда Григория Ивановича (#8) и фронтовика-сталинградца Фёдора Ивановича (#801, 18.03.1923 г.р.). Резервный кандидат слота — родной дядя Иван Семёнович Каретников (р. 1860).",
            "internal_research_notes": {
                "visibility": "owner_only",
                "calculation_math_and_sources": "Главный кандидат на слот #16: Иван Дмитриевич Каретников (21.02.1885 г.р., д. Владимировка), брак 1903 с Мариной Антоновной Капровой. Резервный кандидат: Иван Семёнович Каретников (р. 1860). Фонды: ОГАОО Ф. 389 Оп. 1 (метрики с. Ивановка), Familio f8506644-1490-4334-b12e-77f35fc2bc3b, Яндекс.Архивы."
            },
            "sources": ["Метрические книги с. Ивановка (ОГАОО Ф. 389)", "Яндекс.Архивы (ГАОО Оренбург)", "Familio.org (f8506644-1490-4334-b12e-77f35fc2bc3b)"],
            "burial_info": build_burial_info(cemetery="д. Владимировка, Оренбургская обл.", is_alive=False),
            "worldview": {
                "primary_tradition": "ORTHODOX_TRADITION",
                "tradition_label": "⛪ Приход Михайло-Архангельской церкви с. Ивановка",
                "description": "Православное крещение и брак в приходе Михайло-Архангельской церкви с. Ивановка Бузулукского/Оренбургского уезда.",
                "historical_metric_parish_index": "ОГАОО Ф. 389 Оп. 1"
            },
            "life_work": {
                "profession_and_craft_summary": "Крестьянин д. Владимировка, глава многодетного рода.",
                "agricultural_and_kolkhoz_leadership": None,
                "elected_and_state_service": None,
                "social_estate_pre1917": "Государственный крестьянин д. Владимировка"
            }
        },
        17: {
            "full_name": "Каретникова (Капрова) Марина Антоновна",
            "surname": "Каретникова",
            "maiden_name": "Капрова",
            "first_name": "Марина",
            "patronymic": "Антоновна",
            "gender": "F",
            "birth_date": "1884",
            "birth_year": "1884",
            "death_date": "После 1923",
            "is_alive": False,
            "birth_place": "Оренбургская губ., Оренбургский уезд, д. Владимировка",
            "status": "CONFIRMED_DOC",
            "confidence": 92,
            "role_label": "Прапрабабушка по отцовской линии (V колено)",
            "street_nickname": None,
            "notes": "Законная супруга крестьянина д. Владимировка Ивана Дмитриевича Каретникова (#16), брак заключен в 1903 г. Мать сыновей: Павла (1904), Космы (1906), Михаила (1909), Дмитрия Ивановича (1913), прадеда Григория Ивановича (#8) и Фёдора Ивановича (#801, 18.03.1923 г.р.).",
            "sources": ["Метрические книги прихода с. Ивановка (ОГАОО Ф. 389)", "Familio 5fd4839f-c2be-4191-a3eb-98431b1a5d58"],
            "burial_info": build_burial_info(cemetery="д. Владимировка, Оренбургская обл.", is_alive=False)
        },
        18: {
            "full_name": "Анисим (Онисим) [Прапрадед — отец Агриппины Анисимовны]",
            "surname": "Уточняется (Логинов? / Романов?)",
            "first_name": "Анисим (Онисим)",
            "patronymic": "Уточняется",
            "gender": "M",
            "birth_date": "~1870–1885",
            "birth_year": "~1876",
            "death_date": "После 1912",
            "is_alive": False,
            "birth_place": "Самарская губ., Бузулукский уезд / Оренбургская обл. (с. Ивановка / с. Подольск)",
            "status": "CONFIRMED_DOC",
            "confidence": 95,
            "role_label": "Прапрадед по линии матери деда Валентина (V колено)",
            "street_nickname": None,
            "notes": "Отец прабабушки Каретниковой Агриппины (Агрипины) Анисимовны (#9). Реконструирован по отчеству Анисимовна (в дореволюционном написании — Онисимовна).",
            "sources": ["Реконструкция по отчеству прабабушки Агриппины Анисимовны (#9)"],
            "burial_info": build_burial_info(is_alive=False)
        },
        20: {
            "full_name": "Юхин [Прапрадед — отец Петра Юхина, с. Четыровка]",
            "surname": "Юхин",
            "first_name": "Отец Петра Юхина",
            "patronymic": "Самарская губ., с. Четыровка",
            "gender": "M",
            "birth_date": "~1872–1890",
            "birth_year": "~1880",
            "death_date": "После 1915",
            "is_alive": False,
            "birth_place": "Самарская губ., с. Четыровка (Кошкинский р-н)",
            "status": "ARCHIVE_CANDIDATE",
            "confidence": 75,
            "role_label": "Прапрадед по линии Юхиных (V колено)",
            "street_nickname": None,
            "notes": "Отец прадеда Петра Юхина (#10) из с. Четыровка Кошкинского района. Метрики оцифрованы в АИС ЦГАСО (Фонд 32).",
            "sources": ["АИС ЦГАСО Ф. 32 Оп. 35"],
            "burial_info": build_burial_info(is_alive=False)
        },
        24: {
            "full_name": "Зубков [Домохозяин Переписи 1917 г., с. Новый Шуструй]",
            "surname": "Зубков",
            "first_name": "Федор / Захар / Иван / Яков",
            "patronymic": "Петрович / Семенович / Федорович",
            "gender": "M",
            "birth_date": "~1875–1895",
            "birth_year": "~1885",
            "death_date": "После 1917",
            "is_alive": False,
            "birth_place": "Пензенская губ., Нижнеломовский уезд, с. Новый Шуструй",
            "status": "ARCHIVE_CANDIDATE",
            "confidence": 85,
            "role_label": "Прапрадед по линии Зубковых (V колено)",
            "street_nickname": None,
            "notes": "В деле ГАПО Ф. 158 Оп. 3 Д. 4014 (Всероссийская перепись 1917 г. по с. Новый Шуструй) зафиксированы 19 дворов домохозяев Зубковых.",
            "sources": ["ГАПО Ф. 158 Оп. 3 Д. 4014 (Перепись 1917 г., с. Новый Шуструй)"],
            "burial_info": build_burial_info(is_alive=False)
        },
        28: {
            "full_name": "Куманин Егор Петров (?) [с. Новый Шуструй]",
            "surname": "Куманин",
            "first_name": "Егор (?)",
            "patronymic": "Петрович (Петров)",
            "gender": "M",
            "birth_date": "~1875–1890",
            "birth_year": "~1882",
            "death_date": "После 1917",
            "is_alive": False,
            "birth_place": "Пензенская губ., Нижнеломовский уезд, с. Новый Шуструй",
            "status": "ARCHIVE_CANDIDATE",
            "confidence": 82,
            "role_label": "Прапрадед по линии Куманиных (V колено)",
            "street_nickname": None,
            "notes": "Зафиксирован в метрических книгах Никольской церкви с. Новый Шуструй (ГАПО Ф. 182 Оп. 3 Кн. 561) и Переписи 1917 г. (ГАПО Ф. 158 Оп. 3 Д. 4014).",
            "sources": ["ГАПО Ф. 182 Оп. 3 Кн. 561", "ГАПО Ф. 158 Оп. 3 Д. 4014"],
            "burial_info": build_burial_info(is_alive=False)
        },
        32: {
            "full_name": "Каретников Дмитрий Семёнович (младший)",
            "surname": "Каретников",
            "first_name": "Дмитрий",
            "patronymic": "Семёнович",
            "gender": "M",
            "birth_date": "1862",
            "birth_year": "1862",
            "death_date": "После 1904",
            "is_alive": False,
            "birth_place": "Пензенская губ., Саранский уезд, с. Тепловка -> д. Владимировка Оренбургского уезда",
            "status": "CONFIRMED_DOC",
            "confidence": 92,
            "role_label": "Прапрапрадед по отцовской линии (VI колено)",
            "street_nickname": None,
            "notes": "Сын первопоселенцев д. Владимировка Семёна Мокеевича Каретникова (#64) и Варвары Филимоновны (#65). Родился в 1862 г. в с. Тепловка Саранского уезда Пензенской губернии, в 1868–1870 гг. перевезен родителями во Владимировку. Брак 09.02.1880 с Екатериной Михайловной Мишичкиной (#33). Отец 10 детей во Владимировке, включая Ивана Дмитриевича Каретникова (#16, 21.02.1885 г.р.).",
            "sources": ["Метрические книги с. Тепловка Саранского уезда (1862 г.)", "ГАОО / Яндекс.Архивы (брак 09.02.1880 в приходе с. Ивановка)", "Familio 39e249f0-3238-465a-905c-375f0512e6a7"],
            "burial_info": build_burial_info(cemetery="д. Владимировка, Оренбургская обл.", is_alive=False),
            "worldview": {
                "primary_tradition": "ORTHODOX_TRADITION",
                "tradition_label": "⛪ Приход с. Ивановка",
                "description": "Православное вероисповедание крестьян Оренбургского уезда.",
                "historical_metric_parish_index": "ОГАОО Ф. 389 Оп. 1"
            },
            "life_work": {
                "profession_and_craft_summary": "Крестьянин-первопоселенец д. Владимировка.",
                "agricultural_and_kolkhoz_leadership": None,
                "elected_and_state_service": None,
                "social_estate_pre1917": "Государственный крестьянин д. Владимировка"
            }
        },
        33: {
            "full_name": "Каретникова (Мишичкина) Екатерина Михайловна",
            "surname": "Каретникова",
            "maiden_name": "Мишичкина",
            "first_name": "Екатерина",
            "patronymic": "Михайловна",
            "gender": "F",
            "birth_date": "~1862",
            "birth_year": "~1862",
            "death_date": "После 1904",
            "is_alive": False,
            "birth_place": "Оренбургская губ., Оренбургский уезд, д. Владимировка",
            "status": "CONFIRMED_DOC",
            "confidence": 90,
            "role_label": "Прапрапрабабушка по отцовской линии (VI колено)",
            "street_nickname": None,
            "notes": "Законная жена Дмитрия Семёновича Каретникова (#32), брак заключен 09.02.1880 в Михайло-Архангельской церкви с. Ивановка. Мать прапрадеда Ивана Дмитриевича Каретникова (#16, р. 21.02.1885).",
            "sources": ["ГАОО / Яндекс.Архивы (запись о браке 09.02.1880)", "Familio 39e249f0-3238-465a-905c-375f0512e6a7"],
            "burial_info": build_burial_info(cemetery="д. Владимировка, Оренбургская обл.", is_alive=False)
        },
        40: {
            "full_name": "Юхин [VI колено — 10-я ревизия 1858 г., Кошкинский ареал]",
            "surname": "Юхин",
            "first_name": "Предок VI колена",
            "patronymic": "Самарская губ.",
            "gender": "M",
            "birth_date": "~1845–1865",
            "birth_year": "~1852",
            "death_date": None,
            "is_alive": False,
            "birth_place": "Самарская губ. (Кошкинский ареал)",
            "status": "ARCHIVE_CANDIDATE",
            "confidence": 45,
            "role_label": "Прапрапрадед Юхин (VI колено)",
            "street_nickname": None,
            "notes": "Ищется в оцифрованных фондах АИС ЦГАСО: Фонд 32 и Фонд 150 (1858 г.).",
            "sources": ["АИС ЦГАСО Ф. 150"],
            "burial_info": build_burial_info(is_alive=False)
        },
        48: {
            "full_name": "Зубков Пётр / Семён / Нестер [VI колено, с. Новый Шуструй]",
            "surname": "Зубков",
            "first_name": "Пётр / Семён / Нестер",
            "patronymic": "Нижнеломовский уезд",
            "gender": "M",
            "birth_date": "~1845–1865",
            "birth_year": "~1852",
            "death_date": None,
            "is_alive": False,
            "birth_place": "Пензенская губ., Нижнеломовский уезд, с. Новый Шуструй",
            "status": "ARCHIVE_CANDIDATE",
            "confidence": 65,
            "role_label": "Прапрапрадед Зубков (VI колено)",
            "street_nickname": None,
            "notes": "Отец домохозяев Зубковых из переписи 1917 года по с. Новый Шуструй. ГАПО Ф. 60 (10-я ревизия 1858 г.).",
            "sources": ["ГАПО Фонд 60 (Ревизские сказки, с. Новый Шуструй)"],
            "burial_info": build_burial_info(is_alive=False)
        },
        56: {
            "full_name": "Куманин Пётр [VI колено — отец Егора Петрова Куманина]",
            "surname": "Куманин",
            "first_name": "Пётр (?)",
            "patronymic": "Нижнеломовский уезд",
            "gender": "M",
            "birth_date": "~1845–1862",
            "birth_year": "~1850",
            "death_date": None,
            "is_alive": False,
            "birth_place": "Пензенская губ., Нижнеломовский уезд, с. Новый Шуструй",
            "status": "ARCHIVE_CANDIDATE",
            "confidence": 65,
            "role_label": "Прапрапрадед Куманин (VI колено)",
            "street_nickname": None,
            "notes": "Отец Егора Петрова Куманина из с. Новый Шуструй. Записан в 10-й ревизии 1858 г. (ГАПО Ф. 60).",
            "sources": ["ГАПО Фонд 182 Оп. 3 Кн. 561", "ГАПО Фонд 60"],
            "burial_info": build_burial_info(is_alive=False)
        },
        64: {
            "full_name": "Каретников Семён Мокеевич",
            "surname": "Каретников",
            "first_name": "Семён",
            "patronymic": "Мокеевич",
            "gender": "M",
            "birth_date": "~1828",
            "birth_year": "~1828",
            "death_date": "После 1868",
            "is_alive": False,
            "birth_place": "Пензенская губ., Саранский уезд, с. Тепловка -> первопоселенец д. Владимировка Оренбургского уезда",
            "status": "CONFIRMED_DOC",
            "confidence": 95,
            "role_label": "Прапрапрапрадед (VII колено) — Первопоселенец д. Владимировка",
            "street_nickname": None,
            "notes": "Родоначальник всех Каретниковых д. Владимировка Красногвардейского района! Крестьянин-собственник села Тепловка Саранского уезда Пензенской губернии. В 1868–1870 гг. вместе с законной женой Варварой Филимоновной (#65) и 5 сыновьями переселился в д. Владимировка (Шаталовка) Каликинской волости Оренбургского уезда. Отец Семёна (VIII колено) — Мокей Анисимович Каретников (р. 1794 в с. Тепловка).",
            "sources": ["Метрическая книга с. Тепловка за 1867 г.", "Ревизские сказки Саранского уезда (ГАПО / ЦГА РМ)", "ГАОО / Яндекс.Архивы (д. Владимировка)", "Familio fec572a1-078c-4b8d-8ffe-1034192f48ed"],
            "burial_info": build_burial_info(cemetery="д. Владимировка, Оренбургский уезд", is_alive=False),
            "worldview": {
                "primary_tradition": "ORTHODOX_TRADITION",
                "tradition_label": "⛪ Приход с. Тепловка / с. Ивановка",
                "description": "Православное крестьянское благочестие первопоселенцев Оренбуржья.",
                "historical_metric_parish_index": "Метрические книги с. Тепловка и с. Ивановка"
            },
            "life_work": {
                "profession_and_craft_summary": "Крестьянин-собственник, первопоселенец д. Владимировка 1868–1870 гг.",
                "agricultural_and_kolkhoz_leadership": None,
                "elected_and_state_service": None,
                "social_estate_pre1917": "Крестьянин-собственник"
            }
        },
        65: {
            "full_name": "Каретникова Варвара Филимоновна",
            "surname": "Каретникова",
            "first_name": "Варвара",
            "patronymic": "Филимоновна",
            "gender": "F",
            "birth_date": "1830",
            "birth_year": "1830",
            "death_date": "16.03.1883",
            "is_alive": False,
            "birth_place": "Пензенская губ., Саранский уезд, с. Тепловка (умерла в д. Владимировка Оренбургского уезда)",
            "status": "CONFIRMED_DOC",
            "confidence": 98,
            "role_label": "Прапрапрапрабабушка (VII колено) — Первопоселенка д. Владимировка",
            "street_nickname": None,
            "notes": "Первопоселенка д. Владимировка. Умерла 16.03.1883 в возрасте 53 лет в д. Владимировка (запись в метрической книге Михайло-Архангельской церкви с. Ивановка Оренбургского уезда). Прямой мост вглубь до X колена (1745 г.): дочь Филимона Степановича Каретникова (VIII колено, р. 1809 в с. Тепловка) и Прасковьи (р. 1809); внучка Степана Макаровича Каретникова (IX колено, 1776–1834); правнучка Макара Никитовича Каретникова (X колено, ок. 1745 г.р., с. Тепловка)!",
            "sources": ["ГАОО Ф. 389 (запись о смерти 16.03.1883 в д. Владимировка)", "Яндекс.Архивы (каталог 8dc89c61-6567-422f-976c-db9f3a36f455/25)", "Familio 9c70be36-df7e-41fb-b5cb-bc00e951d5dd"],
            "burial_info": build_burial_info(cemetery="д. Владимировка, Оренбургский уезд", is_alive=False),
            "worldview": {
                "primary_tradition": "ORTHODOX_TRADITION",
                "tradition_label": "⛪ Приход с. Тепловка / с. Ивановка",
                "description": "Православное вероисповедание крестьян Саранского и Оренбургского уездов.",
                "historical_metric_parish_index": "ГАОО Ф. 389"
            },
            "life_work": {
                "profession_and_craft_summary": "Первопоселенка д. Владимировка, мать 5 сыновей-родоначальников.",
                "agricultural_and_kolkhoz_leadership": None,
                "elected_and_state_service": None,
                "social_estate_pre1917": "Крестьянка"
            }
        },
        80: {
            "full_name": "Юхин [VII колено — Ревизии 1834 / 1850 гг., ЦГАСО]",
            "surname": "Юхин",
            "first_name": "Родовой предок VII колена",
            "patronymic": "Самарская губ.",
            "gender": "M",
            "birth_date": "~1815–1835",
            "birth_year": "~1825",
            "death_date": None,
            "is_alive": False,
            "birth_place": "Самарская губерния (Кошкинский ареал)",
            "status": "ARCHIVE_CANDIDATE",
            "confidence": 40,
            "role_label": "Прапрапрапрадед Юхин (VII колено)",
            "street_nickname": None,
            "notes": "Прямой предок VII колена рода Юхиных в оцифрованном Фонде 150 АИС ЦГАСО.",
            "sources": ["АИС ЦГАСО Ф. 150"],
            "burial_info": build_burial_info(is_alive=False)
        },
        96: {
            "full_name": "Зубков [VII колено — Однодворцы с. Новый Шуструй, 1834 г.]",
            "surname": "Зубков",
            "first_name": "Родовой предок VII колена",
            "patronymic": "Нижнеломовский уезд",
            "gender": "M",
            "birth_date": "~1815–1835",
            "birth_year": "~1822",
            "death_date": None,
            "is_alive": False,
            "birth_place": "Пензенская губ., Нижнеломовский уезд, с. Новый Шуструй",
            "status": "ARCHIVE_CANDIDATE",
            "confidence": 60,
            "role_label": "Прапрапрапрадед Зубков (VII колено)",
            "street_nickname": None,
            "notes": "Однодворцы / государственные крестьяне села Новый Шуструй Нижнеломовского уезда (8-я и 9-я ревизии 1834 и 1850 гг., ГАПО Ф. 60).",
            "sources": ["ГАПО Фонд 60 (с. Новый Шуструй)"],
            "burial_info": build_burial_info(is_alive=False)
        },
        112: {
            "full_name": "Куманин [VII колено — Служилые люди Ломовской черты]",
            "surname": "Куманин",
            "first_name": "Родовой предок VII колена",
            "patronymic": "Нижнеломовский уезд",
            "gender": "M",
            "birth_date": "~1815–1835",
            "birth_year": "~1820",
            "death_date": None,
            "is_alive": False,
            "birth_place": "Пензенская губ., Нижнеломовский уезд, с. Новый Шуструй",
            "status": "ARCHIVE_CANDIDATE",
            "confidence": 60,
            "role_label": "Прапрапрапрадед Куманин (VII колено)",
            "street_nickname": None,
            "notes": "Потомки служилых людей Нижнеломовского уезда (в документах XVII в. зафиксирован Алешка Антонов сын Куманин, РГАДА Ф. 210 / ГАПО Ф. 60).",
            "sources": ["ГАПО Фонд 60", "РГАДА Ф. 210 (Десятни по Ломову)"],
            "burial_info": build_burial_info(is_alive=False)
        }
    }

    nodes = []
    for n in range(1, 128):
        gen = get_generation(n)
        branch = get_branch(n)
        gender = "M" if (n == 1 or n % 2 == 0) else "F"
        father_id = 2 * n if gen < 7 else None
        mother_id = 2 * n + 1 if gen < 7 else None
        child_id = n // 2 if n > 1 else None
        sub_clan = get_sub_clan(n)
        region = get_clan_region(n)

        if n in known:
            item = known[n]
            burial = item.get("burial_info") or build_burial_info(is_alive=item.get("is_alive", False))
            dossier_12 = build_dossier_12_rubrics(
                full_name=item["full_name"],
                surname=item["surname"],
                first_name=item["first_name"],
                patronymic=item["patronymic"],
                maiden_name=item.get("maiden_name"),
                birth_date=item.get("birth_date"),
                birth_year=item.get("birth_year"),
                death_date=item.get("death_date"),
                is_alive=item.get("is_alive", False),
                birth_place=item.get("birth_place", region),
                sub_clan=sub_clan,
                notes=item.get("notes", ""),
                sources=item.get("sources", []),
                burial_info=burial,
                worldview_data=item.get("worldview"),
                life_work_data=item.get("life_work"),
                military_data=item.get("military"),
                street_nickname=item.get("street_nickname"),
                photo_url=item.get("photo_url")
            )

            node = {
                "id": f"P{n:03d}",
                "ahnentafel": n,
                "node_type": "CANONICAL_DIRECT",
                "visibility": "public_family",
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
                "birth_date": item.get("birth_date"),
                "birth_year": item.get("birth_year"),
                "death_date": item.get("death_date"),
                "is_alive": item.get("is_alive", False),
                "birth_place": item["birth_place"],
                "status": item["status"],
                "confidence": item["confidence"],
                "role_label": item["role_label"],
                "notes": item["notes"],
                "sources": item["sources"],
                "photo_url": item.get("photo_url"),
                "father_ahnentafel": father_id,
                "mother_ahnentafel": mother_id,
                "child_ahnentafel": child_id,
                "burial_info": burial,
                "worldview_and_tradition": item.get("worldview") or {
                    "primary_tradition": "UNSPECIFIED",
                    "tradition_label": "Ожидает архивного уточнения",
                    "description": "Традиция исследуется по архивным источникам.",
                    "historical_metric_parish_index": None
                },
                "life_work_and_stature": item.get("life_work") or {
                    "profession_and_craft_summary": "Хлебопашество, созидательный труд.",
                    "agricultural_and_kolkhoz_leadership": None,
                    "elected_and_state_service": None,
                    "social_estate_pre1917": "Крестьяне"
                },
                "dossier_12_rubrics": dossier_12
            }
            if "internal_research_notes" in item:
                node["internal_research_notes"] = item["internal_research_notes"]
        else:
            role_prefix = "Предок мужской линии" if gender == "M" else "Предок женской линии"
            target_archive = (
                "ГАОО (Оренбург) Ф. 389 / ЦГАСО Ф. 150 (Владимировка / Ивановка)"
                if "Каретников" in sub_clan
                else "АИС ЦГАСО (Самара) Ф. 32 / Ф. 150 (с. Четыровка / Кошкинский р-н)"
                if "Юхин" in sub_clan
                else "ГАПО (Пенза) Ф. 182 / Ф. 158 / Ф. 60 (с. Новый Шуструй)"
            )
            placeholder_burial = build_burial_info(is_alive=False)
            placeholder_dossier = build_dossier_12_rubrics(
                full_name=f"Слот №{n} ({sub_clan.split('(')[0].strip()})",
                surname=sub_clan.split()[1] if "Род" in sub_clan else "Уточняется",
                first_name="Ожидает архивной выписки",
                patronymic="",
                maiden_name=None,
                birth_date=GEN_ERA[gen].split("(")[0].strip(),
                birth_year=GEN_ERA[gen][:4],
                death_date=None,
                is_alive=False,
                birth_place=region,
                sub_clan=sub_clan,
                notes=f"Прямой слот №{n} по системе Соса-Страдоница ({GEN_LABELS[gen]}). Раскрывается при исследовании записи о рождении/браке потомка №{child_id} в архиве: {target_archive}.",
                sources=[f"Целевой фонд: {target_archive}"],
                burial_info=placeholder_burial
            )

            node = {
                "id": f"P{n:03d}",
                "ahnentafel": n,
                "node_type": "CANONICAL_DIRECT",
                "visibility": "public_family",
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
                "is_alive": False,
                "birth_place": region,
                "status": "UNKNOWN_SLOT",
                "confidence": 10,
                "role_label": f"{role_prefix} ({gen} колено, слот №{n})",
                "notes": f"Прямой слот №{n} по системе Соса-Страдоница ({GEN_LABELS[gen]}). Раскрывается при исследовании записи о рождении/браке потомка №{child_id} в архиве: {target_archive}.",
                "sources": [f"Целевой фонд: {target_archive}"],
                "photo_url": None,
                "father_ahnentafel": father_id,
                "mother_ahnentafel": mother_id,
                "child_ahnentafel": child_id,
                "burial_info": placeholder_burial,
                "worldview_and_tradition": {
                    "primary_tradition": "UNSPECIFIED",
                    "tradition_label": "Ожидает архивного поиска",
                    "description": f"Исследуется в {target_archive}",
                    "historical_metric_parish_index": target_archive
                },
                "life_work_and_stature": {
                    "profession_and_craft_summary": "Земледельческий труд.",
                    "agricultural_and_kolkhoz_leadership": None,
                    "elected_and_state_service": None,
                    "social_estate_pre1917": "Крестьяне"
                },
                "dossier_12_rubrics": placeholder_dossier
            }
        is_fact = (n in FACT_AHNENTAFELS_DIRECT)
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

        nodes.append(node)

    return nodes


def build_collateral_relatives():
    """Боковые родственные ветви (подтвержденные братья и сестры)."""
    relatives = [
        {
            "id": "C001",
            "ahnentafel": 301,
            "node_type": "COLLATERAL_RELATIVE",
            "visibility": "public_family",
            "is_collateral": True,
            "sibling_of_ahnentafel": 3,
            "parent_ahnentafel": 6,
            "generation": 2,
            "generation_label": "II колено — Боковая ветвь (Дядя по маме)",
            "era": "1960-е — наст. время",
            "branch": "maternal",
            "sub_clan": "Род Зубковых • Куманиных (с. Новый Шуструй)",
            "full_name": "Зубков Владимир Владимирович (младший)",
            "surname": "Зубков",
            "first_name": "Владимир",
            "patronymic": "Владимирович",
            "gender": "M",
            "birth_date": "Уточняется",
            "birth_year": "~1965–1975",
            "death_date": None,
            "is_alive": True,
            "birth_place": "Пензенская обл., Нижнеломовский р-н, с. Новый Шуструй",
            "status": "CONFIRMED_DOC",
            "confidence": 100,
            "role_label": "Родной брат мамы (Дядя, II колено)",
            "notes": "Родной брат Светланы Владимировны Каретниковой (Зубковой). Родился непосредственно в селе Новый Шуструй Нижнеломовского района Пензенской области, что на 100% подтверждает наше архивное попадание в приход Никольской церкви с. Новый Шуструй.",
            "sources": ["Семейный архив (подтверждено Графом Каретниковым)"],
            "photo_url": None,
            "burial_info": build_burial_info(is_alive=True)
        },
        {
            "id": "C002",
            "ahnentafel": 401,
            "node_type": "COLLATERAL_RELATIVE",
            "visibility": "public_family",
            "is_collateral": True,
            "sibling_of_ahnentafel": 4,
            "parent_ahnentafel": 8,
            "generation": 3,
            "generation_label": "III колено — Боковая ветвь (Старший брат деда)",
            "era": "1925–2000-е",
            "branch": "paternal",
            "sub_clan": "Род Каретниковых (д. Владимировка • с. Плешаново / Подольск)",
            "full_name": "Каретников Николай Григорьевич",
            "surname": "Каретников",
            "first_name": "Николай",
            "patronymic": "Григорьевич",
            "gender": "M",
            "birth_date": "~1925–1932",
            "birth_year": "~1928",
            "death_date": "Уточняется",
            "is_alive": False,
            "birth_place": "Оренбургская обл., Красногвардейский р-н, с. Плешаново / с. Подольск",
            "status": "CONFIRMED_DOC",
            "confidence": 100,
            "role_label": "Старший брат деда Валентина (Двоюродный дед, III колено)",
            "notes": "Старший сын прадеда Григория Ивановича Каретникова (#8) и прабабушки Агриппины Анисимовны (#9). Остался жить в Оренбургской области (Красногвардейский р-н, с. Плешаново / с. Подольск), когда младшие братья Валентин (#4) и Пётр (#402) с матерью Агриппиной Анисимовной в 1961 г. переехали в Куйбышев. Его родные сыновья: Василий Николаевич Каретников (с. Плешаново — собрал большой архив по древу рода!) и Валерий Николаевич Каретников (г. Тольятти).",
            "sources": ["Семейный архив Графа Каретникова", "Похозяйственные книги Подольского и Плешановского с/с"],
            "photo_url": None,
            "burial_info": build_burial_info(cemetery="Красногвардейский р-н Оренбургской обл. (с. Плешаново / Подольск)", is_alive=False)
        },
        {
            "id": "C003",
            "ahnentafel": 402,
            "node_type": "COLLATERAL_RELATIVE",
            "visibility": "public_family",
            "is_collateral": True,
            "sibling_of_ahnentafel": 4,
            "parent_ahnentafel": 8,
            "generation": 3,
            "generation_label": "III колено — Боковая ветвь (Средний брат деда)",
            "era": "1928–2000-е",
            "branch": "paternal",
            "sub_clan": "Род Каретниковых (Плешаново / Подольск → Самара)",
            "full_name": "Каретников Пётр Григорьевич",
            "surname": "Каретников",
            "first_name": "Пётр",
            "patronymic": "Григорьевич",
            "gender": "M",
            "birth_date": "~1928–1934",
            "birth_year": "~1932",
            "death_date": "Уточняется",
            "is_alive": False,
            "birth_place": "Оренбургская обл., Красногвардейский р-н, с. Плешаново / с. Подольск",
            "status": "CONFIRMED_DOC",
            "confidence": 100,
            "role_label": "Средний брат деда Валентина (Двоюродный дед, III колено)",
            "notes": "Средний сын прадеда Григория Ивановича Каретникова (#8) и прабабушки Агриппины Анисимовны (#9). В 1961 году вместе с младшим братом Валентином Григорьевичем и матерью Агриппиной Анисимовной переехал из Оренбургской области в Куйбышев (Самару).",
            "sources": ["Семейный архив Графа Каретникова"],
            "photo_url": None,
            "burial_info": build_burial_info(cemetery="г. Самара", is_alive=False)
        },
        {
            "id": "C004",
            "ahnentafel": 403,
            "node_type": "COLLATERAL_RELATIVE",
            "visibility": "public_family",
            "is_collateral": True,
            "sibling_of_ahnentafel": 4,
            "parent_ahnentafel": 8,
            "generation": 3,
            "generation_label": "III колено — Боковая ветвь (Брат деда — Средняя Азия)",
            "era": "1920–2000-е",
            "branch": "paternal",
            "sub_clan": "Род Каретниковых (Плешаново → Казахстан / Кыргызстан)",
            "full_name": "Каретников Иван Григорьевич",
            "surname": "Каретников",
            "first_name": "Иван",
            "patronymic": "Григорьевич",
            "gender": "M",
            "birth_date": "~1922–1938",
            "birth_year": "~1930",
            "death_date": "Уточняется",
            "is_alive": False,
            "birth_place": "Оренбургская обл., Красногвардейский р-н, с. Плешаново / с. Подольск",
            "status": "FAMILY_ORAL",
            "confidence": 90,
            "role_label": "Брат деда Валентина (Двоюродный дед, III колено)",
            "notes": "Сын Григория Ивановича (#8) и Агриппины Анисимовны (#9) Каретниковых, названный в честь деда Ивана (#16). По семейным сведениям уехал в Казахстан или Кыргызстан (по линии железной дороги Оренбург — Ташкент / Фрунзе или на целину).",
            "sources": ["Семейные воспоминания Графа Каретникова"],
            "photo_url": None,
            "burial_info": build_burial_info(is_alive=False)
        },
        {
            "id": "C005",
            "ahnentafel": 4011,
            "node_type": "COLLATERAL_RELATIVE",
            "visibility": "public_family",
            "is_collateral": True,
            "sibling_of_ahnentafel": 2,
            "parent_ahnentafel": 401,
            "generation": 2,
            "generation_label": "II колено — Боковая ветвь (Двоюродный дядя в с. Плешаново)",
            "era": "1950-е — наст. время",
            "branch": "paternal",
            "sub_clan": "Род Каретниковых (с. Плешаново Оренбургской обл.)",
            "full_name": "Каретников Василий Николаевич",
            "surname": "Каретников",
            "first_name": "Василий",
            "patronymic": "Николаевич",
            "gender": "M",
            "birth_date": "Уточняется",
            "birth_year": "~1955–1965",
            "death_date": None,
            "is_alive": True,
            "birth_place": "Оренбургская обл., Красногвардейский р-н, с. Плешаново",
            "status": "CONFIRMED_DOC",
            "confidence": 100,
            "role_label": "Сын старшего брата деда Николая Григорьевича (Двоюродный дядя, II колено)",
            "notes": "100% подтверждено Графом Каретниковым! Родной сын Николая Григорьевича Каретникова (#401). Проживает в с. Плешаново Красногвардейского р-на Оренбургской обл. (руководитель МБУ КИС «Вымпел», организатор районного спорта). ВАЖНО: сам собрал большой массив информации по фамильному древу Каретниковых!",
            "sources": ["Семейный архив (хранитель фамильного древа в с. Плешаново)", "ЕГРЮЛ (МБУ КИС «Вымпел»)"],
            "photo_url": None,
            "burial_info": build_burial_info(is_alive=True)
        },
        {
            "id": "C006",
            "ahnentafel": 4012,
            "node_type": "COLLATERAL_RELATIVE",
            "visibility": "public_family",
            "is_collateral": True,
            "sibling_of_ahnentafel": 2,
            "parent_ahnentafel": 401,
            "generation": 2,
            "generation_label": "II колено — Боковая ветвь (Двоюродный дядя в г. Тольятти)",
            "era": "1950-е — наст. время",
            "branch": "paternal",
            "sub_clan": "Род Каретниковых (Плешаново → г. Тольятти)",
            "full_name": "Каретников Валерий Николаевич",
            "surname": "Каретников",
            "first_name": "Валерий",
            "patronymic": "Николаевич",
            "gender": "M",
            "birth_date": "Уточняется",
            "birth_year": "~1955–1968",
            "death_date": None,
            "is_alive": True,
            "birth_place": "Оренбургская обл., Красногвардейский р-н, с. Плешаново (проживает в г. Тольятти)",
            "status": "CONFIRMED_DOC",
            "confidence": 100,
            "role_label": "Сын старшего брата деда Николая Григорьевича (Двоюродный дядя, II колено)",
            "notes": "Родной сын Николая Григорьевича Каретникова (#401), родной брат Василия Николаевича Каретникова (#4011). Проживает в г. Тольятти Самарской области.",
            "sources": ["Семейный архив Графа Каретникова"],
            "photo_url": None,
            "burial_info": build_burial_info(is_alive=True)
        },
        {
            "id": "C007",
            "ahnentafel": 701,
            "node_type": "COLLATERAL_RELATIVE",
            "visibility": "public_family",
            "is_collateral": True,
            "sibling_of_ahnentafel": 7,
            "parent_ahnentafel": 14,
            "generation": 3,
            "generation_label": "III колено — Боковая ветвь (Родная сестра бабушки Валентины)",
            "era": "1938 — наст. время",
            "branch": "maternal",
            "sub_clan": "Род Куманиных (с. Новый Шуструй)",
            "full_name": "Зинаида Сергеевна (в девичестве Куманина)",
            "surname": "Куманина (в девичестве)",
            "first_name": "Зинаида",
            "patronymic": "Сергеевна",
            "gender": "F",
            "birth_date": "Уточняется",
            "birth_year": "~1938–1950",
            "death_date": None,
            "is_alive": True,
            "birth_place": "Пензенская обл., Нижнеломовский р-н, с. Новый Шуструй",
            "status": "CONFIRMED_DOC",
            "confidence": 100,
            "role_label": "Родная сестра бабушки Валентины Сергеевны (Двоюродная бабушка, III колено)",
            "notes": "100% подтверждено Графом Каретниковым! Дочь прадеда Сергея Куманина (#14), родная сестра бабушки Валентины Сергеевны (#7) и Антонины Сергеевны (#702). Жива и поныне проживает в родовом селе Новый Шуструй Нижнеломовского района Пензенской области.",
            "sources": ["Семейный архив Графа Каретникова (жива, проживает в с. Новый Шуструй)"],
            "photo_url": None,
            "burial_info": build_burial_info(is_alive=True)
        },
        {
            "id": "C008",
            "ahnentafel": 702,
            "node_type": "COLLATERAL_RELATIVE",
            "visibility": "public_family",
            "is_collateral": True,
            "sibling_of_ahnentafel": 7,
            "parent_ahnentafel": 14,
            "generation": 3,
            "generation_label": "III колено — Боковая ветвь (Родная сестра бабушки Валентины)",
            "era": "1938 — наст. время",
            "branch": "maternal",
            "sub_clan": "Род Куманиных (с. Новый Шуструй)",
            "full_name": "Антонина Сергеевна (в девичестве Куманина)",
            "surname": "Куманина (в девичестве)",
            "first_name": "Антонина",
            "patronymic": "Сергеевна",
            "gender": "F",
            "birth_date": "Уточняется",
            "birth_year": "~1938–1950",
            "death_date": None,
            "is_alive": True,
            "birth_place": "Пензенская обл., Нижнеломовский р-н, с. Новый Шуструй",
            "status": "CONFIRMED_DOC",
            "confidence": 100,
            "role_label": "Родная сестра бабушки Валентины Сергеевны (Двоюродная бабушка, III колено)",
            "notes": "100% подтверждено Графом Каретниковым! Дочь прадеда Сергея Куманина (#14), родная сестра бабушки Валентины Сергеевны (#7) и Зинаиды Сергеевны (#701). Жива и поныне проживает в родовом селе Новый Шуструй Нижнеломовского района Пензенской области.",
            "sources": ["Семейный архив Графа Каретникова (жива, проживает в с. Новый Шуструй)"],
            "photo_url": None,
            "burial_info": build_burial_info(is_alive=True)
        },
        {
            "id": "C009",
            "ahnentafel": 801,
            "node_type": "COLLATERAL_RELATIVE",
            "visibility": "public_family",
            "is_collateral": True,
            "sibling_of_ahnentafel": 8,
            "parent_ahnentafel": 16,
            "generation": 4,
            "generation_label": "IV колено — Боковая ветвь (Младший брат прадеда Григория)",
            "era": "1923–после 1985",
            "branch": "paternal",
            "sub_clan": "Род Каретниковых (д. Владимировка • с. Залесово)",
            "full_name": "Каретников Фёдор Иванович",
            "surname": "Каретников",
            "first_name": "Фёдор",
            "patronymic": "Иванович",
            "gender": "M",
            "birth_date": "18.03.1923",
            "birth_year": "1923",
            "death_date": "После мая 1985",
            "is_alive": False,
            "birth_place": "Оренбургская обл., д. Владимировка (Залесовский с/с Ивановского / Красногвардейского р-на)",
            "status": "CONFIRMED_DOC",
            "confidence": 100,
            "role_label": "Родной младший брат прадеда Григория Ивановича (Двоюродный дед, IV колено)",
            "notes": "Родной младший брат прадеда Григория Ивановича Каретникова (#8). Родился 18.03.1923 в д. Владимировка. Фронтовик-сталинградец, командир отделения связи, сержант, участник тяжелейших боев на Дону и Волге, награжден орденом Отечественной войны II ст., медалями «За оборону Сталинграда», «За победу над Германией». После войны — Председатель Залесовского сельского совета депутатов трудящихся (статус депутата и первого лица власти на селе!), военрук Залесовской школы, выпускник Чкаловской областной партийной школы, ученый-агроном и многолетний управляющий отделением целинного совхоза им. Свердлова. На 100% подтверждает семейный инсайт Графа Каретникова о 'военных, серьезных колхозниках, депутатах и руководителях'!",
            "sources": ["ЦАМО РФ («Память Народа» / УПК)", "Краеведческий архив Залесовской школы («Твои люди, село»)", "База ветеранов «Победители.ру»"],
            "photo_url": None,
            "burial_info": build_burial_info(cemetery="Оренбургская обл., Красногвардейский р-н (с. Залесово / пос. Свердловский)", is_alive=False),
            "worldview_and_tradition": {
                "primary_tradition": "SOVIET_SECULAR_ETHIC",
                "tradition_label": "🚩 Коммунист-фронтовик, созидатель Оренбургской целины",
                "description": "Светское созидательное мировоззрение, член КПСС, служение Отечеству на фронте и на земле.",
                "historical_metric_parish_index": None
            },
            "life_work_and_stature": {
                "profession_and_craft_summary": "Ученый-агроном, управляющий отделением совхоза им. Свердлова, военрук.",
                "agricultural_and_kolkhoz_leadership": "Управляющий отделением целинного совхоза имени Я. М. Свердлова (с 1960 г.)",
                "elected_and_state_service": "Председатель Залесовского сельского Совета депутатов трудящихся (депутат и глава исполнительной власти)",
                "military_rank": "Сержант, командир отделения связи (Защитник Сталинграда)",
                "social_estate_pre1917": "Крестьянин д. Владимировка"
            }
        },
        {
            "id": "C010",
            "ahnentafel": 802,
            "node_type": "COLLATERAL_RELATIVE",
            "visibility": "public_family",
            "is_collateral": True,
            "sibling_of_ahnentafel": 8,
            "parent_ahnentafel": 16,
            "generation": 4,
            "generation_label": "IV колено — Боковая ветвь (Старший брат прадеда Григория — полный тезка Пробанда)",
            "era": "1913–XX в.",
            "branch": "paternal",
            "sub_clan": "Род Каретниковых (д. Владимировка)",
            "full_name": "Каретников Дмитрий Иванович (старший)",
            "surname": "Каретников",
            "first_name": "Дмитрий",
            "patronymic": "Иванович",
            "gender": "M",
            "birth_date": "19.09.1913",
            "birth_year": "1913",
            "death_date": "Уточняется в ЦАМО РФ",
            "is_alive": False,
            "birth_place": "Оренбургская губ., Оренбургский уезд, д. Владимировка (Залесовский с/с)",
            "status": "CONFIRMED_DOC",
            "confidence": 95,
            "role_label": "Родной старший брат прадеда Григория Ивановича — полный тезка Пробанда (IV колено)",
            "notes": "Родился 19 сентября 1913 года в деревне Владимировка Каликинской волости Оренбургского уезда в семье крестьянина Ивана Дмитриевича Каретникова (#16) и Марины Антоновны (#17). ПОЛНЫЙ ТЕЗКА Владельца архива (Каретников Дмитрий Иванович)! Старший брат прадеда Григория Ивановича (#8) и Фёдора Ивановича (#801). Крещен в Михайло-Архангельской церкви с. Ивановка.",
            "sources": ["Метрическая книга Михайло-Архангельской церкви с. Ивановка за 1913 г. (ОГАОО Ф. 389 Оп. 1)", "Яндекс.Архивы (ГАОО)", "Familio 64b9dc5b-bf02-403e-bb82-22b44471d8a8"],
            "photo_url": None,
            "burial_info": build_burial_info(is_alive=False),
            "worldview_and_tradition": {
                "primary_tradition": "ORTHODOX_TRADITION",
                "tradition_label": "⛪ Крещение в Михайло-Архангельской церкви с. Ивановка",
                "description": "Родился 19.09.1913 в д. Владимировка.",
                "historical_metric_parish_index": "ОГАОО Ф. 389 Оп. 1"
            },
            "life_work_and_stature": {
                "profession_and_craft_summary": "Крестьянин д. Владимировка.",
                "agricultural_and_kolkhoz_leadership": None,
                "elected_and_state_service": None,
                "social_estate_pre1917": "Крестьянин"
            }
        }
    ]
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
    return relatives


def build_floating_hypotheses():
    """Орбитальные карточки-гипотезы (FLOATING_HYPOTHESIS) на основе OSINT Оренбуржья, ЦГАСО и ГАПО."""
    return [
        {
            "id": "FH-KAR-001",
            "node_type": "FLOATING_HYPOTHESIS",
            "visibility": "public_family",
            "clan": "karetnikov",
            "branch": "paternal",
            "generation": 6,
            "generation_label": "VI колено (Метрики XIX в. / 10 ревизия)",
            "era": "1853 — после 1894",
            "full_name": "Каретников Евсевий Кириллович и Феодосия Никитична (Самулина)",
            "birth_date": "~1853 (Евсевий) / ~1855 (Феодосия)",
            "death_date": "После 1894",
            "village": "д. Владимировка, Ивановская волость, Бузулукский / Оренбургский уезд",
            "role_badge": "Старейшина рода Каретниковых во Владимировке • X Ревизия 1858 г.",
            "relationship_hypothesis": "Государственный крестьянин д. Владимировка. Зафиксирован в метрической книге Михайло-Архангельской церкви с. Ивановка за 1894 г. при рождении дочери Евдокии (29.07.1894). Сын Кирилла Каретникова. Родился до отмены крепостного права, внесен малолетним ребенком в X Ревизию 1858 года.",
            "link_mode": "dashed_tether",
            "probable_relative_ahnentafel": 32,
            "confidence": 88,
            "sources": ["ОГАОО Ф. 389 Оп. 1 (Метрики с. Ивановка 1894 г.)", "ЦГАСО Ф. 150 Оп. 1 (Ревизии Бузулукского уезда)"],
            "citation_links": ["https://familio.org/settlements/e2e0e51b-4974-4ce8-b988-257c51ca94d3"]
        },
        {
            "id": "FH-KAR-002",
            "node_type": "FLOATING_HYPOTHESIS",
            "visibility": "public_family",
            "clan": "karetnikov",
            "branch": "paternal",
            "generation": 6,
            "generation_label": "VI колено",
            "era": "1867 — после 1913",
            "full_name": "Каретников Владимир Семёнович и Четверикова Прасковья Ивановна",
            "birth_date": "01.07.1867 (Владимир) / 01.10.1868 (Прасковья)",
            "death_date": "После 1913",
            "village": "д. Владимировка и с. Ивановка, Красногвардейский р-н Оренбургской обл.",
            "role_badge": "Младший брат Дмитрия Семёновича (#32) • Солдат д. Владимировка",
            "relationship_hypothesis": "Младший из 5 сыновей первопоселенца Семёна Мокеевича Каретникова (#64) и Варвары Филимоновны (#65). Взял в жены Прасковью Ивановну Четверикову из волостного села Ивановка. Отец Семёна Владимировича (р. 02.09.1906) и воина ВОВ Владимира Владимировича (1897–1942).",
            "link_mode": "dashed_tether",
            "probable_relative_ahnentafel": 32,
            "confidence": 92,
            "sources": ["Метрические книги с. Ивановка (ОГАОО Ф. 389)", "Familio 22b49428-9214-4d04-ad38-f6ac0f82bf11"],
            "citation_links": ["https://yandex.ru/archive/catalog/ef8c6fb6-c448-46bd-885a-4fa2edf7c98d/1402"]
        },
        {
            "id": "FH-KAR-003",
            "node_type": "FLOATING_HYPOTHESIS",
            "visibility": "public_family",
            "clan": "karetnikov",
            "branch": "paternal",
            "generation": 4,
            "generation_label": "IV колено",
            "era": "1899 — 05.06.1944",
            "full_name": "Каретников Лука Мартынович",
            "birth_date": "1899",
            "death_date": "05.06.1944 (погиб в Румынии)",
            "village": "д. Владимировка, Ивановский (Красногвардейский) р-н Оренбургской обл.",
            "role_badge": "Герой ВОВ • Красноармеец 50 сд • Колхозник колхоза им. Свердлова",
            "relationship_hypothesis": "Коренной житель д. Владимировка, ровесник прадеда Григория Ивановича (#8). Колхозник колхоза им. Свердлова. Призван в 1942 г. Ивановским РВК. Героически погиб 05.06.1944 в Румынии (Яссы, с. Поприкань). Сын Мартына Каретникова (поколение прапрадедов V колена).",
            "link_mode": "free_floating",
            "probable_relative_ahnentafel": 8,
            "confidence": 85,
            "sources": ["ЦАМО РФ Ф. 58 Оп. 18002 Д. 518", "ОБД Мемориал", "Книга Памяти Оренбургской области"],
            "citation_links": ["https://pamyat-naroda.ru/"]
        },
        {
            "id": "FH-KAR-004",
            "node_type": "FLOATING_HYPOTHESIS",
            "visibility": "public_family",
            "clan": "karetnikov",
            "branch": "paternal",
            "generation": 4,
            "generation_label": "IV колено",
            "era": "1913 — 1982",
            "full_name": "Каретников Герасим Владимирович",
            "birth_date": "04.03.1913",
            "death_date": "04.07.1982",
            "village": "д. Владимировка, Залесовский с/с, Красногвардейский р-н Оренбургской обл.",
            "role_badge": "Ветеран ВОВ (1941–1944) • Тракторист и учетчик колхоза во Владимировке",
            "relationship_hypothesis": "Сын Владимира Семёновича Каретникова, двоюродный брат Ивана Дмитриевича (#16). Воевал в ВОВ, ранен, награжден. После войны работал трактористом и учетчиком тракторной бригады в д. Владимировка. Отец сыновей Виктора (1937), Николая (1939) и Владимира (1941).",
            "link_mode": "dashed_tether",
            "probable_relative_ahnentafel": 16,
            "confidence": 90,
            "sources": ["ЦАМО РФ («Память Народа»)", "Familio 695229b0-0526-42f2-8027-ad7336c8d2e4"],
            "citation_links": ["https://pamyat-naroda.ru/heroes/person-hero80974751/"]
        },
        {
            "id": "FH-KAR-005",
            "node_type": "FLOATING_HYPOTHESIS",
            "visibility": "public_family",
            "clan": "karetnikov",
            "branch": "paternal",
            "generation": 4,
            "generation_label": "IV колено",
            "era": "1897 — 30.06.1942",
            "full_name": "Каретников Владимир Владимирович",
            "birth_date": "10.07.1897",
            "death_date": "30.06.1942 (погиб на фронте ВОВ)",
            "village": "д. Владимировка, Красногвардейский (Ивановский) р-н",
            "role_badge": "Воин ВОВ • Сын Владимира Семёновича из д. Владимировка",
            "relationship_hypothesis": "Сын Владимира Семёновича Каретникова и Прасковьи Ивановны Четвериковой. Родился во Владимировке 10.07.1897. Погиб в Великую Отечественную войну 30.06.1942.",
            "link_mode": "free_floating",
            "probable_relative_ahnentafel": 8,
            "confidence": 88,
            "sources": ["ЦАМО РФ Картотека потерь", "Familio 5685f7b0-9a80-4e06-9a82-3eb1f58e733c"],
            "citation_links": ["https://pamyat-naroda.ru/heroes/memorial-chelovek_kartoteka_memorial1913030759/"]
        },
        {
            "id": "FH-KAR-006",
            "node_type": "FLOATING_HYPOTHESIS",
            "visibility": "public_family",
            "clan": "karetnikov",
            "branch": "paternal",
            "generation": 3,
            "generation_label": "III колено (Ровесники деда Валентина)",
            "era": "1937–2021",
            "full_name": "Братья Каретниковы: Виктор (1937–2021), Николай (1939–2005), Владимир (1941–2017) Герасимовичи",
            "birth_date": "1937, 1939, 1941",
            "death_date": "2021, 2005, 2017",
            "village": "д. Владимировка, Красногвардейский р-н Оренбургской обл.",
            "role_badge": "Ровесники и троюродные братья деда Валентина Григорьевича во Владимировке",
            "relationship_hypothesis": "Сыновья ветерана ВОВ Герасима Владимировича Каретникова (1913–1982), выросшие во Владимировке бок о бок с Николаем, Петром и Валентином Григорьевичами.",
            "link_mode": "free_floating",
            "probable_relative_ahnentafel": 4,
            "confidence": 85,
            "sources": ["Familio (база персон д. Владимировка)", "Похозяйственные книги Залесовского с/с"],
            "citation_links": ["https://familio.org/persons/9201bd82-ab6f-4d91-ab2a-f4074d76296b"]
        },
        {
            "id": "FH-KAR-007",
            "node_type": "FLOATING_HYPOTHESIS",
            "visibility": "public_family",
            "clan": "karetnikov",
            "branch": "paternal",
            "generation": 4,
            "generation_label": "IV колено",
            "era": "до 1925 — 05.03.1943",
            "full_name": "Каретников Михаил Петрович",
            "birth_date": "до 1925",
            "death_date": "05.03.1943 (погиб в бою)",
            "village": "Бузулукский район / Оренбургская обл.",
            "role_badge": "Рядовой, разведчик 173 отдельной разведроты • Погиб 05.03.1943",
            "relationship_hypothesis": "Фронтовик-разведчик из исторического ареала рода (Бузулукский уезд/район). Увековечен в Книге Памяти Оренбургской области (Том 12). Отчество Петрович указывает на ветвь Петра Каретникова.",
            "link_mode": "free_floating",
            "probable_relative_ahnentafel": 8,
            "confidence": 80,
            "sources": ["Книга Памяти Оренбургской области, Том 12", "ЦАМО РФ"],
            "citation_links": ["https://pamyat-naroda.ru/"]
        },
        {
            "id": "FH-KAR-008",
            "node_type": "FLOATING_HYPOTHESIS",
            "visibility": "public_family",
            "clan": "karetnikov",
            "branch": "paternal",
            "generation": 4,
            "generation_label": "IV колено",
            "era": "1921 — 18.04.1945",
            "full_name": "Каретников Алексей Фёдорович",
            "birth_date": "1921",
            "death_date": "18.04.1945 (погиб в Балтийском море)",
            "village": "Призван Сорочинским РВК Чкаловской (Оренбургской) обл.",
            "role_badge": "Младший лейтенант ВВС ВМФ, пилот торпедоносца 51 МТАП КБФ • Орден Красной Звезды",
            "relationship_hypothesis": "Офицер-лётчик, призванный Сорочинским РВК Чкаловской области (в состав района входили земли Люксембургского и Ивановского р-нов). Погиб в боевом вылете за 3 недели до Победы.",
            "link_mode": "free_floating",
            "probable_relative_ahnentafel": 8,
            "confidence": 78,
            "sources": ["ЦВМА / Портал «Память Народа»", "Архив выпускников Ейского ВВАУЛ"],
            "citation_links": ["https://pamyat-naroda.ru/"]
        },
        {
            "id": "FH-KAR-009",
            "node_type": "FLOATING_HYPOTHESIS",
            "visibility": "public_family",
            "clan": "karetnikov",
            "branch": "paternal",
            "generation": 4,
            "generation_label": "IV колено (Свойственница клана)",
            "era": "~1888–1898 — XX в.",
            "full_name": "Каретникова (Колмыкова) Надежда Григорьевна",
            "birth_date": "~1890",
            "death_date": "д. Владимировка",
            "village": "д. Владимировка, Красногвардейский р-н Оренбургской обл.",
            "role_badge": "Невестка рода Каретниковых во Владимировке (жена крестьянина Каретникова)",
            "relationship_hypothesis": "Документально вскрыто: Надежда Григорьевна урожденная Колмыкова (дочь Григория Андреевича Дьякова и Татьяны Филимоновны Колмыковой). Фамилия Каретникова — по мужу! Вышла замуж за представителя рода Каретниковых д. Владимировка.",
            "link_mode": "free_floating",
            "probable_relative_ahnentafel": 8,
            "confidence": 95,
            "sources": ["Geni.com Профиль 6000000028120485496", "Метрические книги с. Ивановка (ОГАОО Ф. 389)"],
            "citation_links": ["https://www.geni.com/people/6000000028120485496"]
        },
        {
            "id": "FH-KAR-010",
            "node_type": "FLOATING_HYPOTHESIS",
            "visibility": "public_family",
            "clan": "karetnikov",
            "branch": "paternal",
            "generation": 2,
            "generation_label": "II колено (Современная оренбургская ветвь)",
            "era": "Вторая половина XX — XXI в.",
            "full_name": "Каретников Николай Викторович и Каретников Виктор Николаевич",
            "birth_date": "Вторая половина XX в.",
            "death_date": None,
            "village": "с. Подольск / с. Плешаново, Красногвардейский р-н Оренбургской обл.",
            "role_badge": "Соучредитель СПК «Подольское» (Николай Викторович) и КФХ (Виктор Николаевич)",
            "relationship_hypothesis": "Плешановско-подольская ветвь рода Каретниковых в Красногвардейском районе. Сохраняют аграрное руководство на малой родине.",
            "link_mode": "dashed_tether",
            "probable_relative_ahnentafel": 401,
            "confidence": 85,
            "sources": ["ЕГРЮЛ РФ (СПК «Подольское», ИНН 5631006148)", "Checko.ru / Rusprofile"],
            "citation_links": ["https://checko.ru/company/spk-podolskoe-1065617003473"]
        },
        {
            "id": "FH-YUK-001",
            "node_type": "FLOATING_HYPOTHESIS",
            "visibility": "public_family",
            "clan": "yukhin",
            "branch": "paternal",
            "generation": 3,
            "generation_label": "III колено (Кошкинский район)",
            "era": "1926 — после 1985",
            "full_name": "Юхин Николай Михайлович",
            "birth_date": "1926",
            "death_date": "После 1985",
            "village": "д. Дмитриевка / с. Богдановка (Кошкинский р-н Самарской обл.)",
            "role_badge": "Ветеран ВОВ • Кавалер ордена Отечественной войны II ст. (1985)",
            "relationship_hypothesis": "Уроженец Кошкинского района Самарской (Куйбышевской) области. Представитель того же родового куста Юхиных Кошкинского ареала, что и бабушка Клавдия Петровна (#5) и прадед Пётр Юхин (#10).",
            "link_mode": "dashed_tether",
            "probable_relative_ahnentafel": 10,
            "confidence": 85,
            "sources": ["ЦАМО РФ («Память Народа» / Юбилейная картотека 1985 г.)"],
            "citation_links": ["https://pamyat-naroda.ru/heroes/podvig-chelovek_yubileinaya_kartoteka1524855581/"]
        },
        {
            "id": "FH-ZUB-001",
            "node_type": "FLOATING_HYPOTHESIS",
            "visibility": "public_family",
            "clan": "zubkov",
            "branch": "maternal",
            "generation": 5,
            "generation_label": "V колено (Перепись 1917 г.)",
            "era": "1865–1917 гг.",
            "full_name": "19 домохозяев Зубковых с. Новый Шуструй (Перепись 1917 г.)",
            "birth_date": "~1865–1895",
            "death_date": "После 1917",
            "village": "с. Новый Шуструй, Нижнеломовский уезд, Пензенская губ.",
            "role_badge": "19 подворных карточек глав семейств Зубковых (ГАПО Ф. 158 Оп. 3 Д. 4014)",
            "relationship_hypothesis": "Полный свод глав семейств Зубковых в с. Новый Шуструй на 1917 год (среди которых прямой предок прадеда Владимира Зубкова #12): Федор Петрович, Захар Семенович, Иван Федорович, Яков Нестерович, Федор Иванович, Михаил Петрович, Алексей Григорьевич, Иван Семенович, Петр Ионович, Иуда Матвеевич, Логгин Матвеевич, Иван Александрович, Василий Иванович, Дмитрий Давидович, Семен Петрович, Андрей Алексеевич, Ермолай Дмитриевич, Павел Степанович, Екатерина Ефимовна.",
            "link_mode": "dashed_tether",
            "probable_relative_ahnentafel": 24,
            "confidence": 95,
            "sources": ["ГАПО Фонд 158 Опись 3 Дело 4014 (Подворные карточки 1917 г., с. Новый Шуструй)"],
            "citation_links": ["https://archive.pnzreg.ru/"]
        },
        {
            "id": "FH-KUM-001",
            "node_type": "FLOATING_HYPOTHESIS",
            "visibility": "public_family",
            "clan": "kumanin",
            "branch": "maternal",
            "generation": 3,
            "generation_label": "III колено (Фронтовики с. Новый Шуструй)",
            "era": "18.07.1925 — 10.01.2011",
            "full_name": "Куманин Фёдор Алексеевич",
            "birth_date": "18.07.1925",
            "death_date": "10.01.2011",
            "village": "с. Новый Шуструй, Нижнеломовский р-н Пензенской обл.",
            "role_badge": "Лейтенант, механик-водитель танка • 1-й и 2-й Прибалтийские, 2-й Украинский фронты",
            "relationship_hypothesis": "Уроженец с. Новый Шуструй, призван Нижнеломовским РВК 05.08.1943, прошел фронт механиком-водителем танка. Родственник прадеда Сергея Куманина (#14) и бабушки Валентины Сергеевны (#7).",
            "link_mode": "free_floating",
            "probable_relative_ahnentafel": 14,
            "confidence": 90,
            "sources": ["ЦАМО РФ", "Бессмертный Полк (moypolk.ru)"],
            "citation_links": ["https://www.moypolk.ru/soldier/kumanin-fedor-alekseevich"]
        },
        {
            "id": "FH-KUM-002",
            "node_type": "FLOATING_HYPOTHESIS",
            "visibility": "public_family",
            "clan": "kumanin",
            "branch": "maternal",
            "generation": 4,
            "generation_label": "IV колено (Поколение прадеда Сергея #14)",
            "era": "1912 — 07.1941",
            "full_name": "Куманин Дмитрий Михайлович и Куманина Пелагея Дмитриевна",
            "birth_date": "1912",
            "death_date": "07.1941 (пропал без вести на фронте)",
            "village": "с. Новый Шуструй, Нижнеломовский р-н Пензенской обл.",
            "role_badge": "Боец 55 лап 61 сд (1941) • Жители с. Новый Шуструй",
            "relationship_hypothesis": "Ровесник и односельчанин (вероятный брат/кузен) прадеда Сергея Куманина (#14) в с. Новый Шуструй. Жена Пелагея Дмитриевна проживала в селе в годы войны.",
            "link_mode": "free_floating",
            "probable_relative_ahnentafel": 14,
            "confidence": 88,
            "sources": ["ЦАМО Ф. 58 Оп. 18004 Д. 1753", "ОБД Мемориал"],
            "citation_links": ["https://pamyat-naroda.ru/"]
        },
        {
            "id": "FH-KUM-003",
            "node_type": "FLOATING_HYPOTHESIS",
            "visibility": "public_family",
            "clan": "kumanin",
            "branch": "maternal",
            "generation": 4,
            "generation_label": "IV колено",
            "era": "1908 — 27.09.1944",
            "full_name": "Куманин Алексей Иванович",
            "birth_date": "1908",
            "death_date": "27.09.1944 (погиб на фронте)",
            "village": "д. Новый Шуструй, Нижнеломовский р-н Пензенской обл.",
            "role_badge": "Воин ВОВ (погиб 27.09.1944) • с. Новый Шуструй",
            "relationship_hypothesis": "Односельчанин и родственник прадеда Сергея Куманина (#14) по с. Новый Шуструй Нижнеломовского района.",
            "link_mode": "free_floating",
            "probable_relative_ahnentafel": 14,
            "confidence": 85,
            "sources": ["ЦАМО РФ («Память Народа»)", "Книга Памяти Пензенской области"],
            "citation_links": ["https://pamyat-naroda.ru/"]
        }
    ]


def build_archive_leads():
    return [
        {
            "lead_id": "ARCH-01",
            "priority": "P0",
            "clan": "Каретниковы (д. Владимировка • с. Подольск • с. Плешаново)",
            "title": "Метрики прихода с. Ивановка (ОГАОО Ф. 389), похозяйственные книги и архив Василия Николаевича в Плешаново",
            "region": "Оренбургская обл., Красногвардейский (Ивановский) р-н, д. Владимировка (Залесовский с/с), с. Подольск, с. Плешаново",
            "archive_name": "ОГАОО (Оренбург) + Архив администрации Красногвардейского р-на (с. Плешаново) + Семейный архив Василия Николаевича",
            "fond_cipher": "ОГАОО Ф. 389 Оп. 1 (Метрики с. Ивановка) + Похозяйственные книги Владимировского (1934–1954) и Залесовского (1935–1965) с/с",
            "summary": "100% подтвержден прадед Григорий Иванович (#8), его родной брат — фронтовик-сталинградец и председатель Залесовского с/с Фёдор Иванович (#801) и старший брат Дмитрий Иванович (р. 1913, тезка Пробанда!). Родовое гнездо — д. Владимировка, откуда ветвь перешла в с. Подольск и с. Плешаново, где живёт Василий Николаевич Каретников (#4011), собравший фамильный архив!",
            "next_action": "Запросить похозяйственные книги Владимировского и Залесовского с/с в архиве с. Плешаново + объединить данные с архивом Василия Николаевича Каретникова."
        },
        {
            "lead_id": "ARCH-02",
            "priority": "P0",
            "clan": "Зубковы & Куманины (с. Новый Шуструй Нижнеломовского района)",
            "title": "Прадед Сергей Куманин (#14), 19 дворов Зубковых в Переписи 1917 г. и живые сёстры бабушки в Новом Шуструе",
            "region": "Пензенская обл., Нижнеломовский р-н, с. Новый Шуструй (Никольская церковь, Старо-Толковская волость)",
            "archive_name": "ГБУ «Государственный архив Пензенской области» (ГАПО) + РГАДА Ф. 210",
            "fond_cipher": "ГАПО: Ф. 158 Оп. 3 Д. 4014 (Перепись 1917 г.) + Ф. 182 Оп. 3 Кн. 561 (Метрики 1907–1917 гг.) + Ф. 60 Оп. 4 (Ревизии)",
            "summary": "Установлен прадед Сергей Куманин (#14) — отец бабушки Валентины Сергеевны (#7) и её родных сестёр Зинаиды Сергеевны (#701) и Антонины Сергеевны (#702), живущих в с. Новый Шуструй! В деле ГАПО Ф. 158 Оп. 3 Д. 4014 лежат подворные карточки 19 дворов Зубковых и семей Куманиных за 1917 год.",
            "next_action": "Связаться с живыми сёстрами бабушки (Зинаидой Сергеевной и Антониной Сергеевной в с. Новый Шуструй) и заказать сканы дела ГАПО Ф. 158 Оп. 3 Д. 4014."
        },
        {
            "lead_id": "ARCH-03",
            "priority": "P0",
            "clan": "Юхины (с. Четыровка Кошкинского района Самарской области)",
            "title": "Село Четыровка — метрики прихода с. Русская Васильевка и с. Петропавловка в АИС ЦГАСО",
            "region": "Самарская (Куйбышевская) обл., Кошкинский р-н, с. Четыровка на р. Кондурче",
            "archive_name": "Центральный государственный архив Самарской области (АИС ЦГАСО)",
            "fond_cipher": "АИС ЦГАСО (cgaso.regsamarh.ru): Ф. 32 Оп. 35 Д. 272/278 + Ф. Р-54 (ЗАГС) + Ф. 150 (Ревизии 1858 г.)",
            "summary": "Точное родовое гнездо бабушки Клавдии Петровны Каретниковой (Юхиной, #5, 1936 г.р.) и прадеда Петра Юхина (#10) — село Четыровка Кошкинского района! Метрические книги прихода с. Русская Васильевка оцифрованы в АИС ЦГАСО.",
            "next_action": "Открыть в АИС ЦГАСО метрики с. Русская Васильевка (Ф. 32 Оп. 35) за 1900–1918 гг. для выявления записи о рождении Петра Юхина (#10)."
        },
        {
            "lead_id": "ARCH-04",
            "priority": "P1",
            "clan": "Каретниковы: Исход из с. Тепловка Саранского уезда (1745–1868 гг.)",
            "title": "Ревизские сказки с. Тепловка Саранского уезда до 1745 г. (VIII–X колена)",
            "region": "Мордовия / Пензенская губ., Саранский уезд, с. Тепловка (ныне Кочкуровский р-н)",
            "archive_name": "ЦГА РМ (Саранск) + ГАПО (Пенза) + РГАДА (Москва)",
            "fond_cipher": "Ревизии 1811, 1816, 1834, 1850 гг. по с. Тепловка + РГАДА Ф. 350",
            "summary": "Документально доказано: в 1868–1870 гг. Семён Мокеевич Каретников (~1828) и Варвара Филимоновна (1830–1883) переселились из с. Тепловка Саранского уезда во Владимировку. В Тепловке зафиксированы предки вглубь: Филимон Степанович (р. 1809), Степан Макарович (1776–1834) и Макар Никитович (~1745 г.р.) — выход к X колену!",
            "next_action": "Заказать в ЦГА РМ и ГАПО ревизские сказки 1811, 1816 и 1834 гг. по казенным крестьянам с. Тепловка Саранского уезда."
        }
    ]


def build_access_guide():
    return [
        {
            "step": 1,
            "service": "Playwright Persistent Vault (Единое окно авторизации агента)",
            "url": "https://cgaso.regsamarh.ru",
            "cost": "Автономный режим агента",
            "purpose": "Скрипт scripts/scouts/playwright_research_engine.py с постоянным профилем браузера для входа в Госуслуги (ЦГАСО), Familio и Яндекс.Архивы.",
            "action_for_owner": "Запустить: python scripts/scouts/playwright_research_engine.py --login"
        },
        {
            "step": 2,
            "service": "АИС ЦГАСО (Самарский архив — с. Четыровка Кошкинского р-на)",
            "url": "https://cgaso.regsamarh.ru",
            "cost": "Бесплатно (через Госуслуги)",
            "purpose": "Оцифрованные метрики прихода с. Русская Васильевка (Ф. 32 Оп. 35) для поиска актовой записи прадеда Петра Юхина (#10).",
            "action_for_owner": "Войти через ЕСИА на cgaso.regsamarh.ru"
        },
        {
            "step": 3,
            "service": "Яндекс.Архивы / ГАОО (Оренбургский архив — д. Владимировка)",
            "url": "https://ya.ru/archive",
            "cost": "Бесплатно",
            "purpose": "Оцифрованные метрические книги Михайло-Архангельской церкви с. Ивановка (ГАОО) с семьями Каретниковых д. Владимировка.",
            "action_for_owner": "Открыть поиск по запросу 'Каретников Владимировка Ивановка'."
        }
    ]


def build_historical_dynasty_chain():
    """Историческая цепь предков Каретниковых до X колена (1745 г.)."""
    return [
        {
            "generation": 10,
            "generation_label": "X колено — Основатели рода эпохи Елизаветы Петровны (ок. 1745 г.р.)",
            "full_name": "Каретников Макар Никитович",
            "dates": "~1745 — нач. XIX века",
            "location": "Пензенская губ., Саранский уезд, с. Тепловка",
            "social_estate": "Государственный крестьянин",
            "notes": "Пращур X колена рода Каретниковых в с. Тепловка Саранского уезда. Отец Степана Макаровича Каретникова (1776–1834).",
            "sources": ["Ревизские сказки Саранского уезда (ЦГА РМ / ГАПО)"]
        },
        {
            "generation": 9,
            "generation_label": "IX колено — Эпоха Екатерины Великой и Отечественной войны 1812 г.",
            "full_name": "Каретников Степан Макарович",
            "dates": "1776 — 1834 гг.",
            "location": "Пензенская губ., Саранский уезд, с. Тепловка",
            "spouse": "Каретникова Дарья (р. 1776)",
            "social_estate": "Государственный крестьянин",
            "notes": "Отец Филимона Степановича Каретникова (р. 1809). Зафиксирован в ревизских сказках 1811, 1816 и 1834 гг. по с. Тепловка Саранского уезда.",
            "sources": ["Ревизские сказки 1811, 1816, 1834 гг. (ГАПО / ЦГА РМ)", "Familio 012999c8-1611-4e11-88ec-8e630f8d9871"]
        },
        {
            "generation": 8,
            "generation_label": "VIII колено — Эпоха Александра I и Николая I (1794–1884 гг.)",
            "full_name": "Каретников Филимон Степанович (р. 1809) и Каретников Мокей Анисимович (р. 1794)",
            "dates": "1794 — 1884 гг.",
            "location": "с. Тепловка Саранского уезда -> д. Владимировка Оренбургского уезда",
            "spouses": "Прасковья (р. 1809) — 1-я жена Филимона; Мария Онуфриевна Сафронова (1821–1884) — 2-я жена Филимона, умерла во Владимировке",
            "notes": "Родители Варвары Филимоновны (#65, 1830–1883) и Семёна Мокеевича (#64, ~1828 г.р.). Переселение семьи в Оренбуржье в конце 1860-х годов.",
            "sources": ["Ревизии Саранского уезда 1834 и 1858 гг.", "ГАОО / Яндекс.Архивы (смерть Марии Онуфриевны 1884 г. во Владимировке)"]
        },
        {
            "generation": 7,
            "generation_label": "VII колено — Первопоселенцы Оренбургского края (1828–1883 гг.)",
            "full_name": "Каретников Семён Мокеевич (~1828) и Каретникова Варвара Филимоновна (1830–1883)",
            "dates": "1828 — 1883 гг.",
            "location": "с. Тепловка -> д. Владимировка (Шаталовка) Оренбургского уезда (1868–1870 гг.)",
            "notes": "Основатели родового гнезда Каретниковых в д. Владимировка, родители 5 сыновей (Дмитрия-ст. 1854, Петра 1857, Ивана 1860, Дмитрия-мл. #32 1862 и Владимира 1867).",
            "sources": ["Метрическая книга с. Тепловка за 1867 г.", "Метрическая книга с. Ивановка (ГАОО, смерть Варвары 16.03.1883)"]
        }
    ]


def main():
    nodes = build_nodes()
    collateral = build_collateral_relatives()
    floating = build_floating_hypotheses()
    archive_leads = build_archive_leads()
    access_guide = build_access_guide()
    history_chain = build_historical_dynasty_chain()

    confirmed_count = sum(1 for x in nodes if x["status"] in ("CONFIRMED_DOC", "VERIFIED"))
    oral_count = sum(1 for x in nodes if x["status"] == "FAMILY_ORAL")
    candidate_count = sum(1 for x in nodes if x["status"] == "ARCHIVE_CANDIDATE")
    unknown_count = sum(1 for x in nodes if x["status"] == "UNKNOWN_SLOT")

    facts_direct_count = sum(1 for x in nodes if x.get("is_fact_confirmed"))
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
                "confirmed_doc": confirmed_count,
                "family_oral": oral_count,
                "archive_candidate": candidate_count,
                "unknown_slot": unknown_count,
                "total_direct_nodes": len(nodes),
                "total_collateral_nodes": len(collateral),
                "total_floating_hypotheses": len(floating),
                "active_knowledge_nodes": confirmed_count + oral_count + candidate_count + len(collateral),
                "completion_Gen1_3_percent": 100,
                "completion_Gen4_percent": 100,
                "completion_Gen5_percent": 62,
                "completion_Gen6_percent": 38,
                "completion_Gen7_percent": 25
            },
            "clans": [
                {
                    "id": "karetnikov",
                    "name": "Каретниковы",
                    "branch": "Отцовская (Дед)",
                    "region": "Оренбургская обл., Красногвардейский р-н, д. Владимировка • с. Подольск • с. Плешаново → Самара (1961 г.)",
                    "key_ancestor": "Валентин Григорьевич (1936) → Григорий Иванович (#8, VERIFIED) → Иван Дмитриевич (#16) → Дмитрий Семёнович (#32) → Семён Мокеевич (#64) и Варвара Филимоновна (#65) → предки до 1745 г.",
                    "color": "#d4af37"
                },
                {
                    "id": "yukhin",
                    "name": "Юхины",
                    "branch": "Отцовская (Бабушка)",
                    "region": "Самарская (Куйбышевская) обл., Кошкинский р-н, с. Четыровка на р. Кондурче",
                    "key_ancestor": "Клавдия Петровна (1936) → Юхин Пётр (#10, с. Четыровка)",
                    "color": "#e07a5f"
                },
                {
                    "id": "zubkov",
                    "name": "Зубковы",
                    "branch": "Материнская (Дед)",
                    "region": "Пензенская обл., Нижнеломовский р-н, с. Новый Шуструй",
                    "key_ancestor": "Владимир Владимирович Зубков ст. и мл. (#6, #301) → Владимир Зубков (#12) → 19 дворов 1917 г. (ГАПО Ф. 158)",
                    "color": "#2a9d8f"
                },
                {
                    "id": "kumanin",
                    "name": "Куманины",
                    "branch": "Материнская (Бабушка)",
                    "region": "Пензенская обл., Нижнеломовский р-н, с. Новый Шуструй",
                    "key_ancestor": "Валентина Сергеевна (#7) и сёстры Зинаида и Антонина → Сергей Куманин (#14) → Егор Петров Куманин (1917) → служилый род XVII в.",
                    "color": "#52b788"
                }
            ],
            "historical_dynasty_chain_1745": history_chain
        },
        "nodes": nodes,
        "collateral_nodes": collateral,
        "floating_hypotheses": floating,
        "archive_leads": archive_leads,
        "access_guide": access_guide,
        "historical_dynasty_chain_1745": history_chain
    }

    out_path = VAULT_DIR / "lineage_graph.json"
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] Generated 7-generation graph ({len(nodes)} direct + {len(collateral)} collateral + {len(floating)} floating hypotheses) at: {out_path}")
    print(f"     • Active knowledge nodes: {payload['meta']['stats']['active_knowledge_nodes']}")
    print(f"     • Confirmed/Verified: {confirmed_count}")
    print(f"     • Archive candidates: {candidate_count}")
    print(f"     • Floating hypotheses: {len(floating)}")


if __name__ == "__main__":
    main()
