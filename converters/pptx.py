
import streamlit as st
import os
import subprocess
import tempfile

def render():
    st.subheader("📽️ PPTX to PDF")
    uploaded_files = st.file_uploader("Upload PPTX files", type=["pptx"], accept_multiple_files=True)
    
    if uploaded_files:
        for uploaded_file in uploaded_files:
            if uploaded_file.size > 100 * 1024 * 1024:
                st.error(f"{uploaded_file.name} exceeds 100MB limit.")
                continue

            with tempfile.TemporaryDirectory() as tmpdir:
                pptx_path = os.path.join(tmpdir, uploaded_file.name)
                pdf_path = pptx_path.replace(".pptx", ".pdf")

                with open(pptx_path, "wb") as f:
                    f.write(uploaded_file.read())

                try:
                    subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", pptx_path, "--outdir", tmpdir], check=True)
                    with open(pdf_path, "rb") as pdf_file:
                        st.download_button("Download PDF", pdf_file.read(), file_name=os.path.basename(pdf_path), mime="application/pdf")
                except Exception as e:
                    st.error(f"Conversion failed: {e}")
    