# Week-5 Activity-3
# Inheritance Class Work


#Description: This code demonstrates the use of inheritance in Python by creating a 3 level class hierarchy for a university system. The Top level is the Person class, which is inherited by the Student and Staff classes. The Staff class is further specialized into Academic and General staff.

# display() in student sub class is overriding the parent class and adding student ID

class Person:
    def __init__(self, name, id, address, age):
        self.name = name
        self.address = address
        self.age = age
        self.id = id

    def display(self):
        print(f"Name: {self.name}, ID: {self.id}, Address: {self.address}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, student_id, address, age):
        super().__init__(name, address, age)
        self.student_id = student_id

    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}")

class Staff(Person):
    def __init__(self, name, staff_id, tax_num, address, age):
        super().__init__(name, address, age)
        self.staff_id = staff_id
        self.tax_num = tax_num

    def display(self):
        super().display()
        print(f"Tax Number: {self.tax_num}")

class Academic(Staff):
    def __init__(self, name, id, staff_id, tax_num, publications, address, age):
        super().__init__(name, id, staff_id, tax_num, address, age)
        self.academic_id = staff_id
        self.publications = publications

    def display(self):
        super().display()
        print(f"Publications: {self.publications}")

class General(Staff):
    def __init__(self, name, id, staff_id, tax_num, rate_of_pay, address, age):
        super().__init__(name, id, staff_id, tax_num, address, age)
        self.general_id = staff_id
        self.rate_of_pay = rate_of_pay

    def display(self):
        super().display()
        print(f"Rate of Pay: {self.rate_of_pay}")

def main():
    p = Person("Alice", 101)
    s = Student("Bob", "S123")
    st = Staff("Charlie", 201, "ST456", "TX789")
    a = Academic("David", 301, "AC111", "TX222", ["Paper1", "Paper2"])
    g = General("Eva", 401, "GN555", "TX333", 50.0)

    print("=== Person ===")
    p.display()
    print("\n=== Student ===")
    s.display()
    print("\n=== Staff ===")
    st.display()
    print("\n=== Academic Staff ===")
    a.display()
    print("\n=== General Staff ===")
    g.display()


if __name__ == "__main__":
    main()