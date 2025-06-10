import torch
print(torch.backends.mps.is_available())

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

db = Chroma(
    embedding_function=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
    persist_directory="embeddings/chroma_index"
)

print(db._collection.peek(3))  # returns list of dicts

