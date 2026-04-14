import streamlit as st

# =========================
# Config
# =========================
st.set_page_config(
    page_title="PockLigGPT",
    page_icon="🧬",
    layout="wide",
)

FORM_URL = "https://forms.gle/ZhdqS3GGDu9By4Eh7"
GITHUB_URL = "https://github.com/pvaras8/PockLigGPT"

# =========================
# Estilo
# =========================
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1100px;
    }

    .hero-title {
        text-align: center;
        font-size: 3.2rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }

    .hero-subtitle {
        text-align: center;
        font-size: 1.35rem;
        font-weight: 600;
        color: #4b5563;
        margin-bottom: 1.2rem;
    }

    .hero-text {
        text-align: center;
        font-size: 1.05rem;
        color: #374151;
        max-width: 850px;
        margin: 0 auto 1.8rem auto;
        line-height: 1.7;
    }

    .section-title {
        font-size: 2rem;
        font-weight: 750;
        margin-top: 0.5rem;
        margin-bottom: 1rem;
    }

    .card {
        background: #f8fafc;
        border: 1px solid #e5e7eb;
        border-radius: 18px;
        padding: 1.4rem 1.4rem 1.1rem 1.4rem;
        min-height: 320px;
    }

    .card h3 {
        margin-top: 0.2rem;
        margin-bottom: 0.8rem;
        font-size: 1.6rem;
    }

    .card p, .card li {
        font-size: 1rem;
        line-height: 1.7;
        color: #374151;
    }

    .cta-box {
        background: linear-gradient(180deg, #fafafa 0%, #f5f7fb 100%);
        border: 1px solid #e5e7eb;
        border-radius: 18px;
        padding: 1.5rem 1.5rem 1.2rem 1.5rem;
    }

    .small-note {
        color: #6b7280;
        font-size: 0.95rem;
        margin-top: 0.8rem;
    }

    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 0.9rem;
        margin-top: 2rem;
    }

    div[data-testid="stLinkButton"] a {
        background-color: #111827 !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 0.75rem 1.1rem !important;
        border: none !important;
        font-weight: 600 !important;
        text-decoration: none !important;
    }

    div[data-testid="stLinkButton"] a:hover {
        background-color: #1f2937 !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================
# Header
# =========================
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.image("logo.png", width=260)

st.markdown('<div class="hero-title">PockLigGPT</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-subtitle">AI-driven molecular design for structure-based drug discovery</div>',
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="hero-text">
    PockLigGPT is a pocket-conditioned molecular generation framework based on GPT architectures
    and reinforcement learning. It supports target-guided compound generation and can be used
    as an entry point for broader computational drug discovery studies.
    </div>
    """,
    unsafe_allow_html=True,
)

b1, b2, b3 = st.columns([1.2, 1, 1.2])
with b2:
    st.link_button("View GitHub", GITHUB_URL)

st.divider()

# =========================
# Servicios
# =========================
st.markdown('<div class="section-title">What we offer</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown(
        """
        <div class="card">
            <h3>🧪 Target-based molecule generation</h3>
            <p>
            Generate candidate molecules conditioned on a protein pocket or PDB structure.
            This pathway is suitable for exploratory projects and early-stage target assessment.
            </p>
            <ul>
                <li>Molecule generation</li>
                <li>Compound prioritization</li>
                <li>Preliminary docking evaluation</li>
            </ul>
            <p><b>Best suited for:</b> rapid exploratory studies.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <h3>🧬 Full computational study</h3>
            <p>
            A broader workflow for discovery projects requiring deeper computational analysis
            beyond initial generation.
            </p>
            <ul>
                <li>Advanced docking workflows</li>
                <li>Rescoring (e.g. Glide)</li>
                <li>Molecular dynamics simulations</li>
                <li>Structural and interaction analysis</li>
            </ul>
            <p><b>Best suited for:</b> deeper R&amp;D collaborations.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

# =========================
# CTA
# =========================
st.markdown('<div class="section-title">Request collaboration</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="cta-box">
        <p style="font-size:1.05rem; line-height:1.75; color:#374151;">
        We collaborate with academic and industry partners in early-stage drug discovery.
        If you would like us to evaluate a target, generate compounds, or discuss a broader
        computational study, please submit your request through the form below.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
st.link_button("🚀 Submit collaboration request", FORM_URL)

st.markdown(
    """
    <div class="small-note">
    The form accepts PDB information and optional pocket coordinates. If coordinates are unavailable,
    they can be estimated from the uploaded structure.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="footer">
    PockLigGPT • AI for structure-based drug discovery
    </div>
    """,
    unsafe_allow_html=True,
)