
import streamlit as st
import fitz  # PyMuPDF
from gtts import gTTS
from docx import Document
import io

def render():
    st.subheader("📄 PDF Converter")
    uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)
    target_format = st.selectbox("Convert to format", ["TXT", "MP3", "DOCX"])

    lang_code = "en"
    if target_format == "MP3":
        lang_code = st.selectbox("Select voice language", [
            "en", "de", "pl", "uk", "fr", "es"
        ], format_func=lambda code: {
            "en": "English",
            "de": "German",
            "pl": "Polish",
            "uk": "Ukrainian",
            "fr": "French",
            "es": "Spanish"
        }.get(code, code))

    if uploaded_files:
        for uploaded_file in uploaded_files:
            if uploaded_file.size > 100 * 1024 * 1024:
                st.error(f"{uploaded_file.name} exceeds 100MB limit.")
                continue

            with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
                text = ""
                for page in doc:
                    text += page.get_text()

            if target_format == "TXT":
                st.download_button("Download TXT", text, file_name=uploaded_file.name.replace(".pdf", ".txt"))
            elif target_format == "MP3":
                tts = gTTS(text, lang=lang_code)
                buffer = io.BytesIO()
                tts.write_to_fp(buffer)
                buffer.seek(0)
                st.download_button("Download MP3", buffer, file_name=uploaded_file.name.replace(".pdf", ".mp3"), mime="audio/mpeg")
            elif target_format == "DOCX":
                docx_file = io.BytesIO()
                document = Document()
                document.add_paragraph(text)
                document.save(docx_file)
                docx_file.seek(0)
                st.download_button("Download DOCX", docx_file, file_name=uploaded_file.name.replace(".pdf", ".docx"), mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
