rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
rps = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice > 2 or user_choice < 0:
    print("Invalid choice. Please choose a valid option. Game over!")
else:
    user_choice = rps[user_choice]
    print(user_choice)
    computer_choice = random.choice(rps)
    print(f"Computer chose: \n {computer_choice}")
    if (computer_choice == rps[0] and user_choice == rps[2]) or (computer_choice == rps[2] and user_choice == rps[1]) or (computer_choice == rps[1] and user_choice == rps[0]):
        print("You lose. :(")
    elif computer_choice == user_choice:
        print("It's a tie.")
    else:
        print("You win!")