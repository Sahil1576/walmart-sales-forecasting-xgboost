import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Walmart Sales Forecasting",
    page_icon="📈",
    layout="centered"
)

st.title("📈 Walmart Weekly Sales Forecasting")
st.write("Predict Weekly Sales using XGBoost Regression Model")

# Load Model
model = joblib.load("XGBRegressor.pkl")
encoder = joblib.load("LabelEncoder.pkl")

st.subheader("Enter Store Details")

store = st.number_input("Store", min_value=1, max_value=45, value=1)
dept = st.number_input("Department", min_value=1, max_value=99, value=1)

day = st.number_input("Day", min_value=1, max_value=31, value=1)
month = st.number_input("Month", min_value=1, max_value=12, value=1)
year = st.selectbox("Year", [2010, 2011, 2012])

holiday = st.selectbox("Holiday", ["No", "Yes"])

temperature = st.number_input("Temperature", value=60.0)
fuel_price = st.number_input("Fuel Price", value=3.0)
cpi = st.number_input("CPI", value=210.0)
unemployment = st.number_input("Unemployment", value=8.0)

type_store = st.selectbox("Store Type", ["A", "B", "C"])

size = st.number_input("Store Size (sqft)", value=150000)

rolling3 = st.number_input("Rolling Mean (Last 3 Weeks)", value=25000.0)

rolling7 = st.number_input("Rolling Mean (Last 7 Weeks)", value=26000.0)

lag1 = st.number_input("Previous Week Sales (Lag 1)", value=24000.0)

if holiday == "Yes":
    holiday = 1
else:
    holiday = 0

type_store = encoder.transform([type_store])[0]

input_df = pd.DataFrame({
    "Store":[store],
    "Dept":[dept],
    "Day":[day],
    "Month":[month],
    "Year":[year],
    "IsHoliday":[holiday],
    "Temperature":[temperature],
    "Fuel_Price":[fuel_price],
    "CPI":[cpi],
    "Unemployment":[unemployment],
    "Type":[type_store],
    "Size (sqft)":[size],
    "Rolling_mean_3":[rolling3],
    "Rolling_mean_7":[rolling7],
    "Lag_1":[lag1]
})

if st.button("Predict Weekly Sales"):

    prediction = model.predict(input_df)[0]

    st.success(f"Predicted Weekly Sales : ${prediction:,.2f}")