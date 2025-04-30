import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load('fraud_model.pkl')

st.title("🛡️ Credit Card Fraud Detector")

st.subheader("Enter Transaction Info:")

# Input fields
credit_card_number = st.text_input("Credit Card Number")
merchant_name = st.text_input("Merchant Name")
city = st.text_input("City")
state = st.text_input("State")
job = st.text_input("Job")
transaction_date = st.date_input("Transaction Date")
transaction_time = st.time_input("Transaction Time")
date_of_birth = st.date_input("Date of Birth")
transaction_number = st.text_input("Transaction Number")
merchant_lat = st.number_input("Merchant Latitude", value=0.0)
merchant_long = st.number_input("Merchant Longitude", value=0.0)
amount = st.number_input("Transaction Amount", value=0.0)

if st.button("Predict Fraud"):
    # Prepare single row as DataFrame with updated column names
    new_data = pd.DataFrame([{
        'S.No': 1,  # Assuming 'S.No' is not used for prediction and doesn't affect the model
        'trans_date': str(transaction_date),
        'trans_time': str(transaction_time),
        'Credit_card_number ': credit_card_number,  # Note the extra space here; keep it as is
        'Merchant_name': merchant_name,
        'Unnamed: 5': None,  # Assuming this column is not necessary for prediction
        'city': city,
        'state': state,
        'job': job,
        'dob': str(date_of_birth),
        'trans_num': transaction_number,
        'merch_lat': merchant_lat,
        'merch_long': merchant_long,
        'amount': amount
    }])

    # Predict
    prediction = model.predict(new_data)

    if prediction[0] == 1:
        st.error("⚠️ Fraud Detected!")
    else:
        st.success("✅ Transaction is Safe")
