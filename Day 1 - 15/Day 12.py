import random
logo = """

  ▄████  █    ██ ▓█████   ██████   ██████  ██▓ ███▄    █   ▄████      ▄████  ▄▄▄      ███▄ ▄███▓▓█████ 
 ██▒ ▀█▒ ██  ▓██▒▓█   ▀ ▒██    ▒ ▒██    ▒ ▓██▒ ██ ▀█   █  ██▒ ▀█▒    ██▒ ▀█▒▒████▄   ▓██▒▀█▀ ██▒▓█   ▀ 
▒██░▄▄▄░▓██  ▒██░▒███   ░ ▓██▄   ░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒██░▄▄▄░   ▒██░▄▄▄░▒██  ▀█▄ ▓██    ▓██░▒███   
░▓█  ██▓▓▓█  ░██░▒▓█  ▄   ▒   ██▒  ▒   ██▒░██░▓██▒  ▐▌██▒░▓█  ██▓   ░▓█  ██▓░██▄▄▄▄██▒██    ▒██ ▒▓█  ▄ 
░▒▓███▀▒▒▒█████▓ ░▒████▒▒██████▒▒▒██████▒▒░██░▒██░   ▓██░░▒▓███▀▒   ░▒▓███▀▒ ▓█   ▓██▒██▒   ░██▒░▒████▒
 ░▒   ▒ ░▒▓▒ ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒     ░▒   ▒  ▒▒   ▓▒█░ ▒░   ░  ░░░ ▒░ ░
  ░   ░ ░░▒░ ░ ░  ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░  ░   ░      ░   ░   ▒   ▒▒ ░  ░      ░ ░ ░  ░
░ ░   ░  ░░░ ░ ░    ░   ░  ░  ░  ░  ░  ░   ▒ ░   ░   ░ ░ ░ ░   ░    ░ ░   ░   ░   ▒  ░      ░      ░   
      ░    ░        ░  ░      ░        ░   ░           ░       ░          ░       ░  ░      ░      ░  
"""

welcome_message = """
Welcome to the guessing game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': 
"""

low_message = """Too low.
Guess again."""

high_message = """Too high.
Guess again."""
def guessing_game():
    answer = random.randint(1, 100)
    print(logo)
    difficulty = input(welcome_message).casefold()
    if difficulty == "easy":
        lives = 10
    else:
        lives = 7
    while lives > 0:
        print(f"You have {lives} lives remaining.")
        guess = int(input("Enter your guess: "))
        if guess < answer:
            print(low_message)
        elif guess > answer:
            print(high_message)
        else:
            print(f"You got it correct!!! The number was {answer}.")
            return ""
        lives -= 1
    print("Your lives are over. YOU LOSE.")
    print(f"The correct answer is {answer}")


guessing_game()
