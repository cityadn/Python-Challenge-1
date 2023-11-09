# Counter-controlled iterations

# Subroutine to demonstrate loops
def CharLoop(Message):
    for Index in range(0,len(Message),1):
        Alpha = Message[Index]
        print("Character {} of {} is {}".format(Index, Message, Alpha))

# Main program
Message = "Hello World"
CharLoop(Message)
