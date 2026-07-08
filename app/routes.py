from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    jsonify
)

from app.models import (
    db,
    Storage,
    StorageSection
)
from app.services.scryfall import get_card_printings, get_card_by_id

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


@main.route("/add-card/confirm")
def confirm_add_card():

    scryfall_id = request.args.get("scryfall_id")

    card = get_card_by_id(scryfall_id)

    if card is None:
        return "Card not found.", 404

    # Retrieve every storage location from the database.
    # We'll use these to populate the Storage dropdown
    # on the Add Card page.
    storages = Storage.query.order_by(
        Storage.storage_type,
        Storage.name
    ).all()

    return render_template(
        "confirm_add_card.html",
        card=card,
        storages=storages
    )


@main.route("/storage", methods=["GET", "POST"])
def storage():
    if request.method == "POST":
        storage_type = request.form.get("storage_type")
        name = request.form.get("name")

        uses_sections = request.form.get("uses_sections") == "on"

        if storage_type and name:
            new_storage = Storage(
                storage_type=storage_type,
                name=name,
                uses_sections=uses_sections
            )

            db.session.add(new_storage)
            db.session.commit()

        return redirect(url_for("main.storage"))

    storages = Storage.query.order_by(
        Storage.storage_type,
        Storage.name
    ).all()

    return render_template("storage.html", locations=storages)


@main.route("/storage/<int:storage_id>", methods=["GET", "POST"])
def storage_detail(storage_id):

    storage = Storage.query.get_or_404(storage_id)

    if request.method == "POST":

        section_name = request.form.get("section_name")

        if storage.uses_sections and section_name:

            new_section = StorageSection(
                name=section_name,
                storage_id=storage.id
            )

            db.session.add(new_section)
            db.session.commit()

            return redirect(
                url_for(
                    "main.storage_detail",
                    storage_id=storage.id
                )
            )

    return render_template(
        "storage_detail.html",
        storage=storage
    )

@main.route("/storage/<int:storage_id>/sections")
def get_storage_sections(storage_id):

    storage = Storage.query.get_or_404(storage_id)

    sections = []

    if storage.uses_sections:

        for section in storage.sections:

            sections.append(
                {
                    "id": section.id,
                    "name": section.name
                }
            )

    return jsonify(sections)

@main.route("/storage/delete/<int:storage_id>", methods=["POST"])
def delete_storage(storage_id):
    storage = Storage.query.get_or_404(storage_id)

    db.session.delete(storage)
    db.session.commit()

    return redirect(url_for("main.storage"))