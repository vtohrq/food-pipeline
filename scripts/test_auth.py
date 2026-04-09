import requests 
import os 
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.mercadolibre.com/oauth/token"
CLIENT_ID = os.getenv("ML_CLIENT_ID")
SECRET = os.getenv("ML_CLIENT_SECRET")

response = requests.post(BASE_URL, data={
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": SECRET
})

print(response.json())