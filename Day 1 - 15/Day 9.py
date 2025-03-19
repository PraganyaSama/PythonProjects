# Blind Auction (Used printing 100 blank lines to simulate clearing the terminal here)

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.--------------------------.,_.-._
                          |       | | |                                | | ''-.
                          |       |_| |_                              _| |_..-'
                          |_______| '-' `'--------------------------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /______________\\
'''

print(logo)
count = 0
bidders_count = {}

while count < 2:
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: ₹"))
    bidders_count[name] = bid
    yes_no = input("Are there any other bidders? Type 'yes' or 'no'. \n").casefold()
    if yes_no == "yes":
        for i in range(1000):
            print()
    else:
        count = 2

max_bid = 0
winner = ""
for bidder in bidders_count:
    price = bidders_count[bidder]
    if price > max_bid:
        max_bid = price
    winner = bidder

print(f"The winner is {winner} with a bid of ₹{max_bid}.")
