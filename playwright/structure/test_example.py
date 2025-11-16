from playwright.sync_api import sync_playwright
# זה סתם בשביל לראות שמצליח להריץ פליירייט
def test_open_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")
        print("Title:", page.title())
        browser.close()
