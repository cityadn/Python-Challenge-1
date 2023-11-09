#Prime Number Problem
#Subroutine to find Prime Numbers
def isPrime(num):
    halved = int(num/2+1)
    prime=True
    for i in range(2,halved,1):
        if num % i == 0:
            prime = False
    print(prime)

total = 0
while total == 0:
    num = int(input("Enter a number:\n"))
    isPrime(num)

