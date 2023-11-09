#Initial & Surname Problem
#Function FormatName
ForName = ""
SurName = ""
def FormatName(ForName, SurName):
    ForName = input("Enter your first name:\n")
    SurName = input("Enter your surname:\n")
    Initial = ForName[0]
    FullName = Initial + " " + SurName
    return FullName.upper()
#Main program
print(FormatName(ForName, SurName))
