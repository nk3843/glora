# from langchain_core.documents import Document
# from core.vectorstore import get_relevant_events

# query = "violent protests in Iran in 2022"

# results = get_relevant_events(query, k=5)

# for i, doc in enumerate(results, 1):
#     print(f"\n🔹 Result {i}")
#     print("Text:", doc.page_content)
#     print("Metadata:", doc.metadata)

from core.vectorstore import get_relevant_events

docs, total = get_relevant_events("violence in Pakistan")
for doc in docs:
    print(doc.page_content)

