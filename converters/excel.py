
import streamlit as st
import pandas as pd
import io

def render():
    st.subheader("📊 Excel Converter")
    uploaded_files = st.file_uploader("Upload Excel files", type=["xls", "xlsx", "xlsb", "xlsm", "ods"], accept_multiple_files=True)
    target_format = st.selectbox("Convert to format", ["CSV", "TSV", "JSON", "XML"])
    
    if uploaded_files:
        for uploaded_file in uploaded_files:
            if uploaded_file.size > 100 * 1024 * 1024:
                st.error(f"{uploaded_file.name} exceeds 100MB limit.")
                continue

            df = pd.read_excel(uploaded_file)
            buffer = io.StringIO() if target_format in ["CSV", "TSV"] else io.BytesIO()

            if target_format == "CSV":
                df.to_csv(buffer, index=False)
                st.download_button("Download CSV", buffer.getvalue(), file_name=uploaded_file.name.replace(".xlsx", ".csv"))
            elif target_format == "TSV":
                df.to_csv(buffer, index=False, sep="\t")
                st.download_button("Download TSV", buffer.getvalue(), file_name=uploaded_file.name.replace(".xlsx", ".tsv"))
            elif target_format == "JSON":
                json_bytes = df.to_json(orient="records").encode()
                st.download_button("Download JSON", json_bytes, file_name=uploaded_file.name.replace(".xlsx", ".json"))
            elif target_format == "XML":
                xml = ['<root>']
                for _, row in df.iterrows():
                    xml.append('  <record>')
                    for field in df.columns:
                        xml.append(f'    <{field}>{row[field]}</{field}>')
                    xml.append('  </record>')
                xml.append('</root>')
                xml_data = "\n".join(xml)
                st.download_button("Download XML", xml_data, file_name=uploaded_file.name.replace(".xlsx", ".xml"))
    