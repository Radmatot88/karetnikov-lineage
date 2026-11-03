import asyncio
from playwright.async_api import async_playwright

async def test_scaler():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 390, "height": 844})
        await page.goto("http://localhost:4329/", wait_until="networkidle")

        scale_before = await page.evaluate("() => document.documentElement.getAttribute('data-font-scale')")
        print("Scale before click:", scale_before)

        await page.click(".font-scale-btn[data-scale='lg']")
        await page.wait_for_timeout(300)

        scale_after = await page.evaluate("() => document.documentElement.getAttribute('data-font-scale')")
        print("Scale after click lg:", scale_after)

        btn_active = await page.evaluate("() => document.querySelector('.font-scale-btn[data-scale=\"lg\"]').classList.contains('active')")
        print("Button lg active class:", btn_active)

        await page.click(".font-scale-btn[data-scale='xl']")
        await page.wait_for_timeout(300)
        scale_xl = await page.evaluate("() => document.documentElement.getAttribute('data-font-scale')")
        print("Scale after click xl:", scale_xl)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_scaler())
