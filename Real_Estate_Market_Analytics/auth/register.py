import sqlite3
import bcrypt

def register_user(username, password):

    conn = sqlite3.connect("database/users.db")
    cursor = conn.cursor()

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    try:
        cursor.execute(
            "INSERT INTO users(username, password) VALUES(?, ?)",
            (username, hashed_password)
        )

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()