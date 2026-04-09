from agents.data_finder import data_finder_agent
from agents.risk_analyzer import risk_analyzer_agent
from agents.advisor import advisor_agent
from database import save_result

def validate_input(email):
    return "@" in email and "." in email

def run_pipeline(email):
    if not validate_input(email):
        return {"error": "Invalid email"}

    logs = []

    logs.append("🔍 Data Finder Agent")
    data = data_finder_agent(email)

    logs.append("📊 Risk Analyzer Agent")
    risk = risk_analyzer_agent(data)

    logs.append("🛡 Advisor Agent")
    advice = advisor_agent(risk)

    # Save to DB
    save_result(email, risk["risk"], risk["score"])

    return {
        "data": data,
        "risk": risk,
        "advice": advice,
        "logs": logs
    }