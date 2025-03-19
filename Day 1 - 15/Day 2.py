bill = float(input("""Welcome to the tip calculator!
What was the total bill? ₹"""))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
total_bill = bill + (bill*tip/100)
people = int(input("How many people to split the bill? "))
individual_bill = total_bill/people
print(f"Each person should pay : ₹{individual_bill} ")
