import streamlit as st
import requests
from datetime import date, datetime
import calendar

API_URL = "http://localhost:8000"

def budget_tracker_tab():
    st.header("Monthly Budget Tracker")

    # Month and Year Selection
    selected_year = st.selectbox("Select Year", range(2023, datetime.now().year + 1), index=1)
    selected_month = st.selectbox(
        "Select Month", range(1, 13), format_func=lambda x: calendar.month_name[x]
    )

    # Budget Input
    monthly_budget = st.number_input("Set Your Monthly Budget (₹)", min_value=0, value=10000)

    # Calculate start and end date for selected month
    start_date = date(selected_year, selected_month, 1)
    last_day = calendar.monthrange(selected_year, selected_month)[1]
    end_date = date(selected_year, selected_month, last_day)

    # Fetch monthly data from FastAPI
    payload = {
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d")
    }

    response = requests.post(f"{API_URL}/analytics/", json=payload)

    if response.status_code == 200:
        analytics = response.json()
        total_spent = sum(row["total"] for row in analytics.values())

        st.metric("Total Spent", f"₹{total_spent:,.2f}")
        st.metric("Remaining Budget", f"₹{max(monthly_budget - total_spent, 0):,.2f}")

        progress = min(total_spent / monthly_budget, 1.0) if monthly_budget > 0 else 0
        st.progress(progress)
    else:
        st.error("Failed to retrieve monthly data.")
