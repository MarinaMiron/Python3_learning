from art import logo
import random

ANSWER = random.randint(1, 100)

def check_answer(number):
    """Compares the users guess and the correct answer."""
    if number == ANSWER:
        print(f"You got it! The answer was {ANSWER}.")
    elif number < ANSWER:
        print("Too low.")
        print("Guess again.")
    elif number > ANSWER:
        print("Too high.")
        print("Guess again.")

def difficulty():
    """Takes the difficulty mode and returns how many guesses does the user has."""
    difficulty_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    turns = 0
    if difficulty_mode == "easy":
        turns = 10
    elif difficulty_mode == "hard":
        turns = 5
    return turns
    
def game():
    """Takes the number guessed by the user. Compares the users guess to the actual number,
    until they run out of guesses."""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct answer is {ANSWER}.")
    guess = 0
    attempts = difficulty()
    while guess != ANSWER:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        check_answer(guess)
        attempts -= 1
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return

game()