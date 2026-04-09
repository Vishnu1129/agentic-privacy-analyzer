def advisor_agent(risk_data):
    if risk_data["risk"] == "HIGH":
        return ["Change passwords", "Enable 2FA"]

    elif risk_data["risk"] == "MEDIUM":
        return ["Update passwords", "Enable 2FA"]

    elif risk_data["risk"] == "UNKNOWN":
        return ["Unknown email domain"]

    else:
        return ["Your data looks safe"]