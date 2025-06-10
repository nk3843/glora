# inspect_metadata.py
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Initialize embedding function
embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load vector store
db = Chroma(
    embedding_function=embedding_function,
    persist_directory="embeddings/chroma_index"
)

# Fetch 5 sample documents
retriever = db.as_retriever(search_kwargs={"k": 5})
docs = retriever.invoke("test")

# Print metadata
print("Inspecting sample metadata from ChromaDB...\n")
for i, doc in enumerate(docs):
    print(f"🔹 Document {i + 1}")
    print(f"Text: {doc.page_content}")
    print("Metadata:")
    for key, value in doc.metadata.items():
        print(f"  {key}: {value}")
    print("-" * 40)
