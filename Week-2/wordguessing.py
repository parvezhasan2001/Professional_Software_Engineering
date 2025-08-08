# Word Guessing Game
# Week 2 Word guessing game
import random

def word_guessing_game():
    secret_words = ("python", "driving", "hiking", "surfing")
    word = random.choice(secret_words).lower()
    lives = 5
    
    print("\nI have chosen a word. Can you guess it?")
    while lives > 0:
        guess = input("Enter your guess: ").lower()
        
        if guess == word:
            print(f"🎉 Congratulations! You've guessed the word: {word}")
            return "You Win!"
        
        else:
            lives -= 1
            if lives > 0:
                print("❌ Wrong guess. Try again.")
                print(f"Lives left: {lives}")
            else:
                print(f"💀 Game Over! The word was: {word}")
                return "You Lose!"

def main():
    print("Welcome to the Word Guessing Game!")
    result = word_guessing_game()
    print(result)

if __name__ == "__main__":
    main()
