from typing_extensions import TypedDict
from typing import Annotated
from openai import OpenAI
from dotenv import load_dotenv;
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model;
from langgraph.graph.message import add_messages
from langgraph.checkpoint.mongodb import MongoDBSaver

load_dotenv();

llm = init_chat_model(
    model="gpt-5-mini",
    model_provider="openai"
)

class State(TypedDict):
    messages: Annotated[list, add_messages];

def chatBoat(state:State):
    response = llm.invoke(state.get("messages"))

    return { "messages": [response] } 

graph_builder = StateGraph(State);

graph_builder.add_node("chatBoat", chatBoat);
graph_builder.add_edge(START, "chatBoat");
graph_builder.add_edge("chatBoat", END);


def graph_with_check_pointer(checkpointer):
    graph = graph_builder.compile(checkpointer=checkpointer)
    return graph;

with MongoDBSaver.from_conn_string("mongodb://admin:admin@localhost:27017") as checkpointer:
    check_pointer_graph = graph_with_check_pointer(checkpointer)
    config = {
        "configurable":{
            "thread_id": "parther"
        }
    }
    for chunk in check_pointer_graph.stream(State({"messages": ["what is my name"]}), config, stream_mode="values"):
        chunk["messages"][-1].pretty_print()