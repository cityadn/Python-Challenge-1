#Divisible Problem
#Subroutine to divide the two numbers
def div(num1,num2):
    division = num1/num2
    remainder = num1 % num2
    if num1 == 0 or num2 == 0:
        print("False")
    elif remainder == 0:
        print("True")
    else:
        print("False")
#Main Program
num1 = float(input("Enter a number:\n"))
num2 = float(input("Enter another number:\n"))
div(num1,num2)
