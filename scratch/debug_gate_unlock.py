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

async def debug_unlock():
    dev_vars = load_dev_vars()
    pw = dev_vars.get("LINEAGE_RELATIVE_PASSWORD")
    print(f"Using LINEAGE_RELATIVE_PASSWORD (length: {len(pw) if pw else 0})")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 390, "height": 844})
        
        page.on("console", lambda msg: print(f"[CONSOLE {msg.type}] {msg.text}"))
        page.on("pageerror", lambda err: print(f"[PAGE ERROR] {err}"))

        await page.goto("http://localhost:4329/", wait_until="networkidle")
        await page.fill("#passwordInput", pw)
        await page.click("#unlockBtn")
        
        # Wait up to 5 seconds and poll status text
        for _ in range(10):
            await page.wait_for_timeout(500)
            status_text = await page.inner_text("#authStatus")
            print("Status:", status_text)
            has_unlocked = await page.evaluate("() => document.getElementById('fortressGate').classList.contains('unlocked')")
            if has_unlocked:
                print("GATE UNLOCKED SUCCESS!")
                break
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(debug_unlock())
