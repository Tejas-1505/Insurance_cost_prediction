import streamlit as st
import pandas as pd
import joblib
import numpy as np
from sklearn.utils.validation import check_is_fitted
import requests
import os

backend_url = os.getenv("BACKEND_URL", "http://127.0.0.1:5000/predict")

@st.cache_resource
def load_assets():
    model = joblib.load('insurance_model.joblib')
    scaler = joblib.load('scaler.joblib')
    return model, scaler


try:
    model, scaler = load_assets()
    # Check if the model is actually ready
    check_is_fitted(model)
except Exception as e:
    st.error(f"Model Loading Error: {e}")
    st.stop()

st.title("🏥 Insurance Premium Predictor")

# Input fields
age = st.number_input("Age", 1, 100, 25)
height = st.number_input("Height (cm)", 100, 250, 170)
weight = st.number_input("Weight (kg)", 30, 200, 70)
diabetes = st.selectbox("Diabetes", [0, 1])
bp = st.selectbox("Blood Pressure Problems", [0, 1])
transplants = st.selectbox("Any Transplants", [0, 1])
chronic = st.selectbox("Any Chronic Diseases", [0, 1])
allergies = st.selectbox("Known Allergies", [0, 1])
cancer = st.selectbox("History of Cancer in Family", [0, 1])
surgeries = st.slider("Major Surgeries", 0, 5, 0)

# BMI Calculation
bmi = weight / ((height / 100) ** 2)

if st.button("Predict"):
    # Must be in the EXACT order of your 'feature_names' list
    features = np.array([[age, diabetes, bp, transplants, chronic,
                          height, weight, allergies, cancer, surgeries, bmi]])

    # Apply Scaling
    scaled_features = scaler.transform(features)

    # Predict
    prediction = model.predict(scaled_features)
    st.success(f"Predicted Premium: {prediction[0]:,.2f}")