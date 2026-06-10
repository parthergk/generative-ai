import os;
from dotenv import load_dotenv;

load_dotenv()
from openai import OpenAI

client = OpenAI();

system_prompt="""You are an expert AI assistant in resolving user queries using chain of thought.
You work on START, PLAN, OUTPUT steps.
You need to first PLAN what needs to be done. The plan can be multiple steps.
Once you think enough plan done, finally you can give an OUTPUT.

Rules:
- Strictly follow the given json output format.
- Only run one step at a time.
- The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

Output JSON Format:
{"step": "PLAN" | "OUTPUT", "content": "string}

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

OUTPUT: {"step":"OUTPUT","content":"The answer is 3.5"}"""

reponse = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {"role":"system", "content":system_prompt},
        {"role":"user", "content":"solve this math problem 2+3*5/10"}
    ]
)

print(reponse.choices[0].message.content)