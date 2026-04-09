import streamlit as st
import json
import pandas as pd

from main import run_pipeline
from database import init_db, get_history, login_user, register_user

# Initialize database
init_db()

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Sidebar menu
menu = st.sidebar.selectbox("Menu", ["Login", "Signup"])

# ---------------- LOGIN / SIGNUP ---------------- #
if not st.session_state.logged_in:

    if menu == "Login":
        st.title("🔐 Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if login_user(username, password):
                st.session_state.logged_in = True
                st.success("Login Successful")
                st.rerun()
            else:
                st.error("Invalid credentials")

    elif menu == "Signup":
        st.title("📝 Signup")

        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")

        if st.button("Register"):
            if register_user(new_user, new_pass):
                st.success("User created successfully")
            else:
                st.error("Username already exists")

    st.stop()

# ---------------- MAIN APPLICATION ---------------- #

st.title("🔐 Agentic Privacy Analyzer")

# Logout button
if st.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

email = st.text_input("Enter Email")

if st.button("Analyze"):

    result = run_pipeline(email)

    if "error" in result:
        st.error(result["error"])

    else:
        st.success("Analysis Complete")

        risk = result["risk"]["risk"]
        score = result["risk"]["score"]

        st.subheader("📊 Risk Analysis")
        st.write(f"**Risk Level:** {risk}")
        st.write(f"**Score:** {score}")

        # Visualization
        st.subheader("📈 Risk Visualization")

        if risk == "UNKNOWN":
            st.warning("Risk cannot be determined for this email domain")
        else:
            st.progress(score / 100)
            st.write(f"Risk Score: {score} / 100")

        # Breach data
        st.subheader("🔍 Breach Data")
        st.json(result["data"])

        # Advice
        st.subheader("🛡 Recommendations")
        for tip in result["advice"]:
            st.write(f"- {tip}")

        # Logs
        st.subheader("🔄 Agent Execution Flow")
        for log in result["logs"]:
            st.write(log)

        # Download report
        report = json.dumps(result, indent=2)

        st.download_button(
            label="📥 Download Report",
            data=report,
            file_name="privacy_report.txt",
            mime="text/plain"
        )

# ---------------- DASHBOARD ---------------- #

st.subheader("📊 History Dashboard")

history = get_history()

if history:
    df = pd.DataFrame(history, columns=["Email", "Risk", "Score"])

    st.dataframe(df)

    st.subheader("📈 Risk Score Distribution")
    st.bar_chart(df["Score"])

else:
    st.info("No history available yet.")