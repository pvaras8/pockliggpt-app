# PockLigGPT Web

Landing page for **PockLigGPT**, a pocket-conditioned molecular generation framework based on GPT architectures and reinforcement learning for structure-based drug design.

---

## 🌐 Overview

This application provides a simple interface to:

- Present the PockLigGPT framework
- Link to the scientific publication and GitHub repository
- Offer collaboration opportunities
- Collect project requests from researchers and companies

---

## 🧬 Services

### 🔹 Option A — Target-based molecule generation
- Generation of candidate molecules conditioned on a protein pocket or PDB structure  
- Prioritized compound sets  
- Preliminary docking-based evaluation  

Ideal for exploratory studies and early-stage validation.

---

### 🔹 Option B — Full computational study
- Molecular generation  
- Advanced docking workflows  
- Rescoring (e.g., Glide)  
- Molecular dynamics simulations  
- Structural and interaction analysis  

Designed for deeper R&D collaborations and drug discovery projects.

---

## 🚀 Run locally

```bash
pip install -r requirements.txt
streamlit run app.py