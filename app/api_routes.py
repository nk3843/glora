from fastapi import APIRouter, Request
from app.schemas import QueryRequest, QueryResponse, ResultItem
from core.vectorstore import get_relevant_events

from app.schemas import ChatRequest, ChatResponse
from core.agent import get_chat_chain

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
def query_handler(payload: QueryRequest):
    print(f"🔍 Query: {payload.query}")
    
    paginated_docs, total_count = get_relevant_events(
        query=payload.query,
        k=payload.k,
        page=payload.page,
        page_size=payload.page_size
    )
    return QueryResponse(
        results=[
            ResultItem(text=doc.page_content, metadata=doc.metadata)
            for doc in paginated_docs
        ],
        total=total_count
    )



chat_chain = get_chat_chain()

@router.post("/chat")
def chat_endpoint(payload: dict):
    messages = payload.get("messages", [])

    # Extract the latest user message
    user_message = next((m["content"] for m in reversed(messages) if m["role"] == "user"), "")
    
    # Build chat history
    chat_history = []
    for msg in messages[:-1]:
        if msg["role"] == "user":
            chat_history.append((msg["content"], ""))
        elif msg["role"] == "assistant" and chat_history:
            chat_history[-1] = (chat_history[-1][0], msg["content"])

    # Run the chain
    result = chat_chain({
        "question": user_message,
        "chat_history": chat_history
    })

    return {"response": result["answer"]}

