import time
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from src.state import GraphState

def retrieval_node(state: GraphState):
    print("---RETRIEVAL---")
    question = state["question"]

    start_time = time.time()
    
    vectorstore = Chroma(
        persist_directory="./chroma_db",
        embedding_function=OpenAIEmbeddings()
    )

    docs = vectorstore.similarity_search(question, k=20)
    
    retrieval_time = time.time() - start_time
    
    context = [doc.page_content for doc in docs]
    
    return {"context": context, "retrieval_time": retrieval_time}
