import requests

TEST_URL = "https://streeteasy.com/rental/4981542"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}


def fetch_test_page():
    response = requests.get(TEST_URL, headers=HEADERS, timeout=30)

    print("STATUS:", response.status_code)
    print("FINAL URL:", response.url)
    print("LENGTH:", len(response.text))

    with open("sample_streeteasy.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    print("Saved to sample_streeteasy.html")


if __name__ == "__main__":
    fetch_test_page()