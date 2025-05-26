# number_guessing.py
# A simple number guessing game where the player has to guess a randomly generated number between 1 and 100.

# Import the random module
import random

# welcome message and game setup
print("Welcome to the Number Guessing Game!\n")

while True:
    play = input("Do you want to play? (Y/N): ").strip().upper()
    if play == 'Y':
        print("Great! Let's start the game.\n")
        break
    elif play == "N":
        print("Okay, maybe next time. Byeee.")
        exit()
    else:
        print("Please enter 'Y' for Yes or 'N' for No.")

# Replay
while True:
    secret_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    guess_count = 0  # Initialize the guess counter
    first_attempt = True    # Intro line to be shown only once

    while True:
        try:
            # Ask the user for the guess
            if first_attempt:
                guess = int(input("I'm thinking of a number between 1 and 100. Can you guess it?\n"))
                first_attempt = False   # Update the first_attempt value
            else:
                guess = int(input())
            guess_count += 1

            # Match case to check the user's guess
            match guess:
                case _ if guess == secret_number:
                    print("Congratulations, you guessed it!")
                    # Display the number of guesses taken
                    print(f"It took you {guess_count} guesses to win the game")
                    break
                case _ if guess > secret_number:
                    if guess > 100:
                        print("Invalid input. Please enter a number between 1 and 100.")
                    else:
                        print("Oops, your guess is a bit high. Give it another shot!")
                case _ if guess < secret_number:
                    if guess < 1:
                        print("Invalid input. Please enter a number between 1 and 100.")
                    else:
                        print("Nope, your guess is a bit low. Give it another shot!")

        except ValueError:
            print("Invalid input! Please enter a number.")

    while True:
        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again == "yes":
            print("... (new game starts)")
            break
        elif play_again == "no":
            print("Okay, Thanks for playing. Byee.")
            exit()
        else:
            print("Invalid input! Please enter yes or no.")
