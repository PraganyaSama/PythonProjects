# Hangman : Guess the correct letters of the word. If you don't you lose a life.

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

def printlist(l = list):
    for i in l:
        print(i, end=" ")
    return ""

word_list = ["aardvark", "baboon", "camel", "guitar", "pneumonic", "convolution", "platinum"]
chosen_word = random.choice(word_list)

guess = []
for i in chosen_word:
    guess.append("_")

print(logo + "\n")
print(printlist(guess))
print("\n")

lives = 6
while lives > 0:
    letter = input("Choose a letter : ").lower()
    if letter in chosen_word:
        for i in range(len(guess)):
            if letter == chosen_word[i]:
                guess[i] = letter
        printlist(guess)
        print(stages[lives])
        if  "_" not in guess:
            print("YOU WIN.")
            break
        else:
            continue
    else:
        lives -= 1
        print(f"You guessed {letter}. That's not in the word. You lose a life.")
        if lives == 0:
            print(stages[lives])
            print("You have no lives remaining.")
            print("GAME OVER.")
            print(f"Your word was: {chosen_wordaa}")
        else:
            print(stages[lives])
            print(f"Remaining lives : {lives} \n\n")
            printlist(guess)
            print()
