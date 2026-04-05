from crewai import Agent
from llm.ollama_llm import get_llm

def get_budget_agent():
    return Agent(
        role="Budget Analyst",
        goal="Ensure the travel plan fits within budget",
        backstory="Finance expert for travel planning",
        llm=get_llm(),
        verbose=True
    )