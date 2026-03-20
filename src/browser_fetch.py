from pathlib import Path
from playwright.sync_api import sync_playwright

SEARCH_URL = "https://streeteasy.com/for-rent/nyc/price:-2750%7Cbeds%3C=1"


def run_browser_fetch():
    output_dir = Path("artifacts")
    output_dir.mkdir(exist_ok=True)

    html_path = output_dir / "streeteasy_search.html"
    screenshot_path = output_dir / "streeteasy_search.png"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(SEARCH_URL, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(5000)

        html_path.write_text(page.content(), encoding="utf-8")
        page.screenshot(path=str(screenshot_path), full_page=True)

        print(f"Saved HTML to {html_path}")
        print(f"Saved screenshot to {screenshot_path}")

        browser.close()


if __name__ == "__main__":
    run_browser_fetch()