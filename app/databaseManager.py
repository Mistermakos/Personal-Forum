import sqlite3
import os

DB_FILENAME = os.path.join("data", "database.db")
SQL_SCRIPT  = os.path.join("data", "database.sql")

def get_connection():
    conn = sqlite3.connect(DB_FILENAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    # it creates db only if one does not exit
    if not os.path.exists(DB_FILENAME):
        conn = get_connection()
        with open(SQL_SCRIPT, 'r', encoding='utf-8') as f:
            conn.executescript(f.read())
        conn.close()