import asyncio
import os
import shutil
from playwright.async_api import async_playwright

BRAIN_DIR = r"C:\Users\User\.gemini\antigravity\brain\1895dcac-5397-4f22-acaf-2f85b12321a6"
PORT = 4329

def load_dev_vars():
    vars_dict = {}
    if os.path.exists(".dev.vars"):
        with open(".dev.vars", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    vars_dict[k.strip()] = v.strip().strip('"').strip("'")
    return vars_dict

async def run_heraldic_suite():
    dev_vars = load_dev_vars()
    pw = dev_vars.get("LINEAGE_RELATIVE_PASSWORD") or dev_vars.get("LINEAGE_OWNER_PASSWORD")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 390, "height": 844},
            device_scale_factor=2,
            is_mobile=True,
            has_touch=True,
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
        )
        page = await context.new_page()

        print("[QA 1] Navigating to local preview server...")
        await page.goto(f"http://localhost:{PORT}/", wait_until="networkidle")
        await page.wait_for_timeout(600)

        # Unlock Fortress Vault
        print("[QA 2] Unlocking Fortress Vault...")
        await page.fill("#passwordInput", pw)
        await page.click("#unlockBtn")
        await page.wait_for_selector("#workspace.active", timeout=12000)
        await page.wait_for_timeout(600)

        # 1. Default Synthesis Theme (Все 4 рода) in Scroll
        await page.click(".mob-nav-item[data-mob-view='scroll']")
        await page.wait_for_timeout(500)
        shot1 = "audit_v3_theme_01_all.png"
        await page.screenshot(path=shot1)
        print(f"Captured: {shot1}")

        # 2. Дом Каретниковых (Crimson & Gold)
        print("[QA 3] Switching to Дом Каретниковых...")
        await page.click("#scrollClanPills .clan-theme-pill[data-clan-theme='karetnikov']")
        await page.wait_for_timeout(500)
        shot2 = "audit_v3_theme_02_karetnikov.png"
        await page.screenshot(path=shot2)
        print(f"Captured: {shot2}")

        # 3. Дом Куманиных (Royal French Azure)
        print("[QA 4] Switching to Дом Куманиных (Royal Azure)...")
        await page.click("#scrollClanPills .clan-theme-pill[data-clan-theme='kumanin']")
        await page.wait_for_timeout(500)
        shot3 = "audit_v3_theme_03_kumanin.png"
        await page.screenshot(path=shot3)
        print(f"Captured: {shot3}")

        # 4. Дом Зубковых (Malachite Forest Emerald)
        print("[QA 5] Switching to Дом Зубковых (Malachite Emerald)...")
        await page.click("#scrollClanPills .clan-theme-pill[data-clan-theme='zubkov']")
        await page.wait_for_timeout(500)
        shot4 = "audit_v3_theme_04_zubkov.png"
        await page.screenshot(path=shot4)
        print(f"Captured: {shot4}")

        # 5. Дом Юхиных (Imperial Royal Amethyst)
        print("[QA 6] Switching to Дом Юхиных (Royal Amethyst)...")
        await page.click("#scrollClanPills .clan-theme-pill[data-clan-theme='yukhin']")
        await page.wait_for_timeout(500)
        shot5 = "audit_v3_theme_05_yukhin.png"
        await page.screenshot(path=shot5)
        print(f"Captured: {shot5}")

        # 6. 2D Tree Roadmap under Kumanin Azure Theme
        print("[QA 7] Testing 2D Tree Roadmap under Kumanin Azure...")
        await page.click(".mob-nav-item[data-mob-view='tree']")
        await page.wait_for_timeout(600)
        await page.evaluate("() => { if (typeof setHeraldicClanTheme === 'function') setHeraldicClanTheme('kumanin'); if (typeof focusOnProband === 'function') focusOnProband(); }")
        await page.wait_for_timeout(600)
        shot6 = "audit_v3_theme_06_tree_kumanin.png"
        await page.screenshot(path=shot6)
        print(f"Captured: {shot6}")

        # 7. 2D Tree Roadmap under Zubkov Malachite Theme
        print("[QA 8] Testing 2D Tree Roadmap under Zubkov Malachite...")
        await page.evaluate("() => { if (typeof setHeraldicClanTheme === 'function') setHeraldicClanTheme('zubkov'); if (typeof focusOnProband === 'function') focusOnProband(); }")
        await page.wait_for_timeout(600)
        shot7 = "audit_v3_theme_07_tree_zubkov.png"
        await page.screenshot(path=shot7)
        print(f"Captured: {shot7}")

        await browser.close()

    # Copy all shots to brain
    shots = [shot1, shot2, shot3, shot4, shot5, shot6, shot7]
    for s in shots:
        if os.path.exists(s):
            dst = os.path.join(BRAIN_DIR, s)
            shutil.copy(s, dst)
            print(f"Copied {s} -> {dst}")

    print("\n[SUCCESS] All 7 Heraldic Theme QA screenshots captured & copied!")

if __name__ == "__main__":
    asyncio.run(run_heraldic_suite())
