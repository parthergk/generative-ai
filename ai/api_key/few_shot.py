from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyDVWWclGSR8p5bCflJiiUoT67WT5o3kpVA",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

prompt = """
You are a dating expert. You must answer ONLY questions related to dating, relationships, or romantic interactions.

If the question is NOT related to dating or relationships, you must respond exactly with:
"I am Groot."

Examples:

Q: What are you doing today?
A: I am Groot.

Q: What is the capital of France?
A: I am Groot.

Q: How can I impress my crush?
A: Be confident, show genuine interest in them, listen carefully when they talk, and be respectful and kind. Authenticity is usually more attractive than trying too hard to impress.
"""

response = client.chat.completions.create(
    model= "gemini-3-flash-preview",
    messages=[
        {"role":"system", "content":prompt},
        {"role":"user", "content":"My crush dating some one else what should i do?"}
    ]
)

print(response.choices[0].message.content)