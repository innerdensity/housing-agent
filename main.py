import config
from fetch_page import fetch_test_page

print("Housing agent project is working")
print("Source:", config.SOURCE_SITE)
print("Max price:", config.MAX_PRICE)
print("Allowed home types:", config.ALLOWED_HOME_TYPES)
print("Target neighborhoods:", config.TARGET_NEIGHBORHOODS)
print("Search track:", config.SEARCH_TRACK)

print("\nRunning test fetch...\n")
fetch_test_page()