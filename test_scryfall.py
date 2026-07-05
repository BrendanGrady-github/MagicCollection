from app.services.scryfall import get_card_printings

printings = get_card_printings("Sol Ring")

print(f"Found {len(printings)} printings")

for card in printings[:10]:
    image_url = card.get("image_uris", {}).get("normal", "No image")

    print()
    print("Name:", card["name"])
    print("Set:", card["set_name"])
    print("Collector Number:", card["collector_number"])
    print("Scryfall ID:", card["id"])
    print("Image:", image_url)