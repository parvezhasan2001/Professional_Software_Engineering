# Week -2 Activity- 3

class StringManipulator:
    def __init__(self, text):
        self.text = text

    def find_character(self, char):
        return self.text.find(char)

    def find_string_length(self):
        return len(self.text)

name = StringManipulator("Example")

result = name.find_character("x")
result1 = name.find_string_length()

print(result)
print(result1)