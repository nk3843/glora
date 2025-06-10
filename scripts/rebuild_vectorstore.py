# glora/scripts/rebuild_vectorstore.py
import pandas as pd
from core.vectorstore import save_to_vectorstore
from tqdm import tqdm

print("📦 Loading CSV...")
df = pd.read_csv("data/gdelt_events.csv", low_memory=False)

print("🧹 Cleaning data...")
df = df.dropna(subset=["SQLDATE", "Actor1Name", "Actor2Name", "EventCode", "AvgTone", "NumMentions"])
df["EventCode"] = pd.to_numeric(df["EventCode"], errors="coerce")
df["AvgTone"] = pd.to_numeric(df["AvgTone"], errors="coerce")
df["NumMentions"] = pd.to_numeric(df["NumMentions"], errors="coerce")
df = df.dropna(subset=["EventCode", "AvgTone", "NumMentions"])

df["date"] = pd.to_datetime(df["SQLDATE"], format="%Y%m%d", errors="coerce")
df = df.dropna(subset=["date"])
df["year"] = df["date"].dt.year

texts, metadatas = [], []

print(f"📝 Formatting {len(df)} rows...")
for _, row in tqdm(df.iterrows(), total=len(df)):
    try:
        text = f"{row['date'].date()}: Event {int(row['EventCode'])} between {row['Actor1Name']} and {row['Actor2Name']}. Tone: {round(row['AvgTone'], 2)}, Mentions: {int(row['NumMentions'])}."
        metadata = {
            "actor1": row["Actor1Name"],
            "actor2": row["Actor2Name"],
            "tone": round(row["AvgTone"], 2),
            "date": row["date"].strftime("%Y-%m-%d"),
            "year": int(row["year"]),
        }
        texts.append(text)
        metadatas.append(metadata)
    except Exception as e:
        continue

print("💾 Saving to Chroma vectorstore...")
save_to_vectorstore(texts, metadatas)
print(f"✅ Done! Saved {len(texts)} documents.")
