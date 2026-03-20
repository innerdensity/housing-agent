from pathlib import Path
from playwright.sync_api import sync_playwright

SEARCH_URL = "https://www.zillow.com/queens-new-york-ny/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Queens%2C%20NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-73.981%2C%22east%22%3A-73.700%2C%22south%22%3A40.541%2C%22north%22%3A40.800%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A2750%7D%2C%22beds%22%3A%7B%22max%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%7D"


def run_zillow_fetch():
    output_dir = Path("artifacts")
    output_dir.mkdir(exist_ok=True)

    html_path = output_dir / "zillow_search.html"
    screenshot_path = output_dir / "zillow_search.png"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1440, "height": 2200},
        )

        page.goto(SEARCH_URL, wait_until="domcontentloaded", timeout=90000)
        page.wait_for_timeout(8000)

        html_path.write_text(page.content(), encoding="utf-8")
        page.screenshot(path=str(screenshot_path), full_page=True)

        print(f"Saved HTML to {html_path}")
        print(f"Saved screenshot to {screenshot_path}")

        browser.close()