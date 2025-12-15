from services.llm_client import ask_llm

def get_location(activity: str, city: str) -> str:
    prompt = (
        f"User plans {activity} in {city}. "
        "Suggest 2-3 suitable places in the city."
    )
    return ask_llm(prompt)
