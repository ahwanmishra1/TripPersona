from crewai import Crew, Task
from agents.researcher import get_research_agent
from agents.planner import get_planner_agent
from agents.budget import get_budget_agent

def create_crew(source, destination, days, budget, people):

    researcher = get_research_agent()
    planner = get_planner_agent()
    budgeter = get_budget_agent()

    research_task = Task(
        description=f"Find top attractions in {destination}",
        agent=researcher,
        expected_output="List of attractions"
    )

    planning_task = Task(
        description=f"""
Create a {days}-day travel itinerary.

Trip Details:
From: {source}
To: {destination}
People: {people}
Budget: ₹{budget}

FORMAT (important but flexible):

For each day include:
- Morning activity
- Afternoon activity
- Evening activity
- Cost in INR

Example:

Day 1:
Morning: Beach visit
Afternoon: Lunch + sightseeing
Evening: Dinner
Cost: ₹1500

FINAL SUMMARY:
Total Cost: ₹XXXX
Cost Per Person: ₹XXXX

RULES:
- Always include Day-wise breakdown
- Always include cost per day
- Keep it structured and readable
""",
        agent=planner,
        expected_output="Structured itinerary"
    )

    budget_task = Task(
        description=f"Ensure the plan fits within ₹{budget}",
        agent=budgeter,
        expected_output="Optimized budget"
    )

    crew = Crew(
        agents=[researcher, planner, budgeter],
        tasks=[research_task, planning_task, budget_task],
        verbose=True
    )

    return crew