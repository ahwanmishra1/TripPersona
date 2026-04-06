from crewai import Agent
from llm.ollama_llm import get_llm

def get_planner_agent():
    return Agent(
        role="Travel Planner",
        goal="Create itinerary",
        backstory="Expert trip planner",
        llm=get_llm(),
        verbose=True
    )