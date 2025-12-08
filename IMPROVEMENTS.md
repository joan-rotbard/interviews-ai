# Critical Improvements Needed

Based on the README's 4 issues, here are the prioritized improvements:

## 🔴 CRITICAL (Performance & Cost)

### 1. **Vectorstore Recreation** (Performance)
- **Issue**: `retrieval.py` recreates the ChromaDB connection on every query
- **Impact**: Massive performance hit - database initialization is expensive
- **Fix**: Initialize vectorstore once, reuse across queries

### 2. **Model Name Error** (Cost)
- **Issue**: `generation.py` uses `model="gpt-5.1"` which doesn't exist
- **Impact**: Will fail or use wrong/expensive model
- **Fix**: Use `gpt-4o` or `gpt-3.5-turbo` (cheaper)

### 3. **Excessive Retrieval** (Cost & Accuracy)
- **Issue**: Retrieving k=20 documents sends too many tokens to LLM
- **Impact**: High API costs, includes irrelevant context
- **Fix**: Reduce to k=5-8, add relevance filtering

## 🟡 HIGH PRIORITY (Security & Accuracy)

### 4. **Collection Name Mismatch** (Security)
- **Issue**: `ingest.py` uses `collection_name="documents"` but `retrieval.py` doesn't specify it
- **Impact**: May access wrong collection or fail
- **Fix**: Use consistent collection name in retrieval

### 5. **Hardcoded Paths** (Security)
- **Issue**: Hardcoded `"./chroma_db"` path
- **Impact**: Not configurable, security risk
- **Fix**: Use environment variable or config

### 6. **No Input Validation** (Security)
- **Issue**: User input not sanitized
- **Impact**: Potential injection attacks
- **Fix**: Add input validation/sanitization

### 7. **Basic Prompt** (Accuracy)
- **Issue**: Simple prompt without anti-hallucination instructions
- **Impact**: Model may hallucinate or give irrelevant answers
- **Fix**: Add system message with instructions to only use context, cite sources

## 🟢 MEDIUM PRIORITY (Polish)

### 8. **Graph Reinitialization** (Performance)
- **Issue**: Graph rebuilt on every query in `main.py`
- **Impact**: Minor performance hit
- **Fix**: Initialize once, reuse

### 9. **Error Handling** (Security)
- **Issue**: Exception messages may leak sensitive info
- **Impact**: Information disclosure
- **Fix**: Use generic error messages

### 10. **No Source Citations** (Accuracy)
- **Issue**: Can't verify where answers come from
- **Impact**: Lower trust, harder to debug
- **Fix**: Return document sources with answers

