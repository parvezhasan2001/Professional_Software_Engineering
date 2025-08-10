# Week-2 Activity-5
# Develop a project using class and methods to get a sentence from user input and find the number of words in it. Share your GitHub link at the end


class words:
    def __init__(self, sentence):
        self.sentence = sentence

    def count_words(self):
        return len(self.sentence.split())
    
    def find_character(self, char):
        return self.sentence.find(char)
    
def main():
    user_input = input("Enter a sentence: ")
    word_counter = words(user_input)
    print("Number of words:", word_counter.count_words())
    char_to_find = input("Enter a character to find: ")
    print("Character found at index:", word_counter.find_character(char_to_find))

if __name__ == "__main__":
    main()