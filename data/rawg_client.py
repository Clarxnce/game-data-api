"""
Client to retrieve Video Game Data from RAWG
"""

import requests
from dotenv import load_dotenv
import os

# Retrieve API Key
load_dotenv()
API_KEY = os.getenv("MY_API_KEY")

if not API_KEY:
    raise RuntimeError("MY_API_KEY is not set")

def get_field_data(field: str) -> dict:
    url = "https://api.rawg.io/api/" + field
    payload = {"key": API_KEY}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()