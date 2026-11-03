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

async def run_full_suite():
    dev_vars = load_dev_vars()
    pw = dev_vars.get("LINEAGE_RELATIVE_PASSWORD") or dev_vars.get("LINEAGE_OWNER_PASSWORD")
    assert pw, "Password not found in .dev.vars"

    results = {}

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

        # 1. GATE
        print("[TEST 1] Testing Fortress Gate (Light Imperial Vellum)...")
        await page.goto(f"http://localhost:{PORT}/", wait_until="networkidle")
        await page.wait_for_timeout(800)

        gate_overflow = await page.evaluate("() => document.documentElement.scrollWidth > window.innerWidth")
        results['gate_overflow'] = gate_overflow
        await page.screenshot(path="audit_v2_01_gate.png")
        print(f" -> Gate horizontal overflow: {gate_overflow} [PASS: {not gate_overflow}]")

        # 2. UNLOCK
        print("[TEST 2] Unlocking Vault...")
        await page.fill("#passwordInput", pw)
        await page.click("#unlockBtn")
        await page.wait_for_selector("#workspace.active", timeout=12000)
        await page.wait_for_timeout(800)
        results['vault_unlocked'] = True
        print(" -> Vault unlocked successfully!")

        # 3. SCROLL VIEW & FONT SCALER
        print("[TEST 3] Testing Generation Scroll & Senior Font Scaler...")
        await page.click(".mob-nav-item[data-mob-view='scroll']")
        await page.wait_for_timeout(600)
        scroll_overflow = await page.evaluate("() => document.documentElement.scrollWidth > window.innerWidth")
        results['scroll_overflow'] = scroll_overflow
        print(f" -> Scroll view horizontal overflow: {scroll_overflow} [PASS: {not scroll_overflow}]")

        # Click font scaler A+
        await page.click(".font-scale-btn[data-scale='lg']")
        await page.wait_for_timeout(300)
        font_scale_val = await page.evaluate("() => document.documentElement.getAttribute('data-font-scale')")
        results['font_scale_lg'] = (font_scale_val == 'lg')
        print(f" -> Font scaler active value: {font_scale_val} [PASS: {font_scale_val == 'lg'}]")

        await page.screenshot(path="audit_v2_02_scroll.png")

        # 4. 2D TREE VIEW
        print("[TEST 4] Testing 2D Map Tree View & Proband Auto-Center...")
        await page.click(".mob-nav-item[data-mob-view='tree']")
        await page.wait_for_timeout(1000)
        proband_card_exists = await page.evaluate("() => Boolean(document.querySelector('.rm-node[data-ahnentafel=\"1\"]'))")
        results['proband_exists'] = proband_card_exists
        tree_pan = await page.evaluate("() => ({ panX: window.panX, panY: window.panY, zoom: window.zoom })")
        print(f" -> Proband card exists in tree: {proband_card_exists}")
        await page.screenshot(path="audit_v2_03_tree.png")

        # 5. FAN CHART VIEW & TOUCH INSPECTOR
        print("[TEST 5] Testing Circular Fan Chart & Mobile Inspector Card...")
        await page.click(".mob-nav-item[data-mob-view='fan']")
        await page.wait_for_timeout(800)
        # Click sector #1
        await page.evaluate("() => document.querySelector('#fanChartContainer [data-ahnentafel=\"1\"]').dispatchEvent(new MouseEvent('click', { bubbles: true }))")
        await page.wait_for_timeout(500)
        insp_visible = await page.evaluate("() => document.getElementById('fanMobileInspector').style.display === 'block'")
        results['fan_inspector_visible'] = insp_visible
        print(f" -> Fan Touch Inspector visible on mobile tap: {insp_visible} [PASS: {insp_visible}]")
        await page.screenshot(path="audit_v2_04_fan.png")

        # 6. DOSSIER DRAWER
        print("[TEST 6] Testing Dossier Drawer Slide-Over...")
        await page.click("#fanMobileInspector button")
        await page.wait_for_timeout(800)
        drawer_open = await page.evaluate("() => document.getElementById('dossierDrawer').classList.contains('open')")
        results['drawer_open'] = drawer_open
        print(f" -> Dossier Drawer open: {drawer_open} [PASS: {drawer_open}]")
        await page.screenshot(path="audit_v2_05_drawer.png")

        # Close drawer
        await page.click("#closeDrawerBtn")
        await page.wait_for_timeout(400)

        # 7. HERALDRY VIEW (/heraldry/)
        print("[TEST 7] Testing Heraldry Showcase (/heraldry/)...")
        await page.goto(f"http://localhost:{PORT}/heraldry/", wait_until="networkidle")
        await page.wait_for_timeout(800)
        heraldry_overflow = await page.evaluate("() => document.documentElement.scrollWidth > window.innerWidth")
        results['heraldry_overflow'] = heraldry_overflow
        print(f" -> Heraldry horizontal overflow: {heraldry_overflow} [PASS: {not heraldry_overflow}]")
        await page.screenshot(path="audit_v2_06_heraldry.png")

        await browser.close()

    # Copy all shots to brain
    shot_files = [
        "audit_v2_01_gate.png",
        "audit_v2_02_scroll.png",
        "audit_v2_03_tree.png",
        "audit_v2_04_fan.png",
        "audit_v2_05_drawer.png",
        "audit_v2_06_heraldry.png"
    ]
    for sf in shot_files:
        if os.path.exists(sf):
            dst = os.path.join(BRAIN_DIR, sf)
            shutil.copy(sf, dst)
            print(f"Copied {sf} -> {dst}")

    print("\n================== FULL VERIFICATION SUMMARY ==================")
    for k, v in results.items():
        print(f"  {k}: {v}")
    print("===============================================================\n")

if __name__ == "__main__":
    asyncio.run(run_full_suite())
