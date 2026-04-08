# main.py
from agents.data_finder import data_finder_agent
from agents.risk_analyzer import risk_analyzer_agent
from agents.advisor import advisor_agent

def validate_input(email: str) -> bool:
    return "@" in email and "." in email

def run_pipeline(email: str) -> dict:
    if not validate_input(email):
        return {"error": "Invalid email format"}

    logs = []

    logs.append("🔍 Data Finder Agent started")
    data = data_finder_agent(email)
    logs.append(f"✅ Data Found: {data}")

    logs.append("📊 Risk Analyzer Agent started")
    risk = risk_analyzer_agent(data)
    logs.append(f"✅ Risk Calculated: {risk}")

    logs.append("🛡 Privacy Advisor Agent started")
    advice = advisor_agent(risk)
    logs.append("✅ Advice Generated")

    return {
        "data": data,
        "risk": risk,
        "advice": advice,
        "logs": logs
    }