from services.llm_client import ask_llm

def ask_gpt(prompt: str) -> str:
    """
    Отправка запроса к MPT-7B-Instruct и возврат текста.
    """
    return ask_llm(prompt)
