# Deploy: GitHub + Streamlit Community Cloud

1. **Test locally:** `cd streamlit-app && pip install -r requirements.txt && streamlit run app.py`
2. **GitHub:** sign in at https://github.com → **+ → New repository** → name `HEART-DISEASE-PREDICTOR`, **Public** → Create.
3. **Upload this whole folder:** repo page → **Add file → Upload files** → drag everything in this zip (unzipped) → **Commit changes**.
   Or with git, inside this folder:
   ```
   git init
   git add .
   git commit -m "Heart disease predictor"
   git branch -M main
   git remote add origin https://github.com/Hunain-Riasat/HEART-DISEASE-PREDICTOR.git
   git push -u origin main
   ```
4. **Streamlit:** https://share.streamlit.io → **Sign in with GitHub** → **Create app → Deploy a public app from GitHub**.
5. Repository `Hunain-Riasat/HEART-DISEASE-PREDICTOR`, Branch `main`, **Main file path `streamlit-app/app.py`**, Python **3.11** → **Deploy**.
6. Copy the `https://<name>.streamlit.app` link and paste it at the **top of the notebook** (first cell), in `README.md`, and on the title page of the Word report.
7. If the build fails with `ModuleNotFoundError`: app **Settings → General → Python version → 3.11/3.12**.
