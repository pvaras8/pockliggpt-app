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

st.header("Request collaboration")

with st.form("form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    service = st.selectbox("Service", ["Molecule generation", "Full study"])
    pdb = st.text_input("PDB / Target")
    desc = st.text_area("Project description")

    submit = st.form_submit_button("Send")

if submit:
    st.success("We will contact you soon.")