from langchain_openai import ChatOpenAI
from src.state import GraphState

def generation_node(state: GraphState):
    print("---GENERATION---")
    question = state["question"]
    context = state["context"]

    llm = ChatOpenAI(model="gpt-5.1", temperature=0)

    context_str = "\n\n".join(context)
    
    prompt = f"""
    Answer the question based on the context below:
    
    Context:
    {context_str}
    
    Question:
    {question}
    """

    response = llm.invoke(prompt)
    
    return {"answer": response.content}
