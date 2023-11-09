#addition, subtraction, multiplication and division functions
def add(num1,num2):
    answer = num1 + num2
    return answer
def subtract(num1,num2):
    answer= num1 - num2
    return answer
def divide(num1,num2):
    answer = num1 / num2
    return answer
def multiply(num1,num2):
    answer = num1 * num2
    return answer

#User Inputs
first = int(input("Enter your first number: "))
second = int(input("Enter your second number: "))

#Operand Options
print("Choose an option: (1) Add, (2) Subtract, (3) Divide, (4) Multiply")
choice= int(input())

#Main Program
if choice == 1:
    answer = add(first,second)
elif choice == 2:
    answer = subtract(first,second)
elif choice == 3:
    answer = divide(first,second)
elif choice == 4:
    answer = multiply(first,second)

#Output
print("The answer is",answer)
