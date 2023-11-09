#ASCII to EBCDIC Problem
#Function to convert characters into ASCII and EBCDIC
def conversion(character):
    firstSet = ['A','B','C','D','E','F','G','H','I']
    secondSet = ['J','K','L','M','N','O','P','Q','R']
    thirdSet = ['S','T','U','V','W','X','Y','Z']
    character = character.upper()
    ASCII = ord(character)
    if character == " ":
        EBCDIC = ASCII + 32
    elif character in firstSet:
        #193-65=128
        EBCDIC = ASCII + 128
    elif character in secondSet:
        #209-74=135
        EBCDIC = ASCII + 135
    elif character in thirdSet:
        #226-83=143
        EBCDIC = ASCII + 143
    print(ASCII)
    print(EBCDIC)
character = input("Enter a letter:\n")
conversion(character)
