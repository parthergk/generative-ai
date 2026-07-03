from typing import TypedDict, Literal
from typing_extensions import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    messages: list

def nodeA(state:State):
    print('\n\nstate in node A', state);
    return {"messages": ['hi how are you?']}

def nodeB(state:State) -> Literal["nodeC", "nodeEnd"]:
    print('\n\nstate in node B', state);
    if False:
        return "nodeC"
    return "nodeEnd"

def nodeC(state:State):
    print('\n\nstate in node C', state);
    return {"messages": ['how can i help you?']}
    

def nodeEnd(state:State):
    print('\n\nstate in node end', state)
    return{"messages": ['end of node']}

graph_builder = StateGraph(State);

graph_builder.add_node(nodeA)
graph_builder.add_node(nodeC)
graph_builder.add_node(nodeEnd)

graph_builder.add_edge(START, "nodeA")
graph_builder.add_conditional_edges("nodeA", nodeB)
graph_builder.add_edge("nodeC", "nodeEnd")
graph_builder.add_edge("nodeEnd", END)

graph = graph_builder.compile();

updated_state = graph.invoke(State({"messages": ["Hi"]}))
print("\n\nupdated state", updated_state);
