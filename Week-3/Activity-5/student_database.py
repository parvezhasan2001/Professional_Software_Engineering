from database import create_connection
import sqlite3


def add_user(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()


def add_student(name, address):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Students (Stu_name, Stu_address) VALUES (?, ?)", (name, address))
    conn.commit()
    print(" Student added successfully.")
    conn.close()

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students")
    rows = cursor.fetchall()
    conn.close()
    return rows
