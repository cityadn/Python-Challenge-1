#Passcode Problem
"""Subroutine to convert the vowels
of a word into a passcode"""
def passcode(word, word2):
    vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
    print("Passcode:")
    for i in range(0,len(word)):
        if word[i] in vowels:
            print(i)
    for i in range(0,len(word2)):
        if word2[i] in vowels:
            print(i)
#Main Program
word = input("Enter one word:\n")
word2 = input("Enter another word:\n")
passcode(word, word2)
  
