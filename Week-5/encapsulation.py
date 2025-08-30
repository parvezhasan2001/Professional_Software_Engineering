# Week-5 Activity-6


# Description: Demonstrating encapsulation in Python with private and protected attributes by creating and adding a new class teacher which has salary information as private attribute. subject as protected attribute. and in class student the new grade is a private attribute.


class Student:
    def __init__(self,name,age):
        self.name = name
        self._age = age
        self.__grade = 'A'

    def get_grades(self):
        return self.__grade

    def upgrade_grades(self, new_grade):
        self.__grade = new_grade
        return self.__grade

class Teacher:
    def __init__(self,name,subject):
        self.name = name
        self._subject = subject
        self.__salary = 50000

    def get_salary(self):
        return self.__salary

    def show_info(self):
        return f"Name: {self.name}, Subject: {self._subject}"

def main():
    s = Student("Ali", 20)
    print(s.name)        # Accessible
    print(s._age)       # Accessible but should be treated as protected
    print(s.get_grades())  # Accessible through a public method

    print(s.upgrade_grades("B"))
    print(s.get_grades())   

    t = Teacher("Mr. Smith", "Mathematics")
    print(t.name)        # Accessible
    print(t._subject)   # Accessible but should be treated as protected
    print(t.get_salary())  # Accessible through a public method
    print(t.show_info())

if __name__ == "__main__":
    main()