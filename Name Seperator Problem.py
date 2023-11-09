#Name Seperator Problem
#Function to seperate a full name
def seperate(fullName):
    space = fullName.find(" ")
    lastChar = len(fullName)
    firstName = fullName[:space]
    surName = fullName[space+1:lastChar]
    print(firstName)
    print(surName)
#Main Program
fullName = input("Enter your full name (with a space in between)\n")
seperate(fullName)
