from app.services.scryfall import find_card_by_name

card = find_card_by_name("Sol Rin")

if card is None:
    print("Card not found.")
else:
    print("Found card!")
    print("Name:", card["name"])
    print("Set:", card["set_name"])
    print("Collector Number:", card["collector_number"])
    print("Scryfall ID:", card["id"])