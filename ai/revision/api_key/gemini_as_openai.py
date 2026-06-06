import os
from dotenv import load_dotenv;

load_dotenv();
from openai import OpenAI

gemini_ksy = os.getenv("GEMINI_API_KEY")
client = OpenAI(
    api_key=gemini_ksy,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model= "gemini-2.5-flash",
    messages= [
        {
            "role": "system",
            "content": "You are a girl whose name prachi"
        },
        {
            "role": "user",
            "content": "Do you rember what quesitoin i asked you before this: are you single"
        }
    ]
)

print(response.choices[0].message.content)