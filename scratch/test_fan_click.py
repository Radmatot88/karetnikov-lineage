import asyncio
import os
from playwright.async_api import async_playwright

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

async def test_fan():
    dev_vars = load_dev_vars()
    pw = dev_vars.get("LINEAGE_RELATIVE_PASSWORD")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 390, "height": 844})
        await page.goto("http://localhost:4329/", wait_until="networkidle")
        await page.fill("#passwordInput", pw)
        await page.click("#unlockBtn")
        await page.wait_for_selector("#workspace.active", timeout=12000)

        # Go to fan view
        await page.click(".mob-nav-item[data-mob-view='fan']")
        await page.wait_for_timeout(500)

        # Check sectors count
        sectors = await page.locator("#fanChartContainer [data-ahnentafel]").count()
        print(f"Total fan sectors found: {sectors}")

        # Dispatch click on sector #1
        await page.evaluate("() => document.querySelector('#fanChartContainer [data-ahnentafel=\"1\"]').dispatchEvent(new MouseEvent('click', { bubbles: true }))")
        await page.wait_for_timeout(500)

        insp_display = await page.evaluate("() => document.getElementById('fanMobileInspector').style.display")
        insp_html = await page.inner_html("#fanMobileInspector")
        print(f"Inspector display: {insp_display}")
        print(f"Inspector snippet: {insp_html[:150]}")

        # Now test dossier drawer open from fan inspector
        await page.click("#fanMobileInspector button")
        await page.wait_for_timeout(500)
        drawer_open = await page.evaluate("() => document.getElementById('dossierDrawer').classList.contains('open')")
        print(f"Drawer open from Fan Inspector: {drawer_open}")

        await page.screenshot(path="audit_v2_05_drawer.png")
        print("Captured audit_v2_05_drawer.png successfully!")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_fan())
