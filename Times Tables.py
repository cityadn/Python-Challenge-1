#Times Table Problem
#Subroutine to output the X times table
def TimeTable(X):
    for Counter in range(1,13):
        print("{} x {} = {}".format(Counter, X, Counter * X))
#Main Program
TimeTable(6)
