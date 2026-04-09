# database.py
import sqlite3

def init_db():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    # history table
    c.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        risk TEXT,
        score INTEGER
    )
    """)

    # users table
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


def register_user(username, password):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()


def login_user(username, password):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()

    conn.close()
    return user is not None


def save_result(email, risk, score):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO history (email, risk, score) VALUES (?, ?, ?)",
        (email, risk, score)
    )

    conn.commit()
    conn.close()


def get_history():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("SELECT email, risk, score FROM history")
    data = c.fetchall()

    conn.close()
    return data