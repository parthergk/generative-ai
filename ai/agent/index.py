from openai import OpenAI
from dotenv import load_dotenv
load_dotenv();
import requests;
import json;

client = OpenAI();

def getWeather(city):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    rslt = requests.get(url)
    if rslt.status_code == 200:
        return rslt.text
    return "Something went wrong!"

tools = [
{
    "type": "function",
    "function": {
        "name": "getWeather",
        "description": "Get the current weaterh of a city",
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

city_input = input("Enter a City: ");

message = [
{"role": "user", "content": f"tell me the current weather of {city_input}"}
]

response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=message,
    tools=tools,
)

assistant_message = response.choices[0].message
print("assistant", assistant_message);
message.append(assistant_message)

tool_calls = assistant_message.tool_calls[0]

city = json.loads(tool_calls.function.arguments)["city"]

result = getWeather(city);

message.append({"role": "tool", "tool_call_id": tool_calls.id, "content": result})

output = client.chat.completions.create(
    model="gpt-5-mini",
    messages=message,
    tools=tools,
)

# print(output.choices[0].message.content)
print("output", output.choices[0].message);