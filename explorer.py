# explorer.py
import streamlit as st
import requests

API_URL = "http://localhost:8000/query"

def highlight_metadata(text, metadata):
    def tone_emoji(tone_val):
        if tone_val > 2:
            return "🟢"
        elif tone_val < -2:
            return "🔴"
        else:
            return "🟡"

    for key in ["actor1", "actor2", "date"]:
        if key in metadata:
            val = str(metadata[key])
            if val in text:
                text = text.replace(val, f"**🧩 `{val}`**")

    if "tone" in metadata:
        tone_val = metadata["tone"]
        emoji = tone_emoji(tone_val)
        tone_str = f"{tone_val:.2f}"
        text = text.replace(str(tone_val), f"**🎯 `{tone_str}` {emoji}**")

    return text

def render_explorer_ui():

    if "query" not in st.session_state:
        st.session_state.query = ""
    if "page" not in st.session_state:
        st.session_state.page = 1
    if "page_size" not in st.session_state:
        st.session_state.page_size = 10

    with st.container():
        col1, col2, col3 = st.columns([4, 1, 1])
        with col1:
            st.session_state.query = st.text_input(
                "🔍 Enter your search query",
                placeholder="e.g., Violence in Pakistan or Democratic protest in Iran",
                value=st.session_state.query,
            )
        with col2:
            st.session_state.page_size = st.selectbox(
                "🔢 Page Size", [5, 10, 20],
                index=[5, 10, 20].index(st.session_state.page_size)
            )
        with col3:
            if st.button("🔎 Search"):
                st.session_state.page = 1  # Reset page on search
        with st.expander("💡 Need ideas? Click for example queries"):
            st.markdown("""
            Try these to explore:
            - `Violence in Pakistan`
            - `Protest in Iran`
            - `Attack on civilians in Nigeria`
            - `Military intervention in Ukraine`
            - `Police action in USA`
            """)

    if st.session_state.query:
        payload = {
            "query": st.session_state.query,
            "k": 100,
            "page": st.session_state.page,
            "page_size": st.session_state.page_size,
        }

        with st.spinner("Searching GDELT events..."):
            try:
                response = requests.post(API_URL, json=payload)
                response.raise_for_status()
                data = response.json()
                results = data.get("results", [])
                total = data.get("total", len(results))

                if not results:
                    st.warning("No results found.")
                else:
                    start = (st.session_state.page - 1) * st.session_state.page_size
                    for i, item in enumerate(results, start=start + 1):
                        st.markdown(f"### 🔹 Result {i}")
                        highlighted_text = highlight_metadata(item['text'], item['metadata'])
                        st.markdown(f"**Text**: {highlighted_text}")
                        st.json(item['metadata'])

                    total_pages = (total + st.session_state.page_size - 1) // st.session_state.page_size
                    col_prev, col_page, col_next = st.columns([1, 2, 1])

                    with col_prev:
                        if st.session_state.page > 1 and st.button("⬅️ Previous"):
                            st.session_state.page -= 1
                            st.rerun()
                    with col_page:
                        st.markdown(f"📄 Showing page **{st.session_state.page}** of **{total_pages}**")
                    with col_next:
                        if st.session_state.page < total_pages and st.button("Next ➡️"):
                            st.session_state.page += 1
                            st.rerun()

            except requests.exceptions.RequestException as e:
                st.error(f"❌ Error: {e}")

    st.markdown("---")
    st.caption("🔧 Powered by LangChain, ChromaDB, and GDELT · Built with ❤️ by Nikhil")
