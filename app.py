import streamlit as st
import base64
from analyzer import analyze_answer
from evaluator import evaluate_results
from generator import generate_answer

# -------------------------------
# BACKGROUND
# -------------------------------
def get_base64_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_base64 = get_base64_image("assets/background.png")

st.set_page_config(page_title="Hallucination Detection Engine", layout="wide")

st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background: url("data:image/png;base64,{img_base64}") no-repeat center center fixed;
    background-size: cover;
}}

.block-container {{
    background-color: rgba(15, 23, 42, 0.9);
    padding: 2rem;
    border-radius: 12px;
}}

.card {{
    background-color: rgba(30, 41, 59, 0.9);
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# HEADER
# -------------------------------
st.title("🧠 Hallucination Detection Engine")
st.markdown("Analyze AI outputs and detect unsupported or weakly grounded claims.")

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("⚙️ Controls")

mode = st.sidebar.selectbox(
    "Mode",
    ["Generate Answer (LLM)", "Manual Input"]
)

st.sidebar.markdown("---")
st.sidebar.subheader("📌 Sample Queries")

samples = [
    "What is fusion energy?",
    "Explain hallucination in AI",
    "How do RAG systems work?",
]

query = st.text_input("Enter your question")

for s in samples:
    if st.sidebar.button(s):
        query = s

# -------------------------------
# INPUT
# -------------------------------
if mode == "Manual Input":
    answer = st.text_area("Paste AI Answer")
else:
    answer = None

# -------------------------------
# RUN SYSTEM
# -------------------------------
if st.button("Analyze"):

    # Generate answer if needed
    if mode == "Generate Answer (LLM)":
        with st.spinner("Generating answer..."):
            answer = generate_answer(query)

    if not answer:
        st.error("Please provide input")
    else:
        # Show answer
        st.markdown("### 📄 Generated Answer")
        st.markdown(f"<div class='card'>{answer}</div>", unsafe_allow_html=True)

        # Analyze
        results = analyze_answer(answer)
        final_score = evaluate_results(results)

        # -------------------------------
        # OUTPUT TABS
        # -------------------------------
        tab1, tab2 = st.tabs(["🔍 Sentence Analysis", "📊 Summary"])

        # -------------------------------
        # SENTENCE LEVEL
        # -------------------------------
        with tab1:
            st.markdown("### Sentence Verification")

            for r in results:
                if r["status"] == "Supported":
                    st.success(r["sentence"])
                elif r["status"] == "Weak Evidence":
                    st.warning(r["sentence"])
                else:
                    st.error(r["sentence"])

                st.caption(f"Score: {r['score']:.2f}")
                st.write(f"Evidence: {r['evidence']}")

        # -------------------------------
        # SUMMARY
        # -------------------------------
        with tab2:
            st.markdown("### Overall Reliability Score")
            st.progress(final_score)

            if final_score > 0.75:
                st.success("High Reliability")
            elif final_score > 0.5:
                st.warning("Moderate Reliability")
            else:
                st.error("Low Reliability (Possible Hallucination)")