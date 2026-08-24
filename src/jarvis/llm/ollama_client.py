# src/jarvis/llm/ollama_client.py
import ollama

class OllamaClient:
    def __init__(self, model_name):
        self.model_name = model_name

    def chat(self, user_text):
        response = ollama.chat(
            model=self.model_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are a voice assistant named Jarvis. Respond briefly and naturally."
                },
                {"role": "user", "content": user_text},
            ],
            options={"num_predict": 300},
        )
        return response["message"]["content"]