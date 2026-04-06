from crewai import Crew, Task
from agents.researcher import get_research_agent
from agents.planner import get_planner_agent
from agents.budgeter import get_budget_agent

def create_crew(source, destination, days, budget, people):

    researcher = get_research_agent()
    planner = get_planner_agent()
    budgeter = get_budget_agent()

    research_task = Task(
        description=f"""
Find top attractions in {destination}.
Consider travel from {source}.
""",
        agent=researcher,
        expected_output="List of attractions"
    )

    planning_task = Task(
        description=f"""
Create a {days}-day itinerary.

Trip Details:
From: {source}
To: {destination}
People: {people}
Budget: ₹{budget}

RULES:
- All costs in INR (₹)
- Include travel from {source} to {destination}
- Include per-person cost

FORMAT:

Day 1:
- Activity
- Cost: ₹XXX

Include:
Transport Plan
Hotel Recommendation
Total Cost (INR)
Cost Per Person
Travel Tips
""",
        agent=planner,
        expected_output="Structured itinerary"
    )

    budget_task = Task(
        description=f"""
Optimize the itinerary within ₹{budget} for {people} people.
Suggest cheaper alternatives if needed.
""",
        agent=budgeter,
        expected_output="Optimized budget plan"
    )

    crew = Crew(
        agents=[researcher, planner, budgeter],
        tasks=[research_task, planning_task, budget_task],
        verbose=True
    )

    return crew