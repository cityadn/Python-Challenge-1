#Ten Green Bottles Problem
#Subroutine to output the song
def TenGreen():
    for i in range(10,0,-1):
        if i > 1:
            print("{} green bottles hanging on the wall,\n".format(i))
            print("{} green bottles hanging on the wall,\n".format(i))
            print("And if one green bottle should accidently fall,\n")
            print("There'll be {} green bottles hanging on the wall.\n".format(i-1))
            print("\n")
        else:
            print("{} green bottle hanging on the wall,\n".format(i))
            print("{} green bottle hanging on the wall,\n".format(i))
            print("And if one green bottle should accidently fall,\n")
            print("There'll be {} green bottles hanging on the wall.\n".format(i-1))
#Main Program
TenGreen()
