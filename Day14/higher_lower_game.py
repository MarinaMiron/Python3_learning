from art import *
from game_data import data
import random
from replit import clear

def get_name():
    """Generate a random choice and removes it from the dictionary,
    to make sure we don't have duplicates"""
    choice = random.choice(data)
    data.remove(choice)
    return choice

def compare(choice_a, choice_b):
    """Compares the follower number and returns 'a' for the first
     and 'b' for the second"""
    answer_a = "a"
    answer_b = "b"
    if choice_a["follower_count"] > choice_b["follower_count"]:
        return answer_a
    else:
        return answer_b

def game():
    choice_a = get_name()
    choice_b = get_name()
    score = 0
    should_continue = True
    while should_continue:
        print(logo)
        print(f'Compare A: {choice_a["name"]}, {choice_a["description"]}, from {choice_a["country"]}.')
        print(vs)
        print(f'Against B: {choice_b["name"]}, {choice_b["description"]}, from {choice_b["country"]}.')
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        answer = compare(choice_a, choice_b)
        clear()
        print(logo)
        if guess == answer:
            score += 1
            print(f"You're right! Current score: {score}.")
            choice_a = choice_b
            choice_b = get_name()
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            should_continue = False

game()