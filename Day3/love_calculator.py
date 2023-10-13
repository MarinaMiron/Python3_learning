print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_names = name1 + name2
combined_names = combined_names.lower()
true_oc = 0
true_oc += combined_names.count("t")
true_oc += combined_names.count("r")
true_oc += combined_names.count("u")
true_oc += combined_names.count("e")

love_oc = 0
love_oc += combined_names.count("l")
love_oc += combined_names.count("o")
love_oc += combined_names.count("v")
love_oc += combined_names.count("e")

love_score = int(str(true_oc) + str(love_oc))

if love_score <= 10 or love_score >= 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")