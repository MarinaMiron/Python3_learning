#Step 5- final

import random
from hangman_art import *
from hangman_words import word_list

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
end_of_game = False
lives = 6
#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(len(chosen_word)):
    display.append("_")

while not end_of_game:
    guess= input("Guess a letter: ").lower()
    
  #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(len(chosen_word)):
        #print(f"Current position: {position}\n Current letter: {chosen_word[position]}\n Guessed letter: {guess}")
        if guess == chosen_word[position]:
            display[position] = guess

    #If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You died. :(")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You won!")
    
    #Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])