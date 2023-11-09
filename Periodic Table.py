#Periodic Table Program
#Subroutine to display the elements of group 1 and 2
total = 0
def periodic(element):
    if element == "li" or element == "Li" or element == "LI":
        print("""Element = Lithium
Atomic Weight = 6.94
Group = Alkali Metals""")
    elif element == "na" or element == "Na" or element == "NA":
        print("""Element = Sodium
Atomic Weight = 22.99
Group = Alkali Metals""")
    elif element == "k" or element == "K":
        print("""Element = Potassium
Atomic Weight = 39.1
Group = Alkali Metals""")
    elif element == "he"or element == "He" or element == "HE":
        print("""Element = Helium
Atomic Weight = 4.00
Group = Noble Gases""")
    elif element == "ne" or element == "Ne" or element == "NE":
        print("""Element = Neon
Atomic Weight = 20.18
Group = Noble Gases""")
    elif element == "ar" or element == "Ar" or element == "AR":
        print("""Element = Argon
Atomic Weight = 39.95
Group = Noble Gases""")
#Main Program
element = input("Type in the inital of the element:\n")
periodic(element)
        
