import sqlite3
import os

def create_connection():
    db_file = os.getenv("SQLITE_DB_FILE")

    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print(f"Success'{db_file}' ")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    return connection
