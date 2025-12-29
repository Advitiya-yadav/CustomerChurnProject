# 📉 Customer Churn Prediction Web App

An end-to-end **Machine learning project** that predicts whether a customer is likely to churn based on various input features.
The model is trained using classical ML techniques and deployed as an **Streamlit Web application**.

---

## Project Overview:

Customer churn is an important business problem where customers discontinue a service, leading to revenue loss.
This project aims to **predict churn in advance**, so that the business can work on certain things to increase their customer retention.

The workflow covers:

* Data preprocessing & feature engineering
* Model training and evaluation
* Hyperparameter tuning using GridSearchCV
* Model deployment using Streamlit

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

