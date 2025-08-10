#Week-2 Activity -6 

#Create an interactive Python program that collects a user’s name, age, and address, stores them in a list called personal_details, and prints each detail with labels. Then, ask the user to enter how many years to add to their current age, update the age in the list, and display the updated information in a formatted sentence.


class PersonalDetails:
    def __init__(self):
        self.personal_details = []

    def collect_details(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        address = input("Enter your address: ")
        self.personal_details = [name, age, address]

    def display_details(self):
        if not self.personal_details:
            print("No personal details available. Please collect details first.")
            return
        print("Personal Details:")
        print(f"Name: {self.personal_details[0]}")
        print(f"Age: {self.personal_details[1]}")
        print(f"Address: {self.personal_details[2]}")

    def update_details(self, name=None, age=None, address=None):
        if name:
            self.personal_details[0] = name
        if age is not None:
            self.personal_details[1] += age 
        if address:
            self.personal_details[2] = address

def main():
    details = PersonalDetails()
    details.collect_details()
    details.display_details()

    add_years = int(input("How many years do you want to add to your age? "))
    details.update_details(age=add_years)

    print("\nUpdated Personal Details:")
    details.display_details()

if __name__ == '__main__':
    main()

