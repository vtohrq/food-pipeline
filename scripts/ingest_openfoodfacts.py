import requests
import json
import os
from datetime import datetime

BASE_URL = "https://world.openfoodfacts.org/api/v2/search"
OUTPUT_DIR = "data/raw"
PAGE_SIZE = 100
MAX_PAGES = 5

def fetch_products(category, page):

    params = {
        "categories_tags": category,
        "page_size": PAGE_SIZE,
        "page": page,
        "fields": "product_name,brands,categories,nutriments,countries,ingredients_text"
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()

def save_products(data, category, page):
    today = datetime.now().strftime("%Y-%m-%d")
    directory = f"{OUTPUT_DIR}/{category}/{today}"
    os.makedirs(directory, exist_ok=True)
    filename = f"{directory}/page_{page}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved: {filename}")

def main():
    categories = ["beverages", "dairies", "snacks"]
    for category in categories:
        print(f"Fetching category: {category}")
        for page in range(1, MAX_PAGES + 1):
            print(f"  Page {page}/{MAX_PAGES}")
            data = fetch_products(category, page)
            save_products(data, category, page)
            total = data.get("count", 0)
            print(f"  Total available: {total}")

if __name__ == "__main__":
    main()