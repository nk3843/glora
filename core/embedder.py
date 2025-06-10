# glora/core/embedder.py
from typing import List
from sentence_transformers import SentenceTransformer
import torch
from tqdm import tqdm
from langchain_huggingface import HuggingFaceEmbeddings

device = "mps" if torch.backends.mps.is_available() else "cpu"
model = SentenceTransformer("all-MiniLM-L6-v2", device=device)

# Initialize the embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': True}
)

def embed_texts(texts: List[str], batch_size: int = 64) -> List[List[float]]:
    embeddings = []
    for i in tqdm(range(0, len(texts), batch_size), desc="🔍 Embedding batches"):
        batch = texts[i:i+batch_size]
        batch_emb = model.encode(batch, batch_size=batch_size, show_progress_bar=False, convert_to_numpy=True)
        embeddings.extend(batch_emb)
    return embeddings