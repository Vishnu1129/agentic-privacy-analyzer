from tools.breach_api import check_breach

def data_finder_agent(email):
    return check_breach(email)