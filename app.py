import streamlit as st
from converters import image, pdf

# Set page config
st.set_page_config(
    page_title="Universal File Converter",
    layout="wide",
    page_icon="🔄"
)

# Custom CSS styling
style = """
    <style>
        /* Main container */
        .main {            
            max-width: 1000px;
            padding: 2rem 1rem;
            margin: 0 auto;
        }
        
        /* Title styling */
        .title {
            text-align: center;
            margin-bottom: 2rem;
            font-size: 2.5rem;
            color: #1a237e;
        }
        
        /* Tabs styling */
        div[data-baseweb="tab-list"] {
            gap: 0.5rem;
            margin-bottom: 2rem;
        }
        
        div[data-baseweb="tab"] {
            padding: 0.75rem 1.5rem;
            border-radius: 8px !important;
            transition: all 0.3s ease;
            background: #f5f5f5;
        }
        
        div[data-baseweb="tab"]:hover {
            background: #e8eaf6 !important;
        }
        
        div[data-baseweb="tab"][aria-selected="true"] {
            background: #3f51b5 !important;
            color: white !important;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: #3f51b5 !important;
            transition: all 0.2s ease;
            border-radius: 8px !important;
        }
        
        .stButton>button:hover {
            transform: translateY(-1px);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        /* Footer styling */
        .footer {
            margin-top: 4rem;
            padding-top: 2rem;
            border-top: 1px solid #eee;
            text-align: center;
            color: #666;
        }
        
        .footer a {
            color: #3f51b5 !important;
            text-decoration: none;
            transition: color 0.2s ease;
        }
        
        .footer a:hover {
            color: #283593 !important;
            text-decoration: underline;
        }
    </style>
"""
st.markdown(style, unsafe_allow_html=True)

# Language selector in sidebar
lang = st.sidebar.selectbox("🌐 Interface Language", 
                           ["en", "de", "pl", "uk", "fr", "es"],
                           index=0)

# Main content
st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="title">🔄 Universal File Converter</div>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🖼️ Image Conversion", "📄 PDF Tools"])
with tab1:
    image.render()
with tab2:
    pdf.render()

# Footer
footer = '''
<div class="footer">
    <p>Created with ❤️ by <strong>Vasyl Madei</strong></p>
    <p>
        <a href="https://www.linkedin.com/in/vasyl-madei-399488247/" 
        target="_blank">Connect on LinkedIn</a> •
        <a href="https://github.com/yourprofile" target="_blank">View Source Code</a>
    </p>
</div>
</div>  <!-- Close main div -->
'''
st.markdown(footer, unsafe_allow_html=True)
