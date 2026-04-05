from agents.crew import create_crew

def run():
    destination = input("Destination: ")
    days = input("Days: ")
    budget = input("Budget: ")

    crew = create_crew(destination, days, budget)
    result = crew.kickoff()

    print("\n--- FINAL TRAVEL PLAN ---\n")
    print(result)

if __name__ == "__main__":
    run()