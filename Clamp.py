#Clamp Problem
limit = 50
#Subroutine to establish the maximum limit
def Clamp(number, limit):
    if number == limit:
        print(limit)
    elif number < limit:
        print(number)
    elif number > limit:
        print(limit)
#Main Program
number = float(input("Enter a number:\n"))
while number < 0:
    Clamp(number, limit)
Clamp(number,limit)
