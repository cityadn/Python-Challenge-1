#Dice Game Problem
import random
#Subroutine to calculate the dice score
def ScoreDice(Dice1, Dice2, Dice3):
    if Dice1 == Dice2 == Dice3:
        Score = Dice1 + Dice2 + Dice3
        print("Score =", Score)
    else:
        if Dice1 == Dice2:
            Score = Dice1 + Dice2 - Dice3
            print("Score =", Score)
        elif Dice1 == Dice3:
            Score = Dice1 + Dice3 - Dice2
            print("Score =", Score)
        elif Dice2 == Dice3:
            Score = Dice2 + Dice3 - Dice1
            print("Score =", Score)
        elif Dice1 != Dice2 != Dice3:
            Score = 0
            print("Score =", Score)
#Main Program
Dice1 = random.randint(1,6)
Dice2 = random.randint(1,6)
Dice3 = random.randint(1,6)
ScoreDice(Dice1, Dice2, Dice3)
