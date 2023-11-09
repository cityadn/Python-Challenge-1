#Naming Conventions Problem
#Function to find the identifier
def identification(string, convention):
    if convention == "kebab-case":
        lowerCase = string.lower()
        print(lowerCase.replace(" ", "-"))
    elif convention == "snake_case":
        lowerCase = string.lower()
        print(lowerCase.replace(" ", "_"))
    elif convention == "camelCase":
        firstLetter = string[0:1]
        lowerCase = firstLetter.lower()
        newString = string.replace(" ", "")
        print(newString.replace(firstLetter, lowerCase))
    elif convention == "PascalCase":
        firstLetter = string[:0]
        lowerCase = firstLetter.lower()
        newString = string.replace(" ", "")
        print(newString.replace(firstLetter, lowerCase))
        
#Main Program
string = input("Type in a string:\n")
convention = input("Type in your convention:\n")
identification(string, convention)


        
        
    
