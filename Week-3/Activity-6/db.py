import sqlite3

def create_connection():
    conn = sqlite3.connect("student_management.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Students (
                       Stu_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       Stu_name TEXT NOT NULL,
                       Stu_age INTEGER NOT NULL,
                       Stu_email TEXT NOT NULL,
                       Stu_phone TEXT NOT NULL,
                       Stu_date DATE NOT NULL,
                       Stu_address TEXT NOT NULL
                   )
                   ''')
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Courses (
                       Course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       Course_name TEXT NOT NULL,
                       Course_credits INTEGER NOT NULL,
                       Course_description TEXT NOT NULL
                   )
                   ''')
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Lectures (
                       Lecture_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       Lecture_name TEXT NOT NULL,
                       Lecture_email TEXT NOT NULL,
                       Lecture_phone TEXT NOT NULL,
                       Lecture_topic TEXT NOT NULL,
                       Lecture_date DATE NOT NULL
                   )
                   ''')
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Enrollements (
                       Enrol_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       Stu_id INTEGER NOT NULL,
                       Course_id INTEGER NOT NULL,
                       Enrol_date DATE NOT NULL,
                       FOREIGN KEY (Stu_id) REFERENCES Students (Stu_id),
                       FOREIGN KEY (Course_id) REFERENCES Courses (Course_id)
                   )
                   ''')
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Assessments (
                       Assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       Course_id INTEGER NOT NULL,
                       Assessment_name TEXT NOT NULL,
                       Assessment_date DATE NOT NULL,
                       FOREIGN KEY (Course_id) REFERENCES Courses (Course_id)
                   )
                   ''')
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Classes (
                       Class_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       Course_id INTEGER NOT NULL,
                       Lecture_id INTEGER NOT NULL,
                       Class_date DATE NOT NULL,
                       FOREIGN KEY (Course_id) REFERENCES Courses (Course_id),
                       FOREIGN KEY (Lecture_id) REFERENCES Lectures (Lecture_id)
                   )
                   ''')
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Results (
                       Result_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       Stu_id INTEGER NOT NULL,
                       Assessment_id INTEGER NOT NULL,
                       Result_score REAL NOT NULL,
                       FOREIGN KEY (Stu_id) REFERENCES Students (Stu_id),
                       FOREIGN KEY (Assessment_id) REFERENCES Assessments (Assessment_id)
                   )
                   ''')
    conn.commit()
    conn.close()