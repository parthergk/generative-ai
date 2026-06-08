import os;
import json;
from dotenv import load_dotenv;
load_dotenv();
from openai import OpenAI;

gemini_key = os.getenv("GEMINI_API_KEY");

client = OpenAI(
    api_key=gemini_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

system_prompt = """
You are a helpful AI assistant.

Always respond in JSON.

Format:

{
    "type": "plan",
    "content": "..."
}

or

{
    "type": "output",
    "content": "..."
}

Rules:
- Think step by step.
- Generate one plan at a time.
- When enough planning is done, return type=output.
- Never return anything outside the JSON.
"""

message_history = [
    {"role": "system", "content": system_prompt},
]

user_input = input("You: ");
message_history.append({"role": "user", "content": user_input});

while True:
    response = client.chat.completions.create(
        model= "gemini-3-flash-preview",
        messages= message_history,
        response_format={
        "type": "json_object"
    }
    )

    res_msg = response.choices[0].message.content
    print("Response", res_msg)