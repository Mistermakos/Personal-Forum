import sqlite3
import os

def create_connection():
    db_file = os.getenv("SQLITE_DB_FILE")

    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print(f"Połączenie z bazą SQLite '{db_file}' zostało nawiązane")
    except sqlite3.Error as e:
        print(f"Wystąpił błąd: {e}")
    return connection
