#ASCII Art Problem
#Subroutine to display ASCII Art
def ASCIIArt(name):
    art = ''
    layer = ''
    for index in range(0,len(name),1):
        art = art + "|"+name[index]+"|"
    for index in range(0,int(len(art)/2),1):
        layer=layer+"+-"
    print(layer)
    print(art)
    print(layer)
#Main Program
name = input("Enter anything:\n")
name = name.upper()
ASCIIArt(name)



