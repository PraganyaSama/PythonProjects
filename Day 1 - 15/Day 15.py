# <editor-fold desc="MENU">
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
# </editor-fold>
# <editor-fold desc="resources">
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# </editor-fold>
def make_coffee(drink, menu):
    for i in menu["ingredients"]:
        resources[i] -= menu["ingredients"][i]
    return f"Here is your {drink}. Enjoy!"


def resource_check(drink):
    for i in drink["ingredients"]:
        if resources[i] < drink["ingredients"][i]:
            print(f"Sorry, there was not enough {i}.")
            return False
    return True


def coin_check(total, cost):
    if total > cost:
        print(f"Here is your {total - cost} in change.")
        return True
    elif total == cost:
        return True
    elif total < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def coffee_machine(profit = 0):
    prompt = input("What would you like? (Espresso/Latte/Cappuccino): ").casefold()
    if prompt == "off":
        return""
    elif prompt == "report":
        print(f"""Water: {resources["water"]}mL""")
        print(f"""Milk: {resources["milk"]}mL""")
        print(f"""Coffee: {resources["coffee"]}g""")
        print(f"Money: ${profit}")
    elif prompt in MENU:
        drink = MENU[prompt]
        if not resource_check(drink):
            return""
        print("Please Insert coins: ")
        quarters = int(input("How many Quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total = ((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01))
        cost = drink["cost"]
        if coin_check(total, cost):
            profit += cost
            print(make_coffee(prompt, drink))
    print()
    coffee_machine(profit)


coffee_machine()
