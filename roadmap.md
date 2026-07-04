# Magic Collection Inventory Roadmap

## Goal

Build a browser-based inventory app for my Magic: The Gathering collection.

## Core Features

- Add cards to my collection
- Track quantity
- Track exact storage location
- Track card printing using set code and collector number
- Search and filter cards
- Display card images from Scryfall
- Show card prices from Scryfall

## Physical Organization

### Bulk Drawer

Sections:
- White
- Blue
- Black
- Red
- Green
- Multicolor
- Lands
- Colorless
- Artifact

### Rare Binder

Sections:
- White
- Blue
- Black
- Red
- Green
- Lands / Multicolor / Artifacts / Colorless

### Protected Binder

Sections:
- High Value
- Personal Keepers

## Database Fields

Each collection entry should store:

- Card Name
- Quantity
- Storage Type
- Storage Section
- Set Code
- Collector Number
- Finish
- Condition
- Language
- Notes

## Scryfall Data

Scryfall will provide:

- Color
- Card Type
- Set Name
- Card Image
- Price
- Rarity
- Oracle Text

## Version 1

- Basic homepage
- Display collection table
- Add cards manually
- Store cards in SQLite database

## Version 2

- Search
- Filters
- Edit cards
- Delete cards

## Version 3

- Scryfall lookup
- Hover card images
- Prices

## Version 4

- CSV import/export
- Collection stats
- Deck tracking