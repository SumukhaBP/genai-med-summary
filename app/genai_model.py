import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(text: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful medical assistant."},
            {"role": "user", "content": f"Summarize this medical report: {text}"}
        ]
    )
    return response.choices[0].message['content']