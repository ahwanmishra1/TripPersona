import ollama
from utils.personalities import get_personality_prompt
from memory import memory

def generate_personalities(base_plan, source, destination, people, budget):

    personalities = ["chaotic", "planner", "local"]
    outputs = {}

    for p in personalities:
        prompt = get_personality_prompt(
            p,
            f"""
Trip Context:
From: {source}
To: {destination}
People: {people}
Budget: ₹{budget}

{base_plan}
""",
            memory
        )

        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )

        outputs[p] = response["message"]["content"]

    return outputs