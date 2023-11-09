#FizzBuzz Problem
"""Subroutine to output the numbers between
1 to X that are multiples of 3, or 5, or both"""
def game(x):
    for i in range(1,x+1):
        if (i%3)==0 and (i%5)==0:
            print("FizzBuzz")
        elif (i%3)==0:
            print("Fizz")
        elif (i%5)==0:
            print("Buzz")
        else:
            print(i)
#Main Program
x = int(input("Enter a number above 1:\n"))
game(x)
