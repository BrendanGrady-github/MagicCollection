import requests


SCRYFALL_SEARCH_URL = "https://api.scryfall.com/cards/search"

HEADERS = {
    "User-Agent": (
        "MagicCollectionInventory/0.1 "
        "(Developer: Brendan Grady; "
        "Project: https://github.com/YOUR_GITHUB_USERNAME/MagicCollection)"
    ),
    "Accept": "application/json"
}


def get_card_printings(card_name):
    query = f'!"{card_name}" unique:prints'

    all_printings = []

    response = requests.get(
        SCRYFALL_SEARCH_URL,
        params={"q": query, "order": "released"},
        headers=HEADERS,
        timeout=10
    )

    while True:
        if response.status_code != 200:
            print("Scryfall error:", response.status_code)
            print(response.json())
            return all_printings

        data = response.json()
        all_printings.extend(data["data"])

        if not data.get("has_more"):
            break

        response = requests.get(
            data["next_page"],
            headers=HEADERS,
            timeout=10
        )

    return all_printings