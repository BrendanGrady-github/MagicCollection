import requests


SCRYFALL_NAMED_URL = "https://api.scryfall.com/cards/named"
SCRYFALL_SEARCH_URL = "https://api.scryfall.com/cards/search"
SCRYFALL_CARD_URL = "https://api.scryfall.com/cards"

HEADERS = {
    "User-Agent": (
        "MagicCollectionInventory/0.1 "
        "(https://github.com/BrendanGrady-github/MagicCollection)"
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


def get_card_by_id(scryfall_id):
    response = requests.get(
        f"{SCRYFALL_CARD_URL}/{scryfall_id}",
        headers=HEADERS,
        timeout=10
    )

    if response.status_code != 200:
        print("Scryfall error:", response.status_code)
        print(response.json())
        return None

    return response.json()