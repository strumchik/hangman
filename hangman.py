# Write your code here
import random
from string import ascii_lowercase
print("H A N G M A N")
guess_list = ('python', 'java', 'kotlin', 'javascript')
while True:
    choise = input('Type "play" to play the game, "exit" to quit: ')
    if choise == "exit":
        break
    elif choise != "play":
        continue
    answer = str(random.choice(guess_list))
    leak = "-" * len(answer)
    lives = 8
    typed = []

    while lives > 0:
        print("\n"+leak)
        letter = input('Input a letter: ')
        if len(letter) > 1:
            print("You should print a single letter")
        elif letter not in ascii_lowercase:
            print("It is not an ASCII lowercase letter")
        elif letter in typed:
            print("You already typed this letter")
        else:
            typed.append(letter)
            if letter in answer:
                n_leak = ""
                for n in range(len(answer)):
                    if letter == answer[n]:
                        n_leak += letter
                    else:
                        n_leak += "".join(leak[n])
                leak = str(n_leak)
            else:
                lives -= 1
                print("No such letter in the word")
            if leak == answer:
                break
    if lives > 0:
        print(f'\n{answer}\nYou guessed the word!\nYou survived!')
    else:
        print("You are hanged!")
