from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def ask_llm(prompt: str) -> str:
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"LLM error: {e}"
yfmuyf
y8uky8k
