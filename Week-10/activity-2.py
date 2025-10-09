#Week-10
#Activity-2
#Learning how pylint works

class TextAnalyzer:
    def analyze(self, text):
        total_length = len(text)
        return total_length
    def count_uppercase(self, text):
        uppercase_count = 0
        for char in text:
            if char.isupper():
                uppercase_count += 1

        return uppercase_count
    def analyze_digits(self, text):
        digit_count = 0
        for char in text:
            if char.isdigit():
                digit_count += 1

        return digit_count
    def analyze_special_characters(self, text):
        special_count = 0
        for char in text:
            if not char.isalnum():
                special_count += 1

        return special_count

def main():
    analyzer = TextAnalyzer()
    user_input = input("Enter text to analyze: ")
    print(f"Total length: {analyzer.analyze(user_input)}")
    print(f"Uppercase letters: {analyzer.count_uppercase(user_input)}")
    print(f"Digits count: {analyzer.analyze_digits(user_input)}")
    print(f"Special characters: {analyzer.analyze_special_characters(user_input)}")
if __name__ == "__main__":
    main() 