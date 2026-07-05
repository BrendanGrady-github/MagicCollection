from flask import Blueprint, render_template, request

from app.services.scryfall import get_card_printings

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("home.html")


@main.route("/add-card")
def add_card():
    card_name = request.args.get("card_name", "")
    selected_set = request.args.get("set_name", "")
    page = request.args.get("page", 1, type=int)

    printings = []
    sets = []

    per_page = 50
    total_pages = 0

    if card_name:
        printings = get_card_printings(card_name)

        sets = sorted(set(card["set_name"] for card in printings))

        if selected_set:
            printings = [
                card for card in printings
                if card["set_name"] == selected_set
            ]

        total_pages = (len(printings) + per_page - 1) // per_page

        start = (page - 1) * per_page
        end = start + per_page
        printings = printings[start:end]

    return render_template(
        "add_card.html",
        card_name=card_name,
        selected_set=selected_set,
        sets=sets,
        printings=printings,
        page=page,
        total_pages=total_pages
    )