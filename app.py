import streamlit as st

st.set_page_config(page_title="PockLigGPT", layout="wide")

st.title("PockLigGPT")
st.subheader("AI-driven molecule generation for protein targets")

st.markdown("""
PockLigGPT is a pocket-conditioned molecular generation framework based on GPT architectures and reinforcement learning.

We offer two collaboration options:
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🧪 Option A — Target-based molecule generation")
    st.write("Generate candidate molecules for a given protein or PDB.")

with col2:
    st.markdown("### 🧬 Option B — Full computational study")
    st.write("End-to-end workflow including docking, scoring and simulations.")

st.divider()

FORM_URL = "https://forms.gle/ZhdqS3GGDu9By4Eh7"

st.header("Request collaboration")

st.markdown("""
We support both exploratory molecule generation and full computational drug discovery studies.

- ✔ Target-based molecule generation  
- ✔ Docking and scoring workflows  
- ✔ Molecular dynamics simulations  
- ✔ Structure-based analysis  

We will review your request and contact you shortly.
""")

st.link_button("🚀 Request collaboration", FORM_URL)