import random

# List of 5 predefined words
words = ["python", "hangman", "program", "computer", "developer"]
print("choice from this",words)

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_wrong = 6
wrong_guesses = 0

print(" WELCOME TO HANGMAN GAME ")
print("Guess the word one letter at a time.")
print(f"You have {max_wrong} incorrect guesses.\n")

# Main game loop
while wrong_guesses < max_wrong:

    # Display the current word
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)

    # Check if the player has guessed the complete word
    if all(letter in guessed_letters for letter in word):
        print("\n CONGRATULATIONS! You guessed the word:", word.upper())
        break

    print("Guessed letters:", " ".join(guessed_letters))

    # Take input from player
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter a single alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    # Add the letter to guessed letters
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print(" Good guess!")
    else:
        wrong_guesses += 1
        print(f"Wrong guess! ({wrong_guesses}/{max_wrong})")

# Game over
if wrong_guesses == max_wrong:
    print("\n GAME OVER!")
    print("The word was:", word.upper())