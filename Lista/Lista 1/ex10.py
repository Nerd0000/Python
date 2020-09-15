import random #for the dice stuff
import time #sleep stuff

diceGoal = 0

while True:
    #dice stuff
    print("")
    diceResult = random.randint(1,12)
    print("Rolando os dados")
    print(f"Seu resultado foi {diceResult}")
    print("")

    if diceGoal==0:
        if (diceResult == 7) or (diceResult == 1):
            print("Natural. Venceu")
            break #break the loop

        elif (diceResult == 2) or (diceResult == 3) or (diceResult == 1):
            print("Craps. Perdeu")
            break #break the loop

        else:
            print("Ponto")
            print(f"O dado será jogado até cair no mesmo número ({diceResult}). Caso ele caia você venceu. Porém se você tirar um 7 antes  você perdeu.")
            numberGoal = diceResult

    else:
        if diceResult == 7:
            print("Lose")
            break

        elif diceResult == numberGoal:
            print("Win")
            break
        
        else:
            print(f"O dado será jogado novamente em 2 segundos. Objetivo {numberGoal}")
            time.sleep(2)
print("Jogo finalizado.")