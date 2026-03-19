import config

def build_search_plan():
    return {
        "source_site": config.SOURCE_SITE,
        "search_track": config.SEARCH_TRACK,
        "max_price": config.MAX_PRICE,
        "allowed_home_types": config.ALLOWED_HOME_TYPES,
        "target_neighborhoods": config.TARGET_NEIGHBORHOODS,
    }

if __name__ == "__main__":
    plan = build_search_plan()
    print(plan)