import os;
import json;
from dotenv import load_dotenv;

load_dotenv();
from google import genai;
from google.genai import types

gemini_key = os.getenv("GEMINI_API_KEY");

client = genai.Client(api_key=gemini_key);

system_prompt="""
You are an expert AI assistant in resolving user queries using chain of thought.
You work on START, PLAN, OUTPUT steps.
You need to first PLAN what needs to be done. The plan can be multiple steps.
Once you think enough plan done, finally you can give an OUTPUT.

Rules:
- Strictly follow the given json output format.
- Only run one step at a time.
- The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

Output JSON Format:
{"step": "START" | "PLAN" | "OUTPUT", "content": "string}

Example:
START: Hey, can you solve 2 + 3 * 5 / 10

PLAN: {"step":"PLAN","content":"Seems like the user is asking to solve a mathematical expression."}

PLAN: {"step":"PLAN","content":"Looking at the problem, we should follow the BODMAS order of operations."}

PLAN: {"step":"PLAN","content":"Multiplication and division have higher priority than addition."}

PLAN: {"step":"PLAN","content":"Evaluate from left to right: 3 * 5 = 15."}

PLAN: {"step":"PLAN","content":"Now the expression becomes 2 + 15 / 10."}

PLAN: {"step":"PLAN","content":"Perform division: 15 / 10 = 1.5."}

PLAN: {"step":"PLAN","content":"Now the expression becomes 2 + 1.5."}

PLAN: {"step":"PLAN","content":"Perform addition: 2 + 1.5 = 3.5."}

OUTPUT: {"step":"OUTPUT","content":"The answer is 3.5"}
"""

contents = [
types.Content(
    role="USER",
    parts=[types.Part(text="write a function to add n numbers")]
),
# types.Content(
#     role="MODEL",
#     parts=[types.Part(text=json.dumps({'step': 'START', 'content': "The user wants a function to add 'n' numbers."}))]
# ),
]

raw_res = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=contents,
    config= types.GenerateContentConfig(
        response_mime_type="application/json",
        system_instruction= system_prompt)
)

response = json.loads(raw_res.text)
print(response)