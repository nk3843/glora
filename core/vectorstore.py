from typing import List, Tuple, Dict
from datetime import datetime
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from core.embedder import embedding_model  # embedding_model must support .embed_documents and .embed_query


def save_to_vectorstore(texts: List[str], metadatas: List[Dict]):
    """
    Save a batch of texts and their metadata to the Chroma vectorstore.
    Adds 'year' field to metadata if date is present.
    """
    for metadata in metadatas:
        if "date" in metadata and isinstance(metadata["date"], str):
            try:
                metadata["year"] = datetime.strptime(metadata["date"], "%Y-%m-%d").year
            except ValueError:
                metadata["year"] = None

    Chroma.from_texts(
        texts=texts,
        embedding=embedding_model,
        metadatas=metadatas,
        persist_directory="embeddings/chroma_index"
    )


def get_relevant_events(
    query: str,
    k: int = 100,
    page: int = 1,
    page_size: int = 10
) -> Tuple[List[Document], int]:
    """
    Retrieve top-k semantically relevant events from the Chroma vectorstore using a natural language query.
    Supports pagination.
    """
    db = Chroma(
        embedding_function=embedding_model,
        persist_directory="embeddings/chroma_index"
    )

    retriever = db.as_retriever(search_kwargs={"k": k})
    all_results = retriever.invoke(query)

    start = (page - 1) * page_size
    end = start + page_size
    return all_results[start:end], len(all_results)
