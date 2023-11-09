import sys
print("Hey there! Press enter to play the Word Game Awards!")
word = input("Type in one word:\n")
word_string = word[0:len(word)]
total = 0
for i in range(len(word)):
    if word[i] == " ":
        sys.exit()
    elif word[i] == 'e' or word[i] == 'E':
        total = total + 1
    elif word[i] == 'a' or word[i] == 'A' :
        total = total + 2
    elif word[i] == 'r' or word[i] == 'R' :
        total = total + 3
    elif word[i] == 'i' or word[i] == 'I' :
        total = total + 4
    elif word[i] == 'o' or word[i] == 'O' :
        total = total + 5
    elif word[i] == 't' or word[i] == 'T' :
        total = total + 6
    elif word[i] == 'n' or word[i] == 'N' :
        total = total + 7
    elif word[i] == 's' or word[i] == 'S' :
        total = total + 8
    elif word[i] == 'l' or word[i] == 'L' :
        total = total + 9
    elif word[i] == 'c' or word[i] == 'C' :
        total = total + 10
    elif word[i] == 'u' or word[i] == 'U' :
        total = total + 11
    elif word[i] == 'd' or word[i] == 'D' :
        total = total + 12
    elif word[i] == 'p' or word[i] == 'P' :
        total = total + 13
    elif word[i] == 'm' or word[i] == 'M' :
        total = total + 14
    elif word[i] == 'h' or word[i] == 'H' :
        total = total + 15
    elif word[i] == 'g' or word[i] == 'G' :
        total = total + 16
    elif word[i] == 'b' or word[i] == 'B' :
        total = total + 17
    elif word[i] == 'f' or word[i] == 'F' :
        total = total + 18
    elif word[i] == 'y' or word[i] == 'Y' :
        total = total + 19
    elif word[i] == 'w' or word[i] == 'W' :
        total = total + 20
    elif word[i] == 'k' or word[i] == 'K' :
        total = total + 21
    elif word[i] == 'v' or word[i] == 'V' :
        total = total + 22
    elif word[i] == 'x' or word[i] == 'X' :
        total = total + 23
    elif word[i] == 'z' or word[i] == 'Z' :
        total = total + 24
    elif word[i] == 'j' or word[i] == 'J' :
        total = total + 25
    elif word[i] == 'q' or word[i] == 'Q' :
        total = total + 26
print("Here's your score:", total)
print("Nice!")
