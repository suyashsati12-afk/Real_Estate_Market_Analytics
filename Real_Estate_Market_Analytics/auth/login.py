import sqlite3
import bcrypt

def login_user(username, password):

    conn = sqlite3.connect("database/users.db")
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