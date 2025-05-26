# Number Guessing Game with Match Case Statements

## Overview

This project is a Python challenge designed to practice `match case` statements, user input, and basic game logic. The program creates an interactive number guessing game where the user tries to guess a randomly generated number between 1 and 10. The game uses `match case` to provide feedback on the guess, tracks the number of attempts (bonus challenge), and allows the user to play multiple rounds.

## Objectives

- Use the `random` module to generate a random number between 1 and 10.
- Prompt the user for a guess and validate it as an integer.
- Implement a `match case` statement to compare the guess with the secret number and provide feedback.
- Track the number of guesses taken to find the correct number (bonus).
- Allow the user to play again using an `if` statement and user input.

## Repository

- **GitHub Repository**: [alx_be_python](https://github.com/BunnyeNyash/alx_be_python.git)
- **Directory**: `number_guessing_game`

## Directory Structure

```
number_guessing_game/
├── number_guessing.py         # Main script for the number guessing game
└── README.md                  # Project documentation
```

## File Descriptions

- **number_guessing.py**:
  - Imports the `random` module to generate a secret number between 1 and 10.
  - Prompts the user to guess the number and converts the input to an integer.
  - Uses a `match case` statement to check if the guess is correct, too high, or too low, displaying appropriate messages.
  - Tracks the number of guesses (bonus) and displays it upon winning.
  - Asks the user if they want to play again and restarts the game if requested.
  - Example output: "Congratulations, you guessed it! It took you 3 guesses."

## Prerequisites

- **Python**: Version 3.10 or higher (required for `match case` statements)
- **Tools**: A code editor like VS Code, PyCharm, or IDLE and a terminal/command prompt


## Example Interaction

```bash
python3 number_guessing.py
I'm thinking of a number between 1 and 10. Can you guess it?
5
Nope, your guess is a bit low. Give it another shot!
7
Congratulations, you guessed it! It took you 2 guesses.
Play again? (yes/no)
yes
I'm thinking of a number between 1 and 10. Can you guess it?
...
```

## Notes

- Ensure Python 3.10 or higher is installed, as `match case` is not available in earlier versions.
- Refer to Python’s [official documentation](https://docs.python.org/3/) for details on `match case` and the `random` module.
