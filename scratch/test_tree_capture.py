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

async def test_tree_capture():
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

        await page.goto(f"http://localhost:{PORT}/", wait_until="networkidle")
        await page.wait_for_timeout(500)

        # Unlock
        await page.fill("#passwordInput", pw)
        await page.click("#unlockBtn")
        await page.wait_for_selector("#workspace.active", timeout=12000)
        await page.wait_for_timeout(600)

        # Click 2D Tree tab
        await page.click(".mob-nav-item[data-mob-view='tree']")
        await page.wait_for_timeout(800)

        # Ensure Proband focus is applied
        await page.evaluate("() => { if (typeof focusOnProband === 'function') focusOnProband(); }")
        await page.wait_for_timeout(500)

        shot_path = "audit_v2_03_tree.png"
        await page.screenshot(path=shot_path)
        print("Captured audit_v2_03_tree.png successfully!")

        dst = os.path.join(BRAIN_DIR, shot_path)
        shutil.copy(shot_path, dst)
        print(f"Copied to {dst}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_tree_capture())
