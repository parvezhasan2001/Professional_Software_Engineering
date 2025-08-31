# Week-5 Activity - 7: Library Management System

# Description: This code demonstrates the use of inheritance and encapsulation in Python by creating a simple library management system. The base class is LibraryItem, which is inherited by Books and Magazines classes. The Library class manages a collection of these items, allowing adding, removing, and displaying items in the library.


class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}"

class Books(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title, author)

    def display_info(self):
        return super().display_info()

class Magazines(LibraryItem):
    def __init__(self, title, editor, issue_frequency):
        super().__init__(title, editor)
        self.__issue_frequency = issue_frequency

    def display_info(self):
        return super().display_info() + f", Issue Frequency: {self.__issue_frequency}"

class Library:
    def __init__(self):
        self.items = [] # list to store book and magazine items

    def add_item(self, item):
        self.items.append(item) # adding items to the library
        print(f"Added item: {item.title}")

    def remove_item(self, item):
        for i in self.items:
            if i.title == item.title:
                self.items.remove(i) # removing item from the library
                print(f"Removed item: {i.title}")
                return
        print(f"Item '{item.title}' not found in the library.")

    def display_items(self):
        if not self.items:
            print("No items in the library.")
        else:
            print("Items in the library:")
            for item in self.items:
                print(item.display_info()) # displaying item information

def main():
    
    #Creating Object
    library = Library()

    # Inserting Item
    book1 = Books("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Books("1984", "George Orwell")
    magazine1 = Magazines("National Geographic", "National Geographic Society", "Monthly")

    library.add_item(book1)
    library.add_item(book2)
    library.add_item(magazine1)

    # Displaying Items
    library.display_items()

    # Removing Items
    library.remove_item(book1)
    library.display_items()

if __name__ == "__main__":
    main()