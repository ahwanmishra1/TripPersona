from llm.ollama_llm import get_llm

llm = get_llm()

def apply_personality(text):

    prompt = f"""
Rewrite this into 3 styles:

CHAOTIC:
fun, spontaneous

PLANNER:
structured

LOCAL:
hidden gems

TEXT:
{text}

Separate clearly.
"""

    return llm.invoke(prompt)