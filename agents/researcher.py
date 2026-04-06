from crewai import Agent
from llm.ollama_llm import get_llm

def get_research_agent():
    return Agent(
        role="Travel Researcher",
        goal="Find best attractions",
        backstory="Knows all travel spots",
        llm=get_llm(),
        verbose=True
    )