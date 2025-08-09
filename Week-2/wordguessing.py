# Word Guessing Game
# Week 2 Word guessing game
import random

# def word_guessing_game():
#     secret_words = ("python", "driving", "hiking", "surfing")
#     word = random.choice(secret_words).lower()
#     lives = 3
    
#     print("\nI have chosen a word. Can you guess it?")
#     while lives != 0:
#         guess = input("Enter your guess: ").lower()
        
#         if guess == word:
#             print(f" Congratulations! You've guessed the word: {word}")
#             return "You Win!"
        
#         else:
#             lives -= 1
#             if lives != 0:
#                 print("Wrong guess. Try again.")
#                 print(f"Lives left: {lives}")
#             else:
#                 print(f"Game Over! The word was: {word}")
#                 return "You Lose!"


# Update WordGuessingGame class with Activity -2 requirements

class WordGuessingGame:
    def __init__(self):
        self.secret_words = ("python", "driving", "hiking", "surfing")
        self.word = random.choice(self.secret_words).lower()
        self.lives = 3

    def play(self):
        print("I have chosen a word. Can you guess it?")
        while self.lives != 0:
            guess = input("Enter your guess: ").lower()

            if guess == self.word:
                print("Congratulations! You've guessed the word: {self.word}")
                return "You Win!"

            else:
                self.lives -= 1
                if self.lives != 0:
                    print("Wrong guess. Try again.")
                    print(f"Lives left: {self.lives}")
                else:
                    print(f"Game Over! The word was: {self.word}")
                    return "You Lose!"
                

def main():
    print("Welcome to the Word Guessing Game!")
    game = WordGuessingGame()
    result = game.play()
    print(result)

if __name__ == "__main__":
    main()
