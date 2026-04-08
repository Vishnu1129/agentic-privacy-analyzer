# tools/breach_api.py

def check_breach(email: str) -> dict:
    """
    Deterministic breach checker
    Same input → same output always
    """

    email = email.lower()

    if "test" in email:
        return {
            "breach": True,
            "sites": ["example.com", "oldforum.net"],
            "count": 2
        }

    elif "gmail" in email:
        return {
            "breach": False,
            "sites": [],
            "count": 0
        }

    elif "yahoo" in email:
        return {
            "breach": True,
            "sites": ["yahoo-leak.com"],
            "count": 1
        }

    else:
        return {
            "breach": False,
            "sites": [],
            "count": 0
        }