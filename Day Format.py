#Day Format Problem
#Subroutine to display days
def DayFormat(day, output_format):
    if day == 1:
        if output_format == "day":
            print("Monday")
        elif output_format == "shortday":
            print("Mon")
        elif output_format == "char":
            print("M")
    elif day == 2:
        if output_format == "day":
            print("Tuesday")
        elif output_format == "shortday":
            print("Tue")
        elif output_format == "char":
            print("Tu")
    elif day == 3:
        if output_format == "day":
            print("Wednesday")
        elif output_format == "shortday":
            print("Wed")
        elif output_format == "char":
            print("W")
    elif day == 4:
        if output_format == "day":
            print("Thursday")
        elif output_format == "shortday":
            print("Thu")
        elif output_format == "char":
            print("Th")
    elif day == 5:
        if output_format == "day":
            print("Friday")
        elif output_format == "shortday":
            print("Fri")
        elif output_format == "char":
            print("F")
    elif day == 6:
        if output_format == "day":
            print("Saturday")
        elif output_format == "shortday":
            print("Sat")
        elif output_format == "char":
            print("Sa")
    elif day == 7:
        if output_format == "day":
            print("Sunday")
        elif output_format == "shortday":
            print("Sun")
        elif output_format == "char":
            print("Su")
#Main Program
day = int(input("Enter a day of the week (in number form):\n"))
output_format = input("Enter the format of the day:\n")
DayFormat(day, output_format)
