from langgraph.graph import StateGraph
from agent.state import AgentState
from agent.nodes import intent_node, response_node

def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("intent_node", intent_node)
    builder.add_node("response_node", response_node)

    builder.set_entry_point("intent_node")

    builder.add_edge("intent_node", "response_node")

    return builder.compile()