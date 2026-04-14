import streamlit as st

# Config
st.set_page_config(page_title="PockLigGPT", layout="wide")

FORM_URL = "https://forms.gle/ZhdqS3GGDu9By4Eh7"

# ===== HEADER =====
col_logo, col_title = st.columns([1, 4])

with col_logo:
    st.image("logo.png", width=120)

with col_title:
    st.title("PockLigGPT")
    st.markdown("### AI-driven molecule generation for protein targets")

st.markdown("""
PockLigGPT is a pocket-conditioned molecular generation framework based on GPT architectures and reinforcement learning.
""")

st.divider()

# ===== SERVICES =====
st.markdown("## What we offer?")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🧪 Target-based molecule generation
    
    Generate candidate molecules conditioned on a protein pocket or PDB structure.
    
    - ✔ Molecule generation  
    - ✔ Prioritization  
    - ✔ Preliminary docking  
    
    Ideal for exploratory studies.
    """)

with col2:
    st.markdown("""
    ### 🧬 Full computational study
    
    End-to-end computational drug discovery workflow.
    
    - ✔ Advanced docking  
    - ✔ Rescoring (e.g., Glide)  
    - ✔ Molecular dynamics  
    - ✔ Structural analysis  
    
    Designed for deeper R&D collaborations.
    """)

st.divider()

# ===== CTA =====
st.markdown("## 🚀 Request collaboration")

st.markdown("""
We collaborate with academic and industry partners in early-stage drug discovery.

Submit your project and we will review it and get back to you shortly.
""")

st.link_button("🚀 Submit request", FORM_URL)

st.markdown("---")

# ===== FOOTER =====
st.markdown("""
<small>
PockLigGPT • AI for structure-based drug discovery  
</small>
""", unsafe_allow_html=True)