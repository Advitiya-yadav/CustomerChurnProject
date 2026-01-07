# Customer Churn Prediction – Machine Learning Project

## 📌 Project Overview
This project predicts whether a customer is likely to **churn (leave the service)** based on demographic, contract, and service-related features.

The objective was to build a **reliable, interpretable, and deployable machine learning model**, while avoiding common pitfalls such as data leakage and overfitting.

The final solution follows an **end-to-end ML workflow**:
EDA → Feature Engineering → Model Selection → Evaluation → Deployment.

---

## 📊 Dataset
- **Type:** Customer churn dataset (CSV)
- **Target Variable:** `Churn` (`Yes` / `No`)
- **Problem Type:** Binary Classification

### Key Features Used
- Age  
- Tenure (months)  
- MonthlyCharges  
- Gender  
- ContractType  
- InternetService  
- TechSupport  

> ⚠️ **Important:**  
> Cumulative billing features such as `TotalCharges` were intentionally removed to avoid **target leakage**, which can artificially inflate model performance.

---

## 🔍 Exploratory Data Analysis (EDA)

EDA was performed separately to understand data distribution, class imbalance, and feature–target relationships.

Notebook:
- `Customer_churn_analysis_EDA.ipynb`

### Key Insights
- Churn is strongly associated with:
  - Short tenure
  - Month-to-month contracts
  - Lack of tech support
- The dataset is **imbalanced**, with non-churn customers being the majority
- Certain service-related features are strong churn indicators

## 📈 Exploratory Data Analysis (EDA)

### Correlation
![Correlation](images/Correlation.png)

### Tenure vs Churn
![Monthly Charges histogram distribution](images/Monthly_charges_histogram.png)

### Contract Type 
![Contract Type data](images/Contract_type_data_counts.png)

### Tenure ( left skewed)
![Tenure histogram](images/Tenure_histogram.png)

### Yes and No relative count
![Yes and No pie chart](images/Yes_No_count.png)
