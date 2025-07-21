import streamlit as st
from datetime import datetime
import requests
import pandas as pd
from utils import dataframe_to_pdf

API_URL = "http://localhost:8000"

def analytics_by_month_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input("End Date", datetime(2024, 9, 30))

    if st.button("Get Monthly Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics/monthly/", json=payload)

        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)

            if df.empty:
                st.warning("No expense data found for the selected date range.")
                return

            st.title("Expense Breakdown By Months")

            # Bar chart using 'month' and 'total'
            st.bar_chart(data=df.set_index("month")["total"], use_container_width=True)

            # Format values and rename for table & report
            df["total"] = df["total"].map("{:.2f}".format)
            df_sorted = df.sort_values(by="total", ascending=False)
            display_df = df_sorted.rename(columns={"month": "Month", "total": "Total Expense"})

            st.table(display_df)

            # PDF Download
            pdf_data = dataframe_to_pdf(display_df, title="Expense Breakdown By Months")
            st.download_button(
                label="📄 Download Report as PDF",
                data=pdf_data,
                file_name="monthly_expense_report.pdf",
                mime="application/pdf"
            )
        else:
            st.error("Failed to retrieve data from backend.")
