# setup_db.py
import sqlite3

def setup_database():
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        product TEXT NOT NULL,
        amount REAL NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # Insert sample users
    cursor.executemany("""
    INSERT OR IGNORE INTO users (id, name, email) VALUES (?, ?, ?)
    """, [
        (1, "Alice", "alice@example.com"),
        (2, "Bob", "bob@example.com"),
    ])

    # Insert sample orders
    cursor.executemany("""
    INSERT OR IGNORE INTO orders (id, user_id, product, amount) VALUES (?, ?, ?, ?)
    """, [
        (1, 1, "Laptop", 1200.50),
        (2, 1, "Mouse", 25.00),
        (3, 2, "Keyboard", 75.99),
    ])

    conn.commit()
    conn.close()
    print("✅ Database setup completed!")

if __name__ == "__main__":
    setup_database()
