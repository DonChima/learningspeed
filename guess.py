import random

def number_guessing_game():
    """A simple number guessing game."""

    # The computer picks a random number between 1 and 10
    secret_number = random.randint(1, 10)
    attempts = 0

    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess
            if guess == secret_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Run the game
number_guessing_game()
