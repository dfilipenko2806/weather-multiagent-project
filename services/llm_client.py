from gpt4all import GPT4All
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "mpt-7b-instruct.Q4_0.gguf")

# CPU only
llm = GPT4All(model_name=MODEL_PATH, allow_download=False, n_threads=os.cpu_count())

def ask_llm(prompt: str) -> str:
    try:
        response = llm.generate(prompt)
        if hasattr(response, "text"):
            return response.text.strip()
        elif isinstance(response, str):
            return response.strip()
        elif isinstance(response, list) and len(response) > 0:
            return response[0].get("text", "").strip()
        else:
            return str(response)
    except Exception as e:
        return f"Error running GPT4All: {e}"
