# AI Engineer Interview Task: RAG Pipeline Repair

## Context
We built a quick internal RAG tool for employees to ask questions about company policies.
However, it has several major issues:
1. **Performance:** It's incredibly slow to retrieve answers.
2. **Cost:** Our API bills are skyrocketing.
3. **Accuracy:** Sometimes it gives irrelevant context or hallucinates.
4. **Security:** A security audit flagged it for multiple vulnerabilities.

## The Mission
Your goal is to **diagnose and fix** the most critical issues in the pipeline.
You have **45 minutes**.

Prioritize what you think will have the biggest impact. We value pragmatic engineering over perfection.

## Setup

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment:**
   - Copy `.env.example` to `.env`
   - Add your API Keys (provided in email).

3. **Ingest Data:**
   (This runs the one-time indexing of our documents)
   ```bash
   python ingest.py
   ```

4. **Run the App:**
   ```bash
   python main.py
   ```

## Repository Structure
- `data/`: Contains the raw text data.
- `src/graph.py`: The main LangGraph definition.
- `src/nodes/`: Individual graph nodes (Retrieval, Generation).
- `ingest.py`: Script for indexing data into the Vector DB.

## Good Luck!



