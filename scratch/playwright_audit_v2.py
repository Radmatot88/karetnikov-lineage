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

async def run_audit():
    dev_vars = load_dev_vars()
    pw = (
        dev_vars.get("LINEAGE_OWNER_PASSWORD")
        or dev_vars.get("LINEAGE_MASTER_PASSWORD")
        or dev_vars.get("LINEAGE_RELATIVE_PASSWORD")
    )
    print(f"Loaded password exists: {bool(pw)}")

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
        print("Navigating to http://localhost:4329/ ...")
        await page.goto(f"http://localhost:{PORT}/", wait_until="networkidle")
        await page.wait_for_timeout(1000)

        # Check horizontal overflow on Gate
        gate_overflow = await page.evaluate("() => document.documentElement.scrollWidth > window.innerWidth")
        print(f"Gate horizontal overflow: {gate_overflow}")

        await page.screenshot(path="audit_v2_01_gate.png")
        print("Captured audit_v2_01_gate.png")

        # Unlock
        if pw:
            print("Unlocking vault...")
            await page.fill("#passwordInput", pw)
            await page.click("#unlockBtn")
            await page.wait_for_selector("#workspace.active", timeout=12000)
            await page.wait_for_timeout(1200)

        # 2. SCROLL VIEW
        await page.click(".mob-nav-item[data-mob-view='scroll']")
        await page.wait_for_timeout(800)
        scroll_overflow = await page.evaluate("() => document.documentElement.scrollWidth > window.innerWidth")
        print(f"Scroll view horizontal overflow: {scroll_overflow}")
        await page.screenshot(path="audit_v2_02_scroll.png")
        print("Captured audit_v2_02_scroll.png")

        # Test font scaler
        await page.click(".font-scale-btn[data-scale='lg']")
        await page.wait_for_timeout(400)
        font_scale_val = await page.evaluate("() => document.documentElement.getAttribute('data-font-scale')")
        print(f"Font scaler switched to: {font_scale_val}")

        # 3. 2D TREE VIEW (Check centering on proband)
        await page.click(".mob-nav-item[data-mob-view='tree']")
        await page.wait_for_timeout(1000)
        proband_bounds = await page.evaluate("""() => {
            const el = document.querySelector('[data-roadmap-ahn="1"]');
            if (!el) return null;
            const r = el.getBoundingClientRect();
            return { x: r.x, y: r.y, width: r.width, height: r.height };
        }""")
        print(f"Proband bounds on 2D tree: {proband_bounds}")
        await page.screenshot(path="audit_v2_03_tree.png")
        print("Captured audit_v2_03_tree.png")

        # 4. FAN CHART VIEW
        await page.click(".mob-nav-item[data-mob-view='fan']")
        await page.wait_for_timeout(800)
        # Tap sector #1 to trigger mobile inspector
        await page.click("#fanChartContainer [data-ahnentafel='1']")
        await page.wait_for_timeout(500)
        inspector_visible = await page.is_visible("#fanMobileInspector")
        inspector_text = await page.inner_text("#fanMobileInspector") if inspector_visible else "NOT VISIBLE"
        print(f"Fan Mobile Inspector visible: {inspector_visible} | snippet: {inspector_text[:60]}")
        await page.screenshot(path="audit_v2_04_fan.png")
        print("Captured audit_v2_04_fan.png")

        # 5. DOSSIER DRAWER
        # Click "Открыть досье предка" inside inspector
        if inspector_visible:
            await page.click("#fanMobileInspector button")
            await page.wait_for_timeout(800)
            drawer_open = await page.evaluate("() => document.getElementById('dossierDrawer').classList.contains('open')")
            print(f"Dossier Drawer open: {drawer_open}")
            await page.screenshot(path="audit_v2_05_drawer.png")
            print("Captured audit_v2_05_drawer.png")
            # Close drawer
            await page.click("#closeDrawerBtn")
            await page.wait_for_timeout(500)

        # 6. HERALDRY VIEW (/heraldry/)
        print("Navigating to http://localhost:4329/heraldry/ ...")
        await page.goto(f"http://localhost:{PORT}/heraldry/", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        heraldry_overflow = await page.evaluate("() => document.documentElement.scrollWidth > window.innerWidth")
        print(f"Heraldry horizontal overflow: {heraldry_overflow}")
        await page.screenshot(path="audit_v2_06_heraldry.png")
        print("Captured audit_v2_06_heraldry.png")

        await browser.close()

    # Copy screenshots to BRAIN_DIR
    for fname in ["audit_v2_01_gate.png", "audit_v2_02_scroll.png", "audit_v2_03_tree.png", "audit_v2_04_fan.png", "audit_v2_05_drawer.png", "audit_v2_06_heraldry.png"]:
        if os.path.exists(fname):
            dst = os.path.join(BRAIN_DIR, fname)
            shutil.copy(fname, dst)
            print(f"Copied {fname} -> {dst}")

    print("ALL AUDIT V2 SCREENSHOTS CAPTURED & SAVED!")

if __name__ == "__main__":
    asyncio.run(run_audit())
