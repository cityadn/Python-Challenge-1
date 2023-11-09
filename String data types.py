# String data types

# Subroutine to concat name
def FullName(String1, String2):
    return String1.upper() + " " + String2.upper()

# Main program
Forename = "John"
Surname = "Smith"
Student = FullName(Forename, Surname)
print("Full name: {}".format(Student))
