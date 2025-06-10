# chat_ui.py
import streamlit as st
import requests

CHAT_API_URL = "http://localhost:8000/chat"

def render_chat_ui():
    # 🧠 Initialize session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # 🧭 Page config
    st.title("💬 GloRA - Conversational Agent")
    st.markdown("Ask me about global events. I remember the context of our conversation!")

    # 📜 Display chat history
    for role, content in st.session_state.chat_history:
        with st.chat_message("user" if role == "user" else "assistant"):
            st.markdown(content)

    # 💬 Handle new user input
    if prompt := st.chat_input("Type your question..."):
        st.session_state.chat_history.append(("user", prompt))

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.spinner("GloRA is thinking..."):
            try:
                messages = [{"role": r, "content": c} for r, c in st.session_state.chat_history]
                response = requests.post(CHAT_API_URL, json={"messages": messages})
                response.raise_for_status()
                answer = response.json().get("response", "🤖 Sorry, I couldn't find anything useful.")
            except Exception as e:
                answer = f"❌ Error: {e}"

        st.session_state.chat_history.append(("assistant", answer))
        with st.chat_message("assistant"):
            st.markdown(answer)
