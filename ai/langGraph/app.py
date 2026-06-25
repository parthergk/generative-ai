from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Optional,  Literal
from openai import OpenAI
from langgraph.graph import StateGraph, END, START
load_dotenv()

client = OpenAI();

class State(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good: Optional[bool]

def llm_node(state:State):
    print("\n\nstate from the llm_node", state);
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role":"user", "content": state["user_query"]}
        ]
    )
    state["llm_output"] = response.choices[0].message.content;
    return state;

def output_check(state: State) -> Literal["llm_nodeA", "endnode"]:
    print("\n\nstate from output_check", state)
    if False:
        return "endnode"
    return "llm_nodeA"

def llm_nodeA(state:State):
    print("\n\nstate from llm_nodeA", state)
    state["llm_output"] = "new ouput after check in llm_nodeA"
    return state

def endnode(state:State):
    print("\n\nstate from in end node", state)
    return state

graph_builder = StateGraph(State);

graph_builder.add_node("llm_node", llm_node);
graph_builder.add_node("llm_nodeA", llm_nodeA);
graph_builder.add_node("endnode", endnode);

graph_builder.add_edge(START, "llm_node");

graph_builder.add_conditional_edges("llm_node", output_check)
graph_builder.add_edge("llm_nodeA", "endnode");
graph_builder.add_edge("endnode", END);

graph = graph_builder.compile();

updated_ouput = graph.invoke(State(user_query="Hi"))

print("\n\nupdated uptut", updated_ouput)