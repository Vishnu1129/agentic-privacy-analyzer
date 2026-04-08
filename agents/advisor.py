# agents/advisor.py

def advisor_agent(risk_data: dict) -> list:
    if risk_data["risk"] == "HIGH":
        return [
            "Change all passwords immediately",
            "Enable 2FA on all accounts",
            "Check suspicious login activity"
        ]
    elif risk_data["risk"] == "MEDIUM":
        return [
            "Update important passwords",
            "Enable 2FA where possible"
        ]
    else:
        return [
            "Your data looks safe",
            "Maintain good password hygiene"
        ]