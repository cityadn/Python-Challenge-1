#Save the Change Problem
#Subroutine to calculate difference to nearest 1
def SaveTheChange(Amount):
    if int(Amount) != Amount:
        NearestPound = int(Amount) + 1
        return NearestPound - Amount
    else:
        NearestPound = Amount
    
#Main program
Price=1.20
Savings = SaveTheChange(Price)
print("Debit - purchase: £{:.2f}".format(Price))
print("Debit - Save the change: £{:.2f}".format(Savings))
print("Credit - Save the changes: £{:.2f}".format(Savings))
