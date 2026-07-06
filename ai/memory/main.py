import json
import os
from dotenv import load_dotenv
from mem0 import Memory
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

config = {
    "version": "v2.0.11",
    "embedder": {
        "provider": "openai",
        "config": {"api_key": OPENAI_API_KEY, "model": "text-embedding-3-small"}
    },
    "llm": {
        "provider": "openai",
        "config": {
            "api_key": OPENAI_API_KEY,
            "model": "gpt-4o-mini"
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {"host": "localhost", "port": 6333}
    }
}

client = OpenAI()
m = Memory.from_config(config)

while True:

    user_input = input("> ")

    saved_memory = m.search(query=user_input, filters={"user_id": "parther"});

    memories = [
    f"User_id: {mem.get('id')}\nMemory: {mem.get('memory')}"
    for mem in saved_memory["results"]
    ]
    print("saved memory:", memories)

    SYSTEM_PROMPT = f"""
    Here is the context about the user:
    {json.dumps(memories)}
    """
    response =  client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role":"user", "content": user_input}
        ]
    )

    ouput = response.choices[0].message.content
    print(ouput) 

    messages = [
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": ouput}
    ]

    m.add(messages, user_id="parther")
    print("memory saved....")