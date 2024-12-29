# Guess The Number Game

Create a Python program that implements a simple number guessing game.

The program should generate a random number between 1 and 100, and the user should try to guess the number.

The program provides feedback to the user after each guess, indicating whether the guess is too high, too low, or correct.

## Requirements:

### Random Number Generation:

Generate a random number between 1 and 100.

### User Interaction:

- Prompt the user to enter their guess.
- Ensure the input is a valid integer. If the input is invalid, inform the user and prompt them to enter a valid number.

### Feedback:

- If the user's guess is lower than the generated number, inform the user that their guess is too low.
- If the user's guess is higher than the generated number, inform the user that their guess is too high.
- If the user's guess is correct, congratulate the user and display the number of attempts it took to guess the number.

### Game Loop:

- Continue prompting the user for guesses until they guess the correct number.
- Keep track of the number of attempts the user makes.
