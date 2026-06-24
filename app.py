import streamlit as st
import pandas as pd
import joblib

model = joblib.load("best_model.pkl")

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊"
)

st.title("📊 Customer Churn Prediction")

st.write(
    "Prediksi apakah pelanggan akan churn atau tidak."
)

total_spent = st.number_input(
    "Total Spent",
    min_value=0.0,
    value=1000.0
)

satisfaction_score = st.number_input(
    "Satisfaction Score",
    min_value=1.0,
    max_value=5.0,
    value=3.0
)

support_tickets = st.number_input(
    "Support Tickets",
    min_value=0,
    value=1
)

marketing_spend_per_user = st.number_input(
    "Marketing Spend Per User",
    min_value=0.0,
    value=20.0
)

avg_session_time = st.number_input(
    "Average Session Time",
    min_value=0.0,
    value=10.0
)

lifetime_value = st.number_input(
    "Lifetime Value",
    min_value=0.0,
    value=1000.0
)

membership_days = st.number_input(
    "Membership Days",
    value=365
)

avg_order_value = st.number_input(
    "Average Order Value",
    min_value=0.0,
    value=100.0
)

pages_per_session = st.number_input(
    "Pages Per Session",
    min_value=0.0,
    value=5.0
)

if st.button("Prediksi"):

    data = pd.DataFrame([{
        'total_spent': total_spent,
        'satisfaction_score': satisfaction_score,
        'support_tickets': support_tickets,
        'marketing_spend_per_user': marketing_spend_per_user,
        'avg_session_time': avg_session_time,
        'lifetime_value': lifetime_value,
        'membership_days': membership_days,
        'avg_order_value': avg_order_value,
        'pages_per_session': pages_per_session
    }])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠️ Pelanggan Diprediksi Churn")
    else:
        st.success("✅ Pelanggan Diprediksi Tidak Churn")