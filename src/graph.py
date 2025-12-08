from langgraph.graph import StateGraph, END
from src.state import GraphState
from src.nodes.retrieval import retrieval_node
from src.nodes.generation import generation_node

def build_graph():
    workflow = StateGraph(GraphState)

    # Add nodes
    workflow.add_node("retrieval", retrieval_node)
    workflow.add_node("generation", generation_node)

    # Define the workflow
    workflow.set_entry_point("retrieval")
    workflow.add_edge("retrieval", "generation")
    workflow.add_edge("generation", END)

    return workflow.compile()
