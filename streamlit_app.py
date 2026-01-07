import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="centered"
)

# Load model and feature list
model = joblib.load("model.pkl")
features = joblib.load("features.pkl")

st.title("Customer Churn Prediction 📉")
st.caption("Predict whether a customer is likely to churn")
st.divider()

st.subheader("🧾 Enter Customer Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=10, max_value=100, value=30)
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=240, value=12)
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)

with col2:
    gender = st.selectbox("Gender", ["Male", "Female"])
    contract = st.selectbox("Contract Type",["Month-to-month", "One year", "Two year"])
    internet = st.selectbox("Internet Service",["DSL", "Fiber optic", "No"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No"])

st.divider()

if st.button("Predict Churn"):
    input_df = pd.DataFrame([{
        "Age": age,
        "Tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "Gender": gender,
        "ContractType": contract,
        "InternetService": internet,
        "TechSupport": tech_support
    }])

    # One-hot encode
    input_df = pd.get_dummies(input_df)

    # Align with training features
    input_df = input_df.reindex(columns=features, fill_value=0)

    prediction = model.predict(input_df)[0]

    if prediction == "Yes":
        st.error("⚠️ High Risk of Customer Churn")

    else:
        st.success("✅ Customer is Likely to Stay")

else:
    st.info("Enter customer details and click **Predict Churn**")
