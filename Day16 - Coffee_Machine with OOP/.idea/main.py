from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

def coffee_maker():
    prompt = input(f"What would you like to drink? ({menu.get_items()}): ").casefold()
    if prompt == "off":
        return
    elif prompt == "report":
        coffee_machine.report()
        money_machine.report()
    elif prompt in menu.get_items():
        drink = menu.find_drink(prompt)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
    else:
        menu.find_drink(prompt)
    coffee_maker()


coffee_maker()
