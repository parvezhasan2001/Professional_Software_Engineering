from db import create_connection
import sqlite3

def add_user(user_data):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
                   INSERT INTO Students (Stu_name, Stu_age, Stu_email, Stu_phone, Stu_date, Stu_address)
                   VALUES (?, ?, ?, ?, ?, ?)
                   ''', user_data)
    print("Student added successfully.")
    conn.commit()
    conn.close()

def add_course(course_data):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
                   INSERT INTO Courses (Course_name, Course_credits, Course_description)
                   VALUES (?, ?, ?)
                   ''', course_data)
    print("Course added successfully.")
    conn.commit()
    conn.close()

def add_lecture(lecture_data):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
                   INSERT INTO Lectures (Course_id, Lecture_title, Lecture_date, Lecture_duration)
                   VALUES (?, ?, ?, ?)
                   ''', lecture_data)
    print("Lecture added successfully.")
    conn.commit()
    conn.close()


def add_assessment(assessment_data):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
                   INSERT INTO Assessments (Course_id, Assessment_title, Assessment_date, Assessment_weight)
                   VALUES (?, ?, ?, ?)
                   ''', assessment_data)
    print("Assessment added successfully.")
    conn.commit()
    conn.close()

def add_class(class_data):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
                   INSERT INTO Classes (Class_name, Class_location, Class_time, Course_id)
                   VALUES (?, ?, ?, ?)
                   ''', class_data)
    print("Class added successfully.")
    conn.commit()
    conn.close()

def add_enrollment(enrollment_data):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
                   INSERT INTO Enrollments (Stu_id, Course_id, Enrol_date)
                   VALUES (?, ?, ?)
                   ''', enrollment_data)
    print("Enrollment added successfully.")
    conn.commit()
    conn.close()

def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT * FROM Students
                   ''')
    students = cursor.fetchall()
    conn.close()
    return students

def view_courses():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT * FROM Courses
                   ''')
    courses = cursor.fetchall()
    conn.close()
    return courses


def view_enrollments():
   conn = create_connection()
   cursor = conn.cursor()
   cursor.execute('''
                   SELECT * FROM Enrollments
                   ''')
   enrollments = cursor.fetchall()
   conn.close()
   return enrollments


def search_student(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT * FROM Students WHERE Stu_name LIKE ?
                   ''', ('%' + name + '%',))
    students = cursor.fetchall()
    conn.close()
    return students

def delete_student(stu_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
                   DELETE FROM Students WHERE Stu_id = ?
                   ''', (stu_id,))
    conn.commit()
    conn.close()

def delete_course(course_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
                   DELETE FROM Courses WHERE Course_id = ?
                   ''', (course_id,))
    conn.commit()
    conn.close()

def delete_enrollment(enrol_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
                   DELETE FROM Enrollments WHERE Enrol_id = ?
                   ''', (enrol_id,))
    conn.commit()
    conn.close()
