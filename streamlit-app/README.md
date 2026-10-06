# Heart Disease Predictor — Streamlit App

A small web app to try the trained Heart Disease model in a browser. Built from the model trained in [`2 - Heart Disease Prediction`](../2%20-%20Heart%20Disease%20Prediction) (`Heart_Disease_Prediction.ipynb`).

## Deploying to Streamlit Community Cloud (free)

1. Push this folder's contents (`app.py`, `requirements.txt`, `runtime.txt`, `svc_trained_model.pkl`) to a **public** GitHub repo.
2. Go to **https://share.streamlit.io** and sign in with GitHub.
3. **Create app → Deploy a public app from GitHub**.
4. Repository: `<your-username>/<your-repo>`, Branch: `main`, Main file path: `app.py` (or `streamlit-app/app.py` if inside a subfolder).
5. Click **Deploy**. You get a public `https://<something>.streamlit.app` URL — paste it at the top of the notebook.

If the build fails with `ModuleNotFoundError`, set **Settings → General → Python version** to 3.11 or 3.12.

## Run locally

```bash
cd streamlit-app
pip install -r requirements.txt
streamlit run app.py
```

Opens at `http://localhost:8501`.

## How it works
`app.py` loads `svc_trained_model.pkl` and recreates the same `LabelEncoder`s used in the notebook, so predictions match exactly. Inputs: Gender, Exercise-Induced Angina, ST Depression, Major Vessels.
