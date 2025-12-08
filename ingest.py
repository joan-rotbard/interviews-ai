import os
import glob
import shutil
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

def ingest_data():
    print("Loading data...")
    
    documents = []
    files = glob.glob("./data/**/*.txt", recursive=True)
    
    for file_path in files:
        print(f"Loading {file_path}...")
        loader = TextLoader(file_path)
        documents.extend(loader.load())

    print("Splitting text...")
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=5000,
        chunk_overlap=0
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks.")

    # Clear existing database if it exists to avoid corruption issues
    if os.path.exists("./chroma_db"):
        print("Clearing existing database...")
        shutil.rmtree("./chroma_db")

    print("Embedding and storing in Chroma...")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=OpenAIEmbeddings(),
        persist_directory="./chroma_db",
        collection_name="documents"
    )
    
    print("Ingestion complete!")

if __name__ == "__main__":
    ingest_data()
