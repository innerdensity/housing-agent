import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

import config
from src.search_plan import build_search_plan


def run_intake():
    plan = build_search_plan()

    print("=== HOUSING INTAKE RUNNER ===")
    print(f"Source: {plan['source_site']}")
    print(f"Track: {plan['search_track']}")
    print(f"Max price: {plan['max_price']}")
    print("Home types:", ", ".join(plan["allowed_home_types"]))
    print("Neighborhoods:", ", ".join(plan["target_neighborhoods"]))
    print("Status: intake runner initialized")


if __name__ == "__main__":
    run_intake()