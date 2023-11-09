# Number data types
import random

# Subroutine to generate a random number
def RollDice():
    return random.randint(1,12)

# Main program
random.seed(50)
Dice = RollDice()
print("Rolled a {}".format(Dice))
