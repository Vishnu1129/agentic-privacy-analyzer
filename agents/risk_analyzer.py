# agents/risk_analyzer.py

def risk_analyzer_agent(data: dict) -> dict:
    if data["breach"]:
        if data["count"] >= 2:
            return {"risk": "HIGH", "score": 85}
        return {"risk": "MEDIUM", "score": 60}
    return {"risk": "LOW", "score": 20}