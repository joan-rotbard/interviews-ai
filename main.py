import os
from dotenv import load_dotenv
from src.graph import build_graph

load_dotenv()

def main():
    print("Initializing RAG Pipeline...")
    app = build_graph()

    while True:
        try:
            query = input("\nAsk a question (or 'q' to quit): ")
            if query.lower() == 'q':
                break
            
            inputs = {"question": query}
            
            final_answer = None
            
            retrieval_time = None
            
            for output in app.stream(inputs):
                for key, value in output.items():
                    print(f"Finished node: {key}")
                    if "answer" in value:
                        final_answer = value["answer"]
                    if "retrieval_time" in value:
                        retrieval_time = value["retrieval_time"]
            
            if final_answer:
                print(f"\nAnswer: {final_answer}")
                if retrieval_time is not None:
                    print(f"\nRetrieval took {retrieval_time:.3f} seconds.\n")
                else:
                    print()
            else:
                print("\nError: No answer generated.\n")
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
