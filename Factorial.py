#Factorial Problem
#Subroutine to find the factorial of a number
def Fact(num):
    factorial = 1
    if int(num) >= 1:
        for i in range (1, int(num)+1):
            factorial = factorial * i 
    print("Factorial of {} is: {}".format(num, factorial))
        
#Main Program
total = 0
while total == 0:
    num = int(input("Enter a number:\n"))
    Fact(num)
