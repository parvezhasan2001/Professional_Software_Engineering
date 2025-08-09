# Week -2 Activity- 4

class StringManipulator:
    def find_character(self, text, char):
        return text.find(char)

    def find_string_length(self, text):
        return len(text)

    def upper_case(self,text):
        return text.upper()

def main():
    name = StringManipulator()

    result = name.find_character("Finder","n")
    result1 = name.find_string_length("Finder")
    result2 = name.upper_case("Finder")


    print(result)
    print(result1)
    print(result2)


if __name__ == '__main__':
    main()


# Describe the benefit of using init method in your code as a comment in short paragraph. Please share your GitHub link when you have done.

"""init method is a special method in Python classes that is used for initializing object it ensures user readability and maintainability of the code by not having to repeat the initialization again and again. It allows us to set the initial state of an object and define its attributes at the time of creation."""