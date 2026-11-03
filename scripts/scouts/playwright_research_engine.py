#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Playwright Persistent Research Engine для проекта C:\Karetnikov_Lineage.
Обеспечивает агенту постоянный авторизованный доступ к генеалогическим базам:
- АИС ЦГАСО (cgaso.regsamarh.ru — вход через ЕСИА Госуслуги)
- Familio.org (справочник населенных пунктов и фамилий)
- Forum VGD.ru (выписки из ГАПО, ЦГАСО, ГАОО)
- Яндекс Поиск по Архивам (yandex.ru/archive — OCR рукописных метрик Оренбурга, Самары и Пензы)
- Память Народа (pamyat-naroda.ru)
"""

import json
import time
import argparse
import urllib.parse
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
PROFILE_DIR = PROJECT_ROOT / ".secrets" / "browser_profile"
HARVEST_DIR = PROJECT_ROOT / "data" / "raw_scans"

TARGET_PORTALS = [
    ("cgaso", "https://cgaso.regsamarh.ru/"),
    ("familio", "https://familio.org/"),
    ("vgd", "https://forum.vgd.ru/"),
    ("yandex_archive", "https://yandex.ru/archive"),
    ("pamyat_naroda", "https://pamyat-naroda.ru/heroes/")
]

RESEARCH_QUERIES = [
    {"clan": "Зубковы & Куманины", "query": "Новый Шуструй Зубков Куманин"},
    {"clan": "Каретниковы", "query": "Плешаново Подольск Каретников Григорий Николай Петр"},
    {"clan": "Юхины", "query": "Кошкинский район Юхин Петр Клавдия"}
]


def interactive_login_session():
    PROFILE_DIR.mkdir(parents=True, exist_ok=True)
    print(f"[LOGIN MODE] Opening persistent browser profile at: {PROFILE_DIR}")
    print("Log into Gosuslugi (AIS CGASO), Familio.org, and VGD.ru. Close the browser window when done.")
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),
            headless=False,
            viewport={"width": 1440, "height": 900}
        )
        for idx, (name, url) in enumerate(TARGET_PORTALS):
            page = context.pages[0] if idx == 0 and context.pages else context.new_page()
            try:
                page.goto(url, timeout=30000)
            except Exception as e:
                print(f"[WARN] Could not pre-open {name}: {e}")
        print("[WAITING] Browser is open. Authenticate on the tabs, then close the browser window to save session.")
        try:
            while len(context.pages) > 0:
                time.sleep(1.0)
        except Exception:
            pass
        context.close()
    print("[OK] Session cookies saved to .secrets/browser_profile!")


def autonomous_research_sweep():
    PROFILE_DIR.mkdir(parents=True, exist_ok=True)
    HARVEST_DIR.mkdir(parents=True, exist_ok=True)
    results = []

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),
            headless=True,
            viewport={"width": 1440, "height": 900}
        )
        page = context.pages[0] if context.pages else context.new_page()

        for item in RESEARCH_QUERIES:
            q = item["query"]
            url = f"https://yandex.ru/archive/search?text={urllib.parse.quote(q)}"
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=20000)
                time.sleep(2.0)
                snippets = page.locator("body").inner_text()[:2500]
                results.append({
                    "clan": item["clan"],
                    "query": q,
                    "portal": "yandex_archive",
                    "timestamp": datetime.now().isoformat(),
                    "excerpt": snippets
                })
            except Exception as e:
                results.append({
                    "clan": item["clan"],
                    "query": q,
                    "error": str(e)
                })
        context.close()

    out_file = HARVEST_DIR / "research_harvest.json"
    out_file.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] Saved autonomous research harvest to: {out_file}")


def main():
    parser = argparse.ArgumentParser(description="Playwright Persistent Genealogy Research Engine")
    parser.add_argument("--login", action="store_true", help="Open visible browser to log into archives once")
    parser.add_argument("--research", action="store_true", help="Run autonomous headless archive sweep using saved profile")
    args = parser.parse_args()

    if args.login:
        interactive_login_session()
    elif args.research:
        autonomous_research_sweep()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
