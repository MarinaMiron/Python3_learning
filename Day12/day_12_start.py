################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#Local scope

def drink_potion():
  potion_strength = 2
  print(potion_strength)

drink_potion()
#print(potion_strength)

#Global Scope
player_health = 10
def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

#Modifying Global Scope
enemies = 1

def increase_enemies():
   #global enemies
   print(f"enemies inside function: {enemies}")
   return enemies + 1

increase_enemies()
print(f"enemies outside function {enemies}")

#Global Constants
PI = 3.14159
URL = "https://www.google.com"
