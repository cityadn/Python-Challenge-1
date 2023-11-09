#Scrabble Problem
"""Subroutine to tally up points
based on the letters(scrabble)"""
def points(word):
    score = 0
    word = word.upper()
    x1 = ['E','A','I','O','N','R','T','L','S','U']
    x2 = ['D','G']
    x3 = ['B','C','M','P']
    x4 = ['F','H','V','W','Y']
    x5 = ['K']
    x8 = ['J','X']
    x10 = ['Q','Z']
    for i in range(0,len(word)):
        if word[i] in x1:
            score = score + 1
        elif word[i] in x2:
            score = score + 2
        elif word[i] in x3:
            score = score + 3
        elif word[i] in x4:
            score = score + 4
        elif word[i] in x5:
            score = score + 5
        elif word[i] in x8:
            score = score + 8
        elif word[i] in x10:
            score = score + 10
    totalScore = score
    print(totalScore)
#Main Program
word = input("Enter a word:\n")
points(word)
