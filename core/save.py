import sqlite3
from datetime import datetime

def save_lead(data):
    conn = sqlite3.connect("leads.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS leads (
        id INTEGER PRIMARY KEY,
        intent TEXT,
        location TEXT,
        budget TEXT,
        timeline TEXT,
        contact TEXT,
        score INTEGER,
        created_at TEXT
    )
    """)

    cur.execute("""
    INSERT INTO leads VALUES (NULL,?,?,?,?,?,?,?)
    """, (
        data["intent"],
        data["location"],
        data["budget"],
        data["timeline"],
        data["contact"],
        data["score"],
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()
