from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine= MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    user_choice = input(f"What would you like? ({menu.get_items()}): ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(user_choice)
        if coffe_maker.is_resource_sufficient(coffee):
            if money_machine.make_payment(coffee.cost):
                coffe_maker.make_coffee(coffee)