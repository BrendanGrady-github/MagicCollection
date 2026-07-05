# Application Architecture

## Scryfall

Scryfall is the source of information for:

- Card Name
- Mana Cost
- Oracle Text
- Card Images
- Colors
- Types
- Prices
- Set Information
- Collector Number
- Artist
- Legality
- Rarity

The local database should NOT duplicate this information unless caching is required.

---

## Local Database

The local database stores only collection-specific information.

Each Collection Entry stores:

- Scryfall ID
- Quantity
- Storage Location
- Finish
- Condition
- Notes

---

## Storage

Storage locations are independent objects.

Examples:

- Bulk Drawer → White
- Bulk Drawer → Blue
- Rare Binder → White
- Protected Binder → High Value

---

## Application Workflow

Search Card

↓

Choose Printing

↓

Choose Finish

↓

Choose Storage

↓

Save Collection Entry