#Polyhedral Dice Problem
import random
#Subroutine to generate random number
def roll(faces):
    global x
    x = random.randint(1, faces)
    return x
#Main program
total = 0
while total == 0:
    faces = int(input("How many faces are on your dice/die?\n"))
    if faces <= 0:
        ("Invalid input")
    else:
        roll(faces)
        print("You rolled a/an:", x)
