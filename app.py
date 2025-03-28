
import streamlit as st
from converters import image, pdf, excel, pptx

st.set_page_config(page_title="Universal File Converter", layout="wide")

st.markdown("# 🌐 Universal File Converter")
st.sidebar.markdown("### Theme")
theme = st.sidebar.radio("Choose Theme", ["Light", "Dark"])
st.markdown(
    f"<style>body {{ background-color: {'#ffffff' if theme == 'Light' else '#0f172a'}; color: {'#000' if theme == 'Light' else '#f1f5f9'}; }}</style>",
    unsafe_allow_html=True,
)

tab1, tab2, tab3, tab4 = st.tabs(["🖼️ Image", "📄 PDF", "📊 Excel", "📽️ PPTX"])

with tab1:
    image.render()

with tab2:
    pdf.render()

with tab3:
    excel.render()

with tab4:
    pptx.render()
