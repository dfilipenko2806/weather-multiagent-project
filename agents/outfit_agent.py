from services.llm_client import ask_llm

def get_outfit(activity: str, weather_desc: str) -> str:
    prompt = (
        f"User plans {activity}. "
        f"Weather: {weather_desc}. "
        "Suggest what to wear."
    )
    return ask_llm(prompt)
