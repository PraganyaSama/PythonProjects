# An elementary Calculator.

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def exponent(a, b):
    return a ** b

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

operations = {"+": addition, "-": subtraction, "*": multiplication, "/": division, "**": exponent}


def calculator():
    print(logo)
    num1 = int(input("What's the first number?: "))
    continue_calculating = True

    while continue_calculating:
        for i in operations:
            print(i, end="\n")
        operation = input("Select an operation: ")
        num2 = int(input("Enter the second number: "))
        calculated_function = operations[operation]
        result = calculated_function(num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        yn = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation.").casefold()
        if yn == "y":
            num1 = result
        elif yn == "n":
            continue_calculating = False
            print("\n\n")
            calculator()
        else:
            break


calculator()
