#Dogs Life Problem
#Subroutine to calculate the age of a dog from a human age
def dogAge(age):
    if age<=2:
        dogYears = int(age*12)
        print(dogYears)
    elif age>2:
        dogYears = int(((6.5-2)*6)+24)
        print(dogYears)
#Main Program
age = float(input("Enter the age of the dog in human years:\n"))
dogAge(age)
