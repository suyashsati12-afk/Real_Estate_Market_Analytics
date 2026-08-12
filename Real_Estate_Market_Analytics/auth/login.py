import sqlite3
import bcrypt
import os

# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database path
DB_PATH = os.path.join(BASE_DIR, "database", "users.db")


def login_user(username, password):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM users WHERE username=?",
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        return bcrypt.checkpw(
            password.encode(),
            user[0]
        )

    return False
