from services.llm_client import ask_llm

def suggest(city: str, activity: str):
    prompt = f"""
    Город: {city}
    Активность: {activity}
    Предложи подходящие места.
    """
    return ask_llm(prompt)
