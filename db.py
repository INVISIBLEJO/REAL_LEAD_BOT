import sqlite3

DB_NAME = "leads.db"

def get_db():
    return sqlite3.connect(DB_NAME)