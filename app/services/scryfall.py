import requests


SCRYFALL_NAMED_URL = "https://api.scryfall.com/cards/named"

HEADERS = {
    "User-Agent": (
        "MagicCollectionInventory/0.1 "
        "(Developer: Brendan Grady; "
        "Project: https://github.com/YOUR_GITHUB_USERNAME/MagicCollection)"
    ),
    "Accept": "application/json"
}


def find_card_by_name(card_name):
    response = requests.get(
        SCRYFALL_NAMED_URL,
        params={"fuzzy": card_name},
        headers=HEADERS,
        timeout=10
    )

    if response.status_code != 200:
        print("Scryfall error:", response.status_code)
        print(response.json())
        return None

    return response.json()