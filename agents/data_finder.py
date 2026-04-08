# agents/data_finder.py
from tools.breach_api import check_breach

def data_finder_agent(email: str) -> dict:
    return check_breach(email)