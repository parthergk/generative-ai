from openai import OpenAI;
from dotenv import load_dotenv;
import requests;
import json;
load_dotenv();

def getWeather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url);

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    return "Something went wrong!";

client = OpenAI();

tools = [
    {
        "type": "function",
        "function": {
            "name": "getWeather",
            "description": "Get the current weather of a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

messages = [{"role":'user', "content":'tell me the weather of delhi'}]

response = client.chat.completions.create(
    model= "gpt-5-mini",
    messages= messages,
    tools=tools
)

assistant_message = response.choices[0].message

messages.append(assistant_message)

tool_call = assistant_message.tool_calls[0];

city = json.loads(tool_call.function.arguments)["city"]

result = getWeather(city);

messages.append({
    "role": "tool",
    "tool_call_id" : tool_call.id,
    "content": result
})

output = client.chat.completions.create(
    model= "gpt-5-mini",
    messages= messages,
    tools=tools
)

print(output.choices[0].message.content)