# Exercise 6 - Number Guessing Game
# COP2002 - Python Programming
# Ozcan Celik

import random

def guessing_game():
    """Simple number guessing game using loops and conditionals."""
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("=" * 40)
    print("   NUMBER GUESSING GAME")
    print("=" * 40)
    print(f"Guess a number between 1 and 100.")
    print(f"You have {max_attempts} attempts.\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low! Try higher.\n")
        elif guess > secret:
            print("Too high! Try lower.\n")
        else:
            print(f"\nCorrect! The number was {secret}.")
            print(f"You got it in {attempts} attempt(s)!")
            return

    print(f"\nGame over! The number was {secret}.")

if __name__ == "__main__":
    guessing_game()
