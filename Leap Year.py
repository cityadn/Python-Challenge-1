#Leap Year Problem
"""Subroutine to check if
the year is a leap year"""
def leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            print("Not a leap year")
        elif year % 400 == 0:
            print("Not a leap year")
        else:
            print("It's a leap year")
    else:
        print("Not a leap year")
#Main Program
year = float(input("Enter a year:\n"))
leap(year)
