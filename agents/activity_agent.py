from services.llm_client import ask_llm

def suggest(weather_summary: str):
    prompt = f"""
    Погода: {weather_summary}
    Предложи 3 варианта вечернего досуга.
    """
    return ask_llm(prompt)
