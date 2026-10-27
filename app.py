from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Lead Instructor Delivery Blueprint",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Keep Streamlit's outer shell minimal so the embedded HTML can use the available width.
st.markdown(
    """
    <style>
      #MainMenu, footer, header { visibility: hidden; }
      [data-testid="stAppViewContainer"] > .main { padding-top: 0; }
      [data-testid="stMainBlockContainer"] {
        max-width: 100% !important;
        padding: 0 !important;
      }
      [data-testid="stVerticalBlock"] { gap: 0; }
      iframe { border: 0 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_FILE = Path(__file__).resolve().parent / "lead_instructor_delivery_blueprint_interview.html"

if not HTML_FILE.exists():
    st.error("The blueprint HTML file is missing. Keep app.py and the HTML file in the same folder.")
    st.stop()

html_content = HTML_FILE.read_text(encoding="utf-8")

# The blueprint is self-contained, including its CSS and JavaScript.
# A tall, scrollable iframe preserves the original layout and interactions.
components.html(
    html_content,
    height=1000,
    scrolling=True,
)
