from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Lead Instructor Delivery Blueprint",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="collapsed",
)

APP_DIR = Path(__file__).resolve().parent
HTML_FILE = APP_DIR / "lead_instructor_delivery_blueprint.html"

# Keep the Streamlit shell minimal and give the embedded document the full viewport.
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
      iframe { border: 0 !important; display: block; width: 100%; }
    </style>
    """,
    unsafe_allow_html=True,
)

if not HTML_FILE.is_file():
    st.error("The blueprint HTML file is missing.")
    st.markdown(
        "Place **app.py** and **lead_instructor_delivery_blueprint.html** in the same folder."
    )
    st.stop()

html_content = HTML_FILE.read_text(encoding="utf-8")

# Keep the document inside a tall, independently scrollable iframe. This preserves
# the fixed sidebar, in-page navigation, checkboxes, tabs, search, theme and print controls.
components.html(html_content, height=1100, scrolling=True)
