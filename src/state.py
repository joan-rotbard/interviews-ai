from typing import TypedDict, List, Optional

class GraphState(TypedDict):
    question: str
    context: List[str]
    answer: str
    retrieval_time: Optional[float]



