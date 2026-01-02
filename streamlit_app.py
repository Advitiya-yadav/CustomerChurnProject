import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Churn Prediction", layout="centered")

scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

st.title("📉 Customer Churn Prediction App")
st.caption("Predict whether a customer is likely to churn based on their details")
st.divider()

st.subheader("🧾 Enter Customer Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=5, max_value=110, value=30)
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=240, value=12)

with col2:
    monthlycharge = st.number_input("Monthly Charges", min_value=25, max_value=100, value=50)
    gender = st.selectbox("Gender", ['Male', 'Female'])

st.divider()

predictbutton = st.button("🔍 Predict Churn")
st.divider()

if predictbutton:
    gender_selected = 1 if gender == "Female" else 0

    # ORDER MUST MATCH TRAINING
    X = [age, tenure, monthlycharge, gender_selected]

    X_array = scaler.transform([X])
    prediction = model.predict(X_array)[0]

    predicted = "Yes" if prediction == 1 else "No"

    if predicted == "Yes":
        st.error("High Risk of Churn")
    else:
        st.success("Customer is Likely to Stay")

    st.metric(label="Churn Prediction", value=predicted)

else:
    st.info("Please enter the values and click **Predict Churn**")
