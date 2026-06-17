from openai import OpenAI;
from dotenv import load_dotenv;
load_dotenv()
import json

client = OpenAI();

def save_link(url, description, category):
    import json

    try:
        with open("links.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append({
        "url": url,
        "description": description,
        "category": category
    })

    with open("links.json", "w") as f:
        json.dump(data, f, indent=2)

    return "Link saved successfully"

def search_links(query):
    import json

    with open("links.json", "r") as f:
        data = json.load(f)

    matches = []

    for item in data:
        if query.lower() in json.dumps(item).lower():
            matches.append(item)

    return json.dumps(matches)

tools = [
    {
        "type": "function",
        "function": {
            "name": "save_link",
            "description": "Save a website link with its description and category for future retrieval.",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The website URL to save."
                    },
                    "description": {
                        "type": "string",
                        "description": "A short description of what the website is useful for."
                    },
                    "category": {
                        "type": "string",
                        "description": "Category of the link such as frontend, backend, AI, design, learning, tools, business, etc."
                    }
                },
                "required": ["url", "description", "category"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_links",
            "description": "Search previously saved links using keywords, category, website name, or description.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Keywords used to find matching saved links."
                    }
                },
                "required": ["query"]
            }
        }
    }
]

user_input = input();

messages=[
    {"role":"system", "content":"""You are a Personal Link Memory Agent.

Your job is to help users save, organize, and retrieve important links.

You have access to tools for:
1. Saving links.
2. Searching previously saved links.

Rules:

- When a user wants to save a link, ALWAYS use the save_link tool.
- When a user wants to find, search, recall, retrieve, or look up a previously saved link, ALWAYS use the search_links tool.
- Never claim a link is saved unless the save_link tool confirms success.
- Never invent links.
- Never make up search results.
- Always rely on tool results.

Saving Behavior:

If the user provides a URL and asks to save it, determine:
- URL
- Description
- Category

If the description is not explicitly provided, generate a short, useful description.

If the category is not provided, infer a category from the user's message.

Examples:

User:
"Save https://react.dev"

Tool Call:
save_link(
  url="https://react.dev",
  description="Official React documentation",
  category="frontend"
)

User:
"Remember this website for Tailwind animations"

Tool Call:
save_link(...)

Retrieval Behavior:

If the user asks things like:
- Find the React link I saved.
- Show my frontend resources.
- Search for AI tools.
- What links have I saved about Python?
- Find the website I bookmarked for animations.

ALWAYS use the search_links tool.

After receiving search results:
- Summarize clearly.
- Show URLs.
- Show descriptions when available.
- If no results are found, politely inform the user.

Organization Behavior:

Try to infer useful categories such as:
- frontend
- backend
- ai
- design
- devops
- database
- python
- javascript
- react
- learning
- tools
- productivity
- business
- finance

Response Style:

- Be concise.
- Be accurate.
- Prefer tool usage over assumptions.
- Never answer from memory when a tool can provide the information.
- Always use the available tools when relevant.

Your primary responsibility is to act as a searchable memory system for saved links."""
     },
     {
         "role": "user", "content": user_input
     }
]


respone = client.chat.completions.create(
    model="gpt-5-mini",
    messages=messages,
    tools=tools
)

assistant_message = respone.choices[0].message

messages.append(assistant_message);

tool_call = assistant_message.tool_calls[0]
print(tool_call.function)

if tool_call.function.name == "save_link":
    args = json.loads(tool_call.function.arguments)
    url = args["url"]
    description = args["description"]
    category = args["category"]

    result = save_link(url, description, category)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": result
    })
    output = client.chat.completions.create(
        model="gpt-5-mini",
        messages=messages,
        tools=tools
        )
    print(output.choices[0].message.content)
elif tool_call.function.name == "search_links": 
    query = json.loads(tool_call.function.arguments)["query"]
    result = search_links(query)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": result
    })
    output = client.chat.completions.create(
        model="gpt-5-mini",
        messages=messages,
        tools=tools
        )
    print(output.choices[0].message.content)