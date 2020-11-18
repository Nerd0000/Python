#----------------------------------------------------------- imports
import random as r

#----------------------------------------------------------- initial config
difficulty = []

for i in range(int(input('How long is the range you want? \n'))): # better way to d, probably
    difficulty.append(i+1)

secret_number = r.choice(difficulty)
score = len(difficulty)
answer = False

#----------------------------------------------------------- game core
def choser():
    clue_number = r.choice(difficulty)
    difficulty.remove(clue_number)
    return clue_number

def clue_maker():
    clue_option = r.randint(1, 4)

    #division
    if clue_option == 1:
        clue_number = choser()
        print(f'\nThe number divided by {clue_number} is equal to {secret_number/clue_number}')

    #multiplication
    elif clue_option == 2:
        clue_number = choser()
        print(f'\nThe number multiplied by {clue_number} is equal to {secret_number*clue_number}')

    #adittion
    elif clue_option == 3:
        clue_number = choser()
        print(f'\nThe number added to {clue_number} is equal to {secret_number + clue_number}')

    #subtraction
    elif clue_option == 4:
        clue_number = choser()
        print(f'\nThe number subtracted by {clue_number} is equal to {secret_number - clue_number}')

#----------------------------------------------------------- game
while True:
    clue_maker()
    answer = int(input('Who is the secret number? \n'))

    if secret_number == answer:
        print(f'\nYou won with {score} points!')
        break

    score -= 1
    print('Wrong')

    if score == 1:
        print('\nYou lose!')
        break
