#Nitrates - Dose program
#Subroutine to calculate the nitrate levels
def dose(nitrate):
    #global nitrate
    if nitrate > 10:
        print("For", nitrate, "dose 3ml")
    else:
        if nitrate > 2.5:
            print("For", nitrate, "dose 2ml")
        else:
            if nitrate > 1:
                print("For", nitrate, "dose 1ml")
            else:
                print("For", nitrate, "dose 0.5ml")
#Main Program
nitrate = float(input("Please enter the level of nitrate:\n"))                
dose(nitrate)
