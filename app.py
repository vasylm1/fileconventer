
import streamlit as st
from converters import image, pdf

# Set defaults in session state
if "theme" not in st.session_state:
    st.session_state.theme = "light"
if "lang" not in st.session_state:
    st.session_state.lang = "en"

def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# Apply theme styles
if st.session_state.theme == "dark":
    background = "#0f172a"
    text_color = "#f1f5f9"
    button_color = "#2563eb"
else:
    background = "#ffffff"
    text_color = "#000000"
    button_color = "#3b82f6"

st.markdown(f"""
    <style>
        body {
            background-color: {background};
            color: {text_color};
        }
        .stButton>button {
            background-color: {button_color};
            color: white;
        }
        .stFileUploader, .stSelectbox {
            background-color: {background};
            color: {text_color};
        }
        .footer {
            margin-top: 4rem;
            text-align: center;
            font-size: 0.9rem;
            color: {text_color};
        }
        .footer a {
            color: {button_color};
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar options
st.sidebar.button("🌙 Dark Mode" if st.session_state.theme == "light" else "☀️ Light Mode", on_click=toggle_theme)
lang = st.sidebar.selectbox("🌐 Interface Language", ["en", "de", "pl", "uk", "fr", "es"], index=["en", "de", "pl", "uk", "fr", "es"].index(st.session_state.lang))
st.session_state.lang = lang

# Set page and tabs
st.set_page_config(page_title="Universal File Converter", layout="wide")
st.markdown(f"# 🌐 Universal File Converter ({st.session_state.theme.title()} Theme)")

tab1, tab2 = st.tabs(["🖼️ Image", "📄 PDF"])
with tab1:
    image.render()
with tab2:
    pdf.render()

# Footer
st.markdown('\n<div class="footer">\n    <p>Created by <strong>Vasyl Madei</strong></p>\n    <p><a href="https://www.linkedin.com/in/vasyl-madei-399488247/" target="_blank">Vasyl Madei on LinkedIn</a></p>\n</div>\n', unsafe_allow_html=True)
