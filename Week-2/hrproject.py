# Week 2 - Activity 7 : Develop a basic HR project using OO - Due date 15.8.25, 11:59 PM.
 
# You are tasked with developing a simple program for the Human Resources (HR) department to store and display basic employee information, including each employee’s name, salary, and job title.
# Requirements:
# Create at least two Employee objects with different data.
# Call the display_info() method to show each employee’s details.
# Call the give_raise() method to increase an employee’s salary and display the updated amount.
 
# Share your GitHub link here.
 
class Employee:
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Job Title: {self.job_title}")

    def give_raise(self, amount):
        self.salary += amount
        print(f"New salary for {self.name}: {self.salary}")
        
if __name__ == '__main__':
    emp1 = Employee("Alice", 50000, "Software Engineer")
    emp2 = Employee("Bob", 60000, "Data Scientist")

    emp1.display_info()
    emp2.display_info()

    emp1.give_raise(5000)
    emp2.give_raise(7000)