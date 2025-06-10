from core.loader import load_gdelt_csv
from pipeline.formatter import format_event
from core.embedder import embed_texts
from core.vectorstore import get_vector_store

df = load_gdelt_csv("data/gdelt_events.csv", nrows=100)

# Format text
df["formatted"] = df.apply(format_event, axis=1)

# Prepare metadata
df["metadata"] = df.apply(lambda row: {
    "date": row["SQLDATE"].strftime("%Y-%m-%d"),
    "actor1": row["Actor1Name"],
    "actor2": row["Actor2Name"],
    "tone": row["AvgTone"]
}, axis=1)

# Embed text (optional: skip and let Chroma embed if you trust it)
texts = df["formatted"].tolist()
metadatas = df["metadata"].tolist()

# Store in vector DB
db = get_vector_store(texts, metadatas)

print("✅ Chroma index created with", len(texts), "documents.")
