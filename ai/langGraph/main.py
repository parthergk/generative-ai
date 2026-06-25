from langgraph.graph.message import TypedDict, Annotated 
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    messages: Annotated[list, add_messages]

def nodeA (state: State):
    print("\n\ninside node a sate", state);
    return {"messages": ["Hi this is the message from the nodeA"]};

def nodeB(state: State):
    print("\n\ninside node b state", state);
    return {"messages": ["Hi this is the message of nodeB"]};

graph_builder = StateGraph(State);

graph_builder.add_node("nodeA", nodeA);
graph_builder.add_node("nodeB", nodeB);

graph_builder.add_edge(START, "nodeA");
graph_builder.add_edge("nodeA", "nodeB");
graph_builder.add_edge("nodeB", END);

graph = graph_builder.compile()

updated_state = graph.invoke(State({"messages":["hi how are you"]}))
print("\n\nupdated state", updated_state);