from services.llm_client import ask_llm

def suggest(activity: str, preferences: str):
    prompt = f"""
    Активность: {activity}
    Предпочтения: {preferences}
    Что взять из еды?
    """
    return ask_llm(prompt)
