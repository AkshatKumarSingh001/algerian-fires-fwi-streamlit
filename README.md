# Forest Fire Weather Index (FWI) Prediction

A Streamlit web app that predicts the Forest Fire Weather Index (FWI) using a trained Ridge Regression model.
Users enter environmental conditions and FWI components, and the app returns the predicted FWI value.

**Live App:** https://algerian-fires-fwi-app-h7dvs3qhzkk2azhwjphkqn.streamlit.app/

---

## Features
- Clean Streamlit UI with a simple form
- 9 input features used for prediction
- Pretrained Ridge model + StandardScaler
- Works locally and on Streamlit Cloud

---

## Input Features (in order)
The model expects 9 inputs in this exact order:

1. Temperature (C)
2. Relative Humidity (RH)
3. Wind Speed (Ws)
4. Rain (mm)
5. FFMC
6. DMC
7. ISI
8. Classes (0 = Not Fire, 1 = Fire)
9. Region (0 = Bejaia, 1 = Sidi Bel Abbes)

---

## Project Structure
```
.
├── streamlit_app.py
├── requirements.txt
├── models/
│   ├── ridge.pkl
│   └── scaler.pkl
└── README.md
```

---

## Architecture
- Streamlit UI collects 9 input features from the user.
- Inputs are scaled with the saved StandardScaler.
- The Ridge model predicts the FWI value.
- The app displays the prediction in the UI.

---

## Workflow
1. User enters the 9 required features in the Streamlit form.
2. App loads model artifacts (`ridge.pkl`, `scaler.pkl`).
3. Inputs are scaled using the same scaler used during training.
4. The Ridge model generates the FWI prediction.
5. Result is shown in the app.

---

## Dataset
`Algerian_forest_fires_dataset_UPDATE.csv' This file is used for training and reproducibility, but it is not required for Streamlit deployment.
The dataset was cleaned using exploratory data analysis (EDA) and feature engineering before training.

---

## Run Locally

### 1) Create and activate a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Start the app
```bash
streamlit run streamlit_app.py
```

The app will open in your browser at:
```
http://localhost:8501
```

---

## Deploy on Streamlit Cloud (optional)

1. Push the project to GitHub (including models/ and requirements.txt)
2. Go to https://share.streamlit.io
3. Select your repo and branch
4. Set Main file path to:
   ```
   streamlit_app.py
   ```
5. Click Deploy

---

## Notes
- The model and scaler were trained separately and saved in models/.
- If you change the feature list or order, you must retrain the scaler and model.

---

## License
This project is licensed under the MIT License.
