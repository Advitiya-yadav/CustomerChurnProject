# 📊 Customer Churn Prediction – End-to-End Machine Learning Project
### 📌 Project Overview

Customer churn refers to customers who stop using a company’s product or service.
Predicting churn in advance allows businesses to take proactive actions such as targeted offers, improved support, or retention campaigns.

This project builds an end-to-end machine learning pipeline to predict customer churn using structured customer data, with a strong focus on:

* Proper data preprocessing

* Handling class imbalance

* Comparing multiple ML models

* Avoiding data leakage & overfitting

Deployable, production-ready artifacts

---

## Problem Type:

* **Binary Classification**
* Target variable: `Churn` as a Yes or No

---

## 🛠 Tech Stack

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Streamlit**
* **Joblib**
* **Seaborn**
* **Matplotlib**
* **Git**

---

## 📊 Features Used

* Age
* Gender (encoded manually)
* Tenure
* Monthly Charges

(Additional features will be added to further improve performance.)

---

##  Machine Learning Workflow 🤖

1. **Data Preprocessing**

   * Dropped CustomerID columns
   * Encoded categorical features such as Gender
   * Scaled numerical features (Age,Tenure,Monthly Charges) using a trained scaler

2. **Model Training**

   * Tried multiple models (Logistic Regression, KNN, SVC, Decision Tree, Random forest)
   * Used **GridSearchCV** for hyperparameter tuning
   * Selected the best model using **GridSearchCV.best_estimator_**

3. **Evaluation Metrics**

   * Accuracy

   * Precision

   * Recall

   * F1-Score

   > Note: Since churn datasets are imbalanced, metrics beyond accuracy were considered.

4. **Model Persistence**

   * Saved trained model and scaler using `joblib as model.pkl and scaler.pkl so that they can be reused in the application`

---

## Web Application (Streamlit)

The Streamlit app allows users to:

* Enter customer details via a clean UI
* Get real-time churn predictions
* Visual feedback indicating churn risk

### Example Inputs

* Age
* Gender
* Tenure
* Monthly Charges

### Output

* **Churn Prediction: Yes / No**

---

## How to Run the Project Locally ❓
#### Will soon deploy on huggingface or streamlit cloud !

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd customer-churn-prediction
```

### 2. Install dependencies

```bash
pip install -r req.txt
```

### 3. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
├── app.py            # Streamlit web app
├── model.pkl         # Trained ML model
├── README.md         # Readme file
├── req.txt
├── scaler.pkl        #Trained scaler
```

---

## 🧠 Key Learnings

* Built a complete ML pipeline from scratch
* Understood the importance of preprocessing consistency
* Learned how to avoid data leakage
* Deployed an ML model as a usable web application
* Gained hands-on experience with evaluation metrics for imbalanced data

---

## 🕔 Future Improvements

* Will add more categorial features and encode them to give a better model output (Contract Type, Internet Service, etc.)
* Handle class imbalance using SMOTE
* Deploy the app on a cloud platform like AWS

---

## 📝 Conclusion

This project demonstrates the ability to:

* Solve a real-world business problem
* Apply machine learning correctly
* Build and deploy an end-to-end ML application

