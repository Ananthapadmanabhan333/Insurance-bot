import sqlite3

def create_complaint(user_id, message, sentiment):
    conn = sqlite3.connect("insurance.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            message TEXT,
            sentiment TEXT
        )
    """)

    c.execute(
        "INSERT INTO complaints (user_id, message, sentiment) VALUES (?, ?, ?)",
        (user_id, message, sentiment)
    )
    conn.commit()
    complaint_id = c.lastrowid
    conn.close()
    return complaint_id
