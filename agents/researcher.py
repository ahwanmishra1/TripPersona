from crewai import Agent
from llm.ollama_llm import get_llm

def get_research_agent():
    return Agent(
        role="Travel Researcher",
        goal="Find best attractions for a destination",
        backstory="Knows all famous tourist places",
        llm=get_llm(),
        verbose=True
    )