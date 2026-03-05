import os
from dotenv import load_dotenv

load_dotenv()
from openai import OpenAI

gemini_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=gemini_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

prompt="You are an export in coding and only and only answer the coding realted questions. Your name is groot. don't answer any other questions if question is not related to codign just say I am Groot."

respose = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role":"system", "content":prompt},
        {"role":"user", "content":"What are you doing today?"}
    ]
)

print(respose.choices[0].message.content)