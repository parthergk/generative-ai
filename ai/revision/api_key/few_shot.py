import os;
from dotenv import load_dotenv

load_dotenv()
from openai import OpenAI;

gemini_key = os.getenv("GEMINI_API_KEY");

client = OpenAI(
    api_key=gemini_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
);
prompt = """
You are a BCA graduated boy. and your giving an interview. if question not related to interview just say: Teri ma ka bhosda

Examples:

Question: Tell me about yourself.
Answer: I completed my BCA in 2023. I am learning React and Next.js.

Question: Why should we hire you?
Answer: I learn fast and work hard.

""";

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages= [
        {
            "role": "system",
            "content": prompt
        },
        {
            "role": "user",
            "content": "Are you single"
        }
    ]
)

print(response.choices[0].message.content)