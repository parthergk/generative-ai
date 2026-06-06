import os
from dotenv import load_dotenv;

load_dotenv();
from google import genai

gemini_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=gemini_key)

response = client.models.generate_content(
    model= "gemini-2.5-flash", contents="do you remeber which question i asked you first"
)
print(response.text)