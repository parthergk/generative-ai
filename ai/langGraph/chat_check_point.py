from typing_extensions import TypedDict
from typing import Annotated
from openai import OpenAI
from dotenv import load_dotenv;
from langgraph.graph import StateGraph, START, END
load_dotenv();

client = OpenAI();

class State(TypedDict):
    messages: Annotated[list, "add_message"];

def chatBoat(state:State):
    print("State inside chatBoat", state)
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role":"user", "content": state["messages"]}
        ]
    )
    
    return {"messages": [response.choices[0].message.content]};

graph_builder = StateGraph(State);

graph_builder.add_node("chatBoat", chatBoat);
graph_builder.add_edge(START, "chatBoat");
graph_builder.add_edge("chatBoat", END);

graph = graph_builder.compile()

updated_state = graph.invoke(State({"messages": "Hi, my name is parther"}));
print("Update_State", updated_state);