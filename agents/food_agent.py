from services.llm_client import ask_llm

def get_food(activity: str, preferences: str, city: str) -> str:
    prompt = (
        f"User plans {activity} in {city}. "
        f"Food preferences: {preferences}. "
        "Suggest food options (short list)."
    )
    return ask_llm(prompt)
