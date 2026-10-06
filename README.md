# Heart Disease Prediction — End-to-End Machine Learning System

**Course:** Machine Learning Fundamentals (AIC354), Assignment 2 — COMSATS University Islamabad, Lahore Campus
**Student:** Hunain (FA24-BSE-083) — **Instructor:** Dr. Rao Muhammad Adeel Nawab

An end-to-end ML project built by modifying the Titanic Passenger Survival Prediction notebook, keeping exactly the same steps (Import Libraries → Load Data → Preprocess → Label Encode → Train → Test → Application → Feedback → Deploy).

Predicts whether a patient has heart disease from **4 input attributes** of the Kaggle Heart Disease (Cleveland, heart.csv) dataset, using a Support Vector Classifier.

| Input | Kaggle column | Values |
|---|---|---|
| Gender | `sex` | Male, Female |
| ExerciseAngina | `exang` | No, Yes |
| STDepression | `oldpeak` | Absent, Mild, High |
| Vessels | `ca` | Zero, One, Two, Three |

**Test accuracy: 0.79** (61 held-out patients; precision/recall/F1 0.79).

## Live Demo
**https://heart-disease-predictor.streamlit.app** *(replace with your own Streamlit URL after deploying; see `streamlit-app/README.md`)*

## Contents
- [`2 - Heart Disease Prediction`](./2%20-%20Heart%20Disease%20Prediction) — notebook (`.ipynb` + `.html`), dataset, encoded CSVs, predictions and the trained model `svc_trained_model.pkl`
- [`streamlit-app`](./streamlit-app) — web app used for cloud deployment

## Run locally
```bash
python -m venv venv
venv\Scripts\activate        # Windows  (macOS/Linux: source venv/bin/activate)
pip install -r requirements.txt
jupyter notebook
```

*Educational project — not a medical diagnostic tool.*
