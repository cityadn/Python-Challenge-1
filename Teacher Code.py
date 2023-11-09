#Teacher Code Problem
#Function to return the teacher's intials
def initials(first, middle, sur):
    if middle == "":
        first_initial = first[:1]
        middle_initial = "Z"
        sur_initial = sur[:1]
    else:
        first_initial = first[:1]
        middle_initial = middle[:1]
        sur_initial = sur[:1]
    print(first_initial.upper() + middle_initial.upper() + sur_initial.upper())

#Main Program
first = input("Type in your first name:\n")
middle = input("Type in your middle name:\n")
sur = input("Type in your surname:\n")
initials(first, middle, sur)
    
