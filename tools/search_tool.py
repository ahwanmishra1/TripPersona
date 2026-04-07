import os
import requests
from dotenv import load_dotenv

load_dotenv()

def search_places(query):
    try:
        url = "https://api.tavily.com/search"

        payload = {
            "api_key": os.getenv("TAVILY_API_KEY"),
            "query": query,
            "search_depth": "basic"
        }

        res = requests.post(url, json=payload, timeout=5)
        data = res.json()

        return data.get("results", [])[:3]
    except:
        return []