import streamlit as st
from add_update_ui import add_update_tab
from analytics_by_category import analytics_tab
from analytics_by_month import analytics_by_month_tab
from budget_tracker import budget_tracker_tab
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file if using

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False


def authenticate():
    st.markdown("## 🔐 Login Required")

    # Optional helper message
    st.info("Please enter your password to access the app.")

    password_input = st.text_input("Enter Password", type="password")
    correct_password = os.getenv("APP_PASSWORD", "mysecret123")

    if password_input:
        if password_input == correct_password:
            st.session_state.authenticated = True
            st.success("Access granted ✅")
        else:
            st.session_state.authenticated = False
            st.error("Access denied. Incorrect password.")
            st.stop()
    elif not st.session_state.get("authenticated"):
        st.stop()

authenticate()


st.title("Expense Tracking System")

tab1, tab2, tab3, tab4 = st.tabs(["Add/Update", "Analytics By Category", "Analytics By Months", "Budget Tracker"])

with tab1:
    add_update_tab()
with tab2:
    analytics_tab()
with tab3:
    analytics_by_month_tab()
with tab4:
    budget_tracker_tab()
