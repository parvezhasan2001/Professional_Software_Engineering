# Week-3 Activity-6

from random import choice
from db import create_table
from yoobee import add_user, view_students, search_student, delete_student

def menu():
    print("\n--- Yoobee Management System ---")
    print("1. Add Student")
    print("2. Add Courses")
    print("3. Add Lectures")
    print("4. Add Enrollments")
    print("5. Add Assessments")
    print("6. Add Classes")
    print("7. View Students")
    print("8. Search Student")
    print("9. Delete Student")
    print("10. View Courses")
    print("11. View Enrollments")
    print("12. Delete Course")
    print("13. Delete Enrollment")
    print("14. Exit")
    choice = input("Enter your Choice: ")
    return choice

def main():
    create_table()
    while True:
        choice = menu()
        if choice == '1':
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            email = input("Enter student email: ")
            phone = input("Enter student phone: ")
            date = input("Enter student date: ")
            address = input("Enter student address: ")
            add_user((name, age, email, phone, date, address))
        elif choice == '7':
            students = view_students()
            for student in students:
                print(student)
        elif choice == '8':
            name = input("Enter student name to search: ")
            students = search_student(name)
            for student in students:
                print(student)
        elif choice == '9':
            stu_id = input("Enter student ID to delete: ")
            delete_student(stu_id)
        elif choice == '14':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()