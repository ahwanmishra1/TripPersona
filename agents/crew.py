from crewai import Crew, Task
from agents.researcher import get_research_agent
from agents.planner import get_planner_agent
from agents.budgeter import get_budget_agent

def create_crew(destination, days, budget):

    researcher = get_research_agent()
    planner = get_planner_agent()
    budgeter = get_budget_agent()

    research_task = Task(
        description=f"""
            Find top attractions in {destination}.
            Use general knowledge of popular tourist places.
            """,
        agent=researcher,
        expected_output="List of attractions"
    )

    planning_task = Task(
        description=f"""
            Create a {days}-day itinerary for {destination}.

            STRICT FORMAT:

            Day 1:
            - Place 1
            - Place 2

            Day 2:
            - Place 3
            - Place 4

            Also include:
            Hotel Recommendation:
            Travel Tips:
            """,
        agent=planner,
        expected_output="Structured itinerary"
    )

    budget_task = Task(
        description=f"Adjust the itinerary to fit within {budget}",
        agent=budgeter,
        expected_output="Optimized plan within budget"
    )

    crew = Crew(
        agents=[researcher, planner, budgeter],
        tasks=[research_task, planning_task, budget_task],
        verbose=True
    )

    return crew