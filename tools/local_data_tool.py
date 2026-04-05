from crewai.tools import BaseTool
import json

class FetchPlacesTool(BaseTool):
    name: str = "Fetch Places Tool"
    description: str = "Fetch tourist places for a destination"

    def _run(self, destination: str) -> str:
        with open("data/places.json") as f:
            data = json.load(f)

        places = data.get(destination.lower(), [])
        return ", ".join(places) if places else "No data found"