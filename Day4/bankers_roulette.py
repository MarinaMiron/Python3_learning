import random
names = input("Who are the people at the table? \n")
#Give a string like: Angela, Ben, Jenny, Michael, Chloe
names = names.split(", ") #splits the string after each "," to make the list
num_items = len(names)
choice = random.randint(0, num_items-1) #generates a number that is going to be the index of the list, representing the person that will pay
bill = names[choice]
print(f"{bill} is going to buy the meal today!")
#print(random.choice(names))