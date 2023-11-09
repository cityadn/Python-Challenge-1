#Electric Car Problem
import math
"""Subroutines to calculate the total cost and the points gained
to redeem against their cost of shopping"""
def charge(numCharged, decimals=0):
    if numCharged < 15:
        calc1 = (20 * 15) + 1
        pounds = calc1 / 100
        totalCost = "{:.2f}".format(pounds)
    elif numCharged >= 15:
        calc1 = (20 * numCharged) + 1
        pounds = calc1 / 100
        totalCost = "{:.2f}".format(pounds)
    print("£" + totalCost)
def pointsGained(numCharged, decimals=0):
    calc2 = 22 + (1.5 * numCharged)
    multiplier = 10 ** decimals
    pointsCalc = math.floor(calc2 * multiplier) / multiplier
    print(pointsCalc, "points")   
#Main Program
numCharged = float(input("Enter the number of minutes charged:\n"))
charge(numCharged)
pointsGained(numCharged, decimals=0)


        
