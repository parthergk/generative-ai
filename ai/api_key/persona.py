from dotenv import load_dotenv;
from openai import OpenAI;

load_dotenv();

client = OpenAI();

system_prompt = """
You are an AI Persona Assistant named Gaurav Kumar
You are acting on behalf of Gaurav Kumar who is 25 years old Tech enthusistic and Full stack engineer.
Your main tech stack is JS and Python and You are laearning GenAI tese days.

Example:
Q. Hey
A. Hey, Whats up!
"""

response = client.chat.completions.create(
    model="gpt-5-mini",
     messages=[
        {"role":"system", "content": system_prompt},
        {"role": "user", "content": "Hey There"}
    ]
)

print(response.choices[0].message.content)