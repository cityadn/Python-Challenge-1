#Rock Paper Scissors Problem
import random
import sys
def game(name1, name2):
    global score1
    global score2
    score1 = 0
    score2 = 0

    new = int(input("\nDo you want to start a new game? Type '1' for yes, and '2' for no:\n"))
    if new == 1:
        for i in range(0,3):
            #rock = 1
            #paper = 2
            #scissors = 3
            play1 = random.randint(1,3)
            play2 = random.randint(1,3)

            if play1 == play2:
                print("\nTie, Keep Playing\n")
                print(play1)
                print(play2)
                
            elif play1 == 1 and play2 == 3:
                print("\nRock beats scissors, well done {}\n".format(name1))
                score1 = score1 + 1
                print(play1)
                print(play2)
            
            elif play1 == 3 and play2 == 1:
                print("\nRock beats scissors, well done {}\n".format(name2))
                score2 = score2 + 1
                print(play1)
                print(play2)
            
            elif play1 == 3 and play2 == 2:
                print("\nScissors beats Paper, well done {}\n".format(name1))
                score1 = score1 + 1
                print(play1)
                print(play2)
            
            elif play1 == 2 and play2 == 3:
                print("\nScissors beats Paper, well done {}\n".format(name2))
                score2 = score2 + 1
                print(play1)
                print(play2)
            
            elif play1 == 2 and play2 == 1:
                print("\nPaper beats Rock, well done {}\n".format(name1))
                score1 = score1 + 1
                print(play1)
                print(play2)
            
            elif play1 == 1 and play2 == 2:
                print("\nPaper beats Rock, well done {}\n".format(name2))
                score2 = score2 + 1
                print(play1)
                print(play2)
        
        print("\n{} score:".format(name1), score1)
        print("{} score:".format(name2), score2)

        if score1 > score2:
            print("\nWell done, You won {}!".format(name1))
        elif score1 < score2:
            print("\nWell done, You won {}!".format(name2))
        else:
            print("\nTie")
            
    elif new == 2:
        sys.exit()

        

name1 = input("Player 1, enter a username:\n")
name2 = input("Player 2, enter a username:\n")
total = 0
while total == 0:
    print("\n1 = rock, 2 = paper, 3 = scissors")
    game(name1, name2)




