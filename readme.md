# Magic Collection Inventory

A Flask web application for managing a personal Magic: The Gathering collection using the Scryfall API.

## Project Goal

This app is designed to track my physical Magic: The Gathering collection by storing only the information unique to my collection, while using Scryfall as the source of truth for official card data.

## Core Ideas

- Store collection-specific data locally
- Use Scryfall for card names, images, printings, prices, and Oracle text
- Track exact storage locations
- Support multiple printings and multiple locations for the same card
- Eventually allow card selection by artwork instead of manually entering set codes or collector numbers

## Current Features

- Flask application setup
- SQLite database using SQLAlchemy
- Normalized storage/location database design
- Scryfall API connection
- Custom User-Agent for API requests
- Git/GitHub project workflow

## Planned Features

- Add Card workflow
- Scryfall-powered card search
- Printing and artwork selection
- Collection browser
- Search and filters
- Hover card image previews
- Storage management
- Collection statistics
- Estimated collection value

## Tech Stack

- Python
- Flask
- SQLite
- SQLAlchemy
- HTML
- CSS
- Scryfall API
- Git/GitHub

## Status

Early development.