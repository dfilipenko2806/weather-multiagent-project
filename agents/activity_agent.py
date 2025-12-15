from agents.gpt_agent import ask_gpt
from agents.utils import parse_numbered_list

def suggest_activity(weather_text: str):
    prompt = (
        f"The weather is {weather_text}. "
        "Suggest exactly 3-5 suitable evening activities. "
        "Each activity must be ONE short sentence. "
        "Respond ONLY as a numbered list (1., 2., 3., ...), one item per line, no extra text."
    )
    response = ask_gpt(prompt)
    activities = parse_numbered_list(response)
    return activities
