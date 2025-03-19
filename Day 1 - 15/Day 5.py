# Random password generator using predefined instructions.

import random
import string

print("Welcome to the PyPassword Generator.")
characters = int(input("How many characters would you like in your password?\n"))
symbols = int(input("How many symbols would you like? \n"))
numbers = int(input("How many numbers would you like? \n"))
symbol = ["!", "@", "#", "$", "%", "^", "&", "*"]
password = []

for i in range(symbols):
    a = random.choice(symbol)
    password.append(a)
for j in range(numbers):
    b = random.randint(0,9)
    password.append(str(b))
for k in range(characters - (symbols + numbers)):
    c = random.choice(string.ascii_lowercase + string.ascii_uppercase)
    password.append(c)
random.shuffle(password)

print(f"Here is your password : ", end="")
for i in password:
    print(i, end="")
