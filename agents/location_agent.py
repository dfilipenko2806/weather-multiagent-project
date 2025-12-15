from agents.gpt_agent import ask_gpt
from agents.utils import parse_numbered_list

def suggest_location(activities: list, city: str):
    activities_text = ", ".join(activities)
    prompt = (
        f"The user is in {city} and wants to do: {activities_text}. "
        "Suggest exactly 2-3 specific locations in the city. "
        "Each must be ONE short phrase. "
        "Respond ONLY as a numbered list (1., 2., 3., ...), one item per line, no extra text."
    )
    response = ask_gpt(prompt)
    locations = parse_numbered_list(response)
    return locations
