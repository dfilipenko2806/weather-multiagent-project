from services.llm_client import ask_llm

def get_activity(weather_desc: str, city: str) -> str:
    prompt = (
        f"You are a personal assistant. User is in {city}. "
        f"Weather: {weather_desc}. "
        "Suggest 3 evening activities in a short list."
    )
    return ask_llm(prompt)
877
78k78k
yuuuj
