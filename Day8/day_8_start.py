#Simple function
def greet():
    print("Hello world!")
    print("This is a print statement.")
    print("Inside a function.")

#greet()

#Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"How do you do {name}?")

#greet_with_name("Marina")

#Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"How's the weather in {location}?")

#greet_with("Marina", "Timisoara")

#function with keyword arguments
greet_with(location="Timisoara", name="Marina")