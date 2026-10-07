"""
Heart Disease Prediction - Streamlit App (dark UI)
---------------------------------------------------
Built from the "Heart Disease Prediction" notebook (Assignment 2, AIC354).
Loads the same svc_trained_model.pkl produced by the notebook and recreates the
exact same LabelEncoders (fit on the same fixed category lists), so predictions
match the notebook exactly.

Educational demo only - NOT a medical diagnostic tool.
"""

import pickle
from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder

st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Dark theme styling (also set in .streamlit/config.toml)
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    :root { --bg:#0b0f19; --card:#121826; --card2:#171f31; --line:#26304a;
            --text:#e8ecf5; --muted:#8e9ab5; --accent:#ff4d6d; --accent2:#7c5cff; --ok:#2ee59d; }
    .stApp { background: radial-gradient(1200px 600px at 10% -10%, #1a1440 0%, transparent 60%),
                         radial-gradient(900px 500px at 100% 0%, #3a0f26 0%, transparent 55%), var(--bg);
             color: var(--text); }
    header[data-testid="stHeader"] { background: transparent; }
    section[data-testid="stSidebar"] { background: #0e1424; border-right: 1px solid var(--line); }
    .block-container { padding-top: 2rem; padding-bottom: 5rem; max-width: 1150px; }

    .hero { padding: 28px 32px; border-radius: 20px; border: 1px solid var(--line);
            background: linear-gradient(135deg, rgba(255,77,109,.16), rgba(124,92,255,.16)), var(--card);
            margin-bottom: 18px; }
    .hero h1 { margin: 0; font-size: 2.3rem; letter-spacing: -.5px; }
    .hero p { margin: 6px 0 0; color: var(--muted); font-size: 1.02rem; }
    .pill { display:inline-block; padding: 3px 12px; border-radius: 999px; font-size: .78rem;
            border:1px solid var(--line); background: var(--card2); color: var(--muted); margin: 10px 6px 0 0; }

    .card { background: var(--card); border: 1px solid var(--line); border-radius: 16px; padding: 20px 22px; }
    .card h3 { margin: 0 0 4px; font-size: 1.05rem; }
    .muted { color: var(--muted); font-size: .88rem; }

    .result { border-radius: 18px; padding: 24px 26px; margin-top: 8px; border: 1px solid; }
    .result.bad { background: linear-gradient(135deg, rgba(255,77,109,.20), rgba(255,77,109,.06)); border-color: #ff4d6d; }
    .result.good { background: linear-gradient(135deg, rgba(46,229,157,.18), rgba(46,229,157,.05)); border-color: #2ee59d; }
    .result .big { font-size: 1.9rem; font-weight: 800; margin: 0; }
    .gauge { height: 12px; border-radius: 999px; background: linear-gradient(90deg,#2ee59d,#ffd166,#ff4d6d);
             position: relative; margin: 16px 0 6px; }
    .gauge .dot { position:absolute; top:-5px; width:22px; height:22px; border-radius:50%;
                  background:#fff; border:4px solid #0b0f19; transform: translateX(-50%); }
    .gauge-lbl { display:flex; justify-content:space-between; color: var(--muted); font-size:.78rem; }
    .chip { display:inline-block; padding: 5px 12px; margin: 4px 6px 0 0; border-radius: 10px;
            background: var(--card2); border: 1px solid var(--line); font-size: .85rem; }
    .chip b { color: var(--accent); }

    div[data-testid="stMetric"] { background: var(--card); border: 1px solid var(--line);
                                  border-radius: 14px; padding: 14px 16px; }
    div[data-testid="stMetricValue"] { color: var(--text); }
    div[data-testid="stMetricLabel"] p { color: var(--muted); }
    .stButton > button[kind="primary"] { background: linear-gradient(90deg, var(--accent), var(--accent2));
        border: 0; color: #fff; font-weight: 700; border-radius: 12px; padding: .7rem 1rem; }
    .stButton > button[kind="primary"]:hover { filter: brightness(1.1); transform: translateY(-1px); }
    .stTabs [data-baseweb="tab-list"] { gap: 6px; }
    .stTabs [data-baseweb="tab"] { background: var(--card); border-radius: 10px 10px 0 0; padding: 8px 18px; }
    .footer { position: fixed; left: 0; right: 0; bottom: 0; text-align: center; padding: 10px 0;
              background: linear-gradient(180deg, transparent, #0b0f19 40%); color: var(--muted);
              font-size: .92rem; z-index: 999; pointer-events: none; }
    .footer b { color: var(--text); }
    .footer .heart { color: #ff4d6d; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Model + encoders (same as the notebook)
# ---------------------------------------------------------------------------
MODEL_PATH = Path(__file__).parent / "svc_trained_model.pkl"


@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)


@st.cache_resource
def build_label_encoders():
    """Recreates the exact LabelEncoders used in the notebook (alphabetical codes)."""
    return {
        "Gender": LabelEncoder().fit(["Male", "Female"]),
        "ExerciseAngina": LabelEncoder().fit(["No", "Yes"]),
        "STDepression": LabelEncoder().fit(["Absent", "Mild", "High"]),
        "Vessels": LabelEncoder().fit(["Zero", "One", "Two", "Three"]),
    }


model = load_model()
encoders = build_label_encoders()

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## ❤️ Heart Disease Predictor")
    st.caption("AIC354 · Machine Learning Fundamentals · Assignment 2")
    st.divider()
    st.markdown("**Model**  \nSupport Vector Classifier (SVC)")
    st.markdown("**Data**  \nKaggle Heart Disease (Cleveland), 303 patients")
    st.markdown("**Inputs**  \n4 attributes: Gender, Exercise Angina, ST Depression, Major Vessels")
    st.markdown("**Output**  \nHeart disease: Yes / No")
    st.divider()

# ---------------------------------------------------------------------------
# Hero
# ---------------------------------------------------------------------------
st.markdown(
    """
    <div class="hero">
      <h1>❤️ Heart Disease Predictor</h1>
      <p>Enter four clinical details and the trained machine learning model predicts whether heart disease is present.</p>
      <span class="pill">SVC model</span><span class="pill">4 input attributes</span>
      <span class="pill">Test accuracy 79%</span><span class="pill">Streamlit Cloud</span>
    </div>
    """,
    unsafe_allow_html=True,
)

tab_predict, tab_model, tab_help = st.tabs(["🔍 Predict", "📊 Model Performance", "ℹ️ How it works"])

# ---------------------------------------------------------------------------
# Tab 1: Predict
# ---------------------------------------------------------------------------
with tab_predict:
    left, right = st.columns([1, 1], gap="large")

    with left:
        st.markdown('<div class="card"><h3>Patient details</h3><span class="muted">Choose a value for each attribute</span></div>', unsafe_allow_html=True)
        st.write("")
        gender = st.radio("Gender", ["Male", "Female"], horizontal=True)
        exercise_angina = st.radio(
            "Exercise-Induced Angina", ["No", "Yes"], horizontal=True,
            help="Chest pain triggered by exercise",
        )
        st_depression = st.select_slider(
            "ST Depression (oldpeak)", options=["Absent", "Mild", "High"], value="Absent",
            help="Absent = 0, Mild = above 0 up to 1.5, High = above 1.5",
        )
        vessels = st.select_slider(
            "Major Vessels Coloured (fluoroscopy)", options=["Zero", "One", "Two", "Three"], value="Zero",
            help="Number of major blood vessels (0-3) coloured by fluoroscopy",
        )
        go = st.button("🔍 Predict Heart Disease", type="primary", width="stretch")

    with right:
        if go:
            user_input = pd.DataFrame({
                "Gender": [gender],
                "ExerciseAngina": [exercise_angina],
                "STDepression": [st_depression],
                "Vessels": [vessels],
            })
            encoded = pd.DataFrame({c: encoders[c].transform(user_input[c]) for c in user_input.columns})

            prediction = int(model.predict(encoded)[0])
            score = float(model.decision_function(encoded)[0])  # >0 -> heart disease side
            pos = max(0.0, min(1.0, (score + 1.5) / 3.0)) * 100

            if prediction == 1:
                cls, title, sub = "bad", "⚠️ HEART DISEASE", "The model predicts that heart disease is present for this profile."
            else:
                cls, title, sub = "good", "✅ NO HEART DISEASE", "The model predicts that heart disease is not present for this profile."
            st.markdown(
                f"""
                <div class="result {cls}"><p class="big">{title}</p>
                <span class="muted">{sub}</span>
                <div class="gauge"><div class="dot" style="left:{pos:.0f}%"></div></div>
                <div class="gauge-lbl"><span>Lower risk side</span><span>Higher risk side</span></div>
                <span class="muted">Position shows the model's decision score ({score:+.2f}); it is a margin, not a probability.</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown("**Entered profile**")
            st.markdown(
                f'<span class="chip">Gender: <b>{gender}</b></span>'
                f'<span class="chip">Exercise angina: <b>{exercise_angina}</b></span>'
                f'<span class="chip">ST depression: <b>{st_depression}</b></span>'
                f'<span class="chip">Vessels: <b>{vessels}</b></span>',
                unsafe_allow_html=True,
            )
            with st.expander("See the encoded feature vector sent to the model"):
                st.dataframe(encoded, hide_index=True, width="stretch")
        else:
            st.markdown(
                '<div class="card"><h3>Result</h3><span class="muted">Fill in the patient details and press '
                '<b>Predict Heart Disease</b>. The prediction appears here.</span></div>',
                unsafe_allow_html=True,
            )

# ---------------------------------------------------------------------------
# Tab 2: Model performance (values from the notebook, Step 7)
# ---------------------------------------------------------------------------
with tab_model:
    st.markdown("#### Results on the held-out test set (61 patients)")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Accuracy", "0.79")
    m2.metric("Precision", "0.79")
    m3.metric("Recall", "0.79")
    m4.metric("F1-score", "0.79")

    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown("**Model comparison (accuracy)**")
        st.bar_chart(
            pd.DataFrame({"Accuracy": [0.79, 0.70, 0.80]},
                         index=["SVC (deployed)", "Logistic Regression", "Decision Tree"]),
            color="#ff4d6d",
        )
    with c2:
        st.markdown("**Confusion matrix (SVC)**")
        st.dataframe(
            pd.DataFrame(
                [[24, 8], [5, 24]],
                index=["Actual: No disease", "Actual: Disease"],
                columns=["Predicted: No disease", "Predicted: Disease"],
            ),
            width="stretch",
        )
        st.caption("24 + 24 correct predictions, 8 false alarms, 5 missed cases (recall for disease = 0.83).")

# ---------------------------------------------------------------------------
# Tab 3: How it works
# ---------------------------------------------------------------------------
with tab_help:
    st.markdown("#### The machine learning cycle used in this project")
    steps = [
        ("1 · Data", "Kaggle Heart Disease dataset (Cleveland, 303 patients); 4 attributes selected."),
        ("2 · Encode", "Text values converted to numbers with scikit-learn LabelEncoder."),
        ("3 · Train", "Support Vector Classifier trained on 80% of the data (242 patients)."),
        ("4 · Test", "Evaluated on the unseen 20% (61 patients): accuracy 0.79."),
        ("5 · Apply", "This app: your input is encoded the same way and sent to the saved model."),
        ("6 · Feedback", "Results are reviewed and the model is improved in the next version."),
    ]
    cols = st.columns(3)
    for i, (t, d) in enumerate(steps):
        with cols[i % 3]:
            st.markdown(f'<div class="card" style="margin-bottom:14px"><h3>{t}</h3><span class="muted">{d}</span></div>', unsafe_allow_html=True)

    st.markdown("#### Input attributes")
    st.table(pd.DataFrame({
        "Attribute": ["Gender", "ExerciseAngina", "STDepression", "Vessels"],
        "Original column": ["sex", "exang", "oldpeak", "ca"],
        "Values": ["Male, Female", "No, Yes", "Absent, Mild, High", "Zero, One, Two, Three"],
    }))
    st.caption("Built for teaching purposes. Predictions are not a medical diagnosis.")

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="footer">Made with <span class="heart">❤️</span> by <b>Muhammad Hunain</b></div>',
    unsafe_allow_html=True,
)
