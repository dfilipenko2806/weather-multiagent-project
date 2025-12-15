from agents.gpt_agent import ask_gpt
from agents.utils import parse_numbered_list

def suggest_food(preferences: str):
    prompt = (
        f"The user dislikes: {preferences}. "
        "Suggest exactly 3-5 simple foods or snacks they can prepare or take. "
        "Each item must be ONE short phrase. "
        "Respond ONLY as a numbered list (1., 2., 3., ...), one item per line, no extra text. "
        "Example format:\n1. Bread\n2. Cheese\n3. Wine\nNow suggest foods:"
    )
    response = ask_gpt(prompt)
    foods = parse_numbered_list(response)
    return foods
