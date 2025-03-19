# Rock paper scissors game....press enter key for exiting the game. Better code than this can be created.

import random
rock = '''
    _______
---'   ____)
      (_______)
      (________)
      (______)
---.__(____)
'''

paper = '''
    _______
---'   ____)_______
            ________)
            __________)
           ________)
---.___________)
'''

scissors = '''
    _______
---'   ____)_________
             ________)
           __________)
      (______)
---.__(____)
'''

choices = [rock, paper, scissors]
outcomes = ["You won!", "You lose.", "It's a draw."]
while True:
    choice = input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors. \n")
    computer_choice = random.choice(choices)
    while True:
        if choice == "0":
            index = int(choice)
            print(f"Your choice : \n\n {choices[index]}\n\n")
            print(f"Computer's choice : \n\n {computer_choice}")
            if computer_choice == scissors:
                print(outcomes[0])
            elif computer_choice == paper:
                print(outcomes[1])
            elif computer_choice == rock:
                print(outcomes[2])
            print()
            break
        elif choice == "1":
            index = int(choice)
            print(f"Your choice : \n\n {choices[index]}\n\n")
            print(f"Computer's choice : \n\n {computer_choice}")
            if computer_choice == rock:
                print(outcomes[0])
            elif computer_choice == scissors:
                print(outcomes[1])
            elif computer_choice == paper:
                print(outcomes[2])
            print()
            break
        elif choice == "2":
            index = int(choice)
            print(f"Your choice : \n\n {choices[index]}\n\n")
            print(f"Computer's choice : \n\n {computer_choice}")
            if computer_choice == paper:
                print(outcomes[0])
            elif computer_choice == rock:
                print(outcomes[1])
            elif computer_choice == scissors:
                print(outcomes[2])
            print()
            break
        elif choice == "":
            break
        else:
            print("Incorrect data. Enter again.")
            print()
            break
