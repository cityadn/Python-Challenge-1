#Exam Grade Problem
#Subroutine to calculate grade & marks to next grade
def grade(marks):
    if marks >= 80:
        print("Grade: 9")
    elif marks >= 67:
        print("Grade: 8")
        marks_left = 80 - marks
        print("Marks Left =", marks_left)
    elif marks >= 54:
        print("Grade: 7")
        marks_left = 67 - marks
        print("Marks Left =", marks_left)
    elif marks >= 41:
        print("Grade: 6")
        marks_left = 54 - marks
        print("Marks Left =", marks_left)
    elif marks >= 31:
        print("Grade: 5")
        marks_left = 41 - marks
        print("Marks Left =", marks_left)
    elif marks >= 22:
        print("Grade: 4")
        marks_left = 31 - marks
        print("Marks Left =", marks_left)
    elif marks >= 13:
        print("Grade: 3")
        marks_left = 22 - marks
        print("Marks Left =", marks_left)
    elif marks >= 4:
        print("Grade: 2")
        marks_left = 13 - marks
        print("Marks Left =", marks_left)
    elif marks >= 2:
        print("Grade: 1")
        marks_left = 4 - marks
        print("Marks Left =", marks_left)
    else:
        print("Grade: U")
        marks_left = 2 - marks
        print("Marks Left =", marks_left)
        
#Main Program
marks = int(input("Student exam mark:\n"))
if marks > 100 or marks < 0:
        while marks > 100 or marks < 0:
            marks = int(input("Student exam mark:\n"))
grade(marks)
