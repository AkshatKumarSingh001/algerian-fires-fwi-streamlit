import pickle
from pathlib import Path

import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "ridge.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"


@st.cache_resource
def load_artifacts():
    ridge_model = pickle.load(open(MODEL_PATH, "rb"))
    scaler = pickle.load(open(SCALER_PATH, "rb"))
    return ridge_model, scaler


st.set_page_config(page_title="Forest Fire FWI Prediction", page_icon="🔥", layout="centered")

st.title("Forest Fire Weather Index (FWI) Prediction")
st.write("Enter the environmental and FWI component values to predict FWI.")

with st.form("fwi_form"):
    col1, col2 = st.columns(2)

    with col1:
        temperature = st.number_input("Temperature (°C)", step=0.1, format="%.2f")
        wind_speed = st.number_input("Wind Speed (Ws)", step=0.1, format="%.2f")
        ffmc = st.number_input("FFMC", step=0.1, format="%.2f")
        isi = st.number_input("ISI", step=0.1, format="%.2f")
        classes = st.selectbox("Classes", options=[0, 1], format_func=lambda v: "Not Fire" if v == 0 else "Fire")

    with col2:
        rh = st.number_input("Relative Humidity (RH)", step=0.1, format="%.2f")
        rain = st.number_input("Rain (mm)", step=0.1, format="%.2f")
        dmc = st.number_input("DMC", step=0.1, format="%.2f")
        region = st.selectbox("Region", options=[0, 1], format_func=lambda v: "Bejaia" if v == 0 else "Sidi Bel Abbes")

    submit = st.form_submit_button("Predict")

if submit:
    try:
        ridge_model, scaler = load_artifacts()
        values = [
            float(temperature),
            float(rh),
            float(wind_speed),
            float(rain),
            float(ffmc),
            float(dmc),
            float(isi),
            float(classes),
            float(region),
        ]
        scaled = scaler.transform([values])
        prediction = ridge_model.predict(scaled)[0]
        st.success(f"FWI prediction: {float(prediction):.3f}")
    except Exception as exc:
        st.error(f"Error: {exc}")
