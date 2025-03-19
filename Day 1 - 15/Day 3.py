# Treasure hunting game using loops.

treasure = '''
                                *******************************************************************************
                                          |                   |                  |                     |
                                 _________|________________.=""_;=.______________|_____________________|_______
                                |                   |  ,-"_,=""     `"=.|                  |
                                |___________________|__"=._o`"-._        `"=.______________|___________________
                                          |                `"=._o`"=._      _`"=._                     |
                                 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
                                |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
                                |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                                          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
                                 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
                                |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
                                |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
                                ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
                                /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
                                ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
                                /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
                                ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
                                /______/______/______/______/______/______/______/______/______/______/_____ /
                                *******************************************************************************
                                '''

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
count = 0
while count == 0:
    choice1 = input("""You're at a crossroad. where do you want to go?
    Type "left" or "right" : \n""").casefold()
    if choice1 == "left":
        while count == 0:
            choice2 = input("""There's an island in the middle of the lake.
    Type "wait" to wait for a boat. Type "swim" to swim across. \n""").casefold()
            if choice2 == "wait":
                while count == 0:
                    choice3 = input("""You arrive at the island unharmed. There is a house with three doors.
    One Red, one Yellow and one Blue. Which colour do you choose? \n""").casefold()
                    if choice3 == "red":
                        print("It's a room full of fire. GAME OVER.")
                        again = input("Do you want to be sent back in time and re-think your choice?(enter Y or N): ").casefold()
                        if again == "y":
                            print("OK. SENDING YOU BACK IN TIME....")
                            print()
                            continue
                        elif again == "n":
                            count = 1
                    elif choice3 == "yellow":
                        print("You've found the treasure! YOU WIN!")
                        print(treasure)
                        count = 1
                    elif choice3 == "blue":
                        print("You enter a room full of beasts. GAME OVER.")
                        again = input("Do you want to be sent back in time and re-think your choice?(enter Y or N): ").casefold()
                        if again == "y":
                            print("OK. SENDING YOU BACK IN TIME....")
                            print()
                            continue
                        elif again == "n":
                            count = 1
                    else:
                        print("Invalid choice. Please Re-Enter : ")
                        print()
            elif choice2 == "swim":
                print("You get attacked by an angry trout. GAME OVER.")
                again = input("Do you want to be sent back in time and re-think your choice?(enter Y or N): ").casefold()
                if again == "y":
                    print("OK. SENDING YOU BACK IN TIME....")
                    print()
                    continue
                elif again == "n":
                    count = 1
            else:
                print("Invalid choice. Please Re-Enter : ")
                print()
    elif choice1 == "right":
        print("You fell into a hole. GAME OVER.")
        again = input("Do you want to play again?(enter Y or N): ").casefold()
        if again == "y":
            print("OK. SENDING YOU BACK IN TIME....")
            print()
            continue
        elif again == "n":
            count = 1

    else:
        print("Invalid choice. Please Re-enter : ")
        print()
