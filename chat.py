import ollama

def chat(message):
    response = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {"role": "user", "content": message}
        ]
    )
    return response["message"]["content"]

user_input = input("You: ")
reply = chat(user_input)
print(f"Jarvis: {reply}")