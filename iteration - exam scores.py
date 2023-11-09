#Test Score Problem
total1 = 0
total2 = 0
total3 = 0
for i in range(30):
    test1 = int(input("Enter the student's score for test 1:\n"))
    total1 = total1 + test1
average1 = total1/30
for i in range(30):
    test2 = int(input("Enter the student's score for test 2:\n"))
    total2 = total2 + test2
average2 = total2/30
for i in range(30):
    test3 = int(input("Enter the student's score for test 3:\n"))
    total3 = total3 + test3
average3 = total3/30
print("Average for test 1 = ", int(average1))
print("Average for test 2 = ", int(average2))
print("Average for test 3 = ", int(average3))
average_score = (average1 + average2 + average3) / 3
print("Average Score for the entire year = ", int(average_score))
