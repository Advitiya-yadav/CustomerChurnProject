import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.set_page_config(page_title="Customer Churn Prediction", layout="centered")

# Loading the pipeline
pipeline = joblib.load("pipeline.pkl")

st.title("Customer Churn Prediction App 📉🌐")
st.caption("Predict whether a customer is likely to churn")
st.divider()

st.subheader("🧾 Enter Customer Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=10, max_value=100, value=18)
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=240, value=12)
    total_charges = st.number_input("Total Charges", min_value=0.0, value=500.0)
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)

with col2:
    
    gender = st.selectbox("Gender", ["Male", "Female"])
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No"])

st.divider()

if st.button("Predict Churn", layout="center", size="medium"):
    X = pd.DataFrame(
    [{
        "Age": age,
        "Tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "Gender": gender,
        "ContractType": contract,
        "InternetService": internet,
        "TechSupport": tech_support
    }]
)

    prediction = pipeline.predict(X)[0]

    if prediction == 1:
        st.error("⚠️ High Risk of Customer Churn")
    else:
        st.success("✅ Customer is Likely to Stay")

else:
    st.info("Enter customer details and click **Predict Churn**")
