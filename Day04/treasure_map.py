line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? \n")
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter) #takes the index from the list "abc" at wich we find the letter
number_index = int(position[1]) - 1
map[number_index][letter_index] = " X"
print(f"{line1}\n{line2}\n{line3}")