from services.llm_client import ask_llm

def suggest(weather: str, activity: str):
    prompt = f"""
    Погода: {weather}
    Активность: {activity}
    Что лучше надеть?
    """
    return ask_llm(prompt)
