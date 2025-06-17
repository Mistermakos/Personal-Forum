import sqlite3
from databaseManager import get_connection

class Comment:
    def __init__(self, user_id, post_id, comment_text, id=None):
        self.id = id
        self.user_id = user_id
        self.post_id = post_id
        self.comment_text = comment_text

    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        if self.id:
            cur.execute("UPDATE comments SET UserId=?, PostId=?, Comment=? WHERE CommentId=?",
                        (self.user_id, self.post_id, self.comment_text, self.id))
        else:
            cur.execute("INSERT INTO comments (UserId, PostId, Comment) VALUES (?, ?, ?)",
                        (self.user_id, self.post_id, self.comment_text))
            self.id = cur.lastrowid
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(comment_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT CommentId, UserId, PostId, Comment FROM Comments WHERE id=?", (comment_id,))
        row = cur.fetchone()
        conn.close()
        if row:
            return Comment(row["UserId"], row["PostId"], row["Comment"], id=row["CommentId"])
        return None

    @staticmethod
    def get_all():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT CommentId, UserId, PostId, Comment FROM Comments")
        rows = cur.fetchall()
        conn.close()
        return [Comment(row["UserId"], row["PostId"], row["Comment"], id=row["CommentId"]) for row in rows]

    @staticmethod
    def delete(comment_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM Comments WHERE CommentId=?", (comment_id,))
        conn.commit()
        conn.close()
