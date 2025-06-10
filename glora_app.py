import streamlit as st

st.set_page_config(page_title="GloRA - Global Retrieval Agent", layout="wide")

from explorer import render_explorer_ui
from chat_ui import render_chat_ui  # we'll build this next



mode = st.sidebar.radio("🧭 Select Mode", ["🧠 Chat", "🔎 Explore"])

if mode == "🔎 Explore":
    render_explorer_ui()
else:
    render_chat_ui()  # Coming soon
