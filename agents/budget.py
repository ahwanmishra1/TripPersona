from llm.ollama_llm import get_llm

llm = get_llm()

def breakdown_budget(destination, days, people, budget):

    prompt = f"""
Breakdown ₹{budget} for {people} people traveling to {destination} for {days} days.

Split:
- Travel
- Stay
- Food
- Activities
"""

    return llm.invoke(prompt)