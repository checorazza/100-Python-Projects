import random

def guess_the_number():
    number_to_guess = random.randint(1, 100) # Generate a random number between 1 and 100
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Guess the Number game!")
    print("I have selected a number between 1 and 100.")
    print("Can you guess what it is?")

    while not guessed_correctly:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

guess_the_number()