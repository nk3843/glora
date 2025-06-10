from pydantic import BaseModel
from typing import List, Dict, Optional


class QueryRequest(BaseModel):
    query: str
    k: int = 5
    page: Optional[int] = 1
    page_size: Optional[int] = 10
    # 🚫 Filters removed for natural language querying only


class ResultItem(BaseModel):
    text: str
    metadata: Dict  # This holds fields like date, actor1, actor2, tone, year, etc.


class QueryResponse(BaseModel):
    results: List[ResultItem]
    total: Optional[int] = None  # For pagination client display

# 👇 Add at the bottom of schemas.py

class ChatMessage(BaseModel):
    role: str  # either "user" or "assistant"
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatMessage]

class ChatResponse(BaseModel):
    reply: str

