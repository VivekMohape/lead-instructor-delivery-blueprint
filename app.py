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

APP_DIR = Path(__file__).resolve().parent

# Accept either filename so the app works with the filename already in the GitHub repo
# or with the interview-specific filename from the provided package.
HTML_CANDIDATES = (
    APP_DIR / "lead_instructor_delivery_blueprint.html",
    APP_DIR / "lead_instructor_delivery_blueprint_interview.html",
)
HTML_FILE = next((path for path in HTML_CANDIDATES if path.is_file()), None)

if HTML_FILE is None:
    st.error("The blueprint HTML file is missing.")
    st.markdown(
        "Keep **app.py** and one of these HTML files in the same folder as the app:\n\n"
        "- `lead_instructor_delivery_blueprint.html`\n"
        "- `lead_instructor_delivery_blueprint_interview.html`"
    )
    st.stop()

html_content = HTML_FILE.read_text(encoding="utf-8")

# Render the self-contained HTML, including its CSS and JavaScript, in a scrollable iframe.
components.html(html_content, height=1000, scrolling=True)
