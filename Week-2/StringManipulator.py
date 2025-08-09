# Week -2 Activity- 3

class StringManipulator:
    def __init__(self, text):
        self.text = text

    def find_character(self, char):
        return self.text.find(char)

    def find_string_length(self):
        return len(self.text)

    def upper_case(self):
        return self.text.upper()

def main():
    name = StringManipulator("finder")

    result = name.find_character("n")
    result1 = name.find_string_length()
    result2 = name.upper_case()


    print(result)
    print(result1)
    print(result2)


if __name__ == '__main__':
    main()