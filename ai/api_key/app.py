from google import genai

client = genai.Client(api_key="AIzaSyDVWWclGSR8p5bCflJiiUoT67WT5o3kpVA")

response = client.models.generate_content(
    model= "gemini-2.5-flash", contents = "How are you?"
)

print(response.text)