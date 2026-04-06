from crewai import Agent
from llm.ollama_llm import get_llm

def get_budget_agent():
    return Agent(
        role="Budget Analyst",
        goal="Optimize cost",
        backstory="Cost optimization expert",
        llm=get_llm(),
        verbose=True
    )