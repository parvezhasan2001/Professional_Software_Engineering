# Week-3 Activity -5

from database import create_table
from student_database import add_user, add_student, view_users, view_students

def menu():
    print("\n==== Student Manager ====")
    print("1. Add User")
    print("2. Add Student")
    print("3. View Users")
    print("4. View Students")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    create_table()
    while True:
        choice = menu()
        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == "2":
            name = input("Enter student name: ")
            address = input("Enter student address: ")
            add_student(name, address)
        elif choice == "3":
            users = view_users()
            print("=== Show Users ===")
            for user in users:
                print(f"Name: {user[1]}, Email: {user[2]}")
        elif choice == "4":
            students = view_students()
            print("=== Show Students ===")
            for student in students:
                print(f"Name: {student[1]}, Address: {student[2]}")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()