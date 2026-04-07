from llm.ollama_llm import get_llm

llm = get_llm()

def suggest_transport(source, destination, budget):

    prompt = f"""
Suggest best transport from {source} to {destination}.

Budget: ₹{budget}

Choose:
- Flight
- Train
- Road

Explain briefly.
"""

    return llm.invoke(prompt)