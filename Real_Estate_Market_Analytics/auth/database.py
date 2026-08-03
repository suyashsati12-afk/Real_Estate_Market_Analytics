import sqlite3

def create_database():
    conn = sqlite3.connect("database/users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database created successfully!")