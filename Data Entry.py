#Data Entry Problem
#Subroutine to store and extract details
def file(detail, amount):
    details = []
    for i in range(0, amount, 1):
        detail = input("Enter all your available details:\n")
        details.append(detail)
        i+=1
    print("Details", details)
#Main Program
amount = int(input("How many details do you have with you? (Enter a number amount)\n"))
member_num = int(input("Enter the number of members:\n"))
detail = ""
file(detail, amount)


    
