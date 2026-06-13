from openai import OpenAI;
from dotenv import load_dotenv;
load_dotenv();
import json;
import subprocess


client = OpenAI();


def run_command(cmd):
    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )

    return result.stdout or result.stderr

tools =[
    {
        "type":"function",
        "function":{
            "name": "run_command",
            "description": "run the given command on the system",
            "parameters": {
                "type": "object",
                "properties":{
                    "cmd":{
                        "type": "string"
                    }
                },
                "required": ["cmd"]
            }
        }
    }
]


messages = [
   {
    "role": "system",
    "content": """
You are a Windows 11 command execution assistant.

When a user asks to perform an action on the computer, you MUST use the run_command tool.

Do not explain the command.
Do not ask for confirmation.
Do not answer in natural language before using the tool.
Immediately call the appropriate tool with the correct Windows command.

Only respond normally after receiving the tool result.
"""
},
    {
    "role":"user",
    "content":"Create a folder named parther."
}
]

response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=messages,
    tools=tools
)
assistant_message = response.choices[0].message
messages.append(assistant_message);

tool_call = assistant_message.tool_calls[0]
cmd = json.loads(tool_call.function.arguments)["cmd"]

result = run_command(cmd);

messages.append({
    "role": "tool",
    "tool_call_id": tool_call.id,
    "content": result
})

result = client.chat.completions.create(
    model="gpt-5-mini",
    messages=messages,
    tools=tools
)

print(result.choices[0].message.content)