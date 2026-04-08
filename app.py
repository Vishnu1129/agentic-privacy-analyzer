# app.py
import streamlit as st
import json
from main import run_pipeline

# Page settings
st.set_page_config(page_title="Agentic Privacy Analyzer", layout="centered")

# Title
st.markdown("""
# 🔐 Agentic Digital Footprint Analyzer
### Protect your online identity with AI agents
""")

st.markdown("---")

# Warning
st.warning("⚠️ Only analyze emails you own or have permission to check")

# Input
email = st.text_input("Enter your email")

# Button
if st.button("Analyze"):
    with st.spinner("Agents are analyzing your data..."):
        result = run_pipeline(email)

    if "error" in result:
        st.error(result["error"])
    else:
        st.success("Analysis Complete")

        # Risk
        st.subheader("📊 Risk Analysis")
        st.write(f"**Risk Level:** {result['risk']['risk']}")
        st.write(f"**Score:** {result['risk']['score']}")

        # Clean Visualization
        st.subheader("📈 Risk Visualization")
        st.progress(result["risk"]["score"] / 100)
        st.write(f"Risk Score: {result['risk']['score']} / 100")

        # Breach Data
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
        report = {
            "email": email,
            "risk": result["risk"],
            "data": result["data"],
            "advice": result["advice"]
        }

        report_str = json.dumps(report, indent=2)

        st.download_button(
            label="📥 Download Report",
            data=report_str,
            file_name="privacy_report.txt",
            mime="text/plain"
        )