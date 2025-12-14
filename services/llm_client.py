from openai import OpenAI
from config import LLM_MODEL

client = OpenAI()

def ask_llm(prompt: str):
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": "Ты полезный ассистент."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
