import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(city):
    try:
        key = os.getenv("OPENWEATHERMAP_API_KEY")

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"

        res = requests.get(url, timeout=5).json()

        return f"{res['weather'][0]['description']}, {res['main']['temp']}°C"
    except:
        return "Weather data unavailable"