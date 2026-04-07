from llm.ollama_llm import get_llm
from tools.weather_tool import get_weather

llm = get_llm()

def generate_plan(source, destination, days, people, budget):

    weather = get_weather(destination)

    prompt = f"""
Create a {days}-day travel plan.

From: {source}
To: {destination}
People: {people}
Budget: ₹{budget}

Weather:
{weather}

Keep it practical.
"""

    return llm.invoke(prompt)