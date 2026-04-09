import requests 
import os 
import json 
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

URL_BASE = "https://real-time-amazon-data.p.rapidapi.com/search"
COUNTRY = "US"
MAX_PAGES = 5

def extrair(query, page):
    params = {
        "query": query,
        "page": page,
        "country": COUNTRY
    }
    headers = {
        "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
        "x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
    }
    response = requests.get(URL_BASE, params=params, headers=headers)
    response.raise_for_status()
    return response.json()

def salvar(data, query, page):
    today = datetime.now().strftime("%Y-%m-%d")
    directory = f"data/raw/amazon/{query}/{today}"
    os.makedirs(directory, exist_ok=True)

    filename = f"{directory}/page_{page}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Salvo em: {filename}")

def main():
    queries = ["laptop", "smartphone", "headphones", "tablet", "smart tv"]

    for query in queries:
        print(f"Buscando query: {query}")

        for page in range(1, MAX_PAGES + 1):
            print(f"  Página {page}/{MAX_PAGES}")

            data = extrair(query, page)
            salvar(data, query, page)

if __name__ == "__main__":
    main()