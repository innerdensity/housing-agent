import config

def main():
    print("Housing agent started")
    print("Source:", config.SOURCE_SITE)
    print("Search track:", config.SEARCH_TRACK)
    print("Max price:", config.MAX_PRICE)
    print("Allowed home types:", ", ".join(config.ALLOWED_HOME_TYPES))
    print("Target neighborhoods:", ", ".join(config.TARGET_NEIGHBORHOODS))

if __name__ == "__main__":
    main()