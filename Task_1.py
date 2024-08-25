import random

def select_random_word():
    words = ['python', 'hangman', 'programming', 'algorithm', 'engineering', 'development', 'computer']
    return random.choice(words)

def display_current_progress(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman_game():
    word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print(f"You have {max_incorrect_guesses} chances to guess the word.")

    while incorrect_guesses < max_incorrect_guesses:
        print("\nCurrent progress: " + display_current_progress(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nSorry, you've run out of guesses. The word was: {word}")

if __name__ == "__main__":
    hangman_game()
