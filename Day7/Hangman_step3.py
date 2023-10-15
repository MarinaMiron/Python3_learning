#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(len(chosen_word)):
    display.append("_")

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False
while not end_of_game:
    guess= input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(len(chosen_word)):
        print(f"Current position: {position}\n Current letter: {chosen_word[position]}\n Guessed letter: {guess}")
        if guess == chosen_word[position]:
            display[position] = guess
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You won!")