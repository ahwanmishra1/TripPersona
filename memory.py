memory = {
    "avoid": [],
    "prefer": []
}

def update_memory(feedback: str):
    feedback = feedback.lower()

    if "skip" in feedback or "avoid" in feedback:
        memory["avoid"].append(feedback)

    if "prefer" in feedback or "like" in feedback:
        memory["prefer"].append(feedback)