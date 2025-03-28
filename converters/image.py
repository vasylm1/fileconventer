
import streamlit as st
from PIL import Image
import io

def render():
    st.subheader("🖼️ Image Converter")
    uploaded_files = st.file_uploader("Upload image files", type=["jpg", "jpeg", "png", "webp", "gif"], accept_multiple_files=True)
    target_format = st.selectbox("Convert to format", ["JPG", "PNG", "WEBP", "GIF"])
    
    if uploaded_files:
        for uploaded_file in uploaded_files:
            if uploaded_file.size > 100 * 1024 * 1024:
                st.error(f"{uploaded_file.name} exceeds 100MB limit.")
                continue
            img = Image.open(uploaded_file)
            buffer = io.BytesIO()
            save_format = "JPEG" if target_format == "JPG" else target_format
            img.save(buffer, format=save_format)
            buffer.seek(0)
            st.download_button(label=f"Download {uploaded_file.name}.{target_format.lower()}",
                               data=buffer,
                               file_name=f"{uploaded_file.name}.{target_format.lower()}",
                               mime=f"image/{target_format.lower()}")
    