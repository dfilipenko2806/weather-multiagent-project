from agents.gpt_agent import ask_gpt
from agents.utils import parse_numbered_list

def suggest_outfit(activities: list, weather_text: str):
    activities_text = ", ".join(activities)
    prompt = (
        f"The user will do these activities: {activities_text}. "
        f"Weather: {weather_text}. Suggest exactly 3-5 clothing items (top, bottom, outerwear, shoes). "
        "Each item must be ONE short phrase. "
        "Respond ONLY as a numbered list (1., 2., 3., ...), one item per line, no extra text."
    )
    response = ask_gpt(prompt)
    outfit = parse_numbered_list(response)
    return outfit
