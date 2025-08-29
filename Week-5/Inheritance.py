# Week-5 Activity-3
# Inheritance Class Work


#Description: This code demonstrates the use of inheritance in Python by creating a 3 level class hierarchy for a university system. The Top level is the Person class, which is inherited by the Student and Staff classes. The Staff class is further specialized into Academic and General staff.

class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f"Name: {self.name}, ID: {self.id}")

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name, student_id)

class Staff(Person):
    def __init__(self, name, id, staff_id, tax_num):
        super().__init__(name, id)
        self.staff_id = staff_id
        self.tax_num = tax_num

    def display(self):
        super().display()
        print(f"Tax Number: {self.tax_num}")

class Academic(Staff):
    def __init__(self, name, id, staff_id, tax_num, publications):
        super().__init__(name, id, staff_id, tax_num)
        self.academic_id = staff_id
        self.publications = publications

    def display(self):
        super().display()
        print(f"Publications: {self.publications}")

class General(Staff):
    def __init__(self, name, id, staff_id, tax_num, rate_of_pay):
        super().__init__(name, id, staff_id, tax_num)
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