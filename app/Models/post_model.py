import sqlite3
from databaseManager import get_connection

class Post:
    def __init__(self, user_id, title, post_content, id=None):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.post_content = post_content

    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        if self.id:
            cur.execute("UPDATE Posts SET UserId=?, Title=?, PostContent=? WHERE PostId=?",
                        (self.user_id, self.title, self.post_content, self.id))
        else:
            cur.execute("INSERT INTO Posts (UserId, Title, PostContent) VALUES (?, ?, ?)",
                        (self.user_id, self.title, self.post_content))
            self.id = cur.lastrowid
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(post_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT PostId, UserId, Title, PostContent FROM Posts WHERE PostId=?", (post_id,))
        row = cur.fetchone()
        conn.close()
        if row:
            return Post(row["UserId"], row["Title"], row["PostContent"], id=row["PostId"])
        return None

    @staticmethod
    def get_all():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT PostId, UserId, Title, PostContent FROM Posts")
        rows = cur.fetchall()
        conn.close()
        return [Post(row["UserId"], row["Title"], row["PostContent"], id=row["PostId"]) for row in rows]

    @staticmethod
    def delete(post_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM Posts WHERE PostId=?", (post_id,))
        conn.commit()
        conn.close()
