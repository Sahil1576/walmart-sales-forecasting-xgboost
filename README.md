Time Series Forecasting using XGBoost with Lag Features, Rolling Mean Features, Feature Engineering, and Streamlit Deployment.
# 📈 Walmart Weekly Sales Forecasting using XGBoost

A Machine Learning Time Series Forecasting project that predicts Walmart weekly sales using historical sales data, store information, economic indicators, and feature engineering techniques such as Lag Features and Rolling Mean Features.

---

## 🚀 Project Overview

The objective of this project is to accurately forecast weekly sales for Walmart stores using machine learning.

Instead of traditional forecasting models (ARIMA, SARIMA, Prophet), this project demonstrates how feature engineering combined with XGBoost Regression can effectively solve a time series forecasting problem.

---

## 📂 Dataset

The project uses the Walmart Sales Forecasting dataset containing:

- Historical Weekly Sales
- Store Information
- Economic Indicators
- Holiday Information

Merged Files:

- train.csv
- features.csv
- stores.csv

---

## 📊 Features Used

- Store
- Department
- Day
- Month
- Year
- IsHoliday
- Temperature
- Fuel Price
- CPI
- Unemployment
- Store Type
- Store Size
- Lag_1
- Rolling Mean (3 Weeks)
- Rolling Mean (7 Weeks)

---

## 🛠 Feature Engineering

The following features were created to improve forecasting performance.

### Lag Feature

- Lag_1 (Previous week's sales)

### Rolling Features

- Rolling Mean (Previous 3 Weeks)
- Rolling Mean (Previous 7 Weeks)

To prevent data leakage, rolling features were created using:

```python
shift(1)
```

This ensures that only historical information is available during prediction.

---

## 📈 Model

- XGBoost Regressor

---

## 📊 Train-Test Split

A chronological split was used instead of a random split.

Training Data

- 2010
- 2011

Testing Data

- 2012

This simulates a real-world forecasting scenario.

---

## 📉 Model Performance

| Metric | Value |
|---------|-------|
| R² Score | 0.97 |
| MAE | ~1666 |
| MAPE | ~1.64% |

---

## 📷 Visualizations

- Actual vs Predicted Plot
- <img width="648" height="454" alt="image" src="https://github.com/user-attachments/assets/66208fcf-61bf-4dd5-9cc9-ea06a80d1cd1" />

- Residual Plot
- <img width="642" height="450" alt="image" src="https://github.com/user-attachments/assets/f618f607-331f-4a47-981e-ac918bf80312" />

- Feature Importance Plot
- <img width="673" height="455" alt="image" src="https://github.com/user-attachments/assets/9b57496a-bf04-4dcc-9dda-a85dc0b96946" />


---

## 📦 Deployment

The project is deployed using Streamlit.

---

## 🧰 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- XGBoost
- Joblib
- Streamlit

---

## 📁 Project Structure

```
├── app.py
├── Walmart_Time_Series.ipynb
├── XGBRegressor.pkl
├── LabelEncoder.pkl
├── requirements.txt
├── README.md
```

---

## 🎯 Key Highlights

- Time Series Forecasting
- Feature Engineering
- Lag Features
- Rolling Mean Features
- Data Leakage Prevention
- XGBoost Regression
- Streamlit Deployment

---

## 👨‍💻 Author

**Sahil Katve**

If you found this project useful, feel free to ⭐ this repository.
