#    ############### Our Blackjack House Rules #####################

#    ## The deck is unlimited in size.
#    ## There are no jokers.
#    ## The Jack/Queen/King all count as 10.
#    ## The Ace can count as 11 or 1.
#    ## Use the following list as the deck of cards:
#    ## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#    ## The cards in the list have equal probability of being drawn.
#    ## Cards are not removed from the deck as they are drawn.

import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def print_hand(l):
    s = "( "
    for i in l:
        s += str(i) + " "
    s += ")"
    return s


def card_deal(card, hand):
    a = random.choice(list(card.items()))
    hand.append(a[0])


def sum_hand(d, lyst):
    list1 = []
    for cards in lyst:
        list1.append(d[cards])
    if 11 in list1 and sum(list1) > 21:
        list1.remove(11)
        list1.append(1)
    return sum(list1)


def blackjack():
    card = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
            "10": 10, "K": 10, "Q": 10, "J": 10}
    your_hand = []
    dealers_hand = []
    for i in range(2):
        a = random.choice(list(card.items()))
        b = random.choice(list(card.items()))
        your_hand.append(a[0])
        dealers_hand.append(b[0])
    print(f"Your cards: {print_hand(your_hand)}, Current score: {sum_hand(card, your_hand)}")
    print(f"Dealer's first card: {dealers_hand[0]}")
    while sum_hand(card, your_hand) <= 21:
        choice = input("Tap 'y' to get another card. Tap 'n' to pass: ").casefold()
        if choice == "y":
            card_deal(card, your_hand)
            card_deal(card, dealers_hand)
            print(f"Your cards: {print_hand(your_hand)}, current score: {sum_hand(card, your_hand)}")
            print(f"Dealer's first card: {dealers_hand[0]}")
        else:
            break
    print()
    dealer_sum = sum_hand(card, dealers_hand)
    if dealer_sum < 17:
        card_deal(card, dealers_hand)
    print(f"Your hand: {print_hand(your_hand)}, your score: {sum_hand(card, your_hand)}")
    print(f"The Dealer's hand: {print_hand(dealers_hand)}, The Dealer's score: {sum_hand(card, dealers_hand)}")

    if sum_hand(card, your_hand) <= 21 and sum_hand(card, dealers_hand) <= 21:
        if sum_hand(card, your_hand) == 21 and sum_hand(card, dealers_hand) != 21:
            print("You have a BLACKJACK! YOU WIN!😎")
        elif sum_hand(card, dealers_hand) == 21 and sum_hand(card, your_hand) != 21:
            print("The dealer has a BLACKJACK! You LOSE! 😱")
        elif sum_hand(card, your_hand) > sum_hand(card, dealers_hand):
            print("YOU WIN!😃")
        elif sum_hand(card, your_hand) == sum_hand(card, dealers_hand):
            print("IT'S A DRAW.😒")
        else:
            print("YOU LOSE!😤")
    else:
        if sum_hand(card, dealers_hand) > 21 >= sum_hand(card, your_hand):
            print("BUST! The dealer went over. YOU WIN!😁")
        elif sum_hand(card, your_hand) > 21 >= sum_hand(card, dealers_hand):
            print("BUST! You went over. YOU LOSE!😭")
        elif sum_hand(card, your_hand) > 21 and sum_hand(card, dealers_hand) > 21:
            print("You both went over. BUST! It's a DRAW.😑")
    print("_" * 123)
    print()


def main():
    game = int(input("Do you want to play a game of BlackJack? Type '0' for NO and '1' for YES: "))
    if game == 0:
        return ""
    elif game == 1:
        print(logo)
        blackjack()
        main()
    else:
        main()


print()
main()
