#Valid Address Problem
#Function to validate an email address
def validation(email):
    #First method of checking characters
    special_char1 = "@"
    special_char2 = "."
    """if (special_char1 in email) and (special_char2 in email):
        print("Email Address is valid")
    else:
        print("Email Address is not valid")"""

    #Second method of finding characters
    if ((email.find("@") >= 0) and  (email.find(".") >= 0)):
        print("Email Address is valid")
    else:
        print("Email Address is not valid")

#Main Program
email = input("Enter your email address:\n")
validation(email)
      

