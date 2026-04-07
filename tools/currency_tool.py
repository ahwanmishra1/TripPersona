import os
import requests
from dotenv import load_dotenv

load_dotenv()

def convert_to_inr(amount, currency="USD"):
    try:
        key = os.getenv("EXCHANGE_RATE_API_KEY")

        url = f"https://v6.exchangerate-api.com/v6/{key}/latest/{currency}"
        res = requests.get(url, timeout=5).json()

        rate = res["conversion_rates"]["INR"]

        return amount * rate
    except:
        return amount