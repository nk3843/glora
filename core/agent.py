from langchain_ollama import ChatOllama
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import Chroma
from core.embedder import embedding_model

def get_chat_chain():
    vectorstore = Chroma(
        persist_directory="embeddings/chroma_index",
        embedding_function=embedding_model
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    llm = ChatOllama(model="mistral")  # This is where it failed

    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
