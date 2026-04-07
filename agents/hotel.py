from llm.ollama_llm import get_llm
from tools.search_tool import search_places

llm = get_llm()

def suggest_hotel(destination, budget):

    search_data = search_places(f"best areas to stay in {destination}")

    prompt = f"""
Suggest where to stay in {destination}.

Budget: ₹{budget}

Context:
{search_data}

Give:
- Area
- Type
- Reason
"""

    return llm.invoke(prompt)