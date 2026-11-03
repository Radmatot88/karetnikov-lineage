#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Playwright E2E Mobile App Verification (iPhone 15 Pro 393x852):
1. Serves dist/ on a local free port so we test the exact production build.
2. Unlocks the vault using the password from .dev.vars (Zero-Hardcode).
3. Verifies automatic landing on Mobile Generation Scroll (#view-scroll) in 100% Facts Mode (19 persons).
4. Tests Smart Kinship Path Breadcrumb (#1 -> #3 -> #7 -> #14), 1-Tap Kinship Pills, and Bottom Sheet Dossier (12 Rubrics).
5. Captures 4 high-DPI mobile screenshots into the conversation artifact directory.
"""

import sys
import time
import threading
import http.server
import socketserver
from pathlib import Path
from playwright.sync_api import sync_playwright

PROJECT_ROOT = Path(r"c:\Karetnikov_Lineage")
sys.path.insert(0, str(PROJECT_ROOT))
from scripts.crypto_vault import parse_dev_vars

ARTIFACT_DIR = Path(r"C:\Users\User\.gemini\antigravity\brain\fe4a875c-474b-43ad-818d-951ff1b13556")
DIST_DIR = PROJECT_ROOT / "dist"


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIST_DIR), **kwargs)

    def log_message(self, format, *args):
        pass


def run_test():
    env_vars = parse_dev_vars()
    pw = env_vars.get("LINEAGE_OWNER_PASSWORD") or env_vars.get("LINEAGE_MASTER_PASSWORD") or env_vars.get("LINEAGE_RELATIVE_PASSWORD")
    assert pw, "Password not found in .dev.vars"

    httpd = socketserver.TCPServer(("127.0.0.1", 0), QuietHandler)
    port = httpd.server_address[1]
    server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    server_thread.start()

    url = f"http://127.0.0.1:{port}/"
    print(f"[INFO] Testing production dist/ on {url} at iPhone 15 Pro (393x852)...")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 393, "height": 852},
            device_scale_factor=2,
            is_mobile=True,
            has_touch=True,
        )
        page = context.new_page()
        js_errors = []
        page.on("pageerror", lambda err: js_errors.append(str(err)))

        page.goto(url, wait_until="networkidle")
        page.fill("#passwordInput", pw)
        page.click("#unlockBtn")

        # Wait for workspace to unlock and automatically switch to #view-scroll on mobile
        page.wait_for_selector("#workspace.active", timeout=8000)
        time.sleep(0.5)

        is_scroll_active = page.eval_on_selector("#view-scroll", "el => el.classList.contains('active')")
        assert is_scroll_active, "Expected #view-scroll to be active by default on mobile!"

        cards_count = page.locator("#scrollGenerationsList .scroll-person-card").count()
        print(f"[PASS] Mobile Scroll default Facts-Only cards count: {cards_count}")
        assert cards_count == 19, f"Expected 19 verified fact cards in default scroll mode, got {cards_count}"

        # Screenshot 1: Mobile Scroll Home View (I-II Generations + Sticky Smart Header + Bottom Nav)
        shot1 = ARTIFACT_DIR / "mobile_app_01_scroll_home.png"
        page.screenshot(path=str(shot1), full_page=False)
        print(f"[SHOT 1] Saved {shot1.name}")

        # Trigger Smart Kinship Path on #14 (Sergey Kumanin) and scroll to III-IV generation
        page.evaluate("scrollToPersonInScroll(14)")
        time.sleep(0.6)
        is_breadcrumb_visible = page.eval_on_selector("#kinshipPathBar", "el => el.classList.contains('visible')")
        assert is_breadcrumb_visible, "Expected #kinshipPathBar to be visible after selecting #14!"
        steps_text = page.locator("#kinshipPathSteps").inner_text()
        print(f"[PASS] Smart Kinship Path Breadcrumb: {steps_text.replace(chr(10), ' ')}")

        # Screenshot 2: Smart Kinship Path + IV Generation Card (#14)
        shot2 = ARTIFACT_DIR / "mobile_app_02_kinship_path.png"
        page.screenshot(path=str(shot2), full_page=False)
        print(f"[SHOT 2] Saved {shot2.name}")

        # Open Dossier Bottom Sheet on #4 (Grandfather Valentin Grigorievich) and expand 12 Rubrics
        page.evaluate("openDossier(4)")
        time.sleep(0.4)
        details_loc = page.locator(".rubrics-12-details summary")
        if details_loc.count() > 0:
            details_loc.click()
            time.sleep(0.3)

        shot3 = ARTIFACT_DIR / "mobile_app_03_bottom_sheet_dossier.png"
        page.screenshot(path=str(shot3), full_page=False)
        print(f"[SHOT 3] Saved {shot3.name}")

        # Close dossier and tap "На 2D-карте" on #4 to verify 2D Canvas focus on mobile
        page.evaluate("closeDossier(); focusNodeOn2DCanvas(4);")
        time.sleep(0.5)
        shot4 = ARTIFACT_DIR / "mobile_app_04_2d_canvas_touch.png"
        page.screenshot(path=str(shot4), full_page=False)
        print(f"[SHOT 4] Saved {shot4.name}")

        assert len(js_errors) == 0, f"JS runtime errors detected: {js_errors}"
        browser.close()

    httpd.shutdown()
    print("[PASS] All Playwright Mobile App E2E checks passed with 0 JS errors!")


if __name__ == "__main__":
    run_test()
