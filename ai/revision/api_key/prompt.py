import os
from dotenv import load_dotenv;

load_dotenv();
from openai import OpenAI

gemini_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=gemini_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages= [
        {
            "role": "system",
            "content":"you are a coder! only ansers coding related question. say sorry if question not related to coding."
        },
        {
            "role": "user",
            "content":"Hy can you write a love latter"
        }
    ]
)

print(response.choices[0].message.content)