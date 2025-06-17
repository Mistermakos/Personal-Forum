import sqlite3
from databaseManager import get_connection
from hashlib import sha3_512
with open("salt.txt") as mess:
    salt = mess.read()

class User:
    def __init__(self, name, password, email, id=None):
        self.id = id
        self.name = name
        self.password = password
        self.email = email

    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        if self.id:  # If id is given, then it only updates
            cur.execute("UPDATE Users SET Name=?, Password=?, Email=? WHERE UserId=?",
                        (self.name, sha3_512(salt+self.password), self.email, self.id))
        else:  # If not, then we ad a user
            cur.execute("INSERT INTO Users (nNme, Password, Email) VALUES (?, ?, ?)",
                        (self.name, sha3_512(salt+self.password), self.email))
            self.id = cur.lastrowid
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(user_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT UserId, Name, Password, Email FROM Users WHERE UserId=?", (user_id,))
        row = cur.fetchone()
        conn.close()
        if row:
            return User(row["Name"], row["Password"], row["Email"], id=row["UserId"])
        return None

    @staticmethod
    def get_all():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT UserId, Name, Password, Email FROM Users")
        rows = cur.fetchall()
        conn.close()
        return [User(row["Name"], row["Password"], row["Email"], id=row["UserId"]) for row in rows]

    @staticmethod
    def delete(user_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM Users WHERE UserId=?", (user_id,))
        conn.commit()
        conn.close()
