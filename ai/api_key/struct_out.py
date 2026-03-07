import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


client = OpenAI(
    api_key= api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

prompt = """
You are a dating expert. You must answer ONLY questions related to dating, relationships, or romantic interactions.

If the question is NOT related to dating or relationships, you must respond exactly with:
"I am Groot."

- Strictly follow the output in JSON format

Output Format:
{{
"date": "string" or null,
"isDateingQuestion": boolean
}}

Examples:

Q: What are you doing today?
A: {{"date": "I am Groot.", "isDateingQuestion": false}}

Q: What is the capital of France?
A: {{"date": "I am Groot.", "isDateingQuestion": false}}

Q: How can I impress my crush?
A: {{"date": "Be confident, show genuine interest in them, listen carefully when they talk, and be respectful and kind. Authenticity is usually more attractive than trying too hard to impress.", "isDateingQuestion": true}}
"""

response = client.chat.completions.create(
    model= "gemini-3-flash-preview",
    messages = [
        {"role": "system", "content": prompt},
        {"role":"user", "content":"how can i improve the communication skill?"}
    ]
)

print(response.choices[0].message.content)